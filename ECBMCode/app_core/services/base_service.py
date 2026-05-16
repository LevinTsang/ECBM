# -*- coding: utf-8 -*-
"""业务服务抽象基类模块。

BaseService是所有业务服务的基类，提供：
- 数据仓储引用（_repository）
- 日志记录器（_logger）
- 服务生命周期钩子（initialize / dispose）

具体服务通过继承BaseService并重写钩子方法实现业务逻辑。
"""

import logging
from abc import ABC

from app_data.repositories.base_repository import BaseRepository
from app_infra.logging.log_manager import LogManager


class BaseService(ABC):
    """业务服务抽象基类。

    所有业务服务需继承此类。基类提供：
    - 关联的数据仓储实例引用
    - 日志记录器
    - 初始化和销毁的生命周期钩子

    属性:
        _repository (BaseRepository | None): 关联的数据仓储实例。
        _logger (logging.Logger): 服务日志记录器。
    """

    def __init__(self, repository: BaseRepository | None = None) -> None:
        """初始化业务服务。

        参数:
            repository: 关联的数据仓储实例，可为None（后续注入）。
        """
        self._repository: BaseRepository | None = repository
        self._logger: logging.Logger = LogManager().get_logger(
            self.__class__.__name__
        )

    def initialize(self) -> None:
        """服务初始化钩子。

        在服务启动时调用，用于资源分配、连接建立等初始化操作。
        子类可按需重写此方法。

        异常:
            NotImplementedError: 子类按需重写，基类为空实现。
        """
        self._logger.debug(f"服务 {self.__class__.__name__} 初始化完成")

    def dispose(self) -> None:
        """服务销毁钩子。

        在服务销毁时调用，用于资源释放、连接关闭等清理操作。
        子类可按需重写此方法。
        dispose操作为best-effort：即使清理失败也不应抛出异常。

        异常:
            NotImplementedError: 子类按需重写，基类为空实现。
        """
        self._logger.debug(f"服务 {self.__class__.__name__} 已销毁")

    def set_repository(self, repository: BaseRepository) -> None:
        """注入数据仓储实例。

        参数:
            repository: 数据仓储实例。
        """
        self._repository = repository

    def get_repository(self) -> BaseRepository | None:
        """获取关联的数据仓储实例。

        返回:
            BaseRepository | None: 当前关联的仓储实例。
        """
        return self._repository
