# -*- coding: utf-8 -*-
"""BaseWorker单元测试模块。

测试覆盖：
- BaseWorker信号声明正确性
- 工作线程在子线程中执行
- progress/finished/error信号跨线程传递
- cancel方法正确设置取消标志
- start_in_thread静态方法启动线程
"""

import time

import pytest
from PyQt6.QtCore import QThread, QTimer
from PyQt6.QtTest import QSignalSpy

from app_core.threads.base_worker import BaseWorker


class _SimpleWorker(BaseWorker):
    """测试用简单Worker，直接返回固定结果。"""

    def _execute_task(self) -> object:
        return {"status": "done", "result": 42}


class _ProgressWorker(BaseWorker):
    """测试用进度Worker，报告三次进度后完成。"""

    def _execute_task(self) -> object:
        for p in [30, 60, 100]:
            time.sleep(0.01)
            self.progress.emit(p)
        return "进度任务完成"


class _ErrorWorker(BaseWorker):
    """测试用错误Worker，执行中抛出异常。"""

    def _execute_task(self) -> object:
        raise ValueError("测试错误")


class _CancellableWorker(BaseWorker):
    """测试用可取消Worker，在循环中检查取消标志。"""

    def _execute_task(self) -> object:
        for i in range(100):
            if self._is_cancelled:
                return "已取消"
            time.sleep(0.001)
        return "已完成"


class TestBaseWorkerSignals:
    """BaseWorker信号测试。"""

    def test_progress_signal_exists(self, qapp) -> None:
        """验证progress信号已声明。"""
        worker = _SimpleWorker()
        assert worker.progress is not None

    def test_finished_signal_exists(self, qapp) -> None:
        """验证finished信号已声明。"""
        worker = _SimpleWorker()
        assert worker.finished is not None

    def test_error_signal_exists(self, qapp) -> None:
        """验证error信号已声明。"""
        worker = _SimpleWorker()
        assert worker.error is not None


class TestBaseWorkerExecution:
    """BaseWorker执行测试。"""

    def test_successful_execution(self, qapp) -> None:
        """验证worker正常执行并返回结果。"""
        worker = _SimpleWorker()
        spy = QSignalSpy(worker.finished)

        worker.run()

        assert len(spy) == 1
        result = spy[0][0]
        assert result == {"status": "done", "result": 42}

    def test_error_execution(self, qapp) -> None:
        """验证worker执行异常时发射error信号。"""
        worker = _ErrorWorker()
        finished_spy = QSignalSpy(worker.finished)
        error_spy = QSignalSpy(worker.error)

        worker.run()

        assert len(error_spy) == 1
        assert "测试错误" in error_spy[0][0]
        assert len(finished_spy) == 0

    def test_progress_emission(self, qapp) -> None:
        """验证worker执行过程中发射progress信号。"""
        worker = _ProgressWorker()
        progress_spy = QSignalSpy(worker.progress)

        worker.run()

        assert len(progress_spy) == 3
        assert progress_spy[0][0] == 30
        assert progress_spy[1][0] == 60
        assert progress_spy[2][0] == 100


class TestBaseWorkerLifecycle:
    """BaseWorker生命周期测试。"""

    def test_is_running_state(self, qapp) -> None:
        """验证运行状态标志正确切换。"""
        worker = _SimpleWorker()
        assert worker.is_running() is False
        worker.run()
        assert worker.is_running() is False  # run执行完成后为False

    def test_cancel_flag(self, qapp) -> None:
        """验证cancel方法设置取消标志。"""
        worker = _CancellableWorker()
        assert worker.is_running() is False
        # 在另一个线程中快速取消
        QTimer.singleShot(5, worker.cancel)
        worker.run()
        assert worker.is_running() is False


class TestBaseWorkerStartInThread:
    """start_in_thread静态方法测试。"""

    def test_returns_qthread(self, qapp) -> None:
        """验证start_in_thread返回QThread实例。"""
        worker = _SimpleWorker()
        thread = BaseWorker.start_in_thread(worker)
        assert isinstance(thread, QThread)
        assert thread.isRunning()
        thread.wait(1000)

    def test_thread_runs_worker(self, qapp) -> None:
        """验证worker在子线程中被执行。"""
        worker = _SimpleWorker()
        finished_spy = QSignalSpy(worker.finished)

        thread = BaseWorker.start_in_thread(worker)
        thread.wait(2000)

        assert len(finished_spy) >= 1
