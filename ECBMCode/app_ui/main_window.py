# -*- coding: utf-8 -*-
"""应用主窗口模块。

MainWindow继承自PyQt6的QMainWindow，实现：
- 黄金比例窗口尺寸计算
- 三栏布局（左侧竖向工具栏 + QSplitter三栏容器）
- 主题管理器集成（暗色/亮色切换）
- 尺寸管理器集成（动态比例尺寸计算）
- QSS样式表加载
- 优雅退出流程
"""

from pathlib import Path

from PyQt6.QtWidgets import (
    QMainWindow, QMenuBar, QStatusBar,
    QWidget, QHBoxLayout, QMessageBox,
    QApplication,
)
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QAction, QCloseEvent, QResizeEvent

from app_core.controllers.base_controller import BaseController
from app_ui.signals import SharedSignals
from app_infra.config.config_manager import ConfigManager
from app_infra.logging.log_manager import LogManager
from app_ui.theme_manager import ThemeManager
from app_ui.size_manager import SizeManager
from app_ui.widgets.vertical_tool_bar import VerticalToolBar
from app_ui.widgets.splitter_panels import SplitterPanels


def calculate_golden_window_size(screen) -> tuple[int, int]:
    """根据屏幕可用区域计算黄金比例窗口尺寸。

    窗口宽度 = min(屏幕宽, 屏幕高) * 0.618，
    窗口高度 = 窗口宽度 * 0.618，
    结果受最小/最大约束限制。

    参数:
        screen: QScreen对象。

    返回:
        tuple[int, int]: (窗口宽度, 窗口高度)。
    """
    geo = screen.availableGeometry()
    sw, sh = geo.width(), geo.height()
    base = min(sw, sh)
    w = round(base * 0.618)
    h = round(w * 0.618)
    w = max(800, min(w, int(sw * 0.9)))
    h = max(500, min(h, int(sh * 0.9)))
    return w, h


