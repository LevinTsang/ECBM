# -*- coding: utf-8 -*-
"""ThemeManager 模块单元测试。

测试单例模式、主题切换、颜色字典完整性和QSS加载功能。
"""

import pytest
from app_ui.theme_manager import ThemeManager


class TestThemeManagerSingleton:
    """ThemeManager 单例模式测试。"""

    def test_get_instance_returns_same(self) -> None:
        """多次调用get_instance应返回同一实例。"""
        tm1 = ThemeManager.get_instance()
        tm2 = ThemeManager.get_instance()
        assert tm1 is tm2

    def test_constructor_returns_same(self) -> None:
        """直接构造也应返回同一单例实例。"""
        tm1 = ThemeManager.get_instance()
        tm2 = ThemeManager()
        assert tm1 is tm2


class TestThemeSwitching:
    """主题切换逻辑测试。"""

    def test_set_theme_dark(self) -> None:
        """设置暗色主题应正确反映。"""
        tm = ThemeManager.get_instance()
        tm.set_theme("dark")
        assert tm.get_effective_theme() == "dark"

    def test_set_theme_light(self) -> None:
        """设置亮色主题应正确反映。"""
        tm = ThemeManager.get_instance()
        tm.set_theme("light")
        assert tm.get_effective_theme() == "light"

    def test_set_theme_system(self) -> None:
        """设置跟随系统模式应正确反映。"""
        tm = ThemeManager.get_instance()
        tm.set_theme("system")
        # system模式的具体返回值取决于操作系统主题
        result = tm.get_effective_theme()
        assert result in ("dark", "light")

    def test_toggle_theme(self) -> None:
        """切换主题应在dark和light之间切换。"""
        tm = ThemeManager.get_instance()
        tm.set_theme("dark")
        assert tm.get_effective_theme() == "dark"
        tm.toggle_theme()
        assert tm.get_effective_theme() == "light"
        tm.toggle_theme()
        assert tm.get_effective_theme() == "dark"

    def test_invalid_theme_mode_raises(self) -> None:
        """无效主题模式应抛出ValueError。"""
        tm = ThemeManager.get_instance()
        with pytest.raises(ValueError):
            tm.set_theme("invalid_mode")


class TestColorPalette:
    """颜色调色板完整性测试。"""

    def test_dark_light_same_keys(self) -> None:
        """暗色和亮色调色板应包含完全相同的键集合。"""
        tm = ThemeManager.get_instance()
        dark_keys = set(tm._DARK.keys())
        light_keys = set(tm._LIGHT.keys())
        assert dark_keys == light_keys, (
            f"暗色独有键: {dark_keys - light_keys}, "
            f"亮色独有键: {light_keys - dark_keys}"
        )

    def test_color_values_are_hex(self) -> None:
        """所有颜色值应为合法的hex颜色字符串。"""
        tm = ThemeManager.get_instance()
        for palette in [tm._DARK, tm._LIGHT]:
            for key, value in palette.items():
                assert value.startswith("#"), (
                    f"键 '{key}' 的值 '{value}' 不是hex颜色"
                )
                assert len(value) == 7, (
                    f"键 '{key}' 的值 '{value}' 长度不正确"
                )

    def test_get_color_valid_key(self) -> None:
        """有效语义键应返回颜色值。"""
        tm = ThemeManager.get_instance()
        tm.set_theme("dark")
        color = tm.get_color("bg_primary")
        assert color.startswith("#")
        assert len(color) == 7

    def test_get_color_invalid_key_default(self) -> None:
        """无效语义键应返回默认颜色。"""
        tm = ThemeManager.get_instance()
        color = tm.get_color("non_existent_key")
        assert color == "#000000"


class TestQssLoading:
    """QSS加载功能测试。"""

    def test_load_qss_dark_returns_string(self) -> None:
        """加载暗色主题QSS应返回字符串。"""
        tm = ThemeManager.get_instance()
        qss = tm.load_qss("dark")
        assert isinstance(qss, str)
        assert len(qss) > 0

    def test_load_qss_light_returns_string(self) -> None:
        """加载亮色主题QSS应返回字符串。"""
        tm = ThemeManager.get_instance()
        qss = tm.load_qss("light")
        assert isinstance(qss, str)
        assert len(qss) > 0

    def test_load_qss_caches_result(self) -> None:
        """QSS加载结果应被缓存。"""
        tm = ThemeManager.get_instance()
        qss1 = tm.load_qss("dark")
        qss2 = tm.load_qss("dark")
        assert qss1 is qss2  # 相同对象引用，证明缓存有效

    def test_load_qss_invalid_theme_fallback(self) -> None:
        """无效主题名应返回回退QSS内容。"""
        tm = ThemeManager.get_instance()
        qss = tm.load_qss("nonexistent")
        assert isinstance(qss, str)
        assert len(qss) > 0

    def test_no_unreplaced_placeholders(self) -> None:
        """替换后的QSS不应残留未替换的{{占位符}}。"""
        tm = ThemeManager.get_instance()
        for theme in ("dark", "light"):
            qss = tm.load_qss(theme)
            assert "{{" not in qss, (
                f"{theme}主题QSS存在未替换的占位符"
            )
            assert "}}" not in qss, (
                f"{theme}主题QSS存在未替换的占位符"
            )
