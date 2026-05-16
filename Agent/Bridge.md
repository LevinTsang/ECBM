---
name: Bridge
description: 本文件的作用是各Agent沟通的桥梁。各Agent对本文件都有读写权限。通过写入向其他Agent输出内容。通过读取获取其他Agent写入的内容执行本Agent相关的任务
---
# 模板
```Markdown
---
## 需求解析Agent 2026-05-16 11:37 本次操作概述
### Title 1...
* ... ...
* ... ...

### Title 2...
* ... ...
* ... ...

... ...

---

## 架构设计Agent 2026-05-16 11:41 本次操作概述
### Title 1...
* ... ...
* ... ...

### Title 2...
* ... ...
* ... ...

... ...

---
```

---

## 需求解析Agent 2026-05-16 23:32 项目空白框架初始架构需求解析

### 1. 核心目标
* 创建基于软件工程及计算机科学专业体系的项目空白框架，技术栈限定为 Python 3.14.4 + PyQt 6，框架本身不实现任何业务功能，仅提供分层清晰、模块解耦的项目骨架，使后续功能开发能精准插入到指定位置，保障项目架构长期整洁可维护。

### 2. 需求拆解
* 2.1 分层架构设计
	* 需建立符合软件工程经典分层模式的项目目录结构：表现层 / 业务逻辑层 / 数据访问层 / 基础设施层
	* 各层之间通过明确的接口或信号机制通信，禁止跨层直接调用
	* 每层内部按功能域进一步划分模块子包，遵循高内聚低耦合原则
* 2.2 项目启动与生命周期管理
	* 需定义统一的应用程序入口点 main.py，负责初始化 QApplication 实例
	* 需设计应用生命周期管理机制：启动初始化 -> 运行中状态管理 -> 优雅退出
	* 启动流程需支持：加载配置 -> 初始化日志 -> 初始化核心服务 -> 启动UI主窗口 -> 进入事件循环
* 2.3 配置管理框架
	* 需预留配置文件的加载、解析、热更新能力接口
	* 配置数据与代码严格分离，配置不得硬编码于业务逻辑中
	* 支持多层级配置覆盖：默认配置 -> 用户配置 -> 运行时配置
* 2.4 UI表现层骨架
	* 需基于 PyQt 6 的 QMainWindow / QWidget 体系建立主窗口框架
	* 需预留信号-槽通信机制的声明区域，供后续功能模块注册
	* 需预留自定义 QWidget 组件、QDialog 对话框、QSS 样式表的存放位置
* 2.5 多线程与异步任务基础设施
	* 需预留 QThread 子类工作线程的存放位置，用于将耗时操作从 UI 主线程分离
	* 需预留线程间信号通信的接口定义区域，保障 UI 线程安全
* 2.6 资源文件组织结构
	* 需为图标、图片、国际化翻译文件、QSS 样式文件等静态资源设定统一的存放路径规范
	* 资源通过 Qt 资源系统 QRC 或路径引用方式管理，需预留配置接口
* 2.7 日志与监控基础设施
	* 需基于 Python logging 模块建立统一日志框架，预留日志级别、输出目标、格式化的可配置接口
	* 日志输出需覆盖：应用程序运行日志、异常堆栈日志、用户操作审计日志
* 2.8 异常处理与容错框架
	* 需设计统一的异常处理策略：全局异常捕获 -> 日志记录 -> 用户友好提示
	* 需预留自定义异常类型的存放位置，覆盖业务异常、UI异常、IO异常等分类
* 2.9 测试框架结构
	* 需建立与源码目录同构的测试目录，覆盖单元测试、集成测试、UI自动化测试的存放位置
	* 需预留 pytest / unittest 的配置入口及公共 fixture 定义位置
* 2.10 数据持久化接口
	* 需预留数据模型 Model 的基类定义区域，定义通用 CRUD 接口
	* 需预留数据库连接管理、迁移脚本的存放位置，不限定具体数据库类型
* 2.11 扩展与插件机制
	* 需预留插件/扩展的接口定义区域，支持后续功能以插件形式动态加载
* 2.12 版本与构建管理
	* 需定义项目元信息（版本号、作者、许可证）的存放位置
	* 需预留依赖声明文件 requirements.txt / pyproject.toml 的位置
	* 需预留 .gitignore 规则文件，排除虚拟环境、编译产物、敏感配置

### 3. 技术映射
* 3.1 分层架构 -> Python Package 机制
	* Python 包（含 __init__.py 的目录）天然适合实现分层架构
	* 每层对应一个顶层包，内部子包对应各功能域
	* 层间通信通过 import 接口模块 + PyQt6 Signal 机制实现解耦
* 3.2 UI 表现层 -> PyQt6 核心模块
	* QApplication：应用程序实例管理、事件循环驱动
	* QMainWindow：主窗口框架，支持菜单栏、工具栏、状态栏、中央工作区
	* QWidget / QFrame：自定义组件基类
	* QDialog：模态/非模态对话框基类
	* Signal-Slot：pyqtSignal() 声明信号，@pyqtSlot 装饰绑定槽函数
	* QSS：样式表实现 UI 与样式分离
* 3.3 多线程 -> PyQt6 QThread + Python 线程安全
	* QThread：worker 线程基类，重写 run() 方法承载耗时逻辑
	* pyqtSignal + QObject.moveToThread() 实现工作线程与UI线程安全通信
	* 遵循 PyQt6 线程安全规则：UI 操作必须在主线程执行
