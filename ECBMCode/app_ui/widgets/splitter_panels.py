# -*- coding: utf-8 -*-
"""三栏分割面板容器模块。

SplitterPanels继承QSplitter，管理左中右三栏面板的比例分配
和拖拽交互。通过StyledSplitterHandle实现自定义分隔线绘制。
"""

from PyQt6.QtWidgets import (
    QSplitter, QSplitterHandle, QWidget, QApplication,
)
from PyQt6.QtCore import Qt, QSize, QEvent
from PyQt6.QtGui import QPainter, QColor, QPaintEvent

from app_ui.widgets.left_panel import LeftPanel
from app_ui.widgets.center_panel import CenterPanel
from app_ui.widgets.right_panel import RightPanel
from app_ui.theme_manager import ThemeManager


class StyledSplitterHandle(QSplitterHandle):
    """自定义分割条手柄。

    重写paintEvent使用QPainter绘制带hover效果的细线分割条。

    属性:
        _hovered: 鼠标是否悬浮在手柄上。
    """

    def __init__(
        self,
        orientation: Qt.Orientation,
        parent: QSplitter | None = None,
    ) -> None:
        """初始化自定义手柄。

        参数:
            orientation: 分割方向。
            parent: 父级QSplitter。
        """
        super().__init__(orientation, parent)
        self._hovered: bool = False
        self.setAttribute(Qt.WidgetAttribute.WA_Hover)

    def paintEvent(self, event: QPaintEvent) -> None:
        """绘制分割线。

        hover时使用高亮主色，否则使用边框颜色。

        参数:
            event: 绘制事件对象。
        """
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        tm = ThemeManager.get_instance()
        if self._hovered:
            color = QColor(tm.get_color("accent"))
        else:
            color = QColor(tm.get_color("separator"))

        w, h = self.width(), self.height()

        if self.orientation() == Qt.Orientation.Horizontal:
            # 垂直分割线（horizontal方向，绘制竖线）
            line_w = 2
            painter.fillRect(
                w // 2 - line_w // 2, 0, line_w, h, color
            )
        else:
            # 水平分割线（vertical方向，绘制横线）
            line_h = 2
            painter.fillRect(
                0, h // 2 - line_h // 2, w, line_h, color
            )

        painter.end()

    def sizeHint(self) -> QSize:
        """返回手柄建议尺寸。

        返回:
            QSize: 宽度3px，高度随父组件。
        """
        if self.orientation() == Qt.Orientation.Horizontal:
            return QSize(4, self.parent().height() if self.parent() else 100)
        return QSize(self.parent().width() if self.parent() else 100, 4)

    def enterEvent(self, event: QEvent) -> None:
        """鼠标进入事件。

        标记hover状态并触发重绘。

        参数:
            event: 进入事件。
        """
        self._hovered = True
        self.update()
        super().enterEvent(event)

    def leaveEvent(self, event: QEvent) -> None:
        """鼠标离开事件。

        取消hover状态并触发重绘。

        参数:
            event: 离开事件。
        """
        self._hovered = False
        self.update()
        super().leaveEvent(event)


class SplitterPanels(QSplitter):
    """三栏分割面板容器。

    管理左中右三栏面板的生命周期、比例分配和主题/尺寸同步。

    属性:
        _left_panel: 左栏内容源面板实例。
        _center_panel: 中栏编辑/预览面板实例。
        _right_panel: 右栏输出/结果面板实例。
        _size_info: 当前尺寸信息字典。
        _ratio: 三栏比例元组，默认(3, 4, 3)。
    """

    def __init__(self, parent: QWidget | None = None) -> None:
        """初始化三栏分割面板。

        参数:
            parent: 父组件。
        """
        super().__init__(parent)
        self._left_panel: LeftPanel | None = None
        self._center_panel: CenterPanel | None = None
        self._right_panel: RightPanel | None = None
        self._size_info: dict = {}
        self._ratio: tuple[int, int, int] = (3, 4, 3)

        self.setObjectName("SplitterPanels")
        self.setOrientation(Qt.Orientation.Horizontal)
        self.setChildrenCollapsible(False)
        self.setHandleWidth(1)
        self.splitterMoved.connect(self._on_splitter_moved)

    def setup_ui(self) -> None:
        """初始化三栏子面板。

        依次创建LeftPanel、CenterPanel、RightPanel并添加到QSplitter。
        """
        # 左栏
        self._left_panel = LeftPanel(self)
        self._left_panel.setup_ui()
        self._left_panel.setMinimumWidth(200)
        self.addWidget(self._left_panel)

        # 中栏
        self._center_panel = CenterPanel(self)
        self._center_panel.setup_ui()
        self._center_panel.setMinimumWidth(300)
        self.addWidget(self._center_panel)

        # 右栏
        self._right_panel = RightPanel(self)
        self._right_panel.setup_ui()
        self._right_panel.setMinimumWidth(200)
        self.addWidget(self._right_panel)

    def set_ratio(self, ratio: tuple[int, int, int]) -> None:
        """设置三栏比例。

        参数:
            ratio: 三栏比例元组，如(3, 4, 3)。
        """
        self._ratio = ratio

    @property
    def left_panel(self) -> LeftPanel | None:
        """获取左栏面板实例。"""
        return self._left_panel

    @property
    def center_panel(self) -> CenterPanel | None:
        """获取中栏面板实例。"""
        return self._center_panel

    @property
    def right_panel(self) -> RightPanel | None:
        """获取右栏面板实例。"""
        return self._right_panel

    def update_sizes(self, sizes: dict) -> None:
        """同步尺寸信息到所有子面板。

        参数:
            sizes: SizeManager计算输出的尺寸字典。
        """
        self._size_info = sizes

        for panel in [self._left_panel, self._center_panel, self._right_panel]:
            if panel is not None:
                panel.update_sizes(sizes)

        # 更新handle宽度
        handle_w = sizes.get("splitter_handle_width", 4)
        self.setHandleWidth(max(2, handle_w))

    def update_theme(self, theme: str) -> None:
        """同步主题到所有子面板。

        参数:
            theme: 主题名称（"dark"或"light"）。
        """
        for panel in [self._left_panel, self._center_panel, self._right_panel]:
            if panel is not None:
                panel.update_theme(theme)

    def _on_splitter_moved(self, pos: int, index: int) -> None:
        """分割条拖拽回调。

        检查并修正各栏最小宽度约束。

        参数:
            pos: 分割条新位置。
            index: 移动的分割条索引。
        """

    def createHandle(self) -> QSplitterHandle:
        """创建自定义分割手柄。

        重写QSplitter.createHandle返回StyledSplitterHandle实例。

        返回:
            StyledSplitterHandle: 自定义分割手柄。
        """
        return StyledSplitterHandle(self.orientation(), self)
