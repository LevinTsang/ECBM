# -*- coding: utf-8 -*-
"""自定义异常体系模块。

定义ECBM应用完整的异常类树，所有自定义异常均继承自ECBMException根异常。
异常类包含message（错误描述）和error_code（错误码）两个属性，
便于日志记录、问题定位和用户友好提示。

异常类树：
    ECBMException（根异常）
    ├── BusinessException（业务逻辑异常）
    ├── UIException（用户界面异常）
    ├── DataException（数据访问异常）
    └── ConfigException（配置管理异常）
"""


class ECBMException(Exception):
    """应用根异常类。

    所有ECBM自定义异常的基类，统一携带错误描述信息和错误码。

    属性:
        message (str): 人类可读的错误描述信息。
        error_code (str): 错误码标识，格式为"领域_编号"（如"CFG_001"）。
    """

    def __init__(self, message: str, error_code: str = "ECBM_000") -> None:
        """初始化应用根异常。

        参数:
            message: 错误描述信息。
            error_code: 错误码标识，默认"ECBM_000"。
        """
        self.message: str = message
        self.error_code: str = error_code
        super().__init__(self.message)

    def __str__(self) -> str:
        """返回格式化的异常字符串表示。

        返回:
            str: 格式为"[error_code] message"的异常描述。
        """
        return f"[{self.error_code}] {self.message}"


class BusinessException(ECBMException):
    """业务逻辑异常。

    用于表示业务规则校验失败、业务流程异常等业务层面的错误。
    默认错误码：BIZ_000。
    """

    def __init__(self, message: str, error_code: str = "BIZ_000") -> None:
        """初始化业务异常。

        参数:
            message: 错误描述信息。
            error_code: 错误码标识。
        """
        super().__init__(message, error_code)


class UIException(ECBMException):
    """用户界面异常。

    用于表示UI组件渲染失败、界面交互异常等表现层的错误。
    默认错误码：UI_000。
    """

    def __init__(self, message: str, error_code: str = "UI_000") -> None:
        """初始化UI异常。

        参数:
            message: 错误描述信息。
            error_code: 错误码标识。
        """
        super().__init__(message, error_code)


class DataException(ECBMException):
    """数据访问异常。

    用于表示数据持久化操作失败、数据校验不通过等数据层的错误。
    默认错误码：DAT_000。
    """

    def __init__(self, message: str, error_code: str = "DAT_000") -> None:
        """初始化数据访问异常。

        参数:
            message: 错误描述信息。
            error_code: 错误码标识。
        """
        super().__init__(message, error_code)


class ConfigException(ECBMException):
    """配置管理异常。

    用于表示配置文件加载失败、配置项缺失或格式错误等配置层错误。
    默认错误码：CFG_000。
    """

    def __init__(self, message: str, error_code: str = "CFG_000") -> None:
        """初始化配置异常。

        参数:
            message: 错误描述信息。
            error_code: 错误码标识。
        """
        super().__init__(message, error_code)