* 3.4 配置管理 -> Python dataclass / configparser
	* dataclass 定义配置数据结构
	* JSON/YAML 文件持久化配置
	* 单例模式确保全局配置实例唯一
* 3.5 日志框架 -> Python logging 模块
	* logging.Logger 实例化应用日志记录器
	* logging.Handler 控制输出目标（控制台/文件/远程）
	* logging.Formatter 统一日志格式
* 3.6 异常处理 -> Python 异常体系
	* 自定义 Exception 子类构成异常树
	* 全局 sys.excepthook 捕获未处理异常
	* PyQt6 QApplication 信号绑定异常处理
* 3.7 测试框架 -> Python unittest + pytest
	* unittest.TestCase 编写单元测试
	* pytest fixtures 管理测试前置条件
	* pytest-qt 插件支持 PyQt6 UI 自动化测试
* 3.8 国际化 -> PyQt6 QTranslator + .ts/.qm 文件
	* QTranslator 加载翻译文件
	* pylupdate6 提取可翻译字符串
* 3.9 数据模型 -> Python ABC 抽象基类
	* abc.ABC + @abstractmethod 定义数据访问接口契约
	* 具体实现类在子模块中按需替换
* 3.10 构建与依赖 -> Python venv + pip + requirements.txt / pyproject.toml
	* 虚拟环境隔离项目依赖
	* 依赖声明使用 pip freeze 或 pyproject.toml

### 4. 逻辑指导
* 4.1 项目根目录结构设计
	* 架构设计Agent需首先定义项目根目录 D:\UserFiles\Project\ECBM\ECBMCode 下的一级目录清单
	* 一级目录按功能域划分，避免过度嵌套，建议不超过三层嵌套深度
	* 每个包目录必须包含 __init__.py 文件，即使为空，以明确标识其为 Python 包
* 4.2 分层优先级与依赖方向
	* 依赖方向严格遵循：表现层 -> 业务层 -> 数据层 -> 基础设施层
	* 上层可依赖下层，下层不得反向依赖上层
	* 同层内模块通过接口通信，减少直接耦合
	* 基础设施层（日志、配置、工具类）位于最底层，被所有上层共享
* 4.3 入口文件设计
	* main.py 作为唯一入口点，职责包括：
		1. 解析命令行参数（预留 argparse 接口）
		2. 加载应用配置
		3. 初始化日志系统
		4. 创建 QApplication 实例
		5. 实例化主窗口并显示
		6. 进入事件循环并返回退出码
	* 不得在 main.py 中编写业务逻辑
* 4.4 UI 层设计要点
	* 主窗口类与业务逻辑类分离，主窗口仅负责视图组装和事件分发
	* 所有自定义信号统一在类属性区域声明 pyqtSignal，便于后续开发者快速定位通信接口
	* 预留 QThread 子类的存放目录，线程类统一继承 QObject + 使用 moveToThread 模式
	* QSS 样式文件与 Python 代码分离，主窗口在初始化时统一加载
* 4.5 测试目录设计要点
	* 测试目录结构需与源码目录结构保持镜像对应关系
	* 示例：源码 core/models/user_model.py 对应测试 tests/test_core/test_models/test_user_model.py
	* conftest.py 文件放置在测试根目录，定义全局 fixture
* 4.6 扩展性考虑
	* 各层核心模块预留基类/抽象类定义，后续功能通过继承扩展
	* 插件目录预留于顶层，定义插件接口协议 ABC，后续插件按协议实现后放入即生效
* 4.7 文件命名规范
	* Python 模块文件使用 snake_case 命名
	* 包目录使用全小写单词
	* 类名使用 PascalCase，函数/方法使用 snake_case
	* 常量使用 UPPER_SNAKE_CASE
* 4.8 安全与健壮性考虑
	* 项目根目录放置 .gitignore，排除 __pycache__/、.venv/、*.pyc、.env
	* 敏感配置（密钥、密码等）通过环境变量注入，不写入配置文件
	* 全局异常钩子捕获所有未处理异常，避免应用崩溃

### 5. 参考关联
* 5.1 Python 官方文档参考
	* Gift/Document/Python3.14.4Doc.md 第6章（模块）和第9章（类）：指导 Python 包组织结构和类的设计
	* Gift/Document/Python3.14.4Doc.md 第8章（错误和异常）：指导自定义异常体系设计
	* Gift/Document/Python3.14.4Doc.md 第10章（标准库概览）：logging 模块、argparse 模块的使用参考
* 5.2 PyQt6 官方文档参考
	* Gift/Document/PyQt6Docs.md Introduction 章节：PyQt6 组件清单（QtWidgets、QtCore、QtGui 等）
	* Gift/Document/PyQt6Docs.md Signals and Slots 章节：信号-槽机制的定义、连接与断开
	* Gift/Document/PyQt6Docs.md Qt Designer 章节：pyuic6 工具使用、UI 与代码分离方案
	* Gift/Document/PyQt6Docs.md i18n 章节：国际化和 pylupdate6 的使用
* 5.3 优秀开源项目参考
	* Gift/ReferenceProject/BiliNote：参考其 backend/frontend 分离的分层结构设计模式
	* Gift/ReferenceProject/BiliNote：参考其 config 配置管理、日志、异常处理的基础设施组织方式
	* Gift/ReferenceProject/markitdown：参考其核心逻辑与工具函数分离的模块化组织方式
