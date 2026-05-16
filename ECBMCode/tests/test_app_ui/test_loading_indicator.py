# -*- coding: utf-8 -*-
"""LoadingIndicator 模块单元测试。

测试加载指示器的启动/停止、尺寸设置和生命周期。
"""

import pytest
from PyQt6.QtWidgets import QWidget

from app_ui.widgets.loading_indicator import LoadingIndicator


class TestLoadingIndicatorCreation:
    """加载指示器创建测试。"""

    def test_default_creation(self, qapp) -> None:
        """默认参数创建应成功。"""
        indicator = LoadingIndicator()
        assert indicator is not None
        assert indicator.is_running() is False
        assert not indicator.isVisible()

    def test_custom_size(self, qapp) -> None:
        """自定义尺寸应正确设置。"""
        indicator = LoadingIndicator(size=48)
        assert indicator._size_hint == 48
        assert indicator.width() == 48
        assert indicator.height() == 48

    def test_custom_color(self, qapp) -> None:
        """自定义颜色应正确设置。"""
        indicator = LoadingIndicator(color="#FF0000")
        assert indicator._color.name() == "#ff0000"


class TestLoadingIndicatorLifecycle:
    """加载指示器生命周期测试。"""

    def test_start_shows_and_runs(self, qtbot) -> None:
        """调用start应显示指示器并启动定时器。"""
        indicator = LoadingIndicator()
        indicator.start()
        assert indicator.isVisible()
        assert indicator.is_running()

    def test_stop_hides_and_stops(self, qtbot) -> None:
        """调用stop应停止定时器。"""
        indicator = LoadingIndicator()
        indicator.start()
        indicator.stop()
        assert indicator.is_running() is False

    def test_hide_stops_timer(self, qtbot) -> None:
        """隐藏时应自动停止定时器。"""
        indicator = LoadingIndicator()
        indicator.start()
        assert indicator.is_running()
        indicator.hide()
        assert indicator.is_running() is False

    def test_show_restores_running(self, qtbot) -> None:
        """隐藏后再显示应自动恢复动画（不经过stop的流程）。"""
        indicator = LoadingIndicator()
        indicator.start()
        assert indicator.is_running()
        # 隐藏：定时器停止但_was_running保持True
        indicator.hide()
        assert not indicator.is_running()
        # 显示：因_was_running为True而自动恢复
        indicator.show()
        assert indicator.is_running()


class TestLoadingIndicatorSetters:
    """动态设置方法测试。"""

    def test_set_color(self, qapp) -> None:
        """set_color应更新颜色。"""
        indicator = LoadingIndicator()
        indicator.set_color("#00FF00")
        assert indicator._color.name() == "#00ff00"

    def test_set_size(self, qapp) -> None:
        """set_size应更新组件尺寸和线宽。"""
        indicator = LoadingIndicator(size=32)
        indicator.set_size(64)
        assert indicator._size_hint == 64
        assert indicator.width() == 64
        assert indicator.height() == 64
        assert indicator._arc_width > 0


class TestLoadingIndicatorPaint:
    """绘制功能测试。"""

    def test_paint_event_no_crash_when_hidden(self, qapp) -> None:
        """隐藏状态下paintEvent不应抛出异常。"""
        from PyQt6.QtGui import QPaintEvent
        from PyQt6.QtCore import QRect

        indicator = LoadingIndicator()
        indicator.hide()
        # 模拟绘制事件
        dummy_rect = QRect(0, 0, 32, 32)
        event = QPaintEvent(dummy_rect)
        # 不应抛出异常
        indicator.paintEvent(event)

    def test_paint_event_no_crash_when_visible(self, qapp) -> None:
        """可见状态下paintEvent应正常绘制。"""
        from PyQt6.QtGui import QPaintEvent
        from PyQt6.QtCore import QRect

        indicator = LoadingIndicator()
        indicator.show()
        indicator._angle = 0.5
        dummy_rect = QRect(0, 0, 32, 32)
        event = QPaintEvent(dummy_rect)
        # 不应抛出异常
        indicator.paintEvent(event)

    def test_paint_different_angles(self, qapp) -> None:
        """不同角度值下paintEvent均不应抛出异常。"""
        from PyQt6.QtGui import QPaintEvent
        from PyQt6.QtCore import QRect
        import math

        indicator = LoadingIndicator()
        indicator.show()

        for angle in [0.0, math.pi / 4, math.pi / 2, math.pi, 2 * math.pi]:
            indicator._angle = angle
            dummy_rect = QRect(0, 0, 32, 32)
            event = QPaintEvent(dummy_rect)
            indicator.paintEvent(event)
