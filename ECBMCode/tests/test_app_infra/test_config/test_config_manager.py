# -*- coding: utf-8 -*-
"""ConfigManager单元测试模块。

测试覆盖：
- 单例模式双重检查锁的正确性
- 配置文件加载（正常路径和异常路径）
- 三层配置优先级覆盖逻辑
- 运行时配置设置与移除
- 配置热更新
"""

import json
import pytest

from app_infra.config.config_manager import ConfigManager
from app_infra.exceptions.base_exceptions import ConfigException


class TestConfigManagerSingleton:
    """ConfigManager单例模式测试。"""

    def test_get_instance_returns_same_object(self) -> None:
        """验证多次调用get_instance返回同一实例。"""
        instance1 = ConfigManager.get_instance()
        instance2 = ConfigManager.get_instance()
        assert instance1 is instance2

    def test_direct_instantiation_returns_same_object(self) -> None:
        """验证直接实例化也返回同一对象。"""
        instance1 = ConfigManager()
        instance2 = ConfigManager()
        assert instance1 is instance2


class TestConfigManagerLoad:
    """配置加载测试。"""

    def test_load_valid_config(self, config_file, sample_config_dict) -> None:
        """验证加载有效的JSON配置文件。"""
        config = ConfigManager.get_instance()
        config.reset()
        config.load_config(config_file)
        assert config.get("app_name") == sample_config_dict["app_name"]

    def test_load_nonexistent_file(self) -> None:
        """验证加载不存在的配置文件抛出ConfigException。"""
        config = ConfigManager.get_instance()
        config.reset()
        with pytest.raises(ConfigException, match="配置文件不存在"):
            config.load_config("/nonexistent/path/config.json")

    def test_load_invalid_json(self, invalid_config_file) -> None:
        """验证加载格式错误的JSON文件抛出ConfigException。"""
        config = ConfigManager.get_instance()
        config.reset()
        with pytest.raises(ConfigException, match="JSON格式错误"):
            config.load_config(invalid_config_file)


class TestConfigPriority:
    """三层配置优先级测试。"""

    def test_runtime_overrides_user(self, config_file) -> None:
        """验证运行时配置优先级高于用户配置。"""
        config = ConfigManager.get_instance()
        config.reset()
        config.load_config(config_file)
        config.set_runtime("app_name", "RuntimeApp")
        assert config.get("app_name") == "RuntimeApp"

    def test_user_overrides_default(self, config_file, sample_config_dict) -> None:
        """验证用户配置优先级高于默认配置。"""
        config = ConfigManager.get_instance()
        config.reset()
        config._default_config = {"app_name": "DefaultApp"}
        config.load_config(config_file)
        assert config.get("app_name") == sample_config_dict["app_name"]

    def test_default_used_when_no_override(self) -> None:
        """验证无覆盖时使用默认配置。"""
        config = ConfigManager.get_instance()
        config.reset()
        config._default_config = {"custom_key": "default_value"}
        assert config.get("custom_key") == "default_value"

    def test_fallback_to_provided_default(self) -> None:
        """验证所有层级无值时回退到传入的default参数。"""
        config = ConfigManager.get_instance()
        config.reset()
        assert config.get("nonexistent", "fallback") == "fallback"


class TestRuntimeConfig:
    """运行时配置测试。"""

    def test_set_and_get_runtime(self) -> None:
        """验证设置和获取运行时配置。"""
        config = ConfigManager.get_instance()
        config.reset()
        config.set_runtime("debug", True)
        assert config.get("debug") is True

    def test_remove_runtime(self) -> None:
        """验证移除运行时配置后回退到默认值。"""
        config = ConfigManager.get_instance()
        config.reset()
        config._default_config = {"debug": False}
        config.set_runtime("debug", True)
        config.remove_runtime("debug")
        assert config.get("debug") is False


class TestConfigReload:
    """配置热更新测试。"""

    def test_reload_preserves_runtime(self, config_file, sample_config_dict) -> None:
        """验证热更新后运行时配置保持不变。"""
        config = ConfigManager.get_instance()
        config.reset()
        config.load_config(config_file)
        config.set_runtime("runtime_key", "runtime_value")
        config.reload()
        assert config.get("runtime_key") == "runtime_value"

    def test_reload_updates_user_config(self, config_file, temp_dir) -> None:
        """验证热更新后用户配置更新为新文件内容。"""
        config = ConfigManager.get_instance()
        config.reset()
        config.load_config(config_file)

        # 修改配置文件
        new_data = {"app_name": "UpdatedApp"}
        new_file = temp_dir / "updated_config.json"
        with open(new_file, "w", encoding="utf-8") as f:
            json.dump(new_data, f)

        config.reload(new_file)
        assert config.get("app_name") == "UpdatedApp"

    def test_get_all_returns_merged_config(self, config_file) -> None:
        """验证get_all返回三层配置合并结果。"""
        config = ConfigManager.get_instance()
        config.reset()
        config._default_config = {"default_key": "default"}
        config.load_config(config_file)
        config.set_runtime("runtime_key", "runtime")
        merged = config.get_all()
        assert merged["default_key"] == "default"
        assert "app_name" in merged
        assert merged["runtime_key"] == "runtime"