* 5.4 计算机科学理论依据
	* 分层架构（Layered Architecture）：软件工程的经典架构模式，将系统按功能职责垂直分层
	* 关注点分离（Separation of Concerns）：UI、业务逻辑、数据访问各自独立
	* 依赖倒置原则（Dependency Inversion）：高层模块依赖抽象接口，不依赖具体实现
	* 单一职责原则（Single Responsibility）：每个模块/类仅负责一个功能域
	* 开闭原则（Open-Closed）：框架对扩展开放、对修改封闭，通过继承和接口实现

### 6. 风险提示
* 6.1 模糊点识别
	* 用户未明确指定项目的具体业务领域（如：音视频处理、文档管理、数据分析等），当前解析基于通用软件工程最佳实践，架构设计Agent可在此基础上根据后续具体功能需求进行微调
	* 用户未指定数据库类型，当前方案仅预留数据访问层的抽象接口，不预设具体 ORM 框架
* 6.2 技术栈边界约束
	* Python 3.14.4 是极新版本，需确认目标环境中 PyQt6 v6.11 对该 Python 版本的兼容性；建议架构设计Agent在设计阶段注明依赖版本环境
	* PyQt6 有 GPL v3 和商业许可证双授权，若项目涉及商业分发，需评估许可合规性
* 6.3 架构扩展风险
	* 空白框架需平衡"当前够用"和"未来扩展"的关系，避免过度设计导致目录结构复杂但空置率高
	* 建议架构设计Agent遵循"最小可行架构"原则：每个目录/模块在创建时明确其职责，避免创建不确定用途的空目录
* 6.4 跨平台兼容性
	* 当前作业环境为 Windows 11，若项目未来需跨平台（Linux/macOS），需注意文件路径使用 pathlib.Path 处理、避免 Windows 专有 API、UI 控件尺寸适配不同分辨率

---

## 架构设计Agent 2026-05-17 00:25 项目空白框架初始架构设计

### 整体架构设计
* 分层架构：
	* 系统采用四层经典分层架构，自顶向下依次为：表现层（app_ui）-> 业务逻辑层（app_core）-> 数据访问层（app_data）-> 基础设施层（app_infra），各层通过接口模块与PyQt6信号机制进行解耦通信
	* 表现层（app_ui）：负责所有PyQt6视图组件的声明与组织，包括主窗口、自定义控件、对话框、样式表，仅处理UI渲染和用户交互事件分发，不包含业务逻辑
	* 业务逻辑层（app_core）：负责应用核心服务、控制器、工作线程，处理业务流程编排和数据转换，通过抽象接口调用数据访问层
	* 数据访问层（app_data）：负责数据模型的抽象定义、数据持久化操作和数据库连接管理，提供Repository模式接口
	* 基础设施层（app_infra）：负责配置管理、日志系统、异常体系、通用工具函数，被所有上层模块共享依赖
	* 插件层（app_plugins）：位于顶层侧，独立于四层架构，定义插件接口协议，支持后续功能以插件形式动态注册
	* 依赖方向严格遵循：app_ui -> app_core -> app_data -> app_infra，下层不得反向依赖上层
* 核心模块列表：
	1. main.py：应用程序唯一入口点，负责初始化QApplication、加载配置、初始化日志、显示主窗口、进入事件循环
	2. app_infra：基础设施层包，包含config（配置管理）、logging（日志框架）、exceptions（异常体系）、utils（工具函数）四个子模块
	3. app_data：数据访问层包，包含models（数据模型基类）、repositories（仓储接口）、database（数据库连接管理）三个子模块
	4. app_core：业务逻辑层包，包含services（服务抽象基类）、controllers（控制器基类）、threads（工作线程基类）三个子模块
	5. app_ui：表现层包，包含main_window（主窗口）、widgets（自定义控件目录）、dialogs（对话框目录）、signals（共享信号声明）、styles（QSS样式目录）五个子模块
	6. app_plugins：插件扩展层包，包含base_plugin（插件接口ABC定义）
	7. resources：静态资源根目录，包含icons、images、i18n、styles四个子目录
	8. tests：测试根目录，与源码目录结构镜像对应，包含单元测试、集成测试、UI测试子目录
* 模块交互关系：
	* main.py 启动时依次调用 app_infra.config（加载配置）-> app_infra.logging（初始化日志）-> app_core.services（初始化核心服务）-> app_ui.main_window（显示主窗口）
	* 主窗口通过 app_ui.signals 中定义的共享pyqtSignal与 app_core.controllers 进行通信
	* app_core.controllers 调用 app_core.services 执行业务逻辑
	* app_core.services 通过 app_data.repositories 进行数据持久化操作
	* app_core.threads 中的工作线程通过pyqtSignal向主线程传递进度和结果
	* 所有层均可直接调用 app_infra 中的配置、日志、异常和工具函数
* 接口规范：
	* 跨层通信接口采用Python抽象基类（abc.ABC）定义，具体实现在各层子模块中按需提供
	* 层间数据传递格式：基本数据类型（str/int/float/bool）、dataclass实例、dict、list，禁止传递PyQt6组件引用跨越app_core边界
	* UI层与业务层之间使用pyqtSignal传递数据，信号参数类型遵循PyQt6类型映射规范
	* 插件接口通过app_plugins/base_plugin.py中的PluginBase抽象类定义，包含activate/deactivate/get_info三个抽象方法
