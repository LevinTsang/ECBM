# -*- coding: utf-8 -*-
"""左侧竖向工具栏模块。

VerticalToolBar实现VSCode Activity Bar风格的左侧竖向工具列表栏，
管理工具按钮的注册、互斥选中和面板切换。
包含ToolButton（QPushButton子类）实现hover动画和选中指示器。
"""

from typing import Callable

from PyQt6.QtWidgets import (
    QWidget, QPushButton, QVBoxLayout, QButtonGroup,
    QSizePolicy, QApplication,
)
from PyQt6.QtCore import Qt, QSize, QPropertyAnimation, QEasingCurve, QEvent
from PyQt6.QtGui import QFont, QEnterEvent

from app_ui.animation_utils import scale_icon, is_reduced_motion
from app_ui.theme_manager import ThemeManager


class ToolButton(QPushButton):
    """自定义工具栏按钮。

    继承QPushButton，支持：
    - hover时图标放大动画
    - 互斥checked状态的左侧竖条指示器
    - Unicode文本图标模拟

    属性:
        _tool_id: 工具标识符。
        _icon_text: 图标Unicode文本。
        _icon_size: 正常图标尺寸。
        _hover_size: hover时放大后的图标尺寸。
        _anim: QPropertyAnimation实例（用于iconSize动画）。
    """

    def __init__(
        self,
        tool_id: str,
        icon_text: str,
        tooltip: str,
        parent: QWidget | None = None,
    ) -> None:
        """初始化工具栏按钮。

        参数:
            tool_id: 工具标识符。
            icon_text: 按钮显示文本（Unicode图标字符）。
            tooltip: 鼠标悬浮提示文本。
            parent: 父组件。
        """
        super().__init__(parent)
        self._tool_id: str = tool_id
        self._icon_text: str = icon_text
        self._icon_size: int = 20
        self._hover_size: int = 24

        self.setObjectName(f"ToolButton_{tool_id}")
        self.setText(icon_text)
        self.setToolTip(tooltip)
        self.setCheckable(True)
        self.setSizePolicy(
            QSizePolicy.Policy.Fixed,
            QSizePolicy.Policy.Fixed,
        )

        self._anim = QPropertyAnimation(self, b"font", self)
        self._anim.setDuration(200)
        self._anim.setEasingCurve(QEasingCurve.Type.OutCubic)

    @property
    def tool_id(self) -> str:
        """返回工具标识符。"""
        return self._tool_id

    def set_icon_size(self, size: int) -> None:
        """设置图标尺寸。

        参数:
            size: 图标像素尺寸。
        """
        self._icon_size = size
        self._hover_size = max(size + 4, int(size * 1.15))

        font = self.font()
        font.setPixelSize(size)
        self.setFont(font)

        btn_size = size + 16
        self.setFixedSize(btn_size, btn_size)

        self.setIconSize(QSize(size, size))

    def enterEvent(self, event: QEnterEvent) -> None:
        """鼠标进入事件。

        触发图标放大动画（若未启用减少动效）。

        参数:
            event: 进入事件。
        """
        if is_reduced_motion():
            super().enterEvent(event)
            return

        self._anim.stop()
        font = self.font()
        font.setPixelSize(self._hover_size)
        self._anim.setStartValue(self.font())
        self._anim.setEndValue(font)
        self._anim.setDuration(200)
        self._anim.setEasingCurve(QEasingCurve.Type.OutCubic)
        self._anim.start()
        super().enterEvent(event)

    def leaveEvent(self, event: QEvent) -> None:
        """鼠标离开事件。

        触发图标恢复缩小动画。

        参数:
            event: 离开事件。
        """
        if is_reduced_motion():
            super().leaveEvent(event)
            return

        self._anim.stop()
        font = self.font()
        font.setPixelSize(self._icon_size)
        self._anim.setStartValue(self.font())
        self._anim.setEndValue(font)
        self._anim.setDuration(200)
        self._anim.setEasingCurve(QEasingCurve.Type.OutCubic)
        self._anim.start()
        super().leaveEvent(event)


