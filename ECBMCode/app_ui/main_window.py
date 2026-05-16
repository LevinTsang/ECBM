# -*- coding: utf-8 -*-
"""应用主窗口模块。

MainWindow继承自PyQt6的QMainWindow，实现：
- 经典桌面应用布局（菜单栏、工具栏、中央工作区、状态栏）
- UI组件初始化和组装（setup_ui）
- 业务控制器注入（set_controller）
- QSS样式表加载（load_qss）
- 优雅退出流程（closeEvent）
"""

import logging
from pathlib import Path

from PyQt6.QtWidgets import (
    QMainWindow, QMenuBar, QToolBar, QStatusBar,
    QStackedWidget, QWidget, QLabel, QMessageBox,
    QVBoxLayout, QApplication,
)
from PyQt6.QtCore import Qt, QSize, QEvent
from PyQt6.QtGui import QAction, QCloseEvent, QFont

from app_core.controllers.base_controller import BaseController
from app_ui.signals import SharedSignals
from app_infra.config.config_manager import ConfigManager
from app_infra.logging.log_manager import LogManager
from app_infra.utils.path_utils import get_project_root, get_resource_path
from app_infra.exceptions.base_exceptions import UIException


class MainWindow(QMainWindow):
    """应用主窗口。

    基于QMainWindow构建经典桌面应用布局：
    - 顶部菜单栏（QMenuBar）：文件和帮助菜单
    - 可停靠工具栏（QToolBar）：预留操作按钮区域
    - 中央工作区（QStackedWidget）：支持多页面切换
    - 底部状态栏（QStatusBar）：显示应用状态信息

    属性:
        _controller (BaseController | None): 关联的业务控制器。
        _menu_bar (QMenuBar): 菜单栏对象。
        _tool_bar (QToolBar): 工具栏对象。
        _status_bar (QStatusBar): 状态栏对象。
        _central_widget (QStackedWidget): 中央工作区控件。
        _signals (SharedSignals): 共享信号实例。
        _logger (logging.Logger): 日志记录器。
    """

    def __init__(self) -> None:
        """初始化主窗口。

        设置窗口基本属性（标题、尺寸、objectName）。
        UI组件的具体创建在setup_ui()中完成。
        """
        super().__init__()
        self._controller: BaseController | None = None
        self._menu_bar: QMenuBar | None = None
        self._tool_bar: QToolBar | None = None
        self._status_bar: QStatusBar | None = None
        self._central_widget: QStackedWidget | None = None
        self._signals: SharedSignals = SharedSignals()
        self._logger: logging.Logger = LogManager().get_logger(
            self.__class__.__name__
        )

        # 从配置读取窗口尺寸
        config = ConfigManager.get_instance()
        width = config.get("window_width", 1024)
        height = config.get("window_height", 768)
        min_width = config.get("window_min_width", 800)
        min_height = config.get("window_min_height", 600)

        self.setObjectName("MainWindow")
        self.setWindowTitle("ECBM Application")
        self.resize(width, height)
        self.setMinimumSize(min_width, min_height)

        # 窗口居中显示
        self._center_on_screen()

    def _center_on_screen(self) -> None:
        """将窗口移动到屏幕中央。"""
        screen = QApplication.primaryScreen()
        if screen is not None:
            screen_geometry = screen.availableGeometry()
            window_geometry = self.frameGeometry()
            center_point = screen_geometry.center()
            window_geometry.moveCenter(center_point)
            self.move(window_geometry.topLeft())

    def setup_ui(self) -> None:
        """初始化UI布局和组件。

        按顺序构建：菜单栏 -> 工具栏 -> 中央工作区 -> 状态栏。
        各组件构建方法相互独立，可按需单独调用。
        """
        self.setup_menu_bar()
        self.setup_tool_bar()
        self.setup_central_widget()
        self.setup_status_bar()
        self._logger.info("主窗口UI初始化完成")

    def setup_menu_bar(self) -> None:
        """构建菜单栏。

        创建以下菜单项：
        - 文件菜单（file_menu）：
            - 退出（action_quit）：触发窗口关闭
        - 帮助菜单（help_menu）：
            - 关于（action_about）：显示关于对话框
        """
        self._menu_bar = self.menuBar()
        self._menu_bar.setObjectName("MenuBar")

        # 文件菜单
        file_menu = self._menu_bar.addMenu("文件(&F)")
        file_menu.setObjectName("file_menu")

        action_quit = QAction("退出(&Q)", self)
        action_quit.setObjectName("action_quit")
        action_quit.setShortcut("Ctrl+Q")
        action_quit.triggered.connect(self.close)
        file_menu.addAction(action_quit)

        # 帮助菜单
        help_menu = self._menu_bar.addMenu("帮助(&H)")
        help_menu.setObjectName("help_menu")

        action_about = QAction("关于(&A)", self)
        action_about.setObjectName("action_about")
        action_about.triggered.connect(self._show_about_dialog)
        help_menu.addAction(action_about)

    def setup_tool_bar(self) -> None:
        """构建工具栏。

        创建可移动的工具栏，当前为空。
        后续功能模块可通过addAction动态添加工具栏按钮。
        """
        self._tool_bar = QToolBar("主工具栏", self)
        self._tool_bar.setObjectName("ToolBar")
        self._tool_bar.setMovable(True)
        self._tool_bar.setIconSize(QSize(24, 24))
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, self._tool_bar)

    def setup_central_widget(self) -> None:
        """构建中央工作区。

        使用QStackedWidget作为容器，支持多页面切换。
        默认添加欢迎页面（索引0），显示应用名称和版本信息。
        后续业务页面通过addWidget添加到StackedWidget中。
        """
        self._central_widget = QStackedWidget()
        self._central_widget.setObjectName("CentralStack")

        # 创建欢迎页面
        welcome_page = QWidget()
        welcome_page.setObjectName("welcome_page")

        page_layout = QVBoxLayout(welcome_page)
        page_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        welcome_label = QLabel("ECBM Application v0.1.0")
        welcome_label.setObjectName("welcome_label")
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        welcome_label.setFont(font)

        page_layout.addWidget(welcome_label)
        self._central_widget.addWidget(welcome_page)

        self.setCentralWidget(self._central_widget)

    def setup_status_bar(self) -> None:
        """构建状态栏。

        创建底部状态栏，默认显示"就绪"消息。
        长时间操作时通过showMessage显示进度信息。
        """
        self._status_bar = self.statusBar()
        self._status_bar.setObjectName("StatusBar")
        self._status_bar.showMessage("就绪", 0)

    def set_controller(self, controller: BaseController) -> None:
        """注入业务控制器。

        将BaseController实例关联到主窗口，
        后续UI交互通过controller调用业务逻辑。

        参数:
            controller: BaseController子类实例。
        """
        self._controller = controller
        self._logger.info(
            f"业务控制器已注入: {controller.__class__.__name__}"
        )

    def load_qss(self, file_name: str) -> None:
        """加载QSS样式表文件。

        从resources/styles/目录加载指定QSS文件并应用到全局。
        加载失败时记录警告日志但不抛出异常。

        参数:
            file_name: QSS文件名（不含路径，如"base.qss"）。

        异常:
            UIException: QSS文件不存在或读取失败时抛出（内部捕获，不中断启动）。
        """
        qss_path = get_resource_path(f"styles/{file_name}")

        # 也尝试从app_ui/styles/目录加载（开发时的备用路径）
        if not qss_path.exists():
            qss_path = get_project_root() / "app_ui" / "styles" / file_name

        if not qss_path.exists():
            self._logger.warning(f"QSS样式文件不存在: {qss_path}")
            return

        try:
            with open(qss_path, "r", encoding="utf-8") as f:
                qss_content = f.read()
            self.setStyleSheet(qss_content)
            self._logger.info(f"QSS样式表已加载: {file_name}")
        except Exception as e:
            self._logger.error(f"加载QSS样式表失败: {e}")

    def show_message(
        self, title: str, message: str, msg_type: str = "info"
    ) -> None:
        """显示消息对话框。

        参数:
            title: 对话框标题。
            message: 消息内容文本。
            msg_type: 消息类型（"info"/"warning"/"error"/"question"）。
        """
        msg_map = {
            "info": QMessageBox.Icon.Information,
            "warning": QMessageBox.Icon.Warning,
            "error": QMessageBox.Icon.Critical,
            "question": QMessageBox.Icon.Question,
        }
        icon = msg_map.get(msg_type, QMessageBox.Icon.Information)
        QMessageBox(icon, title, message, parent=self).exec()

    def _show_about_dialog(self) -> None:
        """显示关于对话框。

        展示应用名称、版本、技术栈等信息。
        """
        config = ConfigManager.get_instance()
        app_name = config.get("app_name", "ECBM")
        version = config.get("version", "0.1.0")

        about_text = (
            f"<h3>{app_name}</h3>"
            f"<p>版本: {version}</p>"
            "<p>基于 Python 3.14.4 + PyQt 6 构建的通用桌面应用框架</p>"
            "<p>采用经典四层分层架构设计</p>"
            "<hr>"
            "<p>许可证: GPL-3.0-only</p>"
        )
        QMessageBox.about(self, f"关于 {app_name}", about_text)

    def closeEvent(self, event: QCloseEvent) -> None:
        """重写关闭事件，处理优雅退出流程。

        退出流程：
        1. 发送app_quitting信号通知各模块
        2. 关闭所有正在运行的工作线程
        3. 销毁已注册的服务
        4. 关闭数据库连接
        5. 记录退出日志
        6. 接受关闭事件

        参数:
            event: Qt关闭事件对象。
        """
        self._logger.info("收到窗口关闭请求，开始优雅退出流程...")

        # 1. 广播退出信号
        self._signals.app_quitting.emit()

        # 2. 销毁控制器中的服务
        if self._controller is not None:
            try:
                self._controller.dispose()
            except Exception as e:
                self._logger.error(f"控制器销毁时出错: {e}")

        # 3. 记录退出日志
        self._logger.info("应用程序正常退出")

        # 4. 接受关闭事件
        event.accept()