* 项目根目录结构（D:\UserFiles\Project\ECBM\ECBMCode\）：
```text
main.py
pyproject.toml
requirements.txt
.gitignore
README.md
app_infra/
	__init__.py
	config/
		__init__.py
		config_manager.py
	logging/
		__init__.py
		log_manager.py
	exceptions/
		__init__.py
		base_exceptions.py
	utils/
		__init__.py
		path_utils.py
app_data/
	__init__.py
	models/
		__init__.py
		base_model.py
	repositories/
		__init__.py
		base_repository.py
	database/
		__init__.py
		connection_manager.py
		migrations/
			__init__.py
app_core/
	__init__.py
	services/
		__init__.py
		base_service.py
	controllers/
		__init__.py
		base_controller.py
	threads/
		__init__.py
		base_worker.py
app_ui/
	__init__.py
	main_window.py
	signals.py
	widgets/
		__init__.py
	dialogs/
		__init__.py
	styles/
		__init__.py
		base.qss
app_plugins/
	__init__.py
	base_plugin.py
resources/
	icons/
	i18n/
	images/
	styles/
tests/
	__init__.py
	conftest.py
	test_app_infra/
		__init__.py
		test_config/
			__init__.py
			test_config_manager.py
		test_logging/
			__init__.py
			test_log_manager.py
		test_exceptions/
			__init__.py
			test_base_exceptions.py
	test_app_data/
		__init__.py
		test_models/
			__init__.py
			test_base_model.py
		test_repositories/
			__init__.py
			test_base_repository.py
	test_app_core/
		__init__.py
		test_services/
			__init__.py
		test_controllers/
			__init__.py
		test_threads/
			__init__.py
			test_base_worker.py
	test_app_ui/
		__init__.py
		test_main_window.py
```

### 模块详细设计
#### 1. app_infra（基础设施层）
* 类结构：
	- ConfigManager（app_infra/config/config_manager.py）：全局配置管理单例类
		* 属性：_instance（ConfigManager | None）：单例私有实例，_default_config（dict）：默认配置字典，_user_config（dict）：用户配置文件配置字典，_runtime_config（dict）：运行时覆盖配置字典
		* 方法：get_instance()（@staticmethod）-> ConfigManager：返回单例实例，load_config(config_path: str | Path) -> None：加载用户配置文件（JSON格式支持），get(key: str, default: Any = None) -> Any：按三层优先级（运行时>用户>默认）获取配置值，set_runtime(key: str, value: Any) -> None：设置运行时配置覆盖值，reload(config_path: str | Path) -> None：热更新配置文件，_merge_defaults() -> None：私有方法，合并默认配置
	- LogManager（app_infra/logging/log_manager.py）：统一日志管理类
		* 属性：_logger（logging.Logger）：根日志记录器实例，_handlers（list[logging.Handler]）：已注册的处理器列表
		* 方法：setup(app_name: str, log_level: str, log_dir: str | Path, enable_console: bool, enable_file: bool) -> None：初始化日志系统配置，get_logger(name: str = None) -> logging.Logger：获取具名日志记录器，add_handler(handler: logging.Handler, level: str) -> None：动态添加处理器，set_level(level: str) -> None：动态调整日志级别
	- ECBMException（app_infra/exceptions/base_exceptions.py）：应用根异常类
		* 属性：message（str）：错误描述信息，error_code（str）：错误码
		* 方法：__init__(self, message: str, error_code: str = "ECBM_000") -> None
	- BusinessException（app_infra/exceptions/base_exceptions.py）：业务异常，继承ECBMException
	- UIException（app_infra/exceptions/base_exceptions.py）：UI异常，继承ECBMException
	- DataException（app_infra/exceptions/base_exceptions.py）：数据访问异常，继承ECBMException
	- ConfigException（app_infra/exceptions/base_exceptions.py）：配置异常，继承ECBMException
	- path_utils（app_infra/utils/path_utils.py）：路径工具函数模块
		* 函数：get_project_root() -> Path：返回项目根目录绝对路径，get_resource_path(relative_path: str) -> Path：返回静态资源绝对路径，ensure_dir(dir_path: str | Path) -> Path：确保目录存在不存在则创建
* 输入输出：
	- 输入：ConfigManager接收配置文件路径（str | Path），LogManager接收应用名/日志级别/日志目录等配置参数
	- 输出：ConfigManager返回配置值（Any），LogManager返回logging.Logger实例，path_utils返回pathlib.Path对象
* 依赖关系：app_infra为最底层，不依赖项目内其他层，仅依赖Python标准库（logging、json、pathlib、abc、dataclasses）

#### 2. app_data（数据访问层）
* 类结构：
	- BaseModel（app_data/models/base_model.py）：数据模型抽象基类
		* 属性：_id（str）：模型唯一标识符，_created_at（float）：创建时间戳，_updated_at（float）：更新时间戳
		* 方法：to_dict() -> dict：将模型序列化为字典，from_dict(data: dict)（@classmethod）-> BaseModel：从字典反序列化创建实例，validate() -> bool：数据校验方法（抽象，待子类实现）
	- BaseRepository（app_data/repositories/base_repository.py）：数据仓储接口抽象基类，使用abc.ABC + @abstractmethod
		* 方法：create(entity: BaseModel) -> BaseModel（@abstractmethod）：创建记录，read(entity_id: str) -> BaseModel | None（@abstractmethod）：读取单条记录，update(entity: BaseModel) -> BaseModel（@abstractmethod）：更新记录，delete(entity_id: str) -> bool（@abstractmethod）：删除记录，list_all() -> list[BaseModel]（@abstractmethod）：列出所有记录
	- ConnectionManager（app_data/database/connection_manager.py）：数据库连接管理类
		* 属性：_connection（Any | None）：数据库连接对象，_config（dict）：连接配置参数
		* 方法：initialize(db_type: str, connection_params: dict) -> None：初始化数据库连接，get_connection() -> Any：获取当前连接对象，close() -> None：关闭数据库连接，is_connected() -> bool：检查连接状态
