# -*- coding: utf-8 -*-
"""pytest全局配置文件。

定义测试框架的全局fixture，供所有测试模块共享使用。
包括：QApplication实例、配置管理器、日志管理器、临时目录等。
"""

import sys
import json
import tempfile
import atexit
import shutil
from pathlib import Path

import pytest

from PyQt6.QtWidgets import QApplication


@pytest.fixture(scope="session")
def qapp() -> QApplication:
    """创建session级别的QApplication实例。

    确保整个测试会话中只有一个QApplication实例，
    避免多次创建导致的Qt警告。

    返回:
        QApplication: 测试会话共享的QApplication实例。
    """
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    yield app


@pytest.fixture(scope="function")
def temp_dir() -> Path:
    """创建函数级别的临时目录。

    每个测试函数使用独立的临时目录，
    测试结束后自动清理。

    返回:
        Path: 临时目录的Path对象。
    """
    tmp = Path(tempfile.mkdtemp(prefix="ecbm_test_"))
    yield tmp
    shutil.rmtree(tmp, ignore_errors=True)


@pytest.fixture(scope="function")
def sample_config_dict() -> dict:
    """提供示例配置字典。

    返回:
        dict: 包含完整配置项的示例字典。
    """
    return {
        "app_name": "ECBM_Test",
        "version": "0.1.0",
        "organization": "ECBM",
        "log_level": "DEBUG",
        "log_dir": "",
        "enable_console_log": True,
        "enable_file_log": False,
        "window_width": 1024,
        "window_height": 768,
        "window_min_width": 800,
        "window_min_height": 500,
        "language": "zh_CN",
        "theme_mode": "system",
        "reduce_motion": False,
    }


@pytest.fixture(scope="function")
def config_file(temp_dir: Path, sample_config_dict: dict) -> Path:
    """创建测试用JSON配置文件。

    参数:
        temp_dir: 临时目录fixture。
        sample_config_dict: 示例配置字典fixture。

    返回:
        Path: 测试配置文件路径。
    """
    file_path = temp_dir / "test_config.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(sample_config_dict, f, ensure_ascii=False, indent=2)
    return file_path


@pytest.fixture(scope="function")
def invalid_config_file(temp_dir: Path) -> Path:
    """创建格式错误的测试用JSON配置文件。

    参数:
        temp_dir: 临时目录fixture。

    返回:
        Path: 格式错误的测试配置文件路径。
    """
    file_path = temp_dir / "invalid_config.json"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("{invalid json content {{{")
    return file_path
