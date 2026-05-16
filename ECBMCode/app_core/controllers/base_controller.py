# -*- coding: utf-8 -*-
"""控制器基类模块。

BaseController继承PyQt6的QObject，作为表现层与业务逻辑层的桥梁。
负责注册和管理多个业务服务实例，协调服务的初始化与销毁。
"""

import logging

from PyQt6.QtCore import QObject

from app_core.services.base_service import BaseService
from app_infra.logging.log_manager import LogManager
from app_infra.exceptions.base_exceptions import BusinessException


class BaseController(QObject):
    """控制器基类，继承QObject。

    作为表现层和业务逻辑层之间的中间层，负责：
    - 管理多个BaseService实例的注册和获取
    - 协调服务的批量初始化和销毁
    - 隔离UI层对业务层的直接访问

    属性:
        _services (dict[str, BaseService]): 已注册服务映射字典（名称->实例）。
        _logger (logging.Logger): 控制器日志记录器。
    """

    def __init__(self) -> None:
        """初始化控制器。"""
        super().__init__()
        self._services: dict[str, BaseService] = {}
        self._logger: logging.Logger = LogManager().get_logger(
            self.__class__.__name__
        )

    def register_service(self, name: str, service: BaseService) -> None:
        """注册业务服务。

        将服务实例注册到控制器中，后续可通过get_service获取。
        若名称已存在则覆盖旧实例。

        参数:
            name: 服务唯一名称标识。
            service: BaseService子类实例。

        异常:
            BusinessException: 服务名称为空时抛出。
        """
        if not name:
            raise BusinessException("服务注册名称不能为空", error_code="CTL_001")
        if not isinstance(service, BaseService):
            raise BusinessException(
                f"服务必须是BaseService的子类: {type(service)}",
                error_code="CTL_002"
            )
        self._services[name] = service
        self._logger.info(f"服务已注册: {name} -> {service.__class__.__name__}")

    def get_service(self, name: str) -> BaseService:
        """获取已注册的服务实例。

        参数:
            name: 服务名称标识。

        返回:
            BaseService: 已注册的服务实例。

        异常:
            BusinessException: 服务未注册时抛出。
        """
        if name not in self._services:
            raise BusinessException(
                f"服务未注册: {name}",
                error_code="CTL_003"
            )
        return self._services[name]

    def initialize(self) -> None:
        """初始化所有已注册服务。

        依次调用每个服务的initialize()方法。
        单个服务初始化失败不影响其他服务，但会记录错误日志。
        """
        self._logger.info("控制器开始初始化所有服务...")
        for name, service in self._services.items():
            try:
                service.initialize()
            except Exception as e:
                self._logger.error(f"服务 {name} 初始化失败: {e}")
        self._logger.info(
            f"控制器初始化完成，共 {len(self._services)} 个服务"
        )

    def dispose(self) -> None:
        """销毁所有已注册服务。

        依次调用每个服务的dispose()方法释放资源。
        销毁操作为best-effort：单个服务销毁失败不影响其他服务，
        仅记录错误日志。
        """
        self._logger.info("控制器开始销毁所有服务...")
        for name, service in self._services.items():
            try:
                service.dispose()
            except Exception as e:
                self._logger.error(f"服务 {name} 销毁时出错: {e}")
        self._logger.info("控制器所有服务销毁完成")

    def unregister_service(self, name: str) -> None:
        """注销已注册的服务。

        参数:
            name: 需要注销的服务名称。

        异常:
            BusinessException: 服务未注册时抛出。
        """
        if name not in self._services:
            raise BusinessException(
                f"无法注销未注册的服务: {name}",
                error_code="CTL_004"
            )
        removed = self._services.pop(name)
        self._logger.info(f"服务已注销: {name} -> {removed.__class__.__name__}")
