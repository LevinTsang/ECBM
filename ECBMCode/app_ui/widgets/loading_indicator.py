# -*- coding: utf-8 -*-
"""加载指示器自定义组件模块。

LoadingIndicator继承QWidget，使用QPainter绘制旋转圆弧动画。
通过QTimer驱动帧更新，QElapsedTimer修正帧率波动，
确保旋转速度恒定。
"""

from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import (
    Qt, QTimer, QElapsedTimer, QPointF, QRectF,
)
from PyQt6.QtGui import (
    QPainter, QColor, QPen, QConicalGradient, QBrush,
    QPaintEvent, QShowEvent, QHideEvent,
)
import math


class LoadingIndicator(QWidget):
    """加载指示器自定义组件。

    使用QPainter绘制约270度跨度的旋转圆弧，
    QConicalGradient实现从透明到主色的渐变效果。

    属性:
        _angle: 当前旋转角度（弧度）。
        _timer: 驱动动画的QTimer。
        _color: 圆弧颜色。
        _arc_width: 圆弧线宽。
        _size_hint: 组件尺寸。
        _fps: 目标帧率，默认30。
        _elapsed_timer: 实际时间计时器，用于修正帧率波动。
        _was_running: 隐藏前是否处于运行状态，用于showEvent恢复。
        _gradient: QConicalGradient渐变对象缓存。
    """

    def __init__(
        self,
        parent: QWidget | None = None,
        size: int = 32,
        color: str = "#6C8EBF",
    ) -> None:
        """初始化加载指示器。

        参数:
            parent: 父组件。
            size: 组件宽高（像素），默认32。
            color: 圆弧颜色（hex字符串），默认"#6C8EBF"。
        """
        super().__init__(parent)
        self._angle: float = 0.0
        self._color: QColor = QColor(color)
        self._arc_width: int = max(2, size // 8)
        self._size_hint: int = size
        self._fps: int = 30
        self._was_running: bool = False

        self._timer: QTimer = QTimer(self)
        self._timer.timeout.connect(self._on_tick)
        self._elapsed_timer: QElapsedTimer = QElapsedTimer()

        self._gradient: QConicalGradient = self._build_gradient()

        self.setFixedSize(size, size)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.hide()

    def _build_gradient(self) -> QConicalGradient:
        """构建圆锥渐变对象。

        从透明到主色的渐变效果，用于圆弧绘制。

        返回:
            QConicalGradient: 配置好的渐变对象。
        """
        grad = QConicalGradient()
        grad.setCenter(QPointF(0.5, 0.5))
        grad.setAngle(0.0)

        transparent = QColor(self._color)
        transparent.setAlpha(0)
        grad.setColorAt(0.0, transparent)
        grad.setColorAt(0.3, self._color)
        grad.setColorAt(0.7, self._color)
        grad.setColorAt(1.0, transparent)

        return grad

    def start(self) -> None:
        """启动旋转动画。

        重置QElapsedTimer并启动QTimer开始帧循环。
        若组件不可见则先显示。
        """
        if not self.isVisible():
            self.show()
        self._elapsed_timer.start()
        interval = max(1, 1000 // self._fps)
        self._timer.start(interval)
        self._was_running = True

    def stop(self) -> None:
        """停止旋转动画。

        停止QTimer并记录停止状态。
        """
        self._timer.stop()
        self._was_running = False

    def is_running(self) -> bool:
        """查询动画是否正在运行。

        返回:
            bool: True表示动画运行中。
        """
        return self._timer.isActive()

    def set_color(self, color: str) -> None:
        """动态设置圆弧颜色。

        参数:
            color: 颜色hex字符串。
        """
        self._color = QColor(color)
        self._gradient = self._build_gradient()

    def set_size(self, size: int) -> None:
        """动态设置组件尺寸。

        参数:
            size: 像素尺寸。
        """
        self._size_hint = size
        self._arc_width = max(2, size // 8)
        self.setFixedSize(size, size)

    def _on_tick(self) -> None:
        """定时器回调。

        基于QElapsedTimer实际经过时间更新旋转角度，
        避免帧率波动导致旋转速度不均匀。
        """
        elapsed_sec = self._elapsed_timer.elapsed() / 1000.0
        # 旋转速度：每秒0.8圈（2*pi*0.8弧度/秒）
        self._angle = elapsed_sec * 2.0 * math.pi * 0.8
        self.update()

    def paintEvent(self, event: QPaintEvent) -> None:
        """绘制旋转圆弧。

        使用QPainter绘制约270度跨度的圆弧，
        起始角度由_angle决定实现旋转效果。

        参数:
            event: 绘制事件对象。
        """
        if not self.isVisible():
            return

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # 计算绘制区域（留边距为线宽一半）
        margin = self._arc_width / 2.0
        draw_rect = QRectF(
            margin, margin,
            self.width() - 2 * margin,
            self.height() - 2 * margin,
        )

        # 设置画笔
        pen = QPen()
        pen.setWidth(self._arc_width)
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        pen.setBrush(QBrush(self._gradient))
        painter.setPen(pen)

        # 绘制圆弧（270度跨度，即3/4圆）
        start_angle = int(math.degrees(self._angle)) * 16
        span_angle = int(270 * 16)  # QPainter使用1/16度单位

        painter.drawArc(draw_rect, start_angle, span_angle)
        painter.end()

    def sizeHint(self):
        """返回建议尺寸。"""
        from PyQt6.QtCore import QSize
        return QSize(self._size_hint, self._size_hint)

    def showEvent(self, event: QShowEvent) -> None:
        """组件显示事件。

        若隐藏前为运行状态则自动恢复动画。

        参数:
            event: 显示事件对象。
        """
        super().showEvent(event)
        if self._was_running and not self._timer.isActive():
            self.start()

    def hideEvent(self, event: QHideEvent) -> None:
        """组件隐藏事件。

        停止QTimer避免隐藏后空转消耗CPU，
        但保留_was_running状态以支持showEvent恢复。

        参数:
            event: 隐藏事件对象。
        """
        super().hideEvent(event)
        if self._timer.isActive():
            self._timer.stop()