class MainWindow(QMainWindow):
    """应用主窗口。

    采用全新三栏布局结构：
    - 顶部菜单栏（QMenuBar）：文件/视图/帮助菜单
    - 中央区域（QHBoxLayout）：左侧工具栏 + QSplitter三栏
    - 底部状态栏（QStatusBar）：应用状态显示

    属性:
        _controller: 关联的业务控制器。
        _menu_bar: 菜单栏对象。
        _status_bar: 状态栏对象。
        _central_container: 中央容器QWidget。
        _vertical_tool_bar: 左侧竖向工具栏。
        _splitter_panels: 三栏分割面板容器。
        _theme_manager: 主题管理器单例。
        _size_manager: 尺寸管理器实例。
        _signals: 共享信号实例。
        _logger: 日志记录器。
    """

    def __init__(self) -> None:
        """初始化主窗口。

        获取屏幕分辨率并计算黄金比例窗口尺寸，
        设置窗口基本属性后居中显示。
        """
        super().__init__()
        self._controller: BaseController | None = None
        self._menu_bar: QMenuBar | None = None
        self._status_bar: QStatusBar | None = None
        self._central_container: QWidget | None = None
        self._vertical_tool_bar: VerticalToolBar | None = None
        self._splitter_panels: SplitterPanels | None = None
        self._theme_manager: ThemeManager = ThemeManager.get_instance()
        self._size_manager: SizeManager | None = None
        self._signals: SharedSignals = SharedSignals()
        self._logger: logging.Logger = LogManager().get_logger(
            self.__class__.__name__
        )
        self._save_size_timer: QTimer = QTimer(self)
        self._save_size_timer.setSingleShot(True)
        self._save_size_timer.timeout.connect(self._save_window_size)

        # 计算窗口尺寸
        config = ConfigManager.get_instance()
        screen = QApplication.primaryScreen()
        if screen is not None:
            golden_w, golden_h = calculate_golden_window_size(screen)
        else:
            # headless环境回退
            golden_w, golden_h = 1024, 768

        # 从配置读取已保存尺寸，首次启动使用黄金比例计算值
        saved_w = config.get("window_width", golden_w)
        saved_h = config.get("window_height", golden_h)

        min_width = config.get("window_min_width", 800)
        min_height = config.get("window_min_height", 500)

        self.setObjectName("MainWindow")
        self.setWindowTitle("ECBM")
        self.resize(saved_w, saved_h)
        self.setMinimumSize(min_width, min_height)

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

        按顺序构建：主题管理器 -> 尺寸管理器 -> 菜单栏 ->
        状态栏 -> 中央容器 -> 工具栏 -> 三栏面板 -> QSS加载。
        """
        self._setup_theme_manager()
        self._setup_size_manager()
        self.setup_menu_bar()
        self.setup_status_bar()
        self._setup_central_area()
        self._setup_vertical_tool_bar()
        self._setup_splitter_panels()
        self._connect_signals()
        self._load_theme_qss()
        self._logger.info("主窗口UI初始化完成（新版三栏布局）")

    def _setup_theme_manager(self) -> None:
        """初始化主题管理器。

        从ConfigManager加载已保存的主题偏好。
        """
        config = ConfigManager.get_instance()
        saved_mode = config.get("theme_mode", "system")
        if saved_mode in ("dark", "light", "system"):
            self._theme_manager.set_theme(saved_mode)

    def _setup_size_manager(self) -> None:
        """初始化尺寸管理器。

        以当前窗口尺寸注入SizeManager。
        """
        self._size_manager = SizeManager(
            ref_width=self.width(),
            ref_height=self.height(),
            throttle_ms=100,
        )

    def _setup_central_area(self) -> None:
        """构建中央区域容器。

        创建QHBoxLayout的水平布局容器（margin=0, spacing=0），
        替换原有中心控件。
        """
        self._central_container = QWidget()
        self._central_container.setObjectName("CentralContainer")

        central_layout = QHBoxLayout(self._central_container)
        central_layout.setContentsMargins(0, 0, 0, 0)
        central_layout.setSpacing(0)

        self.setCentralWidget(self._central_container)

    def _setup_vertical_tool_bar(self) -> None:
        """构建左侧竖向工具栏。

        注册默认工具按钮并添加到中央容器最左侧。
        """
        self._vertical_tool_bar = VerticalToolBar(self._central_container)
        self._vertical_tool_bar.setup_ui()

        # 应用尺寸
        if self._size_manager is not None:
            sizes = self._size_manager.calculate_sizes(
                self.width(), self.height()
            )
            self._vertical_tool_bar.setFixedWidth(
                sizes.get("toolbar_width", 48)
            )

        # 注册默认工具按钮
        self._vertical_tool_bar.register_tool(
            "file_explorer", "📁", "文件浏览器"
        )
        self._vertical_tool_bar.register_tool(
            "url_input", "🔗", "URL链接输入"
        )
        self._vertical_tool_bar.register_tool(
            "convert_tasks", "🔄", "转换任务列表"
        )
        self._vertical_tool_bar.register_tool(
            "settings", "⚙", "设置"
        )

        # 添加到中央容器布局
        central_layout = self._central_container.layout()
        if central_layout is not None:
            central_layout.addWidget(self._vertical_tool_bar)

        # 默认选中第一个工具
        self._vertical_tool_bar.switch_to_tool("file_explorer")

    def _setup_splitter_panels(self) -> None:
        """构建三栏分割面板。

        添加到中央容器最右侧（stretch=1占据剩余空间）。
        """
        self._splitter_panels = SplitterPanels(
            self._central_container
        )
        self._splitter_panels.setup_ui()

        # 计算初始三栏尺寸
        toolbar_w = 48
        if self._vertical_tool_bar is not None:
            toolbar_w = self._vertical_tool_bar.width()
        available_w = self.width() - toolbar_w - 8  # 2个handle x 4px
        base = max(1, available_w // 10)
        self._splitter_panels.setSizes(
            [base * 3, base * 4, base * 3]
        )

        # 添加到中央容器布局
        central_layout = self._central_container.layout()
        if central_layout is not None:
            central_layout.addWidget(self._splitter_panels, 1)

    def _connect_signals(self) -> None:
        """连接全局信号到主窗口槽函数。"""
        signals = self._signals

        # 主题切换
        signals.theme_changed.connect(self._on_theme_changed)
        self._theme_manager.theme_changed.connect(self._on_theme_changed)

        # 尺寸变更
        if self._size_manager is not None:
            self._size_manager.size_changed.connect(self._on_size_changed)

        # 工具栏工具选中
        if self._vertical_tool_bar is not None:
            self._vertical_tool_bar.tool_selected.connect(
                self._on_tool_selected
            )

        # 源文件加载 -> 状态栏显示
        signals.source_loaded.connect(self._on_source_loaded)

        # 左栏源选择 -> 中栏加载内容
        if (
            self._splitter_panels is not None
            and self._splitter_panels.left_panel is not None
        ):
            self._splitter_panels.left_panel.source_selected.connect(
                self._on_source_selected
            )

        # 右栏转换请求
        if (
            self._splitter_panels is not None
            and self._splitter_panels.right_panel is not None
        ):
            self._splitter_panels.right_panel.convert_requested.connect(
                self._on_convert_requested
            )

    def _load_theme_qss(self) -> None:
        """加载当前主题的QSS样式表。

        在setup_ui末尾调用，避免窗口先显示无样式再突变。
        """
        effective = self._theme_manager.get_effective_theme()
        self._apply_theme(effective)

    def _apply_theme(self, theme_name: str) -> None:
        """应用指定主题的QSS和面板样式。

        参数:
            theme_name: 主题名称（"dark"或"light"）。
        """
        qss_content = self._theme_manager.load_qss(theme_name)
        app = QApplication.instance()
        if app is not None:
            app.setStyleSheet(qss_content)

        # 更新工具栏主题
        if self._vertical_tool_bar is not None:
            self._vertical_tool_bar.update_theme(theme_name)

        # 更新三栏面板主题
        if self._splitter_panels is not None:
            self._splitter_panels.update_theme(theme_name)

    def _save_window_size(self) -> None:
        """异步保存当前窗口尺寸到ConfigManager。"""
        config = ConfigManager.get_instance()
        config.set_runtime("window_width", self.width())
        config.set_runtime("window_height", self.height())

    # ---- 信号槽 ----

    def _on_theme_changed(self, theme_name: str) -> None:
        """主题切换信号回调。

        参数:
            theme_name: 实际主题名（"dark"或"light"）。
        """
        self._apply_theme(theme_name)
        self._logger.info(f"主题已切换至: {theme_name}")

    def _on_size_changed(self, sizes: dict) -> None:
        """尺寸变更信号回调。

        将新尺寸分发到所有UI组件。

        参数:
            sizes: SizeManager计算输出的尺寸字典。
        """
        if self._vertical_tool_bar is not None:
            self._vertical_tool_bar.update_sizes(sizes)
        if self._splitter_panels is not None:
            self._splitter_panels.update_sizes(sizes)

        # 异步保存窗口尺寸
        if self._save_size_timer.isActive():
            self._save_size_timer.stop()
        self._save_size_timer.start(500)

    def _on_tool_selected(self, tool_id: str) -> None:
        """工具栏工具选中回调。

        根据tool_id路由执行对应逻辑。

        参数:
            tool_id: 被选中的工具ID。
        """
        self._logger.info(f"工具已选中: {tool_id}")
        self._signals.tool_changed.emit(tool_id)

        # 根据不同工具ID路由到不同面板行为
        # file_explorer/url_input -> 左栏获取焦点
        # convert_tasks -> 右栏获取焦点
        # settings -> 预留设置面板

    def _on_source_loaded(self, source: str) -> None:
        """源文件加载信号回调。

        在状态栏显示加载信息。

        参数:
            source: 源文件路径或URL。
        """
        if self._status_bar is not None:
            self._status_bar.showMessage(f"已加载: {source}", 5000)

        # 添加到左栏历史
        if (
            self._splitter_panels is not None
            and self._splitter_panels.left_panel is not None
        ):
            self._splitter_panels.left_panel.add_history_item(source)

    def _on_source_selected(self, source: str) -> None:
        """源文件选择回调（来自左栏）。

        通知中栏加载内容并发射全局信号。

        参数:
            source: 源文件路径或URL。
        """
        self._signals.source_loaded.emit(source)

        # 尝试读取文件内容加载到中栏
        try:
            file_path = Path(source)
            if file_path.exists() and file_path.is_file():
                content = file_path.read_text(encoding="utf-8")
                if (
                    self._splitter_panels is not None
                    and self._splitter_panels.center_panel is not None
                ):
                    self._splitter_panels.center_panel.load_content(content)
            else:
                # URL或其他内容，直接显示在编辑器中
                if (
                    self._splitter_panels is not None
                    and self._splitter_panels.center_panel is not None
                ):
                    self._splitter_panels.center_panel.load_content(
                        f"# 已加载: {source}\n\n（不支持直接预览此内容类型）"
                    )
        except Exception as e:
            self._logger.warning(f"加载源文件内容失败: {e}")

    def _on_convert_requested(self, params: dict) -> None:
        """转换请求信号回调（来自右栏）。

        转发到业务控制器处理转换任务。

        参数:
            params: 转换参数字典。
        """
        self._logger.info(f"收到转换请求: {params}")
        # 预留：通过controller创建工作线程执行转换
        # 转换完成后的处理逻辑在工作线程的finished信号中执行

    # ---- 事件重写 ----

    def resizeEvent(self, event: QResizeEvent) -> None:
        """窗口尺寸变更事件。

        触发SizeManager防抖重算并通知所有组件。

        参数:
            event: 尺寸变更事件。
        """
        super().resizeEvent(event)

        if self._size_manager is not None:
            self._size_manager.on_resize(
                event.size().width(),
                event.size().height(),
            )

    def closeEvent(self, event: QCloseEvent) -> None:
        """重写关闭事件，处理优雅退出流程。

        退出流程：
        1. 保存当前窗口尺寸
        2. 广播app_quitting信号
        3. 销毁控制器中的服务
        4. 记录退出日志
        5. 接受关闭事件

        参数:
            event: Qt关闭事件对象。
        """
        self._logger.info("收到窗口关闭请求，开始优雅退出流程...")

        # 同步保存窗口尺寸
        self._save_window_size()

        # 广播退出信号
        self._signals.app_quitting.emit()

        # 销毁控制器中的服务
        if self._controller is not None:
            try:
                self._controller.dispose()
            except Exception as e:
                self._logger.error(f"控制器销毁时出错: {e}")

        self._logger.info("应用程序正常退出")
        event.accept()

    # ---- 菜单栏（保留原有设计） ----

    def setup_menu_bar(self) -> None:
        """构建菜单栏。

        创建以下菜单项：
        - 文件菜单：退出
        - 视图菜单：切换主题
        - 帮助菜单：关于
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

        # 视图菜单
        view_menu = self._menu_bar.addMenu("视图(&V)")
        view_menu.setObjectName("view_menu")

        action_toggle_theme = QAction("切换主题(&T)", self)
        action_toggle_theme.setObjectName("action_toggle_theme")
        action_toggle_theme.triggered.connect(
            lambda: self._theme_manager.toggle_theme()
        )
        view_menu.addAction(action_toggle_theme)

        # 帮助菜单
        help_menu = self._menu_bar.addMenu("帮助(&H)")
        help_menu.setObjectName("help_menu")

        action_about = QAction("关于(&A)", self)
        action_about.setObjectName("action_about")
        action_about.triggered.connect(self._show_about_dialog)
        help_menu.addAction(action_about)

    def setup_status_bar(self) -> None:
        """构建底部状态栏。

        默认显示"就绪"消息。
        """
        self._status_bar = self.statusBar()
        self._status_bar.setObjectName("StatusBar")
        self._status_bar.showMessage("就绪", 0)

    # ---- 公共方法 ----

    def set_controller(self, controller: BaseController) -> None:
        """注入业务控制器。

        参数:
            controller: BaseController子类实例。
        """
        self._controller = controller
        self._logger.info(
            f"业务控制器已注入: {controller.__class__.__name__}"
        )

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

    # ---- 私有方法 ----

    def _show_about_dialog(self) -> None:
        """显示关于对话框。"""
        config = ConfigManager.get_instance()
        app_name = config.get("app_name", "ECBM")
        version = config.get("version", "0.1.0")

        about_text = (
            f"<h3>{app_name}</h3>"
            f"<p>版本: {version}</p>"
            "<p>基于 Python 3.14.4 + PyQt 6 构建的通用桌面应用框架</p>"
            "<p>采用经典四层分层架构设计</p>"
            "<p>界面特性：三栏布局 / 暗色&亮色双主题 / 动态尺寸适配</p>"
            "<hr>"
            "<p>许可证: GPL-3.0-only</p>"
        )
        QMessageBox.about(self, f"关于 {app_name}", about_text)
