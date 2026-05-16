# -*- coding: utf-8 -*-
"""动画工具函数模块。

封装QPropertyAnimation常用动画模式为模块级静态函数，
供VerticalToolBar和各面板组件直接调用。
支持减少动效模式（通过ConfigManager读取reduce_motion配置）。
"""

from typing import Callable

from PyQt6.QtWidgets import (
    QWidget, QPushButton, QGraphicsOpacityEffect,
)
from PyQt6.QtCore import (
    QPropertyAnimation, QEasingCurve, QByteArray,
)
from PyQt6.QtGui import QColor


def is_reduced_motion() -> bool:
    """检测是否启用减少动效模式。

    从ConfigManager读取reduce_motion配置项，
    若为True则所有动画时长设为0直接跳至终态。

    返回:
        bool: True表示减少动效模式开启。
    """
    try:
        from app_infra.config.config_manager import ConfigManager
        return ConfigManager.get_instance().get("reduce_motion", False)
    except Exception:
        return False


def _get_duration(duration: int) -> int:
    """根据减运动模式获取实际动画时长。

    参数:
        duration: 请求的动画时长（毫秒）。

    返回:
        int: 实际动画时长，减运动模式下为0。
    """
    return 0 if is_reduced_motion() else duration


def _ensure_opacity_effect(widget: QWidget) -> QGraphicsOpacityEffect:
    """确保目标组件拥有透明度效果对象。

    参数:
        widget: 目标组件。

    返回:
        QGraphicsOpacityEffect: 已附加的透明度效果对象。
    """
    effect = widget.graphicsEffect()
    if effect is None or not isinstance(effect, QGraphicsOpacityEffect):
        effect = QGraphicsOpacityEffect(widget)
        widget.setGraphicsEffect(effect)
    return effect


def fade_in(
    widget: QWidget,
    duration: int = 250,
    easing: QEasingCurve.Type = QEasingCurve.Type.OutCubic,
    callback: Callable | None = None,
) -> QPropertyAnimation:
    """淡入动画。

    将组件透明度从0动画过渡到1。

    参数:
        widget: 目标组件。
        duration: 动画时长（毫秒），默认250。
        easing: 缓动曲线类型，默认OutCubic。
        callback: 动画完成回调函数。

    返回:
        QPropertyAnimation: 动画实例。
    """
    actual_dur = _get_duration(duration)
    effect = _ensure_opacity_effect(widget)
    effect.setOpacity(0.0)
    widget.show()

    anim = QPropertyAnimation(effect, QByteArray(b"opacity"), widget)
    anim.setDuration(actual_dur)
    anim.setStartValue(0.0)
    anim.setEndValue(1.0)
    anim.setEasingCurve(easing)

    if callback is not None:
        anim.finished.connect(callback)

    anim.start()
    return anim


def fade_out(
    widget: QWidget,
    duration: int = 250,
    easing: QEasingCurve.Type = QEasingCurve.Type.OutCubic,
    callback: Callable | None = None,
) -> QPropertyAnimation:
    """淡出动画。

    将组件透明度从1动画过渡到0，完成后隐藏组件。

    参数:
        widget: 目标组件。
        duration: 动画时长（毫秒），默认250。
        easing: 缓动曲线类型，默认OutCubic。
        callback: 动画完成回调函数。

    返回:
        QPropertyAnimation: 动画实例。
    """
    actual_dur = _get_duration(duration)
    effect = _ensure_opacity_effect(widget)
    effect.setOpacity(1.0)

    anim = QPropertyAnimation(effect, QByteArray(b"opacity"), widget)
    anim.setDuration(actual_dur)
    anim.setStartValue(1.0)
    anim.setEndValue(0.0)
    anim.setEasingCurve(easing)

    def _on_finished() -> None:
        widget.hide()
        if callback is not None:
            callback()

    anim.finished.connect(_on_finished)
    anim.start()
    return anim


def scale_icon(
    button: QPushButton,
    target_size: int,
    duration: int = 200,
) -> QPropertyAnimation:
    """图标缩放动画。

    动画化按钮的iconSize属性实现缩放效果。

    参数:
        button: 目标按钮。
        target_size: 目标图标尺寸（像素）。
        duration: 动画时长（毫秒），默认200。

    返回:
        QPropertyAnimation: 动画实例。
    """
    actual_dur = _get_duration(duration)
    current_size = button.iconSize()

    anim = QPropertyAnimation(button, QByteArray(b"iconSize"), button)
    anim.setDuration(actual_dur)
    anim.setStartValue(current_size)
    anim.setEndValue(current_size)
    # QPropertyAnimation对iconSize需要实际使用setStartValue/setEndValue
    # 此处使用QSize对象
    from PyQt6.QtCore import QSize
    anim.setStartValue(QSize(current_size.width(), current_size.height()))
    anim.setEndValue(QSize(target_size, target_size))
    anim.setEasingCurve(QEasingCurve.Type.OutCubic)
    anim.start()
    return anim


def flash_button(
    button: QPushButton,
    flash_color: str,
    duration: int = 150,
) -> None:
    """按钮点击反馈闪烁效果。

    短暂改变按钮背景色后恢复，提供即时点击反馈。

    参数:
        button: 目标按钮。
        flash_color: 闪烁颜色（hex字符串，如"#6C8EBF"）。
        duration: 闪烁持续时长（毫秒），默认150。
    """
    actual_dur = _get_duration(duration)
    original_style = button.styleSheet()

    # 构建闪烁样式
    flash_style = (
        f"{original_style}"
        f"QPushButton {{ background-color: {flash_color}; }}"
    )
    button.setStyleSheet(flash_style)

    # 使用QPropertyAnimation无法直接动画化styleSheet，
    # 改用QTimer延迟恢复
    from PyQt6.QtCore import QTimer
    QTimer.singleShot(actual_dur, lambda: button.setStyleSheet(original_style))


def cross_fade(
    old_widget: QWidget,
    new_widget: QWidget,
    duration: int = 250,
) -> tuple[QPropertyAnimation, QPropertyAnimation]:
    """交叉淡入淡出切换。

    旧组件淡出同时新组件淡入，实现平滑视觉切换。

    参数:
        old_widget: 当前显示的组件。
        new_widget: 需要切换到的组件。
        duration: 动画时长（毫秒），默认250。

    返回:
        tuple[QPropertyAnimation, QPropertyAnimation]: (淡出动画, 淡入动画)。
    """
    actual_dur = _get_duration(duration)

    fade_out_anim = fade_out(old_widget, duration=actual_dur)
    fade_in_anim = fade_in(new_widget, duration=actual_dur)

    return (fade_out_anim, fade_in_anim)
