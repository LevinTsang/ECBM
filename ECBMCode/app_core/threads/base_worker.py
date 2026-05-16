# -*- coding: utf-8 -*-
"""工作线程基类模块。

BaseWorker采用QObject + moveToThread的标准模式，
摒弃继承QThread重写run的做法，通过pyqtSignal实现线程安全通信。
工作线程通过信号向主线程传递进度、结果和错误信息。
"""

import logging

from PyQt6.QtCore import QObject, QThread, pyqtSignal

from app_infra.logging.log_manager import LogManager


class BaseWorker(QObject):
    """工作线程基类。

    所有耗时操作的工作线程需继承此类并实现_execute_task方法。
    使用moveToThread模式确保线程安全：
    - 工作代码在子线程执行
    - UI更新通过信号自动在主线程处理

    信号:
        progress(int): 进度更新信号，参数为0-100的进度百分比。
        finished(object): 任务完成信号，携带任务结果数据。
        error(str): 错误发生信号，携带人类可读的错误消息。
    """

    # 进度更新信号：0-100的整数值
    progress = pyqtSignal(int)
    # 任务完成信号：携带任务结果
    finished = pyqtSignal(object)
    # 错误发生信号：携带错误消息字符串
    error = pyqtSignal(str)

    def __init__(self) -> None:
        """初始化工作线程基类。"""
        super().__init__()
        self._is_running: bool = False
        self._is_cancelled: bool = False
        self._logger: logging.Logger = LogManager().get_logger(
            self.__class__.__name__
        )

    def run(self) -> None:
        """工作线程执行入口。

        在QThread.started信号触发时调用（在子线程中执行）。
        自动设置运行状态，捕获异常并通过error信号发送。
        子类可通过重写_execute_task方法定义具体任务逻辑。
        """
        self._is_running = True
        self._is_cancelled = False
        self._logger.debug(f"工作线程 {self.__class__.__name__} 开始执行")

        try:
            result = self._execute_task()
            if not self._is_cancelled:
                self.finished.emit(result)
                self._logger.debug(
                    f"工作线程 {self.__class__.__name__} 执行完成"
                )
        except Exception as e:
            self._logger.error(
                f"工作线程 {self.__class__.__name__} 执行异常: {e}"
            )
            self.error.emit(str(e))
        finally:
            self._is_running = False

    def _execute_task(self) -> object:
        """执行具体任务逻辑（抽象方法，子类必须重写）。

        子类在此方法中实现具体的耗时业务逻辑。
        执行过程中可通过self._is_cancelled检查取消状态。

        返回:
            object: 任务执行结果，通过finished信号传递给主线程。

        异常:
            NotImplementedError: 子类未重写此方法时抛出。
        """
        raise NotImplementedError("子类必须实现_execute_task()方法")

    def cancel(self) -> None:
        """请求取消当前任务。

        设置取消标志，子类的_execute_task应在适当的检查点
        检测此标志并提前终止执行。
        """
        self._is_cancelled = True
        self._logger.debug(
            f"工作线程 {self.__class__.__name__} 收到取消请求"
        )

    def is_running(self) -> bool:
        """查询线程运行状态。

        返回:
            bool: 正在运行返回True，未运行或已结束返回False。
        """
        return self._is_running

    @staticmethod
    def start_in_thread(worker: "BaseWorker") -> QThread:
        """在独立QThread中启动工作线程。

        便捷静态方法，封装moveToThread模式的样板代码：
        1. 创建QThread实例
        2. 将worker移动到新线程
        3. 连接信号槽（started -> run, finished/error -> quit）
        4. 确保线程和worker在完成后自动清理（deleteLater）
        5. 启动线程

        参数:
            worker: BaseWorker子类实例。

        返回:
            QThread: 已启动的QThread实例（调用方可持有引用用于wait）。
        """
        thread = QThread()
        worker.moveToThread(thread)

        # 线程启动时执行worker.run
        thread.started.connect(worker.run)

        # worker完成或出错时退出线程
        worker.finished.connect(thread.quit)
        worker.error.connect(thread.quit)

        # 线程结束后自动清理资源
        thread.finished.connect(thread.deleteLater)
        thread.finished.connect(worker.deleteLater)

        thread.start()
        return thread
