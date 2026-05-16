# -*- coding: utf-8 -*-
"""左栏内容源区面板模块。

LeftPanel提供文件拖放、URL输入和历史记录列表功能，
用于选择待转换的内容来源。
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QListWidget, QListWidgetItem,
    QSizePolicy,
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QDragEnterEvent, QDropEvent, QFont

from app_ui.theme_manager import ThemeManager


class LeftPanel(QWidget):
    """左栏内容源区面板。

    提供三种内容源选择方式：
    - 拖放文件到拖放区域
    - 输入文件路径或URL
    - 从历史记录列表中选择

    属性:
        _title_label: 面板标题标签。
        _drop_area: 文件拖放区域组件。
        _url_input: URL/路径输入框。
        _url_submit_btn: URL提交按钮。
        _history_list: 历史记录列表。
        _layout: 面板主布局。

    信号:
        source_selected(str): 内容源选中信号（文件路径或URL字符串）。
    """

    source_selected = pyqtSignal(str)

    def __init__(self, parent: QWidget | None = None) -> None:
        """初始化左栏面板。

        参数:
            parent: 父组件。
        """
        super().__init__(parent)
        self._title_label: QLabel | None = None
        self._drop_area: QWidget | None = None
        self._drop_label: QLabel | None = None
        self._url_input: QLineEdit | None = None
        self._url_submit_btn: QPushButton | None = None
        self._history_list: QListWidget | None = None

        self.setObjectName("LeftPanel")
        self.setAcceptDrops(True)

    def setup_ui(self) -> None:
        """初始化面板UI布局。

        自上而下排列：标题 -> 拖放区域 -> URL输入行 -> 历史记录列表。
        """
        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(6)

        # 面板标题
        self._title_label = QLabel("内容源")
        self._title_label.setObjectName("PanelTitle")
        self._title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._layout.addWidget(self._title_label)

        # 拖放区域
        self._drop_area = QWidget()
        self._drop_area.setObjectName("DropArea")
        self._drop_area.setAcceptDrops(True)
        self._drop_area.setMinimumHeight(80)
        self._drop_area.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )
        drop_layout = QVBoxLayout(self._drop_area)
        drop_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._drop_label = QLabel("拖放文件到此处\n或输入URL")
        self._drop_label.setObjectName("DropLabel")
        self._drop_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        drop_layout.addWidget(self._drop_label)
        self._layout.addWidget(self._drop_area)

        # URL输入行
        input_layout = QHBoxLayout()
        input_layout.setSpacing(4)
        self._url_input = QLineEdit()
        self._url_input.setObjectName("UrlInput")
        self._url_input.setPlaceholderText("输入文件路径或URL...")
        self._url_input.returnPressed.connect(self._on_url_submit)
        input_layout.addWidget(self._url_input, 1)

        self._url_submit_btn = QPushButton("加载")
        self._url_submit_btn.setObjectName("UrlSubmitBtn")
        self._url_submit_btn.clicked.connect(self._on_url_submit)
        input_layout.addWidget(self._url_submit_btn)
        self._layout.addLayout(input_layout)

        # 历史记录列表
        self._history_list = QListWidget()
        self._history_list.setObjectName("HistoryList")
        self._history_list.setAlternatingRowColors(False)
        self._history_list.itemClicked.connect(self._on_history_item_clicked)
        self._layout.addWidget(self._history_list, 1)

    def update_sizes(self, sizes: dict) -> None:
        """根据尺寸字典更新组件外观。

        参数:
            sizes: SizeManager计算输出的尺寸字典。
        """
        title_font = QFont()
        title_font.setPointSize(sizes.get("panel_title_font", 14))
        if self._title_label is not None:
            self._title_label.setFont(title_font)

        body_font = QFont()
        body_font.setPointSize(sizes.get("panel_body_font", 12))
        if self._drop_label is not None:
            self._drop_label.setFont(body_font)
        if self._url_input is not None:
            self._url_input.setFont(body_font)
        if self._history_list is not None:
            self._history_list.setFont(body_font)

        input_h = sizes.get("input_height", 24)
        if self._url_input is not None:
            self._url_input.setMinimumHeight(input_h)

        btn_h = sizes.get("button_height", 24)
        if self._url_submit_btn is not None:
            self._url_submit_btn.setMinimumHeight(btn_h)

        margin = sizes.get("general_margin", 4)
        padding = sizes.get("general_padding", 8)
        self._layout.setContentsMargins(margin, margin, margin, margin)

        self._apply_theme_styles()

    def update_theme(self, theme: str) -> None:
        """更新面板主题样式。

        参数:
            theme: 主题名称（"dark"或"light"）。
        """
        self._apply_theme_styles()

    def _apply_theme_styles(self) -> None:
        """应用当前主题的内联样式。

        设置拖放区域和输入组件的样式，
        这些样式难以通过全局QSS覆盖。
        """
        tm = ThemeManager.get_instance()

        if self._drop_area is not None:
            self._drop_area.setStyleSheet(
                f"QWidget#DropArea {{"
                f"background-color: {tm.get_color('bg_secondary')};"
                f"border: 2px dashed {tm.get_color('border')};"
                f"border-radius: {8}px;"
                f"}}"
            )
        if self._drop_label is not None:
            self._drop_label.setStyleSheet(
                f"color: {tm.get_color('text_secondary')};"
            )

    def add_history_item(self, source: str) -> None:
        """添加历史记录条目。

        参数:
            source: 源文件路径或URL字符串。
        """
        if self._history_list is None:
            return
        # 避免重复添加
        for i in range(self._history_list.count()):
            if self._history_list.item(i).text() == source:
                return
        self._history_list.insertItem(0, QListWidgetItem(source))
        # 限制历史记录最大500条
        while self._history_list.count() > 500:
            self._history_list.takeItem(self._history_list.count() - 1)

    def _on_url_submit(self) -> None:
        """URL/路径提交处理。

        校验输入非空后发射source_selected信号。
        """
        if self._url_input is None:
            return
        text = self._url_input.text().strip()
        if not text:
            return
        self.add_history_item(text)
        self.source_selected.emit(text)
        self._url_input.clear()

    def _on_history_item_clicked(self, item: QListWidgetItem) -> None:
        """历史记录条目点击处理。

        参数:
            item: 被点击的列表项。
        """
        self.source_selected.emit(item.text())

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        """拖拽进入事件。

        接受包含文件URL的拖放操作。

        参数:
            event: 拖拽进入事件。
        """
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            if self._drop_area is not None:
                self._drop_area.setProperty("drag_hover", True)
                self._drop_area.style().polish(self._drop_area)

    def dragLeaveEvent(self, event) -> None:
        """拖拽离开事件。"""
        if self._drop_area is not None:
            self._drop_area.setProperty("drag_hover", False)
            self._drop_area.style().polish(self._drop_area)

    def dropEvent(self, event: QDropEvent) -> None:
        """文件拖放事件。

        提取第一个文件的本地路径并发射source_selected信号。

        参数:
            event: 拖放事件。
        """
        if self._drop_area is not None:
            self._drop_area.setProperty("drag_hover", False)
            self._drop_area.style().polish(self._drop_area)

        urls = event.mimeData().urls()
        if urls:
            path = urls[0].toLocalFile()
            if path:
                self.add_history_item(path)
                self.source_selected.emit(path)