* 输入输出：
	- 输入：BaseRepository接收BaseModel实例或entity_id字符串，ConnectionManager接收数据库类型和连接参数
	- 输出：BaseRepository返回BaseModel实例或实例列表，ConnectionManager返回数据库连接对象
* 依赖关系：依赖app_infra（exceptions、config），不依赖app_core和app_ui

#### 3. app_core（业务逻辑层）
* 类结构：
	- BaseService（app_core/services/base_service.py）：业务服务抽象基类
		* 属性：_repository（BaseRepository | None）：关联的数据仓储实例，_logger（logging.Logger）：服务日志记录器
		* 方法：initialize() -> None：服务初始化钩子（待子类重写），dispose() -> None：服务销毁钩子（待子类重写）
	- BaseController（app_core/controllers/base_controller.py）：控制器基类，继承PyQt6的QObject
		* 属性：_services（dict[str, BaseService]）：注册的服务映射字典
		* 方法：register_service(name: str, service: BaseService) -> None：注册业务服务，get_service(name: str) -> BaseService：获取已注册服务，initialize() -> None：初始化所有服务，dispose() -> None：销毁所有服务
	- BaseWorker（app_core/threads/base_worker.py）：工作线程基类，继承QObject（使用moveToThread模式）
		* 属性：_is_running（bool）：线程运行状态标志，_logger（logging.Logger）：线程日志记录器
		* 信号：progress（pyqtSignal(int)）：进度更新信号（0-100），finished（pyqtSignal(object)）：任务完成信号，携带结果数据，error（pyqtSignal(str)）：错误发生信号，携带错误消息
		* 方法：run() -> None：线程执行入口（待子类重写），cancel() -> None：请求取消任务，is_running() -> bool：查询运行状态
* 输入输出：
	- 输入：BaseController接收服务名称和实例，BaseWorker的run方法接收通过子类构造函数传入的具体任务参数
	- 输出：BaseWorker通过finished信号携带任务结果，通过progress信号报告进度，通过error信号报告错误
* 依赖关系：依赖app_data（BaseRepository、BaseModel）、app_infra（日志、异常），不依赖app_ui

#### 4. app_ui（表现层）
* 类结构：
	- MainWindow（app_ui/main_window.py）：应用主窗口，继承PyQt6的QMainWindow
		* 属性：_controller（BaseController | None）：关联的业务控制器，_menu_bar（QMenuBar）：菜单栏对象，_tool_bar（QToolBar）：工具栏对象，_status_bar（QStatusBar）：状态栏对象，_central_widget（QStackedWidget）：中央工作区控件
		* 方法：setup_ui() -> None：初始化UI布局和组件，setup_menu_bar() -> None：构建菜单栏，setup_tool_bar() -> None：构建工具栏，setup_status_bar() -> None：构建状态栏，set_controller(controller: BaseController) -> None：注入业务控制器，load_qss(file_name: str) -> None：加载QSS样式表文件，show_message(title: str, message: str, msg_type: str) -> None：显示消息对话框（info/warning/error），closeEvent(event: QCloseEvent) -> None：重写关闭事件，触发优雅退出流程
	- SharedSignals（app_ui/signals.py）：共享信号声明类，继承QObject
		* 信号：app_started（pyqtSignal()）：应用启动完成信号，app_quitting（pyqtSignal()）：应用即将退出信号，config_changed（pyqtSignal(str, object)）：配置变更信号（key, new_value），language_changed（pyqtSignal(str)）：语言切换信号（locale_name）
* 输入输出：
	- 输入：MainWindow接收通过set_controller注入的BaseController实例
	- 输出：通过SharedSignals向其他模块广播全局事件，通过用户操作触发controller中的业务方法
* 依赖关系：依赖app_core（BaseController）、app_infra（ConfigManager），不得依赖app_data直接访问数据

#### 5. app_plugins（插件扩展层）
* 类结构：
	- PluginBase（app_plugins/base_plugin.py）：插件接口抽象基类，使用abc.ABC
		* 方法：activate() -> bool（@abstractmethod）：激活插件，成功返回True，deactivate() -> bool（@abstractmethod）：停用插件，成功返回True，get_info() -> dict（@abstractmethod）：返回插件元信息（name、version、author、description）
* 输入输出：
	- 输入：activate/deactivate不接收参数，通过插件内部持有的ConfigManager或服务引用获取上下文
	- 输出：activate/deactivate返回bool，get_info返回dict（包含插件meta信息）
* 依赖关系：独立于四层架构，可依赖app_infra但不依赖app_core/app_ui/app_data

### 功能实现流程
#### 1. 应用启动流程
* 实现步骤：
	1. main.py入口，调用argparse解析命令行参数（预留--config、--log-level、--debug参数）
	2. 调用ConfigManager.get_instance().load_config()加载默认配置和用户配置文件
	3. 调用LogManager.setup()初始化日志系统（从配置中读取日志级别、输出目标和格式设置）
	4. 实例化QApplication对象，设置应用元信息（applicationName、organizationName、applicationVersion等），连接QApplication的lastWindowClosed信号到退出处理
	5. 注册全局异常钩子：调用sys.excepthook设置为自定义的全局异常处理函数（记录异常日志后弹出QMessageBox友好提示），并重写QApplication的notify方法用于捕获PyQt6事件循环中的未处理异常
	6. 初始化BaseController及其注册的Services，调用controller.initialize()
	7. 实例化MainWindow，调用main_window.setup_ui()构建界面，调用main_window.set_controller(controller)注入控制器
	8. 加载全局QSS样式表：main_window.load_qss("base.qss")
	9. 调用main_window.show()显示主窗口
	10. 调用sys.exit(app.exec())进入Qt事件循环，等待用户操作
