# -*- coding: utf-8 -*-
"""中栏编辑/预览区面板模块。

CenterPanel使用QTabWidget切换编辑模式和预览模式，
提供Markdown源码编辑和HTML渲染预览功能。
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTabWidget,
    QPlainTextEdit, QTextBrowser,
)
from PyQt6.QtCore import Qt, pyqtSignal, QTimer
from PyQt6.QtGui import QFont

from app_ui.theme_manager import ThemeManager


class CenterPanel(QWidget):
    """中栏编辑/预览区面板。

    使用QTabWidget提供两个标签页：
    - 编辑：QPlainTextEdit编辑Markdown源码
    - 预览：QTextBrowser渲染HTML预览

    属性:
        _tab_widget: 编辑/预览切换标签控件。
        _editor: Markdown源码编辑器。
        _preview: Markdown渲染预览控件。
        _current_content: 当前Markdown内容。
        _preview_timer: 预览刷新防抖定时器。

    信号:
        content_changed(str): 内容变更信号。
    """

    content_changed = pyqtSignal(str)

    def __init__(self, parent: QWidget | None = None) -> None:
        """初始化中栏面板。

        参数:
            parent: 父组件。
        """
        super().__init__(parent)
        self._tab_widget: QTabWidget | None = None
        self._editor: QPlainTextEdit | None = None
        self._preview: QTextBrowser | None = None
        self._current_content: str = ""
        self._preview_timer: QTimer | None = None

        self.setObjectName("CenterPanel")

    def setup_ui(self) -> None:
        """初始化面板UI布局。

        创建QTabWidget含编辑和预览两个标签页。
        """
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self._tab_widget = QTabWidget()
        self._tab_widget.setObjectName("EditorTabs")
        self._tab_widget.setTabPosition(QTabWidget.TabPosition.North)

        # 编辑标签页
        self._editor = QPlainTextEdit()
        self._editor.setObjectName("MarkdownEditor")
        self._editor.setPlaceholderText("在此编辑Markdown内容...")
        self._editor.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)
        self._editor.textChanged.connect(self._on_text_changed)
        self._tab_widget.addTab(self._editor, "编辑")

        # 预览标签页
        self._preview = QTextBrowser()
        self._preview.setObjectName("MarkdownPreview")
        self._preview.setOpenExternalLinks(True)
        self._tab_widget.addTab(self._preview, "预览")

        layout.addWidget(self._tab_widget)

        # 预览刷新防抖定时器（500ms）
        self._preview_timer = QTimer(self)
        self._preview_timer.setSingleShot(True)
        self._preview_timer.timeout.connect(self._render_preview)

    def load_content(self, content: str) -> None:
        """加载Markdown内容到编辑器。

        参数:
            content: Markdown格式文本字符串。
        """
        if self._editor is None:
            return
        self._current_content = content
        self._editor.setPlainText(content)

    def get_content(self) -> str:
        """获取当前编辑器内容。

        返回:
            str: 当前Markdown文本内容。
        """
        if self._editor is not None:
            return self._editor.toPlainText()
        return self._current_content

    def update_sizes(self, sizes: dict) -> None:
        """根据尺寸字典更新组件外观。

        参数:
            sizes: SizeManager计算输出的尺寸字典。
        """
        body_font = QFont()
        body_font.setPointSize(sizes.get("panel_body_font", 12))
        if self._editor is not None:
            self._editor.setFont(body_font)
        if self._preview is not None:
            self._preview.setFont(body_font)

    def update_theme(self, theme: str) -> None:
        """更新面板主题样式。

        设置编辑器组件的背景色和文字色，
        这些属性QSS覆盖有限，需代码直接设置。

        参数:
            theme: 主题名称（"dark"或"light"）。
        """
        tm = ThemeManager.get_instance()

        if self._editor is not None:
            self._editor.setStyleSheet(
                f"QPlainTextEdit {{"
                f"background-color: {tm.get_color('input_bg')};"
                f"color: {tm.get_color('text_primary')};"
                f"border: 1px solid {tm.get_color('border')};"
                f"border-radius: {4}px;"
                f"padding: {8}px;"
                f"selection-background-color: {tm.get_color('accent')};"
                f"}}"
            )
        if self._preview is not None:
            self._preview.setStyleSheet(
                f"QTextBrowser {{"
                f"background-color: {tm.get_color('bg_primary')};"
                f"color: {tm.get_color('text_primary')};"
                f"border: 1px solid {tm.get_color('border')};"
                f"border-radius: {4}px;"
                f"padding: {8}px;"
                f"}}"
            )

    def _on_text_changed(self) -> None:
        """编辑器文本变更回调。

        立即发射content_changed信号，
        并启动500ms防抖后自动刷新预览。
        """
        if self._editor is None:
            return
        self._current_content = self._editor.toPlainText()
        self.content_changed.emit(self._current_content)

        if self._preview_timer is not None:
            if self._preview_timer.isActive():
                self._preview_timer.stop()
            self._preview_timer.start(500)

    def _render_preview(self) -> None:
        """渲染Markdown预览。

        尝试使用markdown库转换HTML，若不可用则显示纯文本。
        """
        if self._preview is None or self._editor is None:
            return

        md_text = self._editor.toPlainText()

        try:
            import markdown as md_lib
            html = md_lib.markdown(
                md_text,
                extensions=["fenced_code", "tables", "codehilite"],
            )
        except ImportError:
            # markdown库不可用，回退到纯文本展示
            html = (
                f"<pre style='white-space: pre-wrap;'>"
                f"{self._escape_html(md_text)}"
                f"</pre>"
            )

        self._preview.setHtml(html)

    @staticmethod
    def _escape_html(text: str) -> str:
        """转义HTML特殊字符。

        参数:
            text: 原始文本。

        返回:
            str: 转义后的安全HTML文本。
        """
        return (
            text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&#39;")
        )
