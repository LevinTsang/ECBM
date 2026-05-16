# -*- coding: utf-8 -*-
"""插件接口抽象基类模块。

PluginBase定义所有插件的统一接口契约，包括：
- activate()：激活插件
- deactivate()：停用插件
- get_info()：获取插件元信息

插件开发者必须继承PluginBase并实现全部抽象方法。
"""

from abc import ABC, abstractmethod


class PluginBase(ABC):
    """插件接口抽象基类。

    所有ECBM插件必须继承此类并实现全部抽象方法。
    插件通过动态导入和反射机制加载，调用activate激活后
    注册到全局插件注册表中。

    插件生命周期：
    1. 扫描发现 -> 2. 动态导入 -> 3. 实例化 ->
    4. activate() -> 5. 运行中 -> 6. deactivate() -> 7. 卸载
    """

    @abstractmethod
    def activate(self) -> bool:
        """激活插件。

        在此方法中执行插件初始化逻辑：
        资源分配、信号连接、服务注册等。

        返回:
            bool: 激活成功返回True，失败返回False。
        """
        ...

    @abstractmethod
    def deactivate(self) -> bool:
        """停用插件。

        在此方法中执行插件清理逻辑：
        资源释放、信号断开、服务注销等。

        返回:
            bool: 停用成功返回True，失败返回False。
        """
        ...

    @abstractmethod
    def get_info(self) -> dict:
        """获取插件元信息。

        返回:
            dict: 包含以下键的元信息字典：
                - name (str): 插件名称
                - version (str): 插件版本号
                - author (str): 插件作者
                - description (str): 插件功能描述
        """
        ...
