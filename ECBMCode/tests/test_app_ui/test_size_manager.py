# -*- coding: utf-8 -*-
"""SizeManager 模块单元测试。

测试尺寸计算、防抖机制和信号发射功能。
"""

import pytest
from PyQt6.QtCore import QTimer

from app_ui.size_manager import SizeManager


class TestSizeManagerCalculate:
    """尺寸计算功能测试。"""

    def test_calculate_typical_window(self) -> None:
        """典型窗口尺寸（1186x733）计算结果验证。"""
        sm = SizeManager(ref_width=1186, ref_height=733)
        sizes = sm.calculate_sizes(1186, 733)

        # 验证所有必要键存在
        expected_keys = [
            "toolbar_width", "toolbar_icon_size",
            "panel_title_font", "panel_body_font", "panel_small_font",
            "general_margin", "general_padding", "border_radius",
            "splitter_handle_width", "button_height", "input_height",
            "icon_size_small", "icon_size_medium",
        ]
        for key in expected_keys:
            assert key in sizes, f"缺少键: {key}"

    def test_calculate_returns_window_info(self) -> None:
        """计算结果应包含窗口宽高信息。"""
        sm = SizeManager(ref_width=1024, ref_height=768)
        sizes = sm.calculate_sizes(1000, 600)
        assert sizes["window_width"] == 1000
        assert sizes["window_height"] == 600

    def test_toolbar_width_reasonable(self) -> None:
        """典型窗口工具栏宽度应在合理范围。"""
        sm = SizeManager(ref_width=1186, ref_height=733)
        sizes = sm.calculate_sizes(1186, 733)
        assert 40 <= sizes["toolbar_width"] <= 60

    def test_title_font_reasonable(self) -> None:
        """典型窗口标题字体大小应在合理范围。"""
        sm = SizeManager(ref_width=1186, ref_height=733)
        sizes = sm.calculate_sizes(1186, 733)
        assert 11 <= sizes["panel_title_font"] <= 22

    def test_large_window_sizes(self) -> None:
        """大窗口（2560x1440）计算结果应为正值。"""
        sm = SizeManager(ref_width=2560, ref_height=1440)
        sizes = sm.calculate_sizes(2560, 1440)
        for key, value in sizes.items():
            if isinstance(value, (int, float)):
                assert value > 0, f"键 '{key}' 的值 {value} 不为正数"

    def test_small_window_sizes(self) -> None:
        """小窗口（800x500）计算结果不应低于最小值。"""
        sm = SizeManager(ref_width=800, ref_height=500)
        sizes = sm.calculate_sizes(800, 500)
        assert sizes["toolbar_width"] >= 40
        assert sizes["panel_title_font"] >= 11
        assert sizes["panel_body_font"] >= 10


class TestSizeManagerThrottle:
    """防抖机制测试。"""

    def test_throttle_timer_created(self) -> None:
        """SizeManager应创建防抖定时器。"""
        sm = SizeManager()
        assert sm._throttle_timer is not None
        assert sm._throttle_timer.isSingleShot()

    def test_set_throttle(self) -> None:
        """设置防抖间隔应更新内部值。"""
        sm = SizeManager(throttle_ms=200)
        assert sm._throttle_ms == 200
        sm.set_throttle(50)
        assert sm._throttle_ms == 50

    def test_small_change_skipped(self, qtbot) -> None:
        """小于5px的尺寸变化应跳过。"""
        sm = SizeManager(ref_width=1000, ref_height=600)
        signal_received = []

        sm.size_changed.connect(lambda d: signal_received.append(d))

        # 微小变化应跳过
        sm.on_resize(1002, 601)
        assert signal_received == []  # 防抖未到期，不应发射信号

    def test_large_change_triggers_throttle(self, qtbot) -> None:
        """大于5px的尺寸变化应触发防抖。"""
        sm = SizeManager(ref_width=1000, ref_height=600, throttle_ms=50)
        signal_received = []

        sm.size_changed.connect(lambda d: signal_received.append(d))
        sm.on_resize(1100, 700)

        # 等待防抖到期
        def check():
            assert len(signal_received) >= 1

        qtbot.wait_until(check, timeout=500)

    def test_recalculate_immediate(self) -> None:
        """recalculate应跳过防抖立即计算。"""
        sm = SizeManager(ref_width=1000, ref_height=600)
        signal_received = []

        sm.size_changed.connect(lambda d: signal_received.append(d))
        sm._pending_size = (1100, 700)
        sm.recalculate()

        assert len(signal_received) == 1
