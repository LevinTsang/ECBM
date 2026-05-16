# -*- coding: utf-8 -*-
"""动态尺寸管理器模块。

SizeManager（QObject子类）作为动态尺寸计算中心，
接收窗口尺寸变化事件，通过防抖机制调用size_utils
计算所有组件的比例尺寸，并发射size_changed信号广播。
"""

from PyQt6.QtCore import QObject, pyqtSignal, QTimer

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


class SizeManager(QObject):
    """动态尺寸计算管理器。

    基于窗口宽高按比例计算所有UI组件的尺寸值，
    包含100ms防抖机制避免频繁resize导致的性能问题。

    属性:
        _window_width: 当前窗口宽度。
        _window_height: 当前窗口高度。
        _base_unit: 基础计算单位。
        _ratio_table: 比例常数映射表。
        _throttle_timer: 防抖定时器。
        _pending_size: 待处理的尺寸元组。
        _throttle_ms: 防抖间隔（毫秒），默认100。

    信号:
        size_changed(dict): 尺寸变更信号，携带完整尺寸字典。
    """

    size_changed = pyqtSignal(dict)

    def __init__(
        self,
        ref_width: int = 1024,
        ref_height: int = 768,
        throttle_ms: int = 100,
    ) -> None:
        """初始化尺寸管理器。

        参数:
            ref_width: 初始参考宽度（像素）。
            ref_height: 初始参考高度（像素）。
            throttle_ms: 防抖间隔（毫秒），默认100。
        """
        super().__init__()
        self._window_width: int = ref_width
        self._window_height: int = ref_height
        self._base_unit: float = calculate_base_unit(ref_width, ref_height)
        self._throttle_ms: int = throttle_ms
        self._pending_size: tuple[int, int] | None = None

        self._throttle_timer: QTimer = QTimer(self)
        self._throttle_timer.setSingleShot(True)
        self._throttle_timer.timeout.connect(self._do_calculate)

    def calculate_sizes(
        self, width: int, height: int
    ) -> dict[str, int | float]:
        """计算所有组件尺寸。

        基于给定宽高计算全部UI组件的比例尺寸。

        参数:
            width: 窗口宽度（像素）。
            height: 窗口高度（像素）。

        返回:
            dict: 尺寸字典，包含所有组件的计算后尺寸值。
        """
        base = calculate_base_unit(width, height)
        self._base_unit = base
        self._window_width = width
        self._window_height = height

        return {
            "toolbar_width": calculate_toolbar_width(base),
            "toolbar_icon_size": calculate_toolbar_icon_size(base),
            "panel_title_font": calculate_title_font_size(base),
            "panel_body_font": calculate_body_font_size(base),
            "panel_small_font": calculate_small_font_size(base),
            "general_margin": calculate_general_margin(base),
            "general_padding": calculate_general_padding(base),
            "border_radius": calculate_border_radius(base),
            "splitter_handle_width": calculate_splitter_handle(base),
            "button_height": calculate_button_height(base),
            "input_height": calculate_input_height(base),
            "icon_size_small": calculate_toolbar_icon_size(base),
            "icon_size_medium": max(
                16, int(calculate_toolbar_icon_size(base) * 1.3)
            ),
            "window_width": width,
            "window_height": height,
            "base_unit": base,
        }

    def set_throttle(self, ms: int) -> None:
        """设置防抖间隔。

        参数:
            ms: 防抖间隔（毫秒）。
        """
        self._throttle_ms = max(0, ms)

    def on_resize(self, width: int, height: int) -> None:
        """处理窗口尺寸变更。

        防抖机制：尺寸变化小于5px时跳过，
        否则重置防抖定时器。

        参数:
            width: 新窗口宽度。
            height: 新窗口高度。
        """
        if (
            abs(width - self._window_width) < 5
            and abs(height - self._window_height) < 5
        ):
            return

        self._pending_size = (width, height)

        if self._throttle_timer.isActive():
            self._throttle_timer.stop()
        self._throttle_timer.start(self._throttle_ms)

    def recalculate(self) -> None:
        """强制立即重算尺寸（跳过防抖）。

        适用于窗口最大化/全屏等需要立即响应的场景。
        """
        if self._pending_size is not None:
            width, height = self._pending_size
        else:
            width, height = self._window_width, self._window_height

        self._do_calculate()

    def _do_calculate(self) -> None:
        """执行实际尺寸计算并发射信号。

        由防抖定时器超时触发，或由recalculate直接调用。
        """
        if self._pending_size is not None:
            width, height = self._pending_size
            self._pending_size = None
        else:
            width, height = self._window_width, self._window_height

        sizes = self.calculate_sizes(width, height)
        self.size_changed.emit(sizes)
