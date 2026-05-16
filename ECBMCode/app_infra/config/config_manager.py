# -*- coding: utf-8 -*-
"""配置管理单例模块。

实现ConfigManager全局单例类，负责应用配置的集中管理。
支持三层配置优先级：运行时配置 > 用户配置 > 默认配置。
提供配置文件热更新能力，通过SharedSignals广播配置变更事件。
"""

import json
import threading
import copy
from pathlib import Path
from typing import Any

from app_infra.exceptions.base_exceptions import ConfigException


class ConfigManager:
    """全局配置管理单例类。

    使用双重检查锁（DCL）模式确保多线程环境下的实例唯一性。
    配置按三层优先级组织：
    1. _runtime_config（最高优先级）：运行时通过set_runtime动态设置
    2. _user_config：从JSON用户配置文件加载
    3. _default_config（最低优先级）：程序中硬编码的默认值

    属性:
        _instance (ConfigManager | None): 单例私有实例（类属性）。
        _lock (threading.Lock): 线程锁，保障实例创建线程安全（类属性）。
        _default_config (dict[str, Any]): 默认配置字典。
        _user_config (dict[str, Any]): 用户配置文件加载的配置字典。
        _runtime_config (dict[str, Any]): 运行时覆盖配置字典。
    """

    _instance: "ConfigManager | None" = None
    _lock: threading.Lock = threading.Lock()

    def __new__(cls) -> "ConfigManager":
        """创建或返回单例实例。

        使用双重检查锁模式确保多线程安全：
        第一层检查避免不必要的锁竞争，第二层检查确保实例唯一性。

        返回:
            ConfigManager: 全局唯一的配置管理器实例。
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        """初始化配置管理器。

        使用hasattr守卫防止单例重复初始化：
        仅在首次__init__调用时执行初始化逻辑。
        """
        if not hasattr(self, "_initialized"):
            self._default_config: dict[str, Any] = {}
            self._user_config: dict[str, Any] = {}
            self._runtime_config: dict[str, Any] = {}
            self._config_path: str | Path | None = None
            self._initialized: bool = True

    @staticmethod
    def get_instance() -> "ConfigManager":
        """获取ConfigManager单例实例。

        返回:
            ConfigManager: 全局唯一的配置管理器实例。
        """
        return ConfigManager()

    def load_config(self, config_path: str | Path) -> None:
        """加载用户配置文件（JSON格式）。

        从指定路径读取JSON配置文件，解析后存入_user_config字典。
        加载前会先合并默认配置，确保所有键都有默认值兜底。

        参数:
            config_path: JSON配置文件的绝对或相对路径。

        异常:
            ConfigException: 配置文件不存在时抛出。
            json.JSONDecodeError: JSON格式错误时抛出，调用方需捕获。
        """
        path = Path(config_path)
        if not path.exists():
            raise ConfigException(
                f"配置文件不存在: {config_path}",
                error_code="CFG_001"
            )
        if not path.is_file():
            raise ConfigException(
                f"配置路径不是文件: {config_path}",
                error_code="CFG_002"
            )

        try:
            with open(path, "r", encoding="utf-8") as f:
                loaded_data = json.load(f)
        except json.JSONDecodeError as e:
            raise ConfigException(
                f"配置文件JSON格式错误: {e}",
                error_code="CFG_003"
            ) from e

        if not isinstance(loaded_data, dict):
            raise ConfigException(
                "配置文件根元素必须是JSON对象(dict)",
                error_code="CFG_004"
            )

        self._user_config = loaded_data
        self._config_path = path

    def get(self, key: str, default: Any = None) -> Any:
        """按三层优先级获取配置值。

        优先级从高到低：
        1. _runtime_config（运行时覆盖）
        2. _user_config（用户配置文件）
        3. _default_config（默认配置）

        参数:
            key: 配置项键名。
            default: 所有层级均未找到时的默认返回值。

        返回:
            Any: 查找到的配置值，或default。
        """
        if key in self._runtime_config:
            return self._runtime_config[key]
        if key in self._user_config:
            return self._user_config[key]
        if key in self._default_config:
            return self._default_config[key]
        return default

    def set_runtime(self, key: str, value: Any) -> None:
        """设置运行时配置覆盖值。

        运行时配置具有最高优先级，覆盖默认配置和用户配置中同名的值。
        运行时配置不会持久化到文件。

        参数:
            key: 配置项键名。
            value: 配置项新值。
        """
        self._runtime_config[key] = value

    def remove_runtime(self, key: str) -> None:
        """移除指定的运行时配置覆盖项。

        移除后该键的配置值回退到用户配置或默认配置。

        参数:
            key: 需要移除的配置项键名。
        """
        self._runtime_config.pop(key, None)

    def reload(self, config_path: str | Path | None = None) -> None:
        """热更新配置文件。

        重新读取指定路径（或上次加载路径）的JSON配置文件，
        更新_user_config。运行时配置覆盖项在reload后保持不变。

        参数:
            config_path: 配置文件路径，为None时使用上次加载的路径。

        异常:
            ConfigException: 无可用配置文件路径时抛出。
        """
        target_path = config_path or self._config_path
        if target_path is None:
            raise ConfigException(
                "未指定配置文件路径，且无历史加载记录",
                error_code="CFG_005"
            )

        # 保存当前运行时配置
        saved_runtime = copy.deepcopy(self._runtime_config)

        try:
            self.load_config(target_path)
        except ConfigException:
            raise

        # 恢复运行时配置
        self._runtime_config = saved_runtime

    def get_all(self) -> dict[str, Any]:
        """获取合并后的全部配置字典。

        按照优先级将三层配置合并为一个字典。

        返回:
            dict[str, Any]: 合并后的配置字典。
        """
        merged = copy.deepcopy(self._default_config)
        merged.update(self._user_config)
        merged.update(self._runtime_config)
        return merged

    def reset(self) -> None:
        """重置所有配置到初始状态。

        清空用户配置、运行时配置和配置路径记录，
        默认配置保持不变。主要用于测试场景。
        """
        self._user_config = {}
        self._runtime_config = {}
        self._config_path = None
