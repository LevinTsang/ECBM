# -*- coding: utf-8 -*-
"""自定义异常体系单元测试模块。

测试覆盖：
- 自定义异常类的继承关系验证
- 异常属性（message、error_code）正确传递
- 异常字符串表示格式验证
"""

import pytest

from app_infra.exceptions.base_exceptions import (
    ECBMException,
    BusinessException,
    UIException,
    DataException,
    ConfigException,
)


class TestExceptionInheritance:
    """异常继承关系测试。"""

    def test_business_exception_inherits_ecbm(self) -> None:
        """验证BusinessException继承自ECBMException。"""
        exc = BusinessException("业务错误")
        assert isinstance(exc, ECBMException)
        assert isinstance(exc, Exception)

    def test_ui_exception_inherits_ecbm(self) -> None:
        """验证UIException继承自ECBMException。"""
        exc = UIException("UI错误")
        assert isinstance(exc, ECBMException)

    def test_data_exception_inherits_ecbm(self) -> None:
        """验证DataException继承自ECBMException。"""
        exc = DataException("数据错误")
        assert isinstance(exc, ECBMException)

    def test_config_exception_inherits_ecbm(self) -> None:
        """验证ConfigException继承自ECBMException。"""
        exc = ConfigException("配置错误")
        assert isinstance(exc, ECBMException)


class TestExceptionAttributes:
    """异常属性测试。"""

    def test_default_error_code(self) -> None:
        """验证默认错误码设置。"""
        exc = ECBMException("通用错误")
        assert exc.error_code == "ECBM_000"
        assert exc.message == "通用错误"

    def test_custom_error_code(self) -> None:
        """验证自定义错误码设置。"""
        exc = BusinessException("业务校验失败", error_code="BIZ_101")
        assert exc.error_code == "BIZ_101"
        assert exc.message == "业务校验失败"

    def test_string_representation(self) -> None:
        """验证异常字符串表示格式。"""
        exc = ConfigException("配置项缺失", error_code="CFG_404")
        assert "[CFG_404]" in str(exc)
        assert "配置项缺失" in str(exc)

    def test_exception_raised_and_caught(self) -> None:
        """验证异常可以被正常抛出和捕获。"""
        with pytest.raises(DataException) as exc_info:
            raise DataException("数据校验失败", error_code="DAT_500")
        assert exc_info.value.error_code == "DAT_500"
        assert exc_info.value.message == "数据校验失败"
