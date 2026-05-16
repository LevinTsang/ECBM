# ECBM Application

基于 Python 3.14.4 + PyQt 6 的通用桌面应用框架。

## 技术栈

- **语言**: Python 3.14.4
- **UI框架**: PyQt 6 (>=6.11, <7.0)
- **测试框架**: pytest + pytest-qt

## 项目架构

项目采用经典四层分层架构：

- **app_ui** — 表现层：PyQt6视图组件、主窗口、自定义控件、QSS样式
- **app_core** — 业务逻辑层：核心服务、控制器、工作线程
- **app_data** — 数据访问层：数据模型基类、仓储接口、数据库连接
- **app_infra** — 基础设施层：配置管理、日志、异常体系、工具函数
- **app_plugins** — 插件扩展层：插件接口协议定义

依赖方向：app_ui → app_core → app_data → app_infra（下层不得反向依赖上层）

## 快速开始

### 创建虚拟环境

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

### 安装依赖

```bash
pip install -r requirements.txt
```

### 启动应用

```bash
python main.py
```

### 命令行参数

| 参数 | 说明 |
|------|------|
| `--config PATH` | 指定用户配置文件路径（JSON格式） |
| `--log-level LEVEL` | 日志级别：DEBUG/INFO/WARNING/ERROR/CRITICAL |
| `--debug` | 启用调试模式 |

### 运行测试

```bash
pytest
```

## 项目结构

```text
main.py                  # 应用入口
app_infra/               # 基础设施层
app_data/                # 数据访问层
app_core/                # 业务逻辑层
app_ui/                  # 表现层
app_plugins/             # 插件扩展层
resources/               # 静态资源
tests/                   # 测试代码
```

## 许可证

GPL-3.0-only