* 数据流转：命令行参数 -> ConfigManager（配置加载）-> LogManager（日志初始化）-> QApplication（事件循环启动）-> BaseController（服务初始化）-> MainWindow（UI渲染）-> 事件循环运行
* 异常处理：
	- 配置文件解析失败：捕获json.JSONDecodeError，记录错误日志，使用默认配置继续启动，弹出非阻塞式警告对话框
	- 日志目录创建失败：捕获PermissionError，回退到仅控制台输出模式，记录警告信息
	- 主窗口初始化失败：捕获所有Exception，记录错误日志，弹出QMessageBox.critical对话框后退出应用（返回退出码1）

#### 2. 应用优雅退出流程
* 实现步骤：
	1. 用户点击主窗口关闭按钮或选择菜单"文件->退出"，触发MainWindow.closeEvent()
	2. closeEvent中发送SharedSignals.app_quitting信号，通知各模块准备退出
	3. 检查app_core.threads中是否有正在运行的工作线程，若有则调用worker.cancel()并等待线程安全退出（最多等待5秒超时）
	4. 调用controller.dispose()销毁所有已注册服务（依次调用每个BaseService的dispose()方法）
	5. 调用ConnectionManager.close()关闭数据库连接
	6. 调用ConfigManager保存运行时配置变更（如有需要持久化的运行时配置）
	7. 记录应用退出日志
	8. 接受QCloseEvent，窗口关闭
* 数据流转：用户关闭操作 -> MainWindow.closeEvent() -> SharedSignals.app_quitting信号 -> 各模块退出处理 -> QApplication退出 -> 进程结束
* 异常处理：
	- 线程超时未退出：记录警告日志，强制终止线程（调用QThread.terminate()），提示用户下次启动时检查数据完整性
	- 数据库连接关闭失败：记录错误日志，忽略异常继续退出流程（关闭为best-effort操作）

#### 3. 配置文件热更新流程
* 实现步骤：
	1. 外部触发（用户操作或文件系统监控）调用ConfigManager.reload(config_path)
	2. reload方法重新读取JSON配置文件，解析为新配置字典
	3. 将新配置与现有默认配置合并（默认配置不可变，用户配置更新）
	4. 运行时配置覆盖项保持不变（优先级最高）
	5. 更新ConfigManager._user_config为新读取的配置
	6. 广播SharedSignals.config_changed（key, new_value）信号，通知各关注模块
	7. 各模块根据自身需要监听config_changed信号并做出响应
* 数据流转：配置文件变更 -> ConfigManager.reload() -> 配置合并 -> _user_config更新 -> config_changed信号 -> 各模块响应
* 异常处理：
	- 配置文件不存在：抛出ConfigException，保留现有配置不变，记录错误日志
	- 配置文件格式错误：捕获json.JSONDecodeError，保留现有配置不变，记录错误日志并弹出用户提示

#### 4. 工作线程执行流程
* 实现步骤：
	1. 业务层创建具体Worker实例（继承BaseWorker），设置任务参数
	2. 创建QThread实例，调用worker.moveToThread(thread)将worker移至新线程
	3. 连接thread.started信号到worker.run()槽函数，连接worker.finished到thread.quit，连接worker.error到错误处理槽
	4. 连接worker.progress信号到UI层进度更新槽（线程安全的跨线程通信）
	5. 调用thread.start()启动工作线程
	6. worker.run()中执行耗时操作，周期性发射progress信号（当前进度百分比），完成后发射finished信号（携带结果数据）
	7. UI层在主线程接收progress信号更新进度条/状态文字
	8. 任务完成，finished信号触发，UI层接收结果并展示，thread自动退出
	9. 主线程调用thread.wait()等待线程完全结束，然后清理资源
* 数据流转：业务参数 -> Worker.run() -> progress/finished/error信号（跨线程）-> UI层槽函数（主线程）-> 界面更新
* 异常处理：
	- run()中捕获所有Exception，通过error信号发送错误消息到主线程
	- 主线程收到error信号后弹出错误提示对话框，记录错误日志
	- 线程执行超时：由调用方设置QTimer超时检测，超时后调用worker.cancel()和thread.quit()

#### 5. 插件加载流程
* 实现步骤：
	1. 扫描app_plugins目录下所有符合PluginBase接口的模块
	2. 使用importlib动态导入每个插件模块
	3. 反射查找实现了PluginBase的子类
	4. 实例化插件对象，调用get_info()获取插件元信息
	5. 调用plugin.activate()激活插件
	6. 将激活的插件实例注册到全局插件注册表（dict）
* 数据流转：文件系统扫描 -> importlib导入 -> 类反射查找 -> PluginBase实例化 -> activate() -> 插件注册表
* 异常处理：
	- 插件导入失败：捕获ImportError，记录错误日志，跳过该插件继续加载其余插件
	- 插件activate失败：捕获异常，记录错误日志，标记该插件为加载失败状态

### UI界面设计方案
* 整体布局：
	* 主窗口（QMainWindow）采用经典桌面应用布局：顶部菜单栏（QMenuBar）、可停靠工具栏（QToolBar）、中央工作区（QStackedWidget，预留多页面切换）、底部状态栏（QStatusBar）
	* 中央工作区默认显示空白欢迎页面（QLabel居中显示应用名称和版本信息），后续业务功能通过QStackedWidget切换页面
	* 窗口默认尺寸：1024x768像素，最小尺寸：800x600像素，启动时居中屏幕显示
