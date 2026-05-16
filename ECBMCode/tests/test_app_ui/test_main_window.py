# -*- coding: utf-8 -*-
"""MainWindow单元测试模块。

测试覆盖：
- 主窗口创建和基本属性验证
- UI组件初始化（setup_ui）
- 菜单栏和工具栏构建
- 控制器注入
- 信号声明验证
"""

import pytest
from PyQt6.QtWidgets import QMenuBar, QToolBar, QStatusBar, QStackedWidget

from app_ui.main_window import MainWindow
from app_ui.signals import SharedSignals
from app_core.controllers.base_controller import BaseController


class TestMainWindowCreation:
    """主窗口创建测试。"""

    def test_window_created(self, qapp) -> None:
        """验证主窗口可以正常创建。"""
        window = MainWindow()
        assert window is not None
        assert window.windowTitle() == "ECBM Application"
        assert window.objectName() == "MainWindow"

    def test_window_minimum_size(self, qapp) -> None:
        """验证主窗口最小尺寸设置。"""
        window = MainWindow()
        min_size = window.minimumSize()
        assert min_size.width() >= 800
        assert min_size.height() >= 600

    def test_setup_ui_creates_components(self, qapp) -> None:
        """验证setup_ui创建所有UI组件。"""
        window = MainWindow()
        window.setup_ui()
        assert window._menu_bar is not None
        assert window._tool_bar is not None
        assert window._status_bar is not None
        assert window._central_widget is not None

    def test_setup_ui_idempotent(self, qapp) -> None:
        """验证setup_ui可以安全地多次调用。"""
        window = MainWindow()
        window.setup_ui()
        window.setup_ui()
        assert window._central_widget is not None


class TestMainWindowComponents:
    """主窗口组件测试。"""

    def test_menu_bar_has_file_menu(self, qapp) -> None:
        """验证菜单栏包含文件菜单。"""
        window = MainWindow()
        window.setup_ui()
        menu_bar = window.menuBar()
        actions = menu_bar.actions()
        menu_texts = [a.text() for a in actions]
        assert any("文件" in t for t in menu_texts)

    def test_menu_bar_has_help_menu(self, qapp) -> None:
        """验证菜单栏包含帮助菜单。"""
        window = MainWindow()
        window.setup_ui()
        menu_bar = window.menuBar()
        actions = menu_bar.actions()
        menu_texts = [a.text() for a in actions]
        assert any("帮助" in t for t in menu_texts)

    def test_tool_bar_is_movable(self, qapp) -> None:
        """验证工具栏可移动。"""
        window = MainWindow()
        window.setup_ui()
        assert window._tool_bar.isMovable() is True

    def test_central_widget_is_stacked(self, qapp) -> None:
        """验证中央工作区为QStackedWidget。"""
        window = MainWindow()
        window.setup_ui()
        assert isinstance(window._central_widget, QStackedWidget)
        # 默认至少有一个欢迎页面
        assert window._central_widget.count() >= 1


class TestMainWindowController:
    """控制器注入测试。"""

    def test_set_controller(self, qapp) -> None:
        """验证控制器注入成功。"""
        window = MainWindow()
        controller = BaseController()
        window.set_controller(controller)
        assert window._controller is controller

    def test_controller_none_by_default(self, qapp) -> None:
        """验证默认无控制器。"""
        window = MainWindow()
        assert window._controller is None


class TestSharedSignals:
    """共享信号测试。"""

    def test_singleton(self) -> None:
        """验证SharedSignals为单例。"""
        sig1 = SharedSignals()
        sig2 = SharedSignals()
        assert sig1 is sig2

    def test_signals_declared(self) -> None:
        """验证所有共享信号已声明。"""
        signals = SharedSignals()
        assert hasattr(signals, "app_started")
        assert hasattr(signals, "app_quitting")
        assert hasattr(signals, "config_changed")
        assert hasattr(signals, "language_changed")
