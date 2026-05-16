# -*- coding: utf-8 -*-
"""MainWindow单元测试模块。

测试覆盖：
- 主窗口创建和基本属性验证
- UI组件初始化（setup_ui三栏布局）
- 菜单栏构建（含视图菜单）
- 控制器注入
- 黄金比例窗口尺寸计算
- 信号声明验证
"""

import pytest
from PyQt6.QtWidgets import QMenuBar, QStatusBar, QWidget, QApplication

from app_ui.main_window import MainWindow, calculate_golden_window_size
from app_ui.signals import SharedSignals
from app_core.controllers.base_controller import BaseController


class TestGoldenWindowSize:
    """黄金比例窗口尺寸计算测试。"""

    def test_calculate_typical_screen(self, qapp) -> None:
        """典型屏幕（1920x1080）应返回合理尺寸。"""
        screen = QApplication.primaryScreen()
        if screen is not None:
            w, h = calculate_golden_window_size(screen)
            assert w >= 800
            assert h >= 500

    def test_calculate_respects_minimums(self, qapp) -> None:
        """屏幕尺寸计算应遵守最小约束。"""
        screen = QApplication.primaryScreen()
        if screen is not None:
            w, h = calculate_golden_window_size(screen)
            assert w >= 800
            assert h >= 500


class TestMainWindowCreation:
    """主窗口创建测试。"""

    def test_window_created(self, qapp) -> None:
        """验证主窗口可以正常创建。"""
        window = MainWindow()
        assert window is not None
        assert window.windowTitle() == "ECBM"
        assert window.objectName() == "MainWindow"

    def test_window_minimum_size(self, qapp) -> None:
        """验证主窗口最小尺寸设置。"""
        window = MainWindow()
        min_size = window.minimumSize()
        assert min_size.width() >= 800
        assert min_size.height() >= 500

    def test_setup_ui_creates_components(self, qapp) -> None:
        """验证setup_ui创建所有UI组件（新版三栏布局）。"""
        window = MainWindow()
        window.setup_ui()
        assert window._menu_bar is not None
        assert window._status_bar is not None
        assert window._central_container is not None
        assert window._vertical_tool_bar is not None
        assert window._splitter_panels is not None
        assert window._theme_manager is not None
        assert window._size_manager is not None

    def test_splitter_panels_have_three_tabs(self, qapp) -> None:
        """验证三栏面板容器包含左中右三个面板。"""
        window = MainWindow()
        window.setup_ui()
        splitter = window._splitter_panels
        assert splitter is not None
        assert splitter.left_panel is not None
        assert splitter.center_panel is not None
        assert splitter.right_panel is not None
        assert splitter.count() == 3

    def test_vertical_tool_bar_has_buttons(self, qapp) -> None:
        """验证工具栏注册了默认工具按钮。"""
        window = MainWindow()
        window.setup_ui()
        toolbar = window._vertical_tool_bar
        assert toolbar is not None
        assert "file_explorer" in toolbar._buttons
        assert "url_input" in toolbar._buttons
        assert "convert_tasks" in toolbar._buttons
        assert "settings" in toolbar._buttons


class TestMainWindowMenuBar:
    """菜单栏测试。"""

    def test_menu_bar_has_file_menu(self, qapp) -> None:
        """验证菜单栏包含文件菜单。"""
        window = MainWindow()
        window.setup_ui()
        menu_bar = window.menuBar()
        actions = menu_bar.actions()
        menu_texts = [a.text() for a in actions]
        assert any("文件" in t for t in menu_texts)

    def test_menu_bar_has_view_menu(self, qapp) -> None:
        """验证菜单栏包含视图菜单。"""
        window = MainWindow()
        window.setup_ui()
        menu_bar = window.menuBar()
        actions = menu_bar.actions()
        menu_texts = [a.text() for a in actions]
        assert any("视图" in t for t in menu_texts)

    def test_menu_bar_has_help_menu(self, qapp) -> None:
        """验证菜单栏包含帮助菜单。"""
        window = MainWindow()
        window.setup_ui()
        menu_bar = window.menuBar()
        actions = menu_bar.actions()
        menu_texts = [a.text() for a in actions]
        assert any("帮助" in t for t in menu_texts)

    def test_view_menu_has_theme_action(self, qapp) -> None:
        """验证视图菜单包含主题切换动作。"""
        window = MainWindow()
        window.setup_ui()
        menu_bar = window.menuBar()
        for action in menu_bar.actions():
            if "视图" in action.text():
                submenu = action.menu()
                if submenu is not None:
                    sub_actions = submenu.actions()
                    sub_texts = [a.text() for a in sub_actions]
                    assert any("主题" in t for t in sub_texts), (
                        "视图菜单缺少主题切换选项"
                    )


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


class TestMainWindowTheme:
    """主题管理集成测试。"""

    def test_theme_manager_accessible(self, qapp) -> None:
        """验证主窗口可访问主题管理器。"""
        window = MainWindow()
        assert window._theme_manager is not None

    def test_size_manager_accessible(self, qapp) -> None:
        """验证主窗口可访问尺寸管理器。"""
        window = MainWindow()
        window.setup_ui()
        assert window._size_manager is not None


class TestSharedSignals:
    """共享信号测试。"""

    def test_singleton(self) -> None:
        """验证SharedSignals为单例。"""
        sig1 = SharedSignals()
        sig2 = SharedSignals()
        assert sig1 is sig2

    def test_signals_declared(self) -> None:
        """验证所有共享信号已声明（含新增UI信号）。"""
        signals = SharedSignals()
        assert hasattr(signals, "app_started")
        assert hasattr(signals, "app_quitting")
        assert hasattr(signals, "config_changed")
        assert hasattr(signals, "language_changed")
        assert hasattr(signals, "theme_changed")
        assert hasattr(signals, "size_changed")
        assert hasattr(signals, "tool_changed")
        assert hasattr(signals, "source_loaded")
