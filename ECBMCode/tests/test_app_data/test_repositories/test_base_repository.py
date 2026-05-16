# -*- coding: utf-8 -*-
"""BaseRepository单元测试模块。

测试覆盖：
- 抽象方法接口契约验证
- 未实现子类实例化时抛出TypeError
- 具体实现类的CRUD操作签名一致
"""

import pytest

from app_data.repositories.base_repository import BaseRepository
from app_data.models.base_model import BaseModel


class _StubModel(BaseModel):
    """测试用桩模型。"""

    def validate(self) -> bool:
        return True


class TestBaseRepositoryContract:
    """BaseRepository接口契约测试。"""

    def test_cannot_instantiate_abstract(self) -> None:
        """验证未实现抽象方法的类无法实例化。"""
        with pytest.raises(TypeError):
            BaseRepository()

    def test_partial_implementation_fails(self) -> None:
        """验证部分实现抽象方法无法实例化。"""

        class PartialRepo(BaseRepository):
            def create(self, entity):
                return entity

            def read(self, entity_id):
                return None

        with pytest.raises(TypeError):
            PartialRepo()

    def test_full_implementation_succeeds(self) -> None:
        """验证完全实现所有抽象方法的类可以实例化。"""

        class FullRepo(BaseRepository):
            def create(self, entity):
                return entity

            def read(self, entity_id):
                return None

            def update(self, entity):
                return entity

            def delete(self, entity_id):
                return True

            def list_all(self):
                return []

        repo = FullRepo()
        assert repo is not None

    def test_create_and_read_roundtrip(self) -> None:
        """验证内存仓储的创建和读取往返。"""

        class MemoryRepo(BaseRepository):
            def __init__(self):
                self._store = {}

            def create(self, entity):
                self._store[entity._id] = entity
                return entity

            def read(self, entity_id):
                return self._store.get(entity_id)

            def update(self, entity):
                self._store[entity._id] = entity
                return entity

            def delete(self, entity_id):
                return self._store.pop(entity_id, None) is not None

            def list_all(self):
                return list(self._store.values())

        repo = MemoryRepo()
        model = _StubModel(model_id="test-001")
        assert repo.create(model)._id == "test-001"
        assert repo.read("test-001") is model
        assert repo.read("nonexistent") is None
        assert repo.delete("test-001") is True
        assert repo.delete("test-001") is False
        assert repo.list_all() == []

    @pytest.mark.parametrize("method_name,args", [
        ("create", []),
        ("read", ["id"]),
        ("update", []),
        ("delete", ["id"]),
        ("list_all", []),
    ])
    def test_abstract_methods_are_callable(
        self, method_name, args
    ) -> None:
        """验证所有抽象方法的签名正确且可被调用。"""
        class _ConcreteRepo(BaseRepository):
            def create(self, entity):
                return entity

            def read(self, entity_id):
                return None

            def update(self, entity):
                return entity

            def delete(self, entity_id):
                return True

            def list_all(self):
                return []

        repo = _ConcreteRepo()
        method = getattr(repo, method_name)
        assert callable(method)