* 组件列表：
	1. main_window（QMainWindow）：
		* 父组件：无（顶级窗口）
		* 关键属性：windowTitle="ECBM Application"，objectName="MainWindow"，minimumWidth=800，minimumHeight=600
		* 信号与槽：closeEvent -> 优雅退出流程处理
	2. menu_bar（QMenuBar）：
		* 父组件：main_window
		* 关键属性：objectName="MenuBar"
		* 预留菜单项：文件菜单（QMenu "file_menu"）含退出动作（QAction "action_quit"），帮助菜单（QMenu "help_menu"）含关于动作（QAction "action_about"）
		* 信号与槽：action_quit.triggered -> main_window.close，action_about.triggered -> main_window.show_about_dialog
	3. tool_bar（QToolBar）：
		* 父组件：main_window
		* 关键属性：movable=True，objectName="ToolBar"
		* 预留工具栏按钮区域，当前为空，后续功能按需添加QAction
	4. status_bar（QStatusBar）：
		* 父组件：main_window
		* 关键属性：objectName="StatusBar"
		* 信号与槽：MainWindow.setup_status_bar()中初始化，通过showMessage()显示临时消息
	5. central_widget（QStackedWidget）：
		* 父组件：main_window
		* 关键属性：objectName="CentralStack"
		* 默认页面索引0为欢迎页（QWidget "welcome_page"），内含居中QLabel显示应用名称和版本
	6. welcome_label（QLabel）：
		* 父组件：welcome_page
		* 关键属性：text="ECBM Application v0.1.0"，alignment=Qt.AlignmentFlag.AlignCenter
* 交互逻辑：
	* 用户点击菜单"文件->退出"或关闭窗口 -> QAction.triggered信号 -> MainWindow.close()槽 -> closeEvent()优雅退出流程
	* 用户点击菜单"帮助->关于" -> QAction.triggered信号 -> MainWindow.show_about_dialog()槽 -> QMessageBox.about显示应用信息
	* 状态栏默认显示"就绪"文本，长时间操作时通过worker.progress信号更新为进度信息

### 关键技术实现要点
#### 1. ConfigManager单例模式实现
* 实现思路：使用__new__方法控制实例化，确保全局仅有一个ConfigManager实例，结合线程锁（threading.Lock）保证多线程环境下的实例唯一性
* 关键代码片段：

```python
import threading
from pathlib import Path
from typing import Any

class ConfigManager:
	_instance: "ConfigManager | None" = None
	_lock: threading.Lock = threading.Lock()

	def __new__(cls) -> "ConfigManager":
		if cls._instance is None:
			with cls._lock:
				if cls._instance is None:
					cls._instance = super().__new__(cls)
		return cls._instance

	def __init__(self) -> None:
		if not hasattr(self, "_initialized"):
			self._default_config: dict[str, Any] = {}
			self._user_config: dict[str, Any] = {}
			self._runtime_config: dict[str, Any] = {}
			self._initialized: bool = True
```

* 注意事项：双重检查锁（DCL）模式在实际并发场景下的可靠性依赖Python GIL特性，若未来引入真正多线程场景，应使用threading.RLock替代；__init__中使用hasattr标记防止重复初始化

#### 2. 全局异常捕获钩子
* 实现思路：通过sys.excepthook替换Python默认异常处理，在PyQt6的QApplication.notify()层捕获事件循环中的异常，两者配合确保所有异常均被拦截
* 关键代码片段：

```python
import sys
import traceback
from logging import Logger
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtCore import QObject, QEvent

def setup_global_exception_handler(logger: Logger) -> None:
	def _handler(exc_type, exc_value, exc_tb) -> None:
		if issubclass(exc_type, KeyboardInterrupt):
			sys.__excepthook__(exc_type, exc_value, exc_tb)
			return
		trace_str = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
		logger.critical(f"Unhandled exception:\n{trace_str}")
		QMessageBox.critical(None, "Error", f"异常:\n{exc_value}")
	sys.excepthook = _handler
```

* 注意事项：KeyboardInterrupt应保留系统默认处理以确保Ctrl+C能正常终止应用；QMessageBox.critical可能在QApplication未完全初始化时被调用导致递归异常，需在notify中增加异常保护

#### 3. QThread安全通信模式（moveToThread）
* 实现思路：摒弃继承QThread重写run的模式，采用QObject子类 + moveToThread的标准模式，通过pyqtSignal实现跨线程安全通信
* 关键代码片段：

```python
from PyQt6.QtCore import QObject, QThread, pyqtSignal

class BaseWorker(QObject):
	progress = pyqtSignal(int)
	finished = pyqtSignal(object)
	error = pyqtSignal(str)

	def run(self) -> None:
		try:
			result = self._execute_task()
			self.finished.emit(result)
		except Exception as e:
			self.error.emit(str(e))

	def _execute_task(self) -> object:
		raise NotImplementedError

def start_worker_in_thread(worker: BaseWorker) -> QThread:
	thread = QThread()
	worker.moveToThread(thread)
	thread.started.connect(worker.run)
	worker.finished.connect(thread.quit)
	worker.error.connect(thread.quit)
	thread.finished.connect(thread.deleteLater)
	thread.finished.connect(worker.deleteLater)
	thread.start()
	return thread
```

