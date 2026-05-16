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

        使用hasattr守卫确保仅初始化一次。
        QObject.__init__在单例场景下可多次调用。
        """
        if not hasattr(self, "_signals_initialized"):
            super().__init__()
            self._signals_initialized: bool = True
