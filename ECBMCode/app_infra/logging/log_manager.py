# -*- coding: utf-8 -*-
"""统一日志管理模块。

LogManager封装Python标准logging模块的配置逻辑，
提供应用级日志系统初始化、日志记录器获取、动态处理器管理等功能。
支持控制台输出和文件输出双通道，文件输出使用按日期轮转策略。
"""

import logging
import logging.handlers
from pathlib import Path


class LogManager:
    """统一日志管理类。

    封装Python logging模块，提供便捷的日志系统初始化和管理接口。
    默认日志格式：[时间][级别][模块名] 消息内容
    文件日志使用TimedRotatingFileHandler实现按日期轮转。

    属性:
        _logger (logging.Logger): 根日志记录器实例。
        _handlers (list[logging.Handler]): 已注册处理器列表。
        _formatter (logging.Formatter | None): 日志格式化器。
        _initialized (bool): 是否已完成初始化标记。
    """

    def __init__(self) -> None:
        """初始化LogManager实例。"""
        self._logger: logging.Logger = logging.getLogger("ECBM")
        self._handlers: list[logging.Handler] = []
        self._formatter: logging.Formatter | None = None
        self._initialized: bool = False

    def setup(
        self,
        app_name: str = "ECBM",
        log_level: str = "INFO",
        log_dir: str | Path = "",
        enable_console: bool = True,
        enable_file: bool = True,
    ) -> None:
        """初始化日志系统配置。

        创建根日志记录器，配置日志格式，按需添加控制台和文件处理器。
        若已初始化则跳过（避免重复配置）。

        参数:
            app_name: 应用名称，作为日志记录器名称前缀。
            log_level: 日志级别阈值（DEBUG/INFO/WARNING/ERROR/CRITICAL）。
            log_dir: 日志文件存放目录路径。
            enable_console: 是否启用控制台日志输出。
            enable_file: 是否启用文件日志输出。
        """
        if self._initialized:
            return

        # 重新创建根记录器
        self._logger = logging.getLogger(app_name)

        # 设置日志级别
        level = getattr(logging, log_level.upper(), logging.INFO)
        self._logger.setLevel(level)

        # 防止日志消息向上传播到Python根记录器
        self._logger.propagate = False

        # 创建日志格式化器
        log_format = "[%(asctime)s][%(levelname)s][%(name)s] %(message)s"
        date_format = "%Y-%m-%d %H:%M:%S"
        self._formatter = logging.Formatter(log_format, date_format)

        # 添加控制台处理器
        if enable_console:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(level)
            console_handler.setFormatter(self._formatter)
            self._logger.addHandler(console_handler)
            self._handlers.append(console_handler)

        # 添加文件处理器（按日期轮转）
        if enable_file:
            log_path = Path(log_dir)
            log_path.mkdir(parents=True, exist_ok=True)

            log_file = log_path / f"{app_name}.log"
            file_handler = logging.handlers.TimedRotatingFileHandler(
                filename=str(log_file),
                when="midnight",
                interval=1,
                backupCount=30,
                encoding="utf-8",
            )
            file_handler.suffix = "%Y%m%d"
            file_handler.setLevel(level)
            file_handler.setFormatter(self._formatter)
            self._logger.addHandler(file_handler)
            self._handlers.append(file_handler)

        self._initialized = True

    def get_logger(self, name: str | None = None) -> logging.Logger:
        """获取具名日志记录器。

        若已初始化，返回app_name下的子记录器；
        若未初始化，返回Python根记录器下的子记录器。

        参数:
            name: 日志记录器名称（相对于应用根记录器）。

        返回:
            logging.Logger: 日志记录器实例。
        """
        if name is None:
            return self._logger
        return self._logger.getChild(name)

    def add_handler(self, handler: logging.Handler, level: str = "INFO") -> None:
        """动态添加自定义日志处理器。

        参数:
            handler: logging.Handler实例（如SMTPHandler、HTTPHandler等）。
            level: 该处理器的日志级别阈值。
        """
        handler_level = getattr(logging, level.upper(), logging.INFO)
        handler.setLevel(handler_level)
        if self._formatter is not None:
            handler.setFormatter(self._formatter)
        self._logger.addHandler(handler)
        self._handlers.append(handler)

    def remove_handler(self, handler: logging.Handler) -> None:
        """移除指定的日志处理器。

        参数:
            handler: 需要移除的logging.Handler实例。
        """
        self._logger.removeHandler(handler)
        if handler in self._handlers:
            self._handlers.remove(handler)

    def set_level(self, level: str) -> None:
        """动态调整根日志记录器的日志级别。

        参数:
            level: 新的日志级别（DEBUG/INFO/WARNING/ERROR/CRITICAL）。
        """
        log_level = getattr(logging, level.upper(), logging.INFO)
        self._logger.setLevel(log_level)

    def clear_handlers(self) -> None:
        """清除所有已注册的日志处理器。

        主要用于测试场景，重置日志系统状态。
        """
        for handler in self._handlers[:]:
            self._logger.removeHandler(handler)
        self._handlers.clear()
        self._initialized = False
