# -*- coding: utf-8 -*-
"""BaseModel单元测试模块。

测试覆盖：
- 模型实例化与默认值设置
- 序列化（to_dict）和反序列化（from_dict）的往返一致性
- 时间戳更新（touch）
- 未实现validate的验证
"""

import time
import pytest

from app_data.models.base_model import BaseModel


class _ConcreteModel(BaseModel):
    """测试用具体模型类，实现validate方法。"""

    def validate(self) -> bool:
        return bool(self._id)


class TestBaseModelInit:
    """BaseModel初始化测试。"""

    def test_init_with_defaults(self) -> None:
        """验证使用默认参数创建实例。"""
        model = _ConcreteModel()
        assert model._id is not None
        assert len(model._id) > 0
        assert model._created_at > 0
        assert model._updated_at > 0

    def test_init_with_explicit_id(self) -> None:
        """验证使用显式ID创建实例。"""
        model = _ConcreteModel(model_id="test-001")
        assert model._id == "test-001"
        assert model.id == "test-001"

    def test_init_with_timestamps(self) -> None:
        """验证使用显式时间戳创建实例。"""
        created = 1000.0
        updated = 2000.0
        model = _ConcreteModel(created_at=created, updated_at=updated)
        assert model.created_at == created
        assert model.updated_at == updated

    def test_touch_updates_timestamp(self) -> None:
        """验证touch方法更新时间戳。"""
        model = _ConcreteModel()
        original = model.updated_at
        time.sleep(0.01)
        model.touch()
        assert model.updated_at > original


class TestBaseModelSerialization:
    """BaseModel序列化测试。"""

    def test_to_dict_contains_core_fields(self) -> None:
        """验证to_dict包含核心字段。"""
        model = _ConcreteModel(model_id="uuid-123")
        data = model.to_dict()
        assert data["_id"] == "uuid-123"
        assert "_created_at" in data
        assert "_updated_at" in data

    def test_from_dict_creates_correct_instance(self) -> None:
        """验证from_dict创建正确的实例。"""
        data = {
            "_id": "from-dict-001",
            "_created_at": 1234567890.0,
            "_updated_at": 1234567899.0,
        }
        model = _ConcreteModel.from_dict(data)
        assert model._id == "from-dict-001"
        assert model.created_at == 1234567890.0
        assert model.updated_at == 1234567899.0

    def test_roundtrip_consistency(self) -> None:
        """验证to_dict和from_dict的往返一致性。"""
        original = _ConcreteModel(
            model_id="roundtrip-001",
            created_at=1000.0,
            updated_at=2000.0,
        )
        restored = _ConcreteModel.from_dict(original.to_dict())
        assert restored._id == original._id
        assert restored.created_at == original.created_at
        assert restored.updated_at == original.updated_at

    def test_from_dict_missing_fields(self) -> None:
        """验证from_dict处理缺失字段。"""
        data = {"_id": "partial-001"}
        model = _ConcreteModel.from_dict(data)
        assert model._id == "partial-001"
        # 缺失的时间戳应使用None传入构造，由__init__默认值填充
        assert model.created_at is not None


class TestBaseModelValidation:
    """BaseModel数据校验测试。"""

    def test_concrete_validate_returns_true(self) -> None:
        """验证实现了validate的具体类返回True。"""
        model = _ConcreteModel(model_id="valid-id")
        assert model.validate() is True

    def test_abstract_class_cannot_instantiate(self) -> None:
        """验证未实现validate的抽象类无法实例化。"""
        with pytest.raises(TypeError):
            BaseModel()
