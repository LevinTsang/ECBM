# -*- coding: utf-8 -*-
"""尺寸计算底层工具函数模块。

提供纯数学计算的尺寸工具函数，不依赖PyQt6，
供app_ui层SizeManager调用。
所有计算基于基础单位（base_unit）乘以固定系数。
"""

import math


def calculate_base_unit(
    width: int, height: int, reference: int = 733
) -> float:
    """计算基础单位值。

    基础单位 = min(宽度, 高度) / reference，
    所有其他尺寸计算均基于此单位乘以系数。

    参数:
        width: 窗口宽度（像素）。
        height: 窗口高度（像素）。
        reference: 基准参考高度值，默认733。

    返回:
        float: 基础单位值。
    """
    return min(width, height) / reference


def calculate_toolbar_width(base: float) -> int:
    """计算左侧工具栏宽度。

    对应基准宽度的4%。

    参数:
        base: 基础单位值。

    返回:
        int: 工具栏宽度（像素），最小40。
    """
    return max(40, int(base * 29))


def calculate_toolbar_icon_size(base: float) -> int:
    """计算工具栏图标尺寸。

    对应基准高度的2.8%。

    参数:
        base: 基础单位值。

    返回:
        int: 图标尺寸（像素），最小14。
    """
    return max(14, int(base * 21))


def calculate_title_font_size(base: float) -> int:
    """计算面板标题字体大小。

    对应基准高度的2.2%。

    参数:
        base: 基础单位值。

    返回:
        int: 字体大小（像素），最小11。
    """
    return max(11, int(base * 16))


def calculate_body_font_size(base: float) -> int:
    """计算正文字体大小。

    对应基准高度的1.8%。

    参数:
        base: 基础单位值。

    返回:
        int: 字体大小（像素），最小10。
    """
    return max(10, int(base * 13))


def calculate_small_font_size(base: float) -> int:
    """计算小号字体大小。

    对应基准高度的1.4%。

    参数:
        base: 基础单位值。

    返回:
        int: 字体大小（像素），最小8。
    """
    return max(8, int(base * 10))


def calculate_general_margin(base: float) -> int:
    """计算通用外边距。

    对应基准宽度的0.8%。

    参数:
        base: 基础单位值。

    返回:
        int: 外边距（像素），最小2。
    """
    return max(2, int(base * 6))


def calculate_general_padding(base: float) -> int:
    """计算通用内边距。

    对应基准宽度的1.2%。

    参数:
        base: 基础单位值。

    返回:
        int: 内边距（像素），最小3。
    """
    return max(3, int(base * 9))


def calculate_border_radius(base: float) -> int:
    """计算通用圆角半径。

    对应基准高度的0.8%。

    参数:
        base: 基础单位值。

    返回:
        int: 圆角半径（像素），最小2。
    """
    return max(2, int(base * 6))


def calculate_splitter_handle(base: float) -> int:
    """计算分割条手柄宽度。

    对应基准宽度的0.3%。

    参数:
        base: 基础单位值。

    返回:
        int: 手柄宽度（像素），最小2。
    """
    return max(2, int(base * 0.003))


def calculate_button_height(base: float) -> int:
    """计算按钮高度。

    对应基准高度的3%。

    参数:
        base: 基础单位值。

    返回:
        int: 按钮高度（像素），最小20。
    """
    return max(20, int(base * 22))


def calculate_input_height(base: float) -> int:
    """计算输入框高度。

    对应基准高度的2.7%。

    参数:
        base: 基础单位值。

    返回:
        int: 输入框高度（像素），最小18。
    """
    return max(18, int(base * 20))
