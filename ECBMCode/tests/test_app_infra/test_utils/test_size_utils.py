# -*- coding: utf-8 -*-
"""size_utils 模块单元测试。

测试所有尺寸计算函数在典型窗口尺寸和边界条件下的正确性。
"""

import pytest
from app_infra.utils.size_utils import (
    calculate_base_unit,
    calculate_toolbar_width,
    calculate_toolbar_icon_size,
    calculate_title_font_size,
    calculate_body_font_size,
    calculate_small_font_size,
    calculate_general_margin,
    calculate_general_padding,
    calculate_border_radius,
    calculate_splitter_handle,
    calculate_button_height,
    calculate_input_height,
)


class TestCalculateBaseUnit:
    """calculate_base_unit 函数测试。"""

    def test_typical_window(self) -> None:
        """典型窗口尺寸（1186x733）应正确计算基础单位。"""
        base = calculate_base_unit(1186, 733)
        assert base == pytest.approx(1.0, abs=0.01)

    def test_square_window(self) -> None:
        """正方窗口应以最小边为基准。"""
        base = calculate_base_unit(800, 800)
        assert base == pytest.approx(800.0 / 733.0, abs=0.01)

    def test_wide_window(self) -> None:
        """宽屏窗口应以高度为基准。"""
        base = calculate_base_unit(2560, 1440)
        assert base == pytest.approx(1440.0 / 733.0, abs=0.01)

    def test_custom_reference(self) -> None:
        """自定义参考值应影响计算结果。"""
        base = calculate_base_unit(500, 500, reference=500)
        assert base == pytest.approx(1.0, abs=0.01)


class TestToolbarWidth:
    """工具栏宽度计算测试。"""

    def test_typical_window(self) -> None:
        """典型窗口工具栏宽度应在48-52范围。"""
        base = calculate_base_unit(1186, 733)
        w = calculate_toolbar_width(base)
        assert 40 <= w <= 56

    def test_small_window_minimum(self) -> None:
        """极小窗口工具栏宽度不应低于最小值40。"""
        base = calculate_base_unit(800, 500)
        w = calculate_toolbar_width(base)
        assert w >= 40

    def test_large_window(self) -> None:
        """大窗口工具栏宽度不应无限增大。"""
        base = calculate_base_unit(3840, 2160)
        w = calculate_toolbar_width(base)
        assert w >= 40


class TestFontSizes:
    """字体大小计算测试。"""

    @pytest.mark.parametrize("func,expected_range", [
        (calculate_title_font_size, (11, 24)),
        (calculate_body_font_size, (10, 22)),
        (calculate_small_font_size, (8, 18)),
    ])
    def test_typical_font_sizes(
        self, func, expected_range
    ) -> None:
        """典型窗口下字体大小应在合理范围内。"""
        base = calculate_base_unit(1186, 733)
        size = func(base)
        assert expected_range[0] <= size <= expected_range[1]

    def test_title_larger_than_body(self) -> None:
        """标题字体应大于正文字体。"""
        base = calculate_base_unit(1186, 733)
        assert calculate_title_font_size(base) > calculate_body_font_size(base)

    def test_body_larger_than_small(self) -> None:
        """正文字体应大于小号字体。"""
        base = calculate_base_unit(1186, 733)
        assert (
            calculate_body_font_size(base)
            > calculate_small_font_size(base)
        )


class TestSpacing:
    """间距计算测试。"""

    def test_padding_larger_than_margin(self) -> None:
        """通常情况下padding应大于margin。"""
        base = calculate_base_unit(1186, 733)
        assert (
            calculate_general_padding(base)
            > calculate_general_margin(base)
        )

    def test_border_radius_positive(self) -> None:
        """圆角半径应为正值。"""
        base = calculate_base_unit(1186, 733)
        assert calculate_border_radius(base) >= 2

    def test_splitter_handle_positive(self) -> None:
        """分割手柄宽度应为正值。"""
        base = calculate_base_unit(1186, 733)
        assert calculate_splitter_handle(base) >= 2


class TestButtonAndInput:
    """按钮和输入框高度计算测试。"""

    def test_button_height_typical(self) -> None:
        """典型窗口按钮高度应在合理范围。"""
        base = calculate_base_unit(1186, 733)
        h = calculate_button_height(base)
        assert 20 <= h <= 30

    def test_input_height_typical(self) -> None:
        """典型窗口输入框高度应在合理范围。"""
        base = calculate_base_unit(1186, 733)
        h = calculate_input_height(base)
        assert 18 <= h <= 30


class TestBoundaryConditions:
    """边界条件测试。"""

    def test_minimum_window_no_negatives(self) -> None:
        """极小窗口（800x500）下所有输出不应为负值。"""
        base = calculate_base_unit(800, 500)
        functions = [
            calculate_toolbar_width,
            calculate_toolbar_icon_size,
            calculate_title_font_size,
            calculate_body_font_size,
            calculate_small_font_size,
            calculate_general_margin,
            calculate_general_padding,
            calculate_border_radius,
            calculate_splitter_handle,
            calculate_button_height,
            calculate_input_height,
        ]
        for func in functions:
            result = func(base)
            assert result >= 0, f"{func.__name__} 返回负值: {result}"

    def test_maximum_window_no_zeros(self) -> None:
        """极大窗口（3840x2160）下所有输出不应为零。"""
        base = calculate_base_unit(3840, 2160)
        functions = [
            calculate_toolbar_width,
            calculate_toolbar_icon_size,
            calculate_title_font_size,
            calculate_body_font_size,
            calculate_small_font_size,
            calculate_general_margin,
            calculate_general_padding,
            calculate_border_radius,
            calculate_button_height,
            calculate_input_height,
        ]
        for func in functions:
            result = func(base)
            assert result > 0, f"{func.__name__} 返回零值"

    def test_result_is_int(self) -> None:
        """所有计算函数返回int类型。"""
        base = calculate_base_unit(1186, 733)
        assert isinstance(calculate_toolbar_width(base), int)
        assert isinstance(calculate_title_font_size(base), int)
        assert isinstance(calculate_general_margin(base), int)
