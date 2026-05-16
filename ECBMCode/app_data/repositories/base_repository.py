# -*- coding: utf-8 -*-
"""数据仓储接口抽象基类模块。

BaseRepository使用Python abc模块定义CRUD操作的接口契约，
确保所有仓储实现类遵循统一的方法签名。
具体实现类可按需替换（内存存储、SQLite、MySQL等）。
"""

from abc import ABC, abstractmethod

from app_data.models.base_model import BaseModel


class BaseRepository(ABC):
    """数据仓储接口抽象基类。

    定义通用CRUD操作契约，所有具体仓储实现必须继承此类
    并实现全部抽象方法。
    Repository模式隔离业务逻辑与数据持久化细节。
    """

    @abstractmethod
    def create(self, entity: BaseModel) -> BaseModel:
        """创建新记录。

        参数:
            entity: 待持久化的数据模型实例。

        返回:
            BaseModel: 创建成功后的数据模型实例（含持久化后的状态）。
        """
        ...

    @abstractmethod
    def read(self, entity_id: str) -> BaseModel | None:
        """读取单条记录。

        参数:
            entity_id: 待查询记录的唯一标识符。

        返回:
            BaseModel | None: 查找到的模型实例，不存在时返回None。
        """
        ...

    @abstractmethod
    def update(self, entity: BaseModel) -> BaseModel:
        """更新记录。

        参数:
            entity: 包含更新数据的数据模型实例（_id必须匹配已存在的记录）。

        返回:
            BaseModel: 更新后的模型实例。
        """
        ...

    @abstractmethod
    def delete(self, entity_id: str) -> bool:
        """删除记录。

        参数:
            entity_id: 待删除记录的唯一标识符。

        返回:
            bool: 删除成功返回True，记录不存在返回False。
        """
        ...

    @abstractmethod
    def list_all(self) -> list[BaseModel]:
        """列出所有记录。

        返回:
            list[BaseModel]: 所有模型实例的列表。
        """
        ...