* 注意事项：moveToThread后对象的槽函数在目标线程执行，信号连接的槽函数在接收者线程执行，确保UI更新槽在主线程；thread和worker需在finished信号中调用deleteLater防止内存泄漏

#### 4. 配置热更新实现要点
* 实现思路：ConfigManager持有配置文件的路径引用，reload方法重新读取JSON文件并与默认配置合并，通过SharedSignals.config_changed信号通知变更
* 注意事项：热更新时应做新旧配置对比（dict diff），仅对真正变更的key发送信号，避免不必要的模块响应；运行时配置覆盖项在reload后保持不变，需显式调用remove_runtime才能清除运行时覆盖
* 潜在问题：线程安全问题——reload过程中若有其他线程正在调用get()读取配置，可能出现短暂的配置不一致，解决方案是使用copy-on-write模式或读写锁保护

#### 5. 日志系统设计要点
* 实现思路：LogManager封装Python logging模块的配置逻辑，支持同时输出到控制台和文件，日志格式为"[时间][级别][模块名] 消息内容"，文件日志按日期轮转（使用logging.handlers.TimedRotatingFileHandler）
* 注意事项：日志文件目录需在首次写入前自动创建；日志文件编码需显式设置为UTF-8；多进程场景下需使用QueueHandler避免文件竞争（当前框架预留该扩展点）

### 测试方案设计
* 单元测试要点：
	- ConfigManager单例创建测试：验证多次get_instance()返回同一实例，测试三层配置优先级覆盖逻辑
	- LogManager日志初始化测试：验证setup()正确创建Logger和Handler，验证不同日志级别过滤行为
	- BaseModel序列化测试：验证to_dict()和from_dict()的往返一致性
	- BaseRepository接口契约测试：验证未实现子类实例化方法时抛出TypeError（抽象方法约束）
	- path_utils函数测试：验证get_project_root()返回正确的根目录路径，验证ensure_dir()创建不存在的目录
	- 异常体系测试：验证自定义异常类的继承关系和属性传递
* 集成测试要点：
	- 启动流程集成测试：模拟完整启动流程（配置加载->日志初始化->QApplication创建->MainWindow显示），验证各步骤无异常抛出
	- 退出流程集成测试：模拟各服务的dispose调用顺序，验证资源释放完整性
	- 工作线程通信集成测试：创建模拟Worker，验证progress/finished/error信号正确跨线程传递到主线程槽函数
	- 异常全局捕获集成测试：在业务层抛出未处理异常，验证sys.excepthook正确捕获并弹出QMessageBox
* 性能测试指标：
	- 应用冷启动时间（从main.py执行到MainWindow.show完成）目标 < 2秒
	- 配置文件加载时间目标 < 100ms（1MB以内JSON文件）
	- 工作线程创建和启动开销目标 < 50ms
* 测试数据准备：
	- 测试用配置文件（test_config.json）：合法JSON格式的完整配置数据
	- 测试用配置文件（test_config_invalid.json）：格式错误的JSON文件用于异常路径测试
	- 测试用临时目录：用于日志文件写入、文件创建等IO操作测试

### 参考关联
* [官方技术文档]：Gift/Document/Python3.14.4Doc.md 第6章（模块）、第8章（错误和异常）、第9章（类）、第10章（标准库概览：logging、argparse）
* [官方技术文档]：Gift/Document/PyQt6Docs.md Introduction章节（PyQt6组件清单）、Signals and Slots章节（pyqtSignal/pyqtSlot）、Qt Designer章节（UI与代码分离）、i18n章节（国际化翻译）
* [优秀开源项目]：Gift/ReferenceProject/BiliNote 的.gitignore配置、.env.example环境变量管理方式、分层架构组织思路
* [优秀开源项目]：Gift/ReferenceProject/markitdown 的pyproject.toml配置结构、src/包管理模式、plugin-sample插件接口设计模式
* [工具]：Gift/Tools/GetTime.bat 时间获取工具

### 注意事项
* 依赖版本：Python 3.14.4需确认PyQt6 v6.11及以上版本的wheel兼容性，建议在pyproject.toml中使用"PyQt6>=6.11,<7.0"范围约束
* 编码规范：所有Python文件编码声明为UTF-8，文件首行添加编码注释"# -*- coding: utf-8 -*-"，遵循snake_case文件名、PascalCase类名、snake_case函数/方法名的命名约定
* 线程安全关键点：UI控件操作必须在主线程执行，工作线程通过pyqtSignal自动跨线程传递数据到主线程槽函数，严禁在工作线程的run方法中直接操作UI对象
* QSS加载顺序：在main_window.show()之前完成QSS加载，避免窗口先显示后样式突变导致的视觉闪烁
* 跨平台路径处理：所有文件系统路径操作统一使用pathlib.Path而非os.path或字符串拼接，避免Windows/Linux路径分隔符差异
* 验证标准：main.py能正常启动并显示空白主窗口；配置文件修改后reload能读取最新值；工作线程发射的进度信号在主线程槽中正确接收；未处理异常被全局钩子捕获并弹出提示框；各包目录存在且__init__.py完好
* 潜在Bug风险：QApplication.notify()的重写中若抛出异常将导致无限递归（捕获异常的代码本身又抛出异常），必须在notify中增加try-except保护并确保保护代码不会再次失败
* 性能优化建议：大型配置文件采用懒加载策略（仅在实际读取某key时才解析对应节点）；日志文件使用异步写入（logging.handlers.QueueHandler + QueueListener模式），避免IO阻塞主线程运行
---
