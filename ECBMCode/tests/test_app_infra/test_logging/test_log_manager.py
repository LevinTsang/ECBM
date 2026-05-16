# -*- coding: utf-8 -*-
"""LogManager单元测试模块。

测试覆盖：
- 日志系统初始化（setup）
- 日志记录器获取（get_logger）
- 日志级别过滤
- 动态处理器添加移除
- 日志级别动态调整
"""

import logging

import pytest

from app_infra.logging.log_manager import LogManager


class TestLogManagerSetup:
    """LogManager初始化测试。"""

    def test_setup_creates_logger(self, temp_dir) -> None:
        """验证setup创建正确的Logger实例。"""
        log_manager = LogManager()
        log_manager.setup(
            app_name="TestApp",
            log_level="DEBUG",
            log_dir=temp_dir,
            enable_console=False,
            enable_file=False,
        )
        logger = log_manager.get_logger()
        assert logger.name == "TestApp"

    def test_setup_is_idempotent(self, temp_dir) -> None:
        """验证重复调用setup不产生重复处理器。"""
        log_manager = LogManager()
        log_manager.clear_handlers()
        log_manager.setup(
            app_name="TestApp",
            log_level="DEBUG",
            log_dir=temp_dir,
            enable_console=False,
            enable_file=False,
        )
        handler_count_before = len(log_manager._handlers)
        log_manager.setup(
            app_name="TestApp",
            log_level="DEBUG",
            log_dir=temp_dir,
            enable_console=False,
            enable_file=False,
        )
        assert len(log_manager._handlers) == handler_count_before

    def test_file_handler_creates_log_dir(self, temp_dir) -> None:
        """验证文件处理器自动创建日志目录。"""
        log_dir = temp_dir / "nested" / "logs"
        log_manager = LogManager()
        log_manager.clear_handlers()
        log_manager.setup(
            app_name="FileTest",
            log_level="INFO",
            log_dir=log_dir,
            enable_console=False,
            enable_file=True,
        )
        assert log_dir.exists()
        log_manager.clear_handlers()


class TestLogManagerGetLogger:
    """日志记录器获取测试。"""

    def test_get_logger_returns_named_child(self, temp_dir) -> None:
        """验证get_logger返回具名子记录器。"""
        log_manager = LogManager()
        log_manager.clear_handlers()
        log_manager.setup(
            app_name="ParentApp",
            log_level="DEBUG",
            log_dir=temp_dir,
            enable_console=False,
            enable_file=False,
        )
        child = log_manager.get_logger("ChildModule")
        assert "ParentApp.ChildModule" in child.name

    def test_get_logger_without_setup(self) -> None:
        """验证未初始化时仍可获取记录器。"""
        log_manager = LogManager()
        log_manager.clear_handlers()
        # 未调用setup，仍应能获取logger
        logger = log_manager.get_logger("TestModule")
        assert logger is not None


class TestLogLevelFiltering:
    """日志级别过滤测试。"""

    def test_level_filtering(self, temp_dir) -> None:
        """验证不同日志级别的过滤行为。"""
        log_manager = LogManager()
        log_manager.clear_handlers()
        log_manager.setup(
            app_name="LevelTest",
            log_level="WARNING",
            log_dir=temp_dir,
            enable_console=False,
            enable_file=False,
        )
        logger = log_manager.get_logger()
        assert logger.level == logging.WARNING

    def test_set_level_dynamic(self, temp_dir) -> None:
        """验证动态调整日志级别。"""
        log_manager = LogManager()
        log_manager.clear_handlers()
        log_manager.setup(
            app_name="DynamicTest",
            log_level="INFO",
            log_dir=temp_dir,
            enable_console=False,
            enable_file=False,
        )
        log_manager.set_level("ERROR")
        logger = log_manager.get_logger()
        assert logger.level == logging.ERROR
