# -*- coding: utf-8 -*-
"""应用程序主入口模块。

本模块是ECBM应用的唯一入口点，负责：
1. 解析命令行参数
2. 加载应用配置
3. 初始化日志系统
4. 创建QApplication实例
5. 注册全局异常捕获钩子
6. 初始化核心服务控制器
7. 显示主窗口并进入事件循环
"""

import sys
import argparse
import traceback
from pathlib import Path

from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtCore import QObject, QEvent

from app_infra.config.config_manager import ConfigManager
from app_infra.logging.log_manager import LogManager
from app_infra.utils.path_utils import get_project_root, ensure_dir
from app_core.controllers.base_controller import BaseController
from app_ui.main_window import MainWindow
from app_ui.signals import SharedSignals


def _setup_global_exception_handler(logger) -> None:
    """注册全局异常捕获钩子。

    通过替换sys.excepthook捕获主线程中所有未被try-except处理的异常，
    记录完整堆栈到日志并弹出友好提示对话框。
    KeyboardInterrupt保留系统默认行为以确保Ctrl+C能正常终止应用。
    """

    def _handler(exc_type, exc_value, exc_tb) -> None:
        if issubclass(exc_type, KeyboardInterrupt):
            sys.__excepthook__(exc_type, exc_value, exc_tb)
            return
        trace_str = "".join(traceback.format_exception(
            exc_type, exc_value, exc_tb
        ))
        logger.critical(f"未处理的异常:\n{trace_str}")
        app = QApplication.instance()
        if app is not None:
            try:
                QMessageBox.critical(
                    None,
                    "未处理异常",
                    f"应用程序发生未处理的异常:\n\n{exc_value}\n\n详情请查看日志文件。"
                )
            except Exception:
                pass
        sys.exit(1)

    sys.excepthook = _handler


class _SafeApplication(QApplication):
    """安全QApplication子类。

    重写notify方法以捕获PyQt6事件循环中抛出的异常，
    防止Qt事件处理异常导致应用静默崩溃。
    notify内部的异常保护代码本身不抛出异常，避免无限递归。
    """

    def notify(self, receiver: QObject, event: QEvent) -> bool:
        try:
            return super().notify(receiver, event)
        except Exception:
            try:
                trace_str = "".join(traceback.format_exc())
                print(f"[事件循环异常]\n{trace_str}", file=sys.stderr)
            except Exception:
                print("[事件循环异常] 无法格式化异常详情", file=sys.stderr)
            return False


def _parse_args() -> argparse.Namespace:
    """解析命令行参数。

    预留 --config、--log-level、--debug 三个参数，
    供开发和部署场景灵活配置应用行为。

    返回:
        argparse.Namespace: 解析后的命令行参数对象。
    """
    parser = argparse.ArgumentParser(description="ECBM Application")
    parser.add_argument(
        "--config", type=str, default=None,
        help="用户配置文件的绝对路径（JSON格式）"
    )
    parser.add_argument(
        "--log-level", type=str, default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="日志输出级别阈值"
    )
    parser.add_argument(
        "--debug", action="store_true",
        help="启用调试模式（等价于 --log-level DEBUG）"
    )
    return parser.parse_args()


def _load_configuration(args: argparse.Namespace) -> ConfigManager:
    """加载应用配置。

    按照默认配置 -> 用户配置文件 -> 运行时参数的优先级
    逐层合并配置数据。

    参数:
        args: 命令行参数对象。

    返回:
        ConfigManager: 已加载配置的单例实例。
    """
    config = ConfigManager.get_instance()

    # 构建默认配置
    config._default_config = {
        "app_name": "ECBM",
        "version": "0.1.0",
        "organization": "ECBM",
        "log_level": "INFO",
        "log_dir": "",
        "enable_console_log": True,
        "enable_file_log": True,
        "window_width": 1024,
        "window_height": 768,
        "window_min_width": 800,
        "window_min_height": 500,
        "language": "zh_CN",
        "theme_mode": "system",
        "reduce_motion": False,
    }

    # 加载用户配置文件
    config_path = args.config
    if config_path is not None:
        try:
            config.load_config(config_path)
        except Exception:
            pass

    # 命令行参数覆盖
    if args.debug:
        config.set_runtime("debug", True)
        config.set_runtime("log_level", "DEBUG")

    if args.log_level and not args.debug:
        config.set_runtime("log_level", args.log_level)

    return config


def _initialize_logging(config: ConfigManager) -> LogManager:
    """初始化日志系统。

    从配置中读取日志相关参数，初始化LogManager，
    确保日志目录存在。

    参数:
        config: 已加载的配置管理器。

    返回:
        LogManager: 已初始化的日志管理器。
    """
    log_manager = LogManager()
    app_name = config.get("app_name", "ECBM")
    log_level = config.get("log_level", "INFO")
    log_dir = config.get("log_dir", "")
    enable_console = config.get("enable_console_log", True)
    enable_file = config.get("enable_file_log", True)

    # 如果未指定日志目录，使用项目根目录下的logs子目录
    if not log_dir:
        log_dir = str(get_project_root() / "logs")

    ensure_dir(log_dir)

    log_manager.setup(
        app_name=app_name,
        log_level=log_level,
        log_dir=log_dir,
        enable_console=enable_console,
        enable_file=enable_file,
    )

    return log_manager


def _create_application(config: ConfigManager) -> QApplication:
    """创建并配置QApplication实例。

    参数:
        config: 已加载的配置管理器。

    返回:
        QApplication: 已配置的应用程序实例。
    """
    app = _SafeApplication(sys.argv)
    app.setApplicationName(config.get("app_name", "ECBM"))
    app.setOrganizationName(config.get("organization", "ECBM"))
    app.setApplicationVersion(config.get("version", "0.1.0"))
    return app


def main() -> int:
    """应用程序主入口函数。

    按照启动流程依次完成：解析参数 -> 加载配置 -> 初始化日志 ->
    创建QApplication -> 注册异常钩子 -> 初始化服务 -> 显示主窗口 ->
    进入事件循环。

    返回:
        int: 应用程序退出码（0=正常退出，1=异常退出）。
    """
    args = _parse_args()
    config = _load_configuration(args)
    log_manager = _initialize_logging(config)
    logger = log_manager.get_logger("main")
    logger.info("ECBM 应用程序启动中...")

    _setup_global_exception_handler(logger)

    app = _create_application(config)

    # 连接退出信号
    signals = SharedSignals()
    app.lastWindowClosed.connect(
        lambda: logger.info("最后一个窗口已关闭，应用程序退出")
    )

    try:
        # 初始化核心服务控制器
        controller = BaseController()
        controller.initialize()
        logger.info("核心服务控制器初始化完成")

        # 创建并配置主窗口（窗口尺寸在__init__中通过黄金比例计算）
        main_window = MainWindow()
        main_window.setup_ui()
        main_window.set_controller(controller)

        # 显示主窗口
        main_window.show()
        signals.app_started.emit()
        logger.info("主窗口已显示，进入事件循环")

        exit_code = app.exec()
        logger.info(f"事件循环结束，退出码: {exit_code}")
        return exit_code

    except Exception as e:
        trace_str = "".join(traceback.format_exc())
        logger.critical(f"应用程序启动失败:\n{trace_str}")
        try:
            QMessageBox.critical(
                None,
                "启动失败",
                f"应用程序启动过程中发生致命错误:\n\n{e}"
            )
        except Exception:
            pass
        return 1


if __name__ == "__main__":
    sys.exit(main())