class VerticalToolBar(QWidget):
    """左侧竖向工具栏。

    VSCode Activity Bar风格：
    - 上部区域：工具按钮列表（互斥单选）
    - 下部区域：主题切换按钮（固定于底部）

    属性:
        _buttons: 工具按钮列表字典（tool_id -> ToolButton）。
        _button_group: 按钮互斥分组。
        _current_tool_id: 当前选中工具ID。
        _theme: 当前主题名称。
        _size_info: 当前尺寸信息字典。
        _tool_layout: 工具按钮区域布局。
        _theme_toggle_btn: 主题切换按钮。
        _on_tool_callback: 工具切换回调函数。

    信号:
        tool_selected(str): 工具选中信号，携带tool_id。
    """

    from PyQt6.QtCore import pyqtSignal
    tool_selected = pyqtSignal(str)

    def __init__(self, parent: QWidget | None = None) -> None:
        """初始化竖向工具栏。

        参数:
            parent: 父组件。
        """
        super().__init__(parent)
        self._buttons: dict[str, ToolButton] = {}
        self._button_group: QButtonGroup = QButtonGroup(self)
        self._current_tool_id: str | None = None
        self._theme: str = "dark"
        self._size_info: dict = {}
        self._tool_layout: QVBoxLayout | None = None
        self._theme_toggle_btn: ToolButton | None = None
        self._on_tool_callback: Callable[[str], None] | None = None

        self.setObjectName("VerticalToolBar")
        self._button_group.setExclusive(True)
        self._button_group.idClicked.connect(self._on_button_clicked)

    def setup_ui(self) -> None:
        """初始化工具栏UI布局。

        上部为工具按钮区（带stretch底部推至下方），
        底部固定分界线+主题切换按钮。
        """
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 8, 0, 8)
        main_layout.setSpacing(2)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 工具按钮区域（顶部）
        self._tool_layout = QVBoxLayout()
        self._tool_layout.setSpacing(4)
        self._tool_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        main_layout.addLayout(self._tool_layout)

        # 弹性空间（将主题按钮推至底部）
        main_layout.addStretch(1)

        # 底部分隔区域
        separator = QWidget()
        separator.setObjectName("ToolBarSeparator")
        separator.setFixedHeight(1)
        main_layout.addWidget(separator)

        # 主题切换按钮（底部固定）
        tm = ThemeManager.get_instance()
        effective = tm.get_effective_theme()
        icon_text = "🌙" if effective == "dark" else "☀"

        self._theme_toggle_btn = ToolButton(
            "theme_toggle", icon_text,
            "切换主题",
            self,
        )
        self._theme_toggle_btn.setCheckable(False)
        self._theme_toggle_btn.clicked.connect(self._on_theme_toggle)
        main_layout.addWidget(
            self._theme_toggle_btn, 0, Qt.AlignmentFlag.AlignCenter
        )

    def register_tool(
        self,
        tool_id: str,
        icon_text: str,
        tooltip: str,
        callback: Callable[[str], None] | None = None,
    ) -> None:
        """注册工具按钮。

        参数:
            tool_id: 工具唯一标识。
            icon_text: 按钮显示文本（Unicode图标）。
            tooltip: 鼠标悬浮提示。
            callback: 工具被选中时的回调函数。
        """
        if tool_id in self._buttons:
            return

        btn = ToolButton(tool_id, icon_text, tooltip, self)
        btn.clicked.connect(
            lambda checked, tid=tool_id: self._on_tool_clicked(tid, checked)
        )

        btn_id = self._button_group.id(btn)
        if btn_id < 0:
            self._button_group.addButton(btn)
        else:
            # 重新添加以确保ID注册
            self._button_group.addButton(btn)

        self._buttons[tool_id] = btn

        if self._tool_layout is not None:
            self._tool_layout.addWidget(
                btn, 0, Qt.AlignmentFlag.AlignCenter
            )

        # 应用当前尺寸设置
        if self._size_info:
            icon_size = self._size_info.get("toolbar_icon_size", 20)
            btn.set_icon_size(icon_size)

    def switch_to_tool(self, tool_id: str) -> None:
        """切换到指定工具（模拟按钮点击）。

        参数:
            tool_id: 目标工具ID。
        """
        if tool_id not in self._buttons:
            return
        btn = self._buttons[tool_id]
        btn.setChecked(True)
        self._current_tool_id = tool_id

    def update_sizes(self, sizes: dict) -> None:
        """根据尺寸字典更新组件外观。

        参数:
            sizes: SizeManager计算输出的尺寸字典。
        """
        self._size_info = sizes

        toolbar_width = sizes.get("toolbar_width", 48)
        self.setFixedWidth(toolbar_width)

        icon_size = sizes.get("toolbar_icon_size", 20)
        for btn in self._buttons.values():
            btn.set_icon_size(icon_size)

        if self._theme_toggle_btn is not None:
            self._theme_toggle_btn.set_icon_size(icon_size)

    def update_theme(self, theme: str) -> None:
        """更新主题样式并刷新主题切换按钮图标。

        参数:
            theme: 主题名称（"dark"或"light"）。
        """
        self._theme = theme

        if self._theme_toggle_btn is not None:
            if theme == "dark":
                self._theme_toggle_btn.setText("🌙")
                self._theme_toggle_btn.setToolTip("切换到亮色主题")
            else:
                self._theme_toggle_btn.setText("☀")
                self._theme_toggle_btn.setToolTip("切换到暗色主题")

    def _on_button_clicked(self, btn_id: int) -> None:
        """按钮组点击回调。

        根据QButtonGroup的ID找到对应按钮并发射tool_selected信号。

        参数:
            btn_id: QButtonGroup分配的按钮ID。
        """
        btn = self._button_group.button(btn_id)
        if btn is not None and isinstance(btn, ToolButton):
            self._current_tool_id = btn.tool_id
            self.tool_selected.emit(btn.tool_id)
            if self._on_tool_callback is not None:
                self._on_tool_callback(btn.tool_id)

    def _on_tool_clicked(self, tool_id: str, checked: bool) -> None:
        """单个工具按钮点击处理。

        参数:
            tool_id: 被点击工具ID。
            checked: 按钮是否被选中。
        """
        if checked:
            self._current_tool_id = tool_id

    def _on_theme_toggle(self) -> None:
        """主题切换按钮点击处理。

        调用ThemeManager.toggle_theme切换主题。
        """
        ThemeManager.get_instance().toggle_theme()
