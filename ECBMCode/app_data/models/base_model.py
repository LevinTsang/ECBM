# -*- coding: utf-8 -*-
"""数据模型抽象基类模块。

BaseModel是所有业务数据模型的基类，提供：
- 通用标识和审计字段（_id、_created_at、_updated_at）
- 序列化/反序列化方法（to_dict/from_dict）
- 数据校验接口（validate抽象方法）
"""

import time
import uuid
from abc import ABC, abstractmethod


class BaseModel(ABC):
    """数据模型抽象基类。

    所有具体数据模型需继承此类并实现validate()抽象方法。
    提供开箱即用的序列化/反序列化能力和自动时间戳管理。

    属性:
        _id (str): 模型唯一标识符，默认使用UUID4生成。
        _created_at (float): 创建时间戳（Unix时间戳，秒级精度）。
        _updated_at (float): 最后更新时间戳（Unix时间戳，秒级精度）。
    """

    def __init__(
        self,
        model_id: str | None = None,
        created_at: float | None = None,
        updated_at: float | None = None,
    ) -> None:
        """初始化数据模型实例。

        参数:
            model_id: 模型唯一标识，为None时自动生成UUID4。
            created_at: 创建时间戳，为None时使用当前时间。
            updated_at: 更新时间戳，为None时使用当前时间。
        """
        self._id: str = model_id or str(uuid.uuid4())
        self._created_at: float = created_at or time.time()
        self._updated_at: float = updated_at or time.time()

    @property
    def id(self) -> str:
        """获取模型唯一标识符。"""
        return self._id

    @property
    def created_at(self) -> float:
        """获取创建时间戳。"""
        return self._created_at

    @property
    def updated_at(self) -> float:
        """获取最后更新时间戳。"""
        return self._updated_at

    def touch(self) -> None:
        """更新模型的更新时间戳为当前时间。"""
        self._updated_at = time.time()

    def to_dict(self) -> dict:
        """将模型序列化为字典。

        子类可重写此方法以包含额外的字段。

        返回:
            dict: 包含模型核心数据的字典。
        """
        return {
            "_id": self._id,
            "_created_at": self._created_at,
            "_updated_at": self._updated_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "BaseModel":
        """从字典反序列化创建模型实例。

        子类可重写此方法以处理额外的字段。

        参数:
            data: 包含模型数据的字典。

        返回:
            BaseModel: 从字典数据创建的模型实例。
        """
        return cls(
            model_id=data.get("_id"),
            created_at=data.get("_created_at"),
            updated_at=data.get("_updated_at"),
        )

    @abstractmethod
    def validate(self) -> bool:
        """校验模型数据完整性。

        子类必须实现此方法，定义各业务模型的数据校验规则。

        返回:
            bool: 数据校验通过返回True，否则返回False。

        异常:
            NotImplementedError: 子类未实现此方法时抛出。
        """
        raise NotImplementedError("子类必须实现validate()方法")

    def __repr__(self) -> str:
        """返回模型的字符串表示。"""
        return (
            f"{self.__class__.__name__}("
            f"id={self._id!r}, "
            f"created_at={self._created_at!r})"
        )
