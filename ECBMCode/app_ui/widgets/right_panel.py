# -*- coding: utf-8 -*-
"""右栏输出/结果区面板模块。

RightPanel提供输出路径配置、导出格式选择、转换控制和进度显示功能。
"""

from pathlib import Path

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QComboBox, QProgressBar,
    QFileDialog, QSizePolicy,
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont

from app_ui.theme_manager import ThemeManager
from app_ui.widgets.loading_indicator import LoadingIndicator


class RightPanel(QWidget):
    """右栏输出/结果区面板。

    提供以下功能组件：
    - 输出路径选择（输入框+浏览按钮）
    - 导出格式下拉选择
    - 开始转换按钮
    - 转换进度条
    - 状态文本显示
    - 加载指示器

    属性:
        _title_label: 面板标题标签。
        _output_path_input: 输出路径输入框。
        _browse_btn: 浏览按钮。
        _format_combo: 导出格式选择下拉框。
        _convert_btn: 开始转换按钮。
        _progress_bar: 转换进度条。
        _status_label: 状态文本标签。
        _loading_indicator: 加载指示器实例。

    信号:
        convert_requested(dict): 转换请求信号。
    """

    convert_requested = pyqtSignal(dict)

    def __init__(self, parent: QWidget | None = None) -> None:
        """初始化右栏面板。

        参数:
            parent: 父组件。
        """
        super().__init__(parent)
        self._title_label: QLabel | None = None
        self._output_path_input: QLineEdit | None = None
        self._browse_btn: QPushButton | None = None
        self._format_combo: QComboBox | None = None
        self._convert_btn: QPushButton | None = None
        self._progress_bar: QProgressBar | None = None
        self._status_label: QLabel | None = None
        self._loading_indicator: LoadingIndicator | None = None

        self.setObjectName("RightPanel")

    def setup_ui(self) -> None:
        """初始化面板UI布局。

        自上而下排列：标题 -> 输出路径行 -> 导出格式 ->
        转换按钮 -> 进度条 -> 状态标签+加载指示器。
        """
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(6)

        # 面板标题
        self._title_label = QLabel("输出设置")
        self._title_label.setObjectName("PanelTitle")
        self._title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self._title_label)

        # 输出路径行
        path_layout = QHBoxLayout()
        path_layout.setSpacing(4)
        self._output_path_input = QLineEdit()
        self._output_path_input.setObjectName("OutputPath")
        self._output_path_input.setPlaceholderText("选择输出目录...")
        self._output_path_input.setReadOnly(True)
        path_layout.addWidget(self._output_path_input, 1)

        self._browse_btn = QPushButton("浏览")
        self._browse_btn.setObjectName("BrowseBtn")
        self._browse_btn.clicked.connect(self._on_browse_clicked)
        path_layout.addWidget(self._browse_btn)
        layout.addLayout(path_layout)

        # 导出格式选择
        format_layout = QHBoxLayout()
        format_layout.setSpacing(4)
        format_label = QLabel("导出格式:")
        format_label.setObjectName("FormatLabel")
        format_layout.addWidget(format_label)

        self._format_combo = QComboBox()
        self._format_combo.setObjectName("FormatCombo")
        self._format_combo.addItems([
            "Markdown (.md)",
            "HTML (.html)",
            "纯文本 (.txt)",
        ])
        format_layout.addWidget(self._format_combo, 1)
        layout.addLayout(format_layout)

        # 转换按钮
        self._convert_btn = QPushButton("开始转换")
        self._convert_btn.setObjectName("ConvertBtn")
        self._convert_btn.clicked.connect(self._on_convert_clicked)
        self._convert_btn.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed,
        )
        layout.addWidget(self._convert_btn)

        # 进度条
        self._progress_bar = QProgressBar()
        self._progress_bar.setObjectName("ProgressBar")
        self._progress_bar.setRange(0, 100)
        self._progress_bar.setValue(0)
        self._progress_bar.setTextVisible(True)
        self._progress_bar.setFormat("%p%")
        layout.addWidget(self._progress_bar)

        # 状态标签 + 加载指示器
        status_layout = QHBoxLayout()
        status_layout.setSpacing(6)

        self._status_label = QLabel("就绪")
        self._status_label.setObjectName("StatusLabel")
        self._status_label.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed,
        )
        status_layout.addWidget(self._status_label)

        self._loading_indicator = LoadingIndicator(
            self, size=24,
            color=ThemeManager.get_instance().get_color("accent"),
        )
        self._loading_indicator.setObjectName("LoadingIndicator")
        status_layout.addWidget(self._loading_indicator)
        status_layout.addStretch()

        layout.addLayout(status_layout)
        layout.addStretch()

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
        for widget in [
            self._output_path_input, self._format_combo,
            self._status_label,
        ]:
            if widget is not None:
                widget.setFont(body_font)

        btn_font = QFont()
        btn_font.setPointSize(sizes.get("panel_body_font", 12))
        for btn in [self._browse_btn, self._convert_btn]:
            if btn is not None:
                btn.setFont(btn_font)

        input_h = sizes.get("input_height", 24)
        btn_h = sizes.get("button_height", 24)
        if self._output_path_input is not None:
            self._output_path_input.setMinimumHeight(input_h)
        if self._format_combo is not None:
            self._format_combo.setMinimumHeight(input_h)
        if self._convert_btn is not None:
            self._convert_btn.setMinimumHeight(btn_h)
        if self._browse_btn is not None:
            self._browse_btn.setMinimumHeight(btn_h)

        progress_h = sizes.get("input_height", 24)
        if self._progress_bar is not None:
            self._progress_bar.setMinimumHeight(progress_h)

    def update_theme(self, theme: str) -> None:
        """更新面板主题样式。

        参数:
            theme: 主题名称（"dark"或"light"）。
        """
        tm = ThemeManager.get_instance()

        # 更新加载指示器颜色
        if self._loading_indicator is not None:
            self._loading_indicator.set_color(tm.get_color("accent"))

    def update_progress(self, value: int) -> None:
        """更新进度条值。

        参数:
            value: 进度值（0-100整数）。
        """
        if self._progress_bar is not None:
            self._progress_bar.setValue(max(0, min(100, value)))

    def set_status(self, text: str) -> None:
        """设置状态文本。

        参数:
            text: 状态描述文本。
        """
        if self._status_label is not None:
            self._status_label.setText(text)

    def show_loading(self) -> None:
        """显示加载指示器并启动动画。"""
        if self._loading_indicator is not None:
            self._loading_indicator.start()

    def hide_loading(self) -> None:
        """隐藏加载指示器并停止动画。"""
        if self._loading_indicator is not None:
            self._loading_indicator.stop()

    def _on_browse_clicked(self) -> None:
        """浏览按钮点击处理。

        打开目录选择对话框选择输出目录。
        """
        dir_path = QFileDialog.getExistingDirectory(
            self,
            "选择输出目录",
            str(Path.home()),
        )
        if dir_path and self._output_path_input is not None:
            self._output_path_input.setText(dir_path)

    def _on_convert_clicked(self) -> None:
        """转换按钮点击处理。

        收集输出路径、格式等参数并发射convert_requested信号。
        """
        output_path = ""
        if self._output_path_input is not None:
            output_path = self._output_path_input.text().strip()

        if not output_path:
            # 默认使用用户主目录
            output_path = str(Path.home())

        format_map = {
            "Markdown (.md)": "md",
            "HTML (.html)": "html",
            "纯文本 (.txt)": "txt",
        }
        format_text = ""
        if self._format_combo is not None:
            format_text = self._format_combo.currentText()
        fmt = format_map.get(format_text, "md")

        params = {
            "output_path": output_path,
            "format": fmt,
            "source": "",
            "content": "",
        }

        self.show_loading()
        self.set_status("转换中...")
        self.convert_requested.emit(params)
