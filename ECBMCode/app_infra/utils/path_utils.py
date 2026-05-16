# -*- coding: utf-8 -*-
"""路径工具函数模块。

提供项目根目录获取、资源路径计算、目录创建等文件系统路径相关工具函数。
所有路径操作统一使用pathlib.Path，确保跨平台兼容。
"""

from pathlib import Path


# 全局缓存项目根目录路径，避免重复计算
_project_root: Path | None = None


def get_project_root() -> Path:
    """返回项目根目录绝对路径。

    项目根目录定义为ECBMCode目录（即main.py所在目录）。
    通过本模块文件的位置向上推算得到。
    结果会被缓存，避免重复计算。

    返回:
        Path: 项目根目录的绝对路径对象。
    """
    global _project_root
    if _project_root is None:
        # 当前文件位于 app_infra/utils/path_utils.py
        # 向上3级到达ECBMCode根目录
        _project_root = Path(__file__).resolve().parent.parent.parent
    return _project_root


def get_resource_path(relative_path: str) -> Path:
    """返回静态资源的绝对路径。

    资源根目录为项目根目录下的resources/子目录。

    参数:
        relative_path: 相对于resources/的资源子路径。

    返回:
        Path: 静态资源的绝对路径对象。
    """
    return get_project_root() / "resources" / relative_path


def ensure_dir(dir_path: str | Path) -> Path:
    """确保目录存在，若不存在则递归创建。

    参数:
        dir_path: 目录路径（字符串或Path对象）。

    返回:
        Path: 已存在的目录的Path对象。
    """
    path = Path(dir_path)
    path.mkdir(parents=True, exist_ok=True)
    return path
