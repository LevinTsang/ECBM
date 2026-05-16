# -*- coding: utf-8 -*-
"""数据库连接管理模块。

ConnectionManager提供数据库连接的统一管理接口，
包括连接的初始化、获取、状态检查和关闭。
当前为抽象实现，具体数据库驱动在子类或运行时按需注入。
"""

from typing import Any

from app_infra.logging.log_manager import LogManager
from app_infra.exceptions.base_exceptions import DataException


class ConnectionManager:
    """数据库连接管理类。

    管理数据库连接的生命周期，提供连接获取和关闭的接口。
    不绑定特定数据库类型，通过initialize方法按需初始化。

    属性:
        _connection (Any | None): 数据库连接对象。
        _config (dict): 数据库连接配置参数。
        _db_type (str): 数据库类型标识（如"sqlite"、"mysql"等）。
        _logger (logging.Logger): 日志记录器。
    """

    def __init__(self) -> None:
        """初始化连接管理器。"""
        self._connection: Any | None = None
        self._config: dict = {}
        self._db_type: str = ""
        self._logger = LogManager().get_logger("ConnectionManager")

    def initialize(self, db_type: str, connection_params: dict) -> None:
        """初始化数据库连接。

        根据数据库类型和连接参数建立数据库连接。
        当前为预留接口，具体驱动实现由子类负责。

        参数:
            db_type: 数据库类型标识（如"sqlite"、"mysql"、"postgresql"）。
            connection_params: 数据库连接参数字典（如host、port、database等）。

        异常:
            DataException: 数据库类型不支持或连接参数无效时抛出。
        """
        if not db_type:
            raise DataException("数据库类型不能为空", error_code="DB_001")

        self._db_type = db_type
        self._config = connection_params.copy()
        self._logger.info(
            f"数据库连接配置已保存（类型: {db_type}），等待具体驱动初始化"
        )

    def get_connection(self) -> Any:
        """获取当前数据库连接对象。

        返回:
            Any: 数据库连接对象，未初始化时返回None。

        异常:
            DataException: 连接未初始化时抛出。
        """
        if self._connection is None:
            raise DataException("数据库连接尚未建立", error_code="DB_002")
        return self._connection

    def close(self) -> None:
        """关闭数据库连接。

        安全关闭当前数据库连接并释放资源。
        关闭操作为best-effort：即使关闭失败也不抛出异常，
        仅记录错误日志。
        """
        if self._connection is not None:
            try:
                # 预留：不同数据库驱动的close方法不同
                # 子类或具体实现中按需重写此方法
                self._connection = None
                self._logger.info("数据库连接已关闭")
            except Exception as e:
                self._logger.error(f"关闭数据库连接时出错: {e}")
                self._connection = None

    def is_connected(self) -> bool:
        """检查数据库连接状态。

        返回:
            bool: 已连接返回True，未连接返回False。
        """
        return self._connection is not None
