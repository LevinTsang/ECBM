# -*- coding: utf-8 -*-
"""共享信号声明模块。

SharedSignals类集中定义应用级全局信号，
供各模块进行跨层解耦通信。
所有信号通过pyqtSignal声明，参数类型遵循PyQt6类型映射规范。
"""

from PyQt6.QtCore import QObject, pyqtSignal


class SharedSignals(QObject):
    """共享信号声明类。

    集中管理应用级的全局pyqtSignal信号，
    各模块通过连接/发射这些信号实现解耦通信。
    使用单例模式确保全局仅有一套信号实例。

    信号:
        app_started(): 应用启动完成信号。
        app_quitting(): 应用即将退出信号。
        config_changed(str, object): 配置变更信号（配置键，新值）。
        language_changed(str): 语言切换信号（区域名称，如"zh_CN"）。
        theme_changed(str): 主题切换信号（携带"dark"或"light"）。
        size_changed(dict): 尺寸重算完成信号（携带尺寸字典）。
        tool_changed(str): 当前活跃工具变更信号（携带tool_id）。
        source_loaded(str): 内容源加载完成信号（携带源路径或URL）。
    """

    # 私有单例实例
    _instance: "SharedSignals | None" = None

    # 应用启动完成信号
    app_started = pyqtSignal()
    # 应用即将退出信号
    app_quitting = pyqtSignal()
    # 配置变更信号：key（str），new_value（object）
    config_changed = pyqtSignal(str, object)
    # 语言切换信号：locale_name（str）
    language_changed = pyqtSignal(str)
    # 主题切换信号：actual_theme_name（str，"dark"或"light"）
    theme_changed = pyqtSignal(str)
    # 尺寸重算完成信号：sizes（dict）
    size_changed = pyqtSignal(dict)
    # 当前活跃工具变更信号：tool_id（str）
    tool_changed = pyqtSignal(str)
    # 内容源加载完成信号：source（str，路径或URL）
    source_loaded = pyqtSignal(str)

    def __new__(cls) -> "SharedSignals":
        """创建或返回信号单例实例。

        返回:
            SharedSignals: 全局唯一的信号实例。
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        """初始化共享信号实例。

        QObject.__init__必须先行调用以确保hasattr守卫正常工作。
        """
        super().__init__()

        if not hasattr(self, "_signals_initialized"):
            self._signals_initialized: bool = True
