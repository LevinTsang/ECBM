# -*- coding: utf-8 -*-
"""主题管理器模块。

ThemeManager单例（QObject子类）负责管理暗色/亮色主题切换、
系统主题跟随和QSS动态加载。
采用{{color_key}}占位符替换方案实现QSS主题变量系统。
"""

from pathlib import Path

from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtWidgets import QApplication

from app_infra.config.config_manager import ConfigManager
from app_infra.utils.path_utils import get_project_root


class ThemeManager(QObject):
    """主题管理器单例。

    管理应用主题模式（暗色/亮色/跟随系统），
    维护语义化颜色字典，通过{{color_key}}占位符替换
    实现QSS主题变量系统。

    属性:
        _instance: 单例实例（类属性）。
        _theme_mode: 当前主题模式（"dark"/"light"/"system"）。
        _color_palette: 语义化颜色字典（暗色和亮色各一套）。
        _qss_cache: QSS文件内容缓存字典。

    信号:
        theme_changed(str): 主题变更信号，携带actual_theme_name。
    """

    _instance: "ThemeManager | None" = None

    theme_changed = pyqtSignal(str)

    # 暗色主题颜色调色板
    _DARK: dict[str, str] = {
        "bg_primary": "#1E1E2E",
        "bg_secondary": "#2A2A3C",
        "bg_tertiary": "#222236",
        "text_primary": "#E0E0F0",
        "text_secondary": "#A0A0C0",
        "accent": "#6C8EBF",
        "accent_hover": "#7DA0D4",
        "border": "#3A3A50",
        "separator": "#2A2A3A",
        "toolbar_bg": "#1A1A28",
        "button_bg": "#2A2A3C",
        "button_hover": "#3A3A50",
        "button_checked": "#3A3A5A",
        "input_bg": "#1E1E2E",
        "input_border": "#3A3A50",
        "input_focus_border": "#6C8EBF",
        "scrollbar_bg": "#1A1A28",
        "scrollbar_handle": "#3A3A50",
        "scrollbar_handle_hover": "#4A4A60",
        "progress_bg": "#2A2A3C",
        "progress_chunk": "#6C8EBF",
        "status_success": "#4CAF50",
        "status_warning": "#FF9800",
        "status_error": "#F44336",
        "shadow": "#000000",
    }

    # 亮色主题颜色调色板
    _LIGHT: dict[str, str] = {
        "bg_primary": "#F5F5F5",
        "bg_secondary": "#EAEAEA",
        "bg_tertiary": "#E0E0E0",
        "text_primary": "#1E1E2E",
        "text_secondary": "#606070",
        "accent": "#4A7ABF",
        "accent_hover": "#3A6AAF",
        "border": "#C0C0D0",
        "separator": "#D0D0D0",
        "toolbar_bg": "#E8E8F0",
        "button_bg": "#EAEAEA",
        "button_hover": "#D8D8E0",
        "button_checked": "#D0D0E0",
        "input_bg": "#FFFFFF",
        "input_border": "#C0C0D0",
        "input_focus_border": "#4A7ABF",
        "scrollbar_bg": "#EAEAEA",
        "scrollbar_handle": "#C0C0D0",
        "scrollbar_handle_hover": "#A0A0B0",
        "progress_bg": "#EAEAEA",
        "progress_chunk": "#4A7ABF",
        "status_success": "#388E3C",
        "status_warning": "#F57C00",
        "status_error": "#D32F2F",
        "shadow": "#000000",
    }

    def __new__(cls) -> "ThemeManager":
        """创建或返回单例实例。

        返回:
            ThemeManager: 全局唯一的主题管理器实例。
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @staticmethod
    def get_instance() -> "ThemeManager":
        """获取ThemeManager单例实例。

        返回:
            ThemeManager: 全局唯一的主题管理器实例。
        """
        return ThemeManager()

    def __init__(self) -> None:
        """初始化主题管理器。

        使用hasattr守卫确保单例仅初始化一次。
        从ConfigManager读取已保存的主题偏好。
        """
        # QObject.__init__必须先行调用，确保hasattr守卫正常工作
        super().__init__()

        if not hasattr(self, "_initialized"):
            self._theme_mode: str = "system"
            self._color_palette: dict[str, dict[str, str]] = {
                "dark": self._DARK,
                "light": self._LIGHT,
            }
            self._qss_cache: dict[str, str] = {}
            self._initialized: bool = True

            # 从配置加载主题偏好
            config = ConfigManager.get_instance()
            saved_mode = config.get("theme_mode", "system")
            if saved_mode in ("dark", "light", "system"):
                self._theme_mode = saved_mode

            self._connect_system_theme()

    def _connect_system_theme(self) -> None:
        """连接系统主题变化信号。

        监听QStyleHints.colorSchemeChanged信号（Qt 6.5+），
        仅当用户设置主题模式为"system"时自动响应。
        """
        app = QApplication.instance()
        if app is not None:
            try:
                app.styleHints().colorSchemeChanged.connect(
                    self._on_system_theme_changed
                )
            except AttributeError:
                # Qt版本低于6.5，不支持colorSchemeChanged
                pass

    def _on_system_theme_changed(self) -> None:
        """系统主题变化回调。

        仅当当前模式为"system"时响应系统主题变化，
        重新计算effective_theme并发射信号。
        """
        if self._theme_mode == "system":
            effective = self.get_effective_theme()
            self.theme_changed.emit(effective)

    def set_theme(self, mode: str) -> None:
        """设置主题模式。

        参数:
            mode: 主题模式字符串（"dark"/"light"/"system"）。

        异常:
            ValueError: 无效的主题模式字符串。
        """
        if mode not in ("dark", "light", "system"):
            raise ValueError(
                f"无效的主题模式: {mode}，可选值: dark/light/system"
            )

        previous_effective = self.get_effective_theme()
        self._theme_mode = mode

        # 持久化主题偏好
        config = ConfigManager.get_instance()
        config.set_runtime("theme_mode", mode)

        effective = self.get_effective_theme()
        if effective != previous_effective:
            self.theme_changed.emit(effective)

    def toggle_theme(self) -> None:
        """切换主题（在暗色和亮色之间切换）。

        若当前为system模式，则根据当前effective_theme
        切换到相反主题并改为手动模式。
        """
        current = self.get_effective_theme()
        new_mode = "light" if current == "dark" else "dark"
        self.set_theme(new_mode)

    def get_effective_theme(self) -> str:
        """获取当前实际生效的主题名称。

        若为system模式，通过检测系统配色方案判断实际主题。

        返回:
            str: 实际主题名（"dark"或"light"）。
        """
        if self._theme_mode == "system":
            app = QApplication.instance()
            if app is not None:
                try:
                    from PyQt6.QtGui import QStyleHints
                    scheme = app.styleHints().colorScheme()
                    from PyQt6.QtCore import Qt
                    if scheme == Qt.ColorScheme.Dark:
                        return "dark"
                except (AttributeError, ImportError):
                    pass
            # 默认回退到亮色主题
            return "light"
        return self._theme_mode

    def load_qss(self, theme_name: str) -> str:
        """加载并处理QSS样式表。

        从app_ui/styles/{theme_name}_theme.qss读取QSS模板，
        将{{color_key}}占位符替换为对应颜色值。

        参数:
            theme_name: 主题名称（"dark"或"light"）。

        返回:
            str: 替换占位符后的完整QSS样式表字符串。
        """
        if theme_name in self._qss_cache:
            return self._qss_cache[theme_name]

        qss_path = (
            get_project_root() / "app_ui" / "styles"
            / f"{theme_name}_theme.qss"
        )

        if not qss_path.exists():
            return self._build_fallback_qss(theme_name)

        try:
            tpl = qss_path.read_text(encoding="utf-8")
        except Exception:
            return self._build_fallback_qss(theme_name)

        palette = self._color_palette.get(
            theme_name, self._color_palette["light"]
        )
        for key, value in palette.items():
            tpl = tpl.replace("{{" + key + "}}", value)

        self._qss_cache[theme_name] = tpl
        return tpl

    def get_color(self, semantic_name: str) -> str:
        """根据语义名称获取当前主题对应的颜色值。

        参数:
            semantic_name: 语义颜色键名（如"bg_primary"）。

        返回:
            str: 颜色hex字符串，未找到时返回"#000000"。
        """
        theme = self.get_effective_theme()
        palette = self._color_palette.get(theme, self._color_palette["light"])
        return palette.get(semantic_name, "#000000")

    def _build_fallback_qss(self, theme_name: str) -> str:
        """构建回退最小QSS样式表。

        当主题QSS文件不存在或读取失败时使用，
        基于QPalette的基础配色方案。

        参数:
            theme_name: 主题名称。

        返回:
            str: 回退QSS样式表字符串。
        """
        palette = self._color_palette.get(
            theme_name, self._color_palette["light"]
        )
        return f"""
            QMainWindow {{
                background-color: {palette.get("bg_primary", "#F5F5F5")};
            }}
            QMenuBar {{
                background-color: {palette.get("bg_secondary", "#EAEAEA")};
                color: {palette.get("text_primary", "#1E1E2E")};
            }}
            QStatusBar {{
                background-color: {palette.get("bg_secondary", "#EAEAEA")};
                color: {palette.get("text_secondary", "#606070")};
            }}
        """
