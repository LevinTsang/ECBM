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

## 需求解析Agent 2026-05-17 01:17 ECBM软件UI界面设计需求解析

### 1. 核心目标
* 为ECBM软件（任意文件/链接转Markdown格式工具）设计一个具备科技感、简约风格的三栏式主界面，包含VSCode风格的最左侧竖向工具列表栏，支持暗色/亮色双主题随系统或手动切换，界面中所有组件尺寸和字体大小均为基于显示器分辨率的动态变量，避免UI重叠、遮挡、显示不全等问题。

### 2. 需求拆解
* 2.1 窗口尺寸动态计算
	* 首次启动时获取当前显示器分辨率
	* 主窗口宽度 = round(屏幕宽度 x 0.618)
	* 主窗口高度 = round(主窗口宽度 x 0.618)
	* 窗口默认居中显示于屏幕
	* 窗口尺寸不是固定值，支持用户手动缩放
	* 最小窗口尺寸限制确保界面不崩溃（建议最小宽度800，最小高度500）
* 2.2 三栏式布局（3:4:3比例）
	* 三栏从左侧工具栏右侧开始，分为左栏（内容源区）、中栏（编辑/预览区）、右栏（输出/结果区）
	* 三栏宽度比为 3:4:3（总和10份）
	* 三栏之间支持拖动调整宽度（使用QSplitter实现）
	* 各栏内部组件的长宽和字体大小均为变量，随窗口尺寸按比例缩放
* 2.3 左侧竖向工具列表栏（VSCode Activity Bar风格）
	* 位于主窗口最左侧，固定窄宽度（约48-56px，按屏幕比例计算）
	* 竖向排列的图标按钮列表（工具项）
	* 每个按钮代表一个功能模块（如：文件浏览器、URL输入、转换任务列表、设置等）
	* 选中状态高亮标记（颜色区分、左侧竖条指示器）
	* 鼠标悬浮时显示工具提示（QToolTip）
	* 当前选中工具项与右侧三栏联动切换对应面板
* 2.4 暗色系/亮色系双主题
	* 默认使用暗色系主题
	* 支持跟随系统主题自动切换（监听系统主题变化）
	* 支持用户手动切换（界面内提供切换入口，可置于左侧工具栏底部或设置面板中）
	* 组件与背景、字体与背景之间存在足够对比度差异，确保显示清晰
	* 暗色主题：深色背景（#1E1E2E或类似色系）、浅色文字、组件略亮于背景
	* 亮色主题：浅色背景（#F5F5F5或类似色系）、深色文字、组件略暗于背景
	* 颜色方案参考unified-ui项目的oklch色彩空间设计理念，使用语义化颜色变量
* 2.5 科技感动效
	* 左侧工具栏图标hover时微动效（如轻微缩放、颜色渐变过渡）
	* 工具栏选中项切换时平滑过渡动画
	* 三栏面板切换时淡入过渡
	* 按钮点击反馈动效（如短暂的颜色闪烁）
	* 加载状态指示动画（如旋转指示器、骨架屏）
	* 所有动效时长控制在200-400ms之间，使用缓动曲线，不僵硬
	* 支持prefers-reduced-motion偏好（参考webtui和unified-ui的减运动策略）
* 2.6 界面风格
	* 整体具备科技感但简约，不过度装饰
	* 采用扁平化设计风格，轻微圆角（4-8px）
	* 使用细线条分隔（1px），透明度控制层次
	* 图标风格统一（推荐使用SVG矢量图标或Unicode符号）
	* 字体：优先使用系统等宽或无衬线字体（如Consolas、Segoe UI、Microsoft YaHei）

### 3. 技术映射
* 3.1 窗口动态尺寸 -> QScreen + QMainWindow
	* 使用 QApplication.primaryScreen() 获取QScreen对象
	* QScreen.availableGeometry() 或 QScreen.size() 获取屏幕分辨率
	* 计算公式：window_width = round(screen_width x 0.618), window_height = round(window_width x 0.618)
	* QMainWindow.resize(window_width, window_height) 设置初始尺寸
	* QMainWindow.setMinimumSize() 设置最小尺寸约束
	* 首次运行时将计算结果持久化到ConfigManager中，后续启动使用已保存的尺寸（除非用户重置）
* 3.2 三栏布局 -> QSplitter + 自定义QWidget面板
	* 使用 QSplitter(Qt.Orientation.Horizontal) 作为三栏容器
	* QSplitter.setSizes([3 x base, 4 x base, 3 x base]) 初始化比例
	* QSplitter.setStretchFactor() 确保缩放时按比例调整
	* QSplitter.setHandleWidth(2-4px) 设置拖动把手宽度
	* 自定义QSplitterHandle样式（QSS），hover时高亮
	* 每个面板为独立的QWidget子类，内部使用QVBoxLayout/QHBoxLayout管理子组件
	* 所有子组件的尺寸通过布局百分比或stretch factor控制，不设固定像素值
* 3.3 左侧工具栏 -> 自定义VerticalToolBar（QWidget）
	* 继承QWidget实现VSCode风格的竖向工具列表
	* 固定宽度约48-56px（按屏幕宽度的3%-5%计算）
	* 内部布局：QVBoxLayout，顶部为工具按钮组（QPushButton + icon），中间弹性空间，底部为主题切换和设置按钮
	* 工具按钮：setCheckable(True) + 互斥QButtonGroup实现单选
	* 选中状态通过QSS伪状态选择器(QPushButton:checked)实现高亮
	* 左侧竖条指示器通过QPushButton的左边框或自定义paintEvent绘制
	* 按钮hover动效：QPropertyAnimation控制iconSize或样式属性
	* 可配合QStackedWidget或QToolBox实现工具面板切换
* 3.4 暗色/亮色主题 -> QPalette + QSS + 主题管理器
	* 创建ThemeManager单例类，管理当前主题状态（dark/light/system）
	* 主题切换通过setStyleSheet()全局应用对应的QSS文件
	* 暗色主题QSS：定义全局颜色变量（--bg-primary, --bg-secondary, --text-primary等）
	* 亮色主题QSS：同样的变量名映射到亮色值
	* 系统主题跟随：监听QApplication.styleHints().colorSchemeChanged信号，当系统主题变化时自动切换
	* QPalette作为QSS回退方案，设置窗口级别的调色板
	* 颜色对比度确保可读性（深色背景与浅色文字、浅色背景与深色文字之间保持足够差异）
* 3.5 动效实现 -> QPropertyAnimation + QGraphicsOpacityEffect + QVariantAnimation
	* 工具栏图标hover：QPropertyAnimation缩放iconSize（如48->56）
	* 面板切换：QGraphicsOpacityEffect + QPropertyAnimation opacity淡入（0->1, 250ms）
	* 按钮点击反馈：短暂修改背景色后恢复，使用QTimer控制恢复时机
	* 加载指示器：自定义QWidget使用QPainter绘制旋转圆弧，QTimer驱动角度增量
	* 所有动画统一使用QEasingCurve.Type.OutCubic缓动曲线
	* 通过ConfigManager读取是否启用减少动效
* 3.6 变量化尺寸系统 -> SizeManager工具类
	* 创建SizeManager工具类，根据窗口当前尺寸动态计算所有组件尺寸
	* 基础计算公式：base_unit = min(window_width, window_height) / 参考值
	* 字体大小：title_font_size = base_unit x 系数，body_font_size = base_unit x 系数
	* 组件间距：margin = base_unit x 系数，padding = base_unit x 系数
	* 图标尺寸：icon_size = base_unit x 系数
	* 窗口resizeEvent中触发重新计算，更新所有组件
	* 每个自定义组件实现update_sizes()方法，接收SizeManager计算的尺寸字典

### 4. 逻辑指导
* 4.1 UI层文件组织结构
	* app_ui包下新增以下模块：
		1. vertical_tool_bar.py：左侧竖向工具列表栏组件
		2. splitter_panels.py：三栏分割面板容器组件
		3. left_panel.py：左栏（内容源区）面板组件
		4. center_panel.py：中栏（编辑/预览区）面板组件
		5. right_panel.py：右栏（输出/结果区）面板组件
		6. theme_manager.py：主题管理器（暗色/亮色切换）
		7. size_manager.py：动态尺寸计算管理器
		8. animation_utils.py：动画工具函数集合
		9. loading_indicator.py：加载指示器动画组件
		10. styles/dark_theme.qss：暗色主题样式表
		11. styles/light_theme.qss：亮色主题样式表
	* 架构设计Agent需在app_ui/widgets/下创建上述新模块文件
* 4.2 主窗口重构优先级
	* 第一优先级：修改MainWindow.setup_ui()，将原有的中央工作区QStackedWidget替换为[垂直工具栏 + QSplitter三栏布局]的整体布局结构
	* 第二优先级：实现SizeManager和ThemeManager基础框架，确保主窗口启动时能正确计算尺寸和加载主题
	* 第三优先级：实现左侧VerticalToolBar，完成基本按钮布局和面板切换逻辑
	* 第四优先级：实现三栏面板的基础框架（各栏内部先放置占位QLabel）
	* 第五优先级：实现主题切换和动画动效
	* 第六优先级：实现加载指示器等辅助UI组件
* 4.3 主窗口布局结构设计
	* MainWindow.setup_ui()中构建以下布局层次：
		1. 创建一个QWidget作为centralWidget
		2. 该centralWidget使用QHBoxLayout，间距为0
		3. 布局从左到右依次添加：VerticalToolBar（固定宽度）、QSplitter（三栏容器）
		4. QSplitter中添加left_panel、center_panel、right_panel
		5. 菜单栏和状态栏保留原有实现
		6. 移除原有的QToolBar（或将其整合到左侧工具栏中）
	* 所有布局margin和spacing设为0，由各面板内部控制边距
* 4.4 尺寸变量系统设计
	* SizeManager类设计关键点：
		1. 接收参考窗口尺寸（width, height）
		2. 定义基础比例常数表（如：工具栏宽度比例0.04、标题字体比例0.025、正文字体比例0.018等）
		3. 提供calculate_all()方法返回尺寸字典，包含所有组件的宽高、字体大小、间距、图标尺寸
		4. 尺寸字典格式建议：{"toolbar_width": 52, "panel_font_size": 14, "title_font_size": 18, "icon_size": 24, "margin": 8, "padding": 12, "border_radius": 6, ...}
		5. 窗口resize时重新计算，通过信号通知各面板更新
	* 比例常数参考值（基于1920x1080屏幕，窗口约1186x733）：
		* 左侧工具栏宽度：窗口宽度的 0.04
		* 标题字体大小：窗口高度的 0.022
		* 正文字体大小：窗口高度的 0.018
		* 小字体大小：窗口高度的 0.014
		* 图标尺寸：窗口高度的 0.028
		* 通用边距：窗口宽度的 0.008
		* 通用内边距：窗口宽度的 0.012
		* 圆角半径：窗口高度的 0.008
* 4.5 主题切换实现逻辑
	* ThemeManager类设计关键点：
		1. 单例模式，管理theme_mode属性（"dark" | "light" | "system"）
		2. 提供toggle_theme()、set_theme(mode)、get_effective_theme()方法
		3. get_effective_theme()：若mode为system则查询系统主题，返回实际dark或light
		4. 主题切换时发射theme_changed(str)信号
		5. 提供load_qss(theme_name)方法，读取对应QSS文件内容
		6. 在MainWindow中连接theme_changed信号到全局样式更新槽
	* 主题持久化：当前用户选择的主题模式存储到ConfigManager中
	* 系统主题监听：连接QApplication.styleHints().colorSchemeChanged信号
	* QSS样式表编写要求：
		1. 使用语义化objectName选择器（如#LeftPanel、#CenterPanel、#ToolButton）
		2. 暗色和亮色分别定义颜色变量（通过QSS注释约定或Python变量替换）
		3. 区分不同交互状态的样式（normal、hover、pressed、checked、disabled）
		4. 确保滚动条（QScrollBar）样式与整体主题协调
* 4.6 动画实现指导
	* 工具栏项目hover动画：
		1. 使用QEvent.Enter/QEvent.Leave事件或QSS:hover + transition（PyQt6中QSS transition支持有限）
		2. 建议方案：在自定义ToolButton中重写enterEvent/leaveEvent，使用QPropertyAnimation动画化图标尺寸或背景透明度
		3. 动画时长200ms，缓动曲线OutCubic
	* 面板切换动画：
		1. 使用QGraphicsOpacityEffect设置面板opacity
		2. QPropertyAnimation驱动opacity从0到1
		3. 动画时长250ms
		4. 淡入完成后移除opacity effect以恢复渲染性能
	* 加载指示器：
		1. 自定义QWidget子类，重写paintEvent
		2. 使用QPainter绘制圆弧（QPainter.drawArc）
		3. QTimer每30ms触发一次角度更新（约33fps）
		4. 圆弧颜色使用主题色，两端带渐变透明度
	* 按钮点击反馈：
		1. 在mousePressEvent中临时修改样式
		2. QTimer.singleShot(150ms)后恢复
		3. 或使用QSS的pressed伪状态（瞬时自动恢复）
	* 减运动支持：
		1. ThemeManager或ConfigManager中读取"reduce_motion"配置
		2. 当reduce_motion为True时，所有动画时长设为0或直接跳转到最终状态
		3. 系统级别的prefers-reduced-motion通过QStyleHints检测
* 4.7 三栏面板内容规划（预留接口，暂不实现业务）
	* 左栏（内容源区）：
		* 提供文件拖放区域（QWidget + dragEnterEvent/dropEvent）
		* 提供URL输入栏（QLineEdit + 提交按钮）
		* 提供历史记录列表（QListWidget）
		* 预留信号：source_selected(str) -- 发射文件路径或URL
	* 中栏（编辑/预览区）：
		* 提供QTabWidget切换Markdown源码编辑和渲染预览
		* 编辑模式：QPlainTextEdit，支持语法高亮预留
		* 预览模式：QTextBrowser，渲染Markdown为HTML显示
		* 预留信号：content_changed(str) -- 发射当前Markdown内容
	* 右栏（输出/结果区）：
		* 提供输出文件路径配置（QLineEdit + 浏览按钮）
		* 提供导出格式选项（QComboBox）
		* 提供转换进度条和状态显示
		* 提供"开始转换"按钮（QPushButton）
		* 预留信号：convert_requested(dict) -- 发射转换参数

### 5. 参考关联
* 5.1 unified-ui项目（Gift/ReferenceProject/unified-ui/）
	* 参考其三栏CSS Grid布局设计思路（src/components/layout/notebook/client.tsx），转化为PyQt6的QSplitter + QHBoxLayout实现
	* 参考其Sidebar系统设计（packages/unified-ui/src/components/sidebar.tsx），特别是折叠为图标的模式和provider上下文管理，转化为左侧工具栏的按钮组管理模式
	* 参考其ResizablePanelGroup（packages/unified-ui/src/components/resizable.tsx）的可拖拽分隔设计，对应QSplitter的handle定制
	* 参考其暗色/亮色主题CSS变量架构（packages/unified-ui/styles.css），转化为QSS的语义化objectName选择器体系
	* 参考其Framer Motion动效预设（packages/unified-ui/src/motion/presets.ts），将fadeIn、scaleIn、slideIn等动效映射为QPropertyAnimation实现
	* 参考其减运动策略（useReducedMotion hook），在PyQt6中通过配置开关和QStyleHints实现
	* 参考其主题customizer模式（packages/unified-ui/src/theme/customizer-store.tsx），设计主题管理器的持久化和运行时切换机制
	* 参考其WCAG对比度校验工具（packages/unified-ui/src/utils/contrast.ts），在QSS颜色选择时确保可读性
* 5.2 webtui项目（Gift/ReferenceProject/webtui/）
	* 参考其CSS @layer分层样式架构（packages/css/src/full.css），应用于QSS文件的组织结构设计（基础变量层、组件样式层、动画层）
	* 参考其属性驱动的样式模式（如[is-="button"]、[variant-="primary"]），在QSS中使用objectName和property选择器
	* 参考其ch/lh单位动态尺寸系统，适配为PyQt6中基于窗口尺寸的比例计算系统
	* 参考其纯CSS动画实现（spinner.css的step动画、tooltip.css的延迟过渡），映射为PyQt6的QTimer驱动动画
	* 参考其绝对定位滚动容器模式，在三栏面板内部实现内容区域的自适应高度
* 5.3 markitdown项目（Gift/ReferenceProject/markitdown/）
	* 参考其插件系统设计（entry_points + register_converters），预留UI插件区域（如左侧工具栏可动态注册新工具按钮）
	* 参考其Converter优先级机制，在UI中设计面板的按需加载策略
	* 参考其CLI参数设计，在UI中设计对应的配置选项（如--keep-data-uris等转换为高级设置面板选项）
* 5.4 PyQt6官方文档（Gift/Document/PyQt6Docs.md）
	* QScreen类：获取屏幕尺寸和分辨率
	* QSplitter类：可拖拽分割面板容器
	* QPropertyAnimation类：属性动画引擎
	* QGraphicsOpacityEffect类：透明度效果
	* Signals and Slots章节：跨组件信号通信
	* QSS样式表：Qt样式表选择器语法
	* QStyleHints.colorSchemeChanged：系统主题变化信号
* 5.5 Python 3.14.4官方文档（Gift/Document/Python3.14.4Doc.md）
	* pathlib.Path：跨平台文件路径处理
	* logging模块：日志记录
	* dataclass：配置数据结构定义
* 5.6 现有项目架构（ECBMCode/）
	* 保留当前的MainWindow类框架，在其基础上重构setup_ui()方法
	* 保留SharedSignals单例，新增theme_changed、size_changed等全局信号
	* 保留ConfigManager，新增主题、尺寸相关的配置项
	* 保留分层架构不变，新UI组件放置在app_ui包内
	* 保留main.py的启动流程，调整MainWindow初始化逻辑

### 6. 风险提示
* 6.1 技术边界约束
	* PyQt6的QSS不支持CSS变量（var(--xxx)）语法，主题切换需通过替换整个QSS字符串或使用Python变量替换方案实现，建议架构设计Agent在ThemeManager中维护颜色字典，动态生成QSS内容
	* PyQt6的QSS不支持transition和animation属性，所有动效必须通过QPropertyAnimation和QTimer实现，开发量较CSS方案大，关注点需集中在关键交互的动效而非全面动画覆盖
	* QSplitter的默认handle样式定制受限，需要子类化QSplitterHandle并重写paintEvent实现自定义外观
* 6.2 需求模糊点
	* 用户未明确左侧工具栏具体包含哪些工具项，当前仅给出"类似VSCode资源管理器按钮"的描述，建议架构设计Agent初期设计通用的工具注册机制，工具项通过配置列表驱动，后续可灵活增减
	* 用户提及"动效"但未指定哪些元素需要动效、动效的具体程度，建议优先实现核心交互（工具栏切换、面板切换、加载状态）的动效，后期按需扩展
	* "科技感"视觉风格主观性强，建议架构设计Agent以unified-ui的暗色主题色板为基础做变体，确保审美基准一致
* 6.3 设计冲突识别
	* 需求同时要求"窗口尺寸为非固定值"和"所有组件尺寸为变量"，这两个概念在本质上一致但表述不同，实际实现为：窗口初始尺寸基于屏幕分辨率计算，用户可自由缩放窗口，组件尺寸通过比例计算跟随窗口变化。架构设计Agent需注意区分"初始尺寸计算"和"运行时响应式缩放"这两个阶段
	* 左侧工具栏"类似VSCode"暗示包含图标+面板切换+选中状态指示，但同时要求"简约"，需要平衡功能完整性和视觉简洁度，建议初期实现4-6个核心工具按钮，避免过度密集
* 6.4 性能风险
	* 窗口resize事件中频繁重新计算所有组件尺寸可能导致性能问题，建议在SizeManager中使用防抖机制（throttle，如100ms内只执行最后一次计算），避免resize事件密集触发时过度重绘
	* QGraphicsOpacityEffect在部分平台上存在渲染性能下降问题，面板切换动画完成后应立即通过setGraphicsEffect(None)移除效果
	* 加载指示器的QTimer驱动绘制需控制帧率（不超过30fps），避免不必要的CPU占用
* 6.5 跨分辨率适配风险
	* 用户在2K/4K高DPI屏幕上使用时，0.618倍的窗口计算可能导致窗口过大，建议设置窗口最大尺寸上限（如不超过屏幕可用区域的90%）
	* 低分辨率屏幕（如1366x768笔记本）上，0.618 x 1366 = 约844宽，0.618 x 844 = 约521高，三栏中最小栏宽约844 x 0.3 = 约253px，仍可接受。但若屏幕更小（如1280x720），建议设定最小栏宽阈值（如200px），低于阈值时自动折叠左栏或右栏
* 6.6 架构兼容性
	* 当前项目已有空白框架代码（ECBMCode/），新UI设计需在现有MainWindow类基础上重构setup_ui()方法，不得改动分层架构的依赖关系和接口定义
	* 原有菜单栏、状态栏的实现可保留，但工具栏（QToolBar）需移除或整合到左侧VerticalToolBar中
	* ConfigManager中的window_width/window_height配置项需配合新的动态尺寸计算逻辑：首次启动使用屏幕分辨率计算，后续启动使用已保存的用户调整后尺寸
---

## 架构设计Agent 2026-05-17 01:50 ECBM软件UI界面设计架构方案

### 整体架构设计
* 分层架构：
	* 本次UI界面设计在现有四层架构基础上进行扩展，所有新增模块归属表现层（app_ui），仅新增一个基础设施层工具类（app_infra/utils/size_utils.py）支持尺寸计算
	* 表现层（app_ui）新增子模块：vertical_tool_bar（左侧竖向工具栏）、splitter_panels（三栏分割面板容器）、left_panel（左栏内容源区）、center_panel（中栏编辑/预览区）、right_panel（右栏输出/结果区）、theme_manager（主题管理器）、size_manager（动态尺寸管理器）、animation_utils（动画工具函数）、loading_indicator（加载指示器组件）
	* 基础设施层（app_infra）新增：utils/size_utils.py（尺寸计算底层工具函数，供app_ui层调用）
	* 依赖方向不变：app_ui -> app_core -> app_data -> app_infra，新增模块遵循现有依赖约束
* 核心模块列表：
	1. VerticalToolBar（app_ui/widgets/vertical_tool_bar.py）：VSCode Activity Bar风格的左侧竖向工具列表栏，QWidget子类，管理工具按钮注册和面板切换
	2. SplitterPanels（app_ui/widgets/splitter_panels.py）：三栏QSplitter容器组件，管理左中右三栏的比例分配和拖拽交互
	3. LeftPanel（app_ui/widgets/left_panel.py）：左栏内容源区面板，提供文件拖放、URL输入、历史记录列表
	4. CenterPanel（app_ui/widgets/center_panel.py）：中栏编辑/预览区面板，QTabWidget切换编辑模式和预览模式
	5. RightPanel（app_ui/widgets/right_panel.py）：右栏输出/结果区面板，提供输出路径配置、格式选项、转换控制
	6. ThemeManager（app_ui/theme_manager.py）：主题管理器单例，管理暗色/亮色主题切换、系统主题跟随、QSS动态加载
	7. SizeManager（app_ui/size_manager.py）：动态尺寸计算管理器，基于窗口尺寸计算所有组件的比例尺寸
	8. AnimationUtils（app_ui/animation_utils.py）：动画工具函数集合，封装QPropertyAnimation常用动画模式
	9. LoadingIndicator（app_ui/widgets/loading_indicator.py）：加载指示器自定义QWidget，QPainter绘制旋转圆弧动画
	10. SharedSignals扩展（app_ui/signals.py）：在现有信号声明类中新增UI相关的全局信号
	11. MainWindow重构（app_ui/main_window.py）：在现有MainWindow类基础上重构setup_ui方法，整合新布局结构
	12. size_utils（app_infra/utils/size_utils.py）：底层尺寸计算工具函数，提供纯数学计算不依赖PyQt6
* 模块交互关系：
	* MainWindow.setup_ui()初始化时依次创建SizeManager（注入当前窗口尺寸）-> ThemeManager（加载主题）-> VerticalToolBar -> SplitterPanels -> 三栏面板组件
	* VerticalToolBar中的工具按钮点击信号连接到MainWindow的面板切换槽函数，使用信号映射机制切换右侧三栏中对应面板的内容显示
	* ThemeManager发射theme_changed信号 -> MainWindow接收后调用load_qss重新加载QSS文件 -> 各面板组件通过update_theme方法更新自身样式
	* SizeManager在主窗口resizeEvent中触发重算 -> 发射size_changed信号 -> 各面板组件的update_sizes方法接收新尺寸字典并调整子组件尺寸
	* 三栏面板间通过SharedSignals传递数据（如左栏source_selected -> 中栏加载内容 -> 右栏准备输出配置）
	* LoadingIndicator由各面板按需创建和显示，通过自身的start/stop方法控制动画运行
	* AnimationUtils为独立工具模块，被VerticalToolBar和各面板组件直接调用静态方法
	* 对话框组件（QMessageBox等）通过MainWindow的show_message方法统一管理，确保主题一致性
* 接口规范：
	* ThemeManager接口：set_theme(mode: str) -> None（mode: "dark"|"light"|"system"），get_effective_theme() -> str（返回实际主题名），load_qss(theme_name: str) -> str（返回QSS内容字符串）
	* SizeManager接口：calculate_sizes(w: int, h: int) -> dict[str, int]（输入窗口宽高，返回所有组件尺寸字典），recalculate() -> None（触发重算并发射信号）
	* 面板接口：各面板类实现update_sizes(sizes: dict) -> None和update_theme(theme: str) -> None两个统一方法，供MainWindow统一批量调用
	* 工具栏接口：register_tool(tool_id: str, icon: str, label: str, callback: Callable) -> None（注册工具按钮），switch_to_tool(tool_id: str) -> None（切换到指定工具对应的面板显示）
	* 数据传递格式：面板间通信使用Python基本类型（str、dict、list），pyqtSignal参数类型明确声明

### 模块详细设计
#### 1. SizeManager（app_ui/size_manager.py）
* 类结构：
	- SizeManager（QObject子类）：
		* 属性：_window_width（int）：当前窗口宽度，_window_height（int）：当前窗口高度，_base_unit（float）：基础计算单位 = min(w, h) / 733，_ratio_table（dict[str, float]）：比例常数映射表，_throttle_timer（QTimer | None）：防抖定时器，_pending_size（tuple[int, int] | None）：待处理的尺寸
		* 信号：size_changed（pyqtSignal(dict)）：尺寸变更信号，携带所有计算后的尺寸值字典
		* 方法：__init__(self, ref_width: int, ref_height: int, throttle_ms: int = 100) -> None，calculate_sizes(self, width: int, height: int) -> dict[str, Any]，set_throttle(self, ms: int) -> None，on_resize(self, width: int, height: int) -> None，_do_calculate(self) -> None
* 输入输出：
	- 输入：窗口宽度（int）、窗口高度（int）
	- 输出：尺寸字典 dict{"toolbar_width", "toolbar_icon_size", "panel_title_font", "panel_body_font", "panel_small_font", "general_margin", "general_padding", "border_radius", "splitter_handle_width", "button_height", "input_height", "icon_size_small", "icon_size_medium"}
* 依赖关系：依赖app_infra.utils.size_utils（底层计算函数），不依赖app_core/app_data

#### 2. ThemeManager（app_ui/theme_manager.py）
* 类结构：
	- ThemeManager（QObject子类，单例模式）：
		* 属性：_instance（ThemeManager | None）：单例实例（类属性），_theme_mode（str）：当前主题模式（"dark"/"light"/"system"），_color_palette（dict[str, dict[str, str]]）：语义化颜色字典（暗色和亮色各一套），_qss_cache（dict[str, str]）：QSS文件内容缓存
		* 信号：theme_changed（pyqtSignal(str)）：主题变更信号，携带actual_theme_name（"dark"或"light"）
		* 方法：get_instance()（@staticmethod）-> ThemeManager，set_theme(self, mode: str) -> None，toggle_theme(self) -> None，get_effective_theme(self) -> str，load_qss(self, theme_name: str) -> str，get_color(self, semantic_name: str) -> str，_load_color_palette(self) -> None，_on_system_theme_changed(self) -> None
* 输入输出：
	- 输入：set_theme接收mode字符串（"dark"/"light"/"system"）
	- 输出：get_color返回颜色值字符串（如"#1E1E2E"），load_qss返回QSS样式表字符串
* 依赖关系：依赖app_infra.ConfigManager（持久化主题偏好），依赖QApplication.styleHints().colorSchemeChanged信号监听系统主题变化

#### 3. VerticalToolBar（app_ui/widgets/vertical_tool_bar.py）
* 类结构：
	- VerticalToolBar（QWidget子类）：
		* 属性：_buttons（list[QPushButton]）：工具按钮列表，_button_group（QButtonGroup）：按钮互斥分组，_current_tool_id（str | None）：当前选中工具ID，_theme（str）：当前主题名称，_size_info（dict）：当前尺寸信息，_animations（dict[str, QPropertyAnimation]）：动画实例缓存
		* 信号：tool_selected（pyqtSignal(str)）：工具选中信号，携带tool_id
		* 方法：__init__(self, parent: QWidget | None = None) -> None，setup_ui(self) -> None，register_tool(self, tool_id: str, icon_text: str, tooltip: str) -> None，switch_to_tool(self, tool_id: str) -> None，update_sizes(self, sizes: dict) -> None，update_theme(self, theme: str) -> None，_on_button_clicked(self, button_id: str) -> None，_apply_button_animation(self, button: QPushButton, property_name: str, start_val, end_val, duration: int) -> None，enterEvent(self, event)，leaveEvent(self, event)
* 输入输出：
	- 输入：register_tool接收工具ID、图标文本（Unicode或SVG路径）、提示文本；update_sizes接收SizeManager输出的尺寸字典
	- 输出：tool_selected信号发射选中的工具ID字符串
* 依赖关系：依赖AnimationUtils（按钮动效），依赖ThemeManager（颜色获取），不依赖app_core/app_data

#### 4. SplitterPanels（app_ui/widgets/splitter_panels.py）
* 类结构：
	- SplitterPanels（QSplitter子类）：
		* 属性：_left_panel（LeftPanel）：左栏实例，_center_panel（CenterPanel）：中栏实例，_right_panel（RightPanel）：右栏实例，_size_info（dict）：当前尺寸信息，_ratio（tuple[int, int, int]）：三栏比例，默认(3, 4, 3)
		* 方法：__init__(self, parent: QWidget | None = None) -> None，setup_ui(self) -> None，set_ratio(self, ratio: tuple[int, int, int]) -> None，update_sizes(self, sizes: dict) -> None，update_theme(self, theme: str) -> None，_on_splitter_moved(self, pos: int, index: int) -> None，createHandle(self) -> QSplitterHandle（重写，返回自定义StyledSplitterHandle实例）
	- StyledSplitterHandle（QSplitterHandle子类）：
		* 方法：__init__(self, orientation, parent) -> None，paintEvent(self, event) -> None（绘制带hover效果的细线分隔条），sizeHint(self) -> QSize，enterEvent(self, event)，leaveEvent(self, event)
* 输入输出：
	- 输入：无显式输入参数；通过update_sizes和update_theme接收全局尺寸和主题配置
	- 输出：暴露_left_panel、_center_panel、_right_panel属性供外部访问，通过内部信号连接间接输出面板数据
* 依赖关系：依赖LeftPanel/CenterPanel/RightPanel三个面板类，依赖ThemeManager获取分割线颜色

#### 5. LeftPanel（app_ui/widgets/left_panel.py）
* 类结构：
	- LeftPanel（QWidget子类）：
		* 属性：_title_label（QLabel）：面板标题，_drop_area（QWidget）：文件拖放区域，_url_input（QLineEdit）：URL输入框，_url_submit_btn（QPushButton）：URL提交按钮，_history_list（QListWidget）：历史记录列表，_layout（QVBoxLayout）：面板主布局
		* 信号：source_selected（pyqtSignal(str)）：内容源选中信号（文件路径或URL字符串）
		* 方法：__init__(self, parent: QWidget | None = None) -> None，setup_ui(self) -> None，update_sizes(self, sizes: dict) -> None，update_theme(self, theme: str) -> None，add_history_item(self, source: str) -> None，_on_drop(self, event: QDropEvent) -> None，_on_url_submit(self) -> None，dragEnterEvent(self, event)，dropEvent(self, event)
* 输入输出：
	- 输入：通过拖放或URL输入接收文件路径/链接
	- 输出：source_selected信号发射源路径字符串
* 依赖关系：依赖ThemeManager获取颜色，不依赖app_core/app_data（仅通过SharedSignals信号通信）

#### 6. CenterPanel（app_ui/widgets/center_panel.py）
* 类结构：
	- CenterPanel（QWidget子类）：
		* 属性：_tab_widget（QTabWidget）：编辑/预览切换标签控件，_editor（QPlainTextEdit）：Markdown源码编辑器，_preview（QTextBrowser）：Markdown渲染预览控件，_current_content（str）：当前Markdown内容
		* 信号：content_changed（pyqtSignal(str)）：内容变更信号
		* 方法：__init__(self, parent: QWidget | None = None) -> None，setup_ui(self) -> None，load_content(self, content: str) -> None，get_content(self) -> str，update_sizes(self, sizes: dict) -> None，update_theme(self, theme: str) -> None，_on_text_changed(self) -> None，_render_preview(self) -> None
* 输入输出：
	- 输入：load_content接收Markdown字符串，update_sizes接收尺寸字典
	- 输出：content_changed信号发射当前编辑内容字符串，get_content返回当前内容
* 依赖关系：依赖ThemeManager获取编辑器配色方案，依赖markdown库（可选依赖）渲染HTML预览

#### 7. RightPanel（app_ui/widgets/right_panel.py）
* 类结构：
	- RightPanel（QWidget子类）：
		* 属性：_title_label（QLabel）：面板标题，_output_path_input（QLineEdit）：输出路径输入框，_browse_btn（QPushButton）：浏览按钮，_format_combo（QComboBox）：导出格式选择下拉框，_progress_bar（QProgressBar）：转换进度条，_status_label（QLabel）：状态文本标签，_convert_btn（QPushButton）：开始转换按钮，_loading_indicator（LoadingIndicator | None）：加载指示器实例
		* 信号：convert_requested（pyqtSignal(dict)）：转换请求信号，携带参数字典{"output_path", "format", "source", "content"}
		* 方法：__init__(self, parent: QWidget | None = None) -> None，setup_ui(self) -> None，update_progress(self, value: int) -> None，set_status(self, text: str) -> None，show_loading(self) -> None，hide_loading(self) -> None，update_sizes(self, sizes: dict) -> None，update_theme(self, theme: str) -> None，_on_browse_clicked(self) -> None，_on_convert_clicked(self) -> None
* 输入输出：
	- 输入：update_progress接收进度值（int 0-100），update_sizes接收尺寸字典
	- 输出：convert_requested信号发射转换参数字典
* 依赖关系：依赖ThemeManager获取颜色，依赖LoadingIndicator组件显示加载动画

#### 8. AnimationUtils（app_ui/animation_utils.py）
* 类结构：使用模块级函数，不定义类
	- 函数：fade_in(widget: QWidget, duration: int = 250, easing: QEasingCurve.Type = QEasingCurve.Type.OutCubic, callback: Callable | None = None) -> QPropertyAnimation：淡入动画，fade_out(widget: QWidget, duration: int = 250, easing: QEasingCurve.Type = QEasingCurve.Type.OutCubic, callback: Callable | None = None) -> QPropertyAnimation：淡出动画，scale_icon(button: QPushButton, target_size: int, duration: int = 200) -> QPropertyAnimation：图标缩放动画，flash_button(button: QPushButton, flash_color: str, duration: int = 150) -> None：按钮点击反馈闪烁效果，cross_fade(old_widget: QWidget, new_widget: QWidget, duration: int = 250) -> tuple[QPropertyAnimation, QPropertyAnimation]：交叉淡入淡出切换，is_reduced_motion() -> bool：检测是否启用减少动效模式
* 输入输出：
	- 输入：目标QWidget/QPushButton实例、动画参数（时长、缓动曲线、颜色等）
	- 输出：QPropertyAnimation实例（供调用方管理动画生命周期）
* 依赖关系：依赖QPropertyAnimation/QGraphicsOpacityEffect/PyQt6动画机制，通过ConfigManager读取reduce_motion配置

#### 9. LoadingIndicator（app_ui/widgets/loading_indicator.py）
* 类结构：
	- LoadingIndicator（QWidget子类）：
		* 属性：_angle（float）：当前旋转角度（弧度），_timer（QTimer）：驱动动画的定时器，_color（QColor）：圆弧颜色，_arc_width（int）：圆弧线宽，_size_hint（int）：组件尺寸，_fps（int）：帧率（默认30），_elapsed_timer（QElapsedTimer）：实际时间计时，用于修正帧率波动
		* 方法：__init__(self, parent: QWidget | None = None, size: int = 32, color: str = "#6C8EBF") -> None，start(self) -> None，stop(self) -> None，is_running(self) -> bool，set_color(self, color: str) -> None，set_size(self, size: int) -> None，paintEvent(self, event)，sizeHint(self) -> QSize，showEvent(self, event)，hideEvent(self, event)
* 输入输出：
	- 输入：构造函数参数size（像素）、color（颜色字符串），set_color/set_size动态调整外观
	- 输出：无直接输出，通过QWidget渲染在当前父组件中显示旋转加载动画
* 依赖关系：仅依赖PyQt6的QPainter/QTimer/QColor/QElapsedTimer，无项目内模块依赖

#### 10. size_utils（app_infra/utils/size_utils.py）
* 类结构：使用模块级函数，不定义类
	- 函数：calculate_base_unit(width: int, height: int, reference: int = 733) -> float：计算基础单位 = min(w, h) / reference，calculate_toolbar_width(base: float) -> int：return int(base * 29)，对应 0.04 * 基准宽度，calculate_toolbar_icon_size(base: float) -> int：return int(base * 21)，对应 0.028 * 基准高度，calculate_title_font_size(base: float) -> int：return int(base * 16)，对应 0.022 * 基准高度，calculate_body_font_size(base: float) -> int：return int(base * 13)，对应 0.018 * 基准高度，calculate_small_font_size(base: float) -> int：return int(base * 10)，对应 0.014 * 基准高度，calculate_general_margin(base: float) -> int：return int(base * 6)，对应 0.008 * 基准宽度，calculate_general_padding(base: float) -> int：return int(base * 9)，对应 0.012 * 基准宽度，calculate_border_radius(base: float) -> int：return int(base * 6)，对应 0.008 * 基准高度，calculate_splitter_handle(base: float) -> int：return max(2, int(base * 0.003))，calculate_button_height(base: float) -> int：return int(base * 22)，对应 0.03 * 基准高度，calculate_input_height(base: float) -> int：return int(base * 20)，对应 0.027 * 基准高度
* 输入输出：
	- 输入：窗口width（int）、height（int），可选reference（int）基准参考高度值
	- 输出：各组件尺寸值（int）
* 依赖关系：仅依赖Python标准库（math模块），无PyQt6依赖，无项目内模块依赖

#### 11. SharedSignals扩展（app_ui/signals.py）
* 类结构：在现有SharedSignals单例类中新增信号声明
	- 新增信号：theme_changed（pyqtSignal(str)）：主题切换信号（携带 "dark" 或 "light" ），size_changed（pyqtSignal(dict)）：尺寸重算完成信号（携带尺寸字典），tool_changed（pyqtSignal(str)）：当前活跃工具变更信号（携带 tool_id），source_loaded（pyqtSignal(str)）：内容源加载完成信号（携带源路径或URL）
* 输入输出：与现有SharedSignals保持一致的设计模式
* 依赖关系：仅依赖PyQt6的pyqtSignal

### 功能实现流程
#### 1. 启动流程（UI初始化阶段）
* 实现步骤：
	1. main.py调用main_window = MainWindow()创建主窗口实例，构造函数中获取屏幕分辨率并计算黄金比例窗口尺寸
	2. MainWindow.__init__中调用QApplication.primaryScreen().availableGeometry()获取屏幕可用区域尺寸
	3. 计算 window_width = round(screen_width * 0.618)，window_height = round(window_width * 0.618)
	4. 对计算结果应用上下限约束：min_width=800, min_height=500, max_width=round(screen_width*0.9), max_height=round(screen_height*0.9)
	5. 检查ConfigManager中是否有已保存的窗口尺寸（首次启动无已保存值，使用计算值；非首次启动使用已保存值）
	6. self.resize(window_width, window_height)，self.setMinimumSize(min_width, min_height)，调用_center_on_screen居中窗口
	7. main.py中调用main_window.setup_ui()进入UI布局初始化
	8. MainWindow.setup_ui()按序调用私有方法：_setup_theme_manager() -> _setup_size_manager() -> _setup_central_area() -> _setup_vertical_tool_bar() -> _setup_splitter_panels() -> _load_theme_qss()
* 数据流转：屏幕分辨率 -> 黄金比例计算 -> 窗口尺寸设置 -> ThemeManager初始化 -> SizeManager初始化 -> VerticalToolBar构建 -> SplitterPanels构建 -> 三栏面板构建 -> QSS加载 -> 界面显示
* 异常处理：
	- QApplication.primaryScreen()返回None（headless环境）：回退使用预设虚拟尺寸1920x1080，记录警告日志
	- 黄金比例计算结果超出屏幕可用范围：自动钳制到min/max约束范围内，记录警告日志
	- 主题QSS文件缺失：回退使用QPalette基础配色方案，记录错误日志，不阻塞启动

#### 2. 三栏布局构建流程
* 实现步骤：
	1. MainWindow._setup_central_area()创建QWidget作为central_widget，设置QHBoxLayout，margins=0, spacing=0
	2. 通过setCentralWidget(central_widget)替换原有QStackedWidget中央控件
	3. MainWindow._setup_vertical_tool_bar()创建VerticalToolBar实例，从SizeManager获取toolbar_width，调用toolbar.setFixedWidth(toolbar_width)
	4. VerticalToolBar添加到central_widget布局中（布局索引0，最左侧位置）
	5. MainWindow._setup_splitter_panels()创建SplitterPanels实例（QSplitter子类，Qt.Orientation.Horizontal）
	6. SplitterPanels.setup_ui()中依次创建LeftPanel、CenterPanel、RightPanel实例，addWidget添加到QSplitter中
	7. 计算三栏初始尺寸：available_width = window_width - toolbar_width - splitter_handles_width（约2个handle x 3px），base = available_width // 10，设置setSizes([base*3, base*4, base*3])
	8. 设置各栏最小宽度：左栏和右栏setMinimumWidth(200)，中栏setMinimumWidth(300)，setCollapsible分别控制折叠行为
	9. SplitterPanels添加到central_widget布局中（布局索引1，占据剩余全部空间，stretch=1）
* 数据流转：SizeManager计算 -> toolbar_width -> VerticalToolBar.setFixedWidth -> 计算三栏base值 -> SplitterPanels.setSizes -> 各面板实例化及setup_ui
* 异常处理：
	- 面板最小宽度之和超过可用宽度导致QSplitter无法满足约束：逐级降低最小宽度约束（最小至100px），记录警告日志

#### 3. 窗口resize尺寸响应流程
* 实现步骤：
	1. 用户拖拽窗口边框触发QMainWindow.resizeEvent
	2. MainWindow重写resizeEvent：获取当前QMainWindow.width()和height()
	3. 调用SizeManager.on_resize(new_width, new_height)（内部触发防抖定时器重置）
	4. SizeManager防抖定时器（100ms）到期后调用_do_calculate()执行实际尺寸计算
	5. _do_calculate中调用size_utils各函数计算所有组件新尺寸并组装尺寸字典
	6. 发射SizeManager.size_changed信号，携带完整尺寸字典
	7. MainWindow接收size_changed信号：依次调用vertical_tool_bar.update_sizes(sizes)、splitter_panels.update_sizes(sizes)
	8. splitter_panels.update_sizes遍历三个子面板调用各自的update_sizes方法
	9. 各面板在update_sizes中更新内部组件的字体大小、间距、图标尺寸等属性
	10. 异步保存当前窗口尺寸到ConfigManager.set_runtime（"window_width"/"window_height"）
* 数据流转：窗口尺寸变更 -> resizeEvent -> SizeManager防抖 -> size_utils数学计算 -> size_changed信号 -> 各组件update_sizes -> 界面自动重绘
* 异常处理：
	- 极度频繁resize导致防抖队列堆积：QTimer.setSingleShot(True)确保每次on_resize先stop旧定时器再start新定时器，只有最新尺寸被处理
	- resize计算耗时过长：所有计算为纯整数运算耗时在微秒级别，不存在界面卡顿风险

#### 4. 主题切换流程
* 实现步骤：
	1. 触发源检测：用户点击VerticalToolBar底部主题切换按钮 或 系统主题变化（QStyleHints.colorSchemeChanged信号自动触发）
	2. 用户手动切换：调用ThemeManager.set_theme("dark"/"light"/"system")
	3. 系统自动切换：ThemeManager._on_system_theme_changed()检查当前mode若为"system"则重新计算effective_theme并发射信号
	4. set_theme方法：更新_theme_mode属性，将新模式持久化到ConfigManager（theme_mode键），调用get_effective_theme()获取实际主题名
	5. 若实际主题名与当前已生效主题名相同则直接返回跳过（避免重复切换开销）
	6. 发射theme_changed信号，携带实际主题名字符串（"dark" 或 "light"）
	7. MainWindow接收theme_changed信号：调用ThemeManager.load_qss(theme_name)获取替换占位符后的QSS字符串
	8. QApplication.instance().setStyleSheet(qss_content)全局应用新样式表
	9. 遍历所有已注册面板调用update_theme(theme_name)方法，各面板更新QSS无法覆盖的内联样式（如QPlainTextEdit背景色需代码设置）
	10. 更新VerticalToolBar中主题切换按钮的图标文本（月亮unicode/太阳unicode）
* 数据流转：切换触发源 -> ThemeManager.set_theme -> ConfigManager持久化偏好 -> theme_changed信号 -> QSS文件读取+占位符替换 -> 全局setStyleSheet -> 各面板update_theme
* 异常处理：
	- QSS文件缓存未命中：调用load_qss从文件系统读取，捕获FileNotFoundError后使用内置最小QSS兜底内容
	- QApplication.instance()为None（极端场景）：跳过全局样式设置步骤，仅调用各面板update_theme方法

#### 5. 工具栏按钮交互流程
* 实现步骤：
	1. 应用启动时MainWindow调用toolbar.register_tool(tool_id, icon_text, tooltip)注册所有工具按钮
	2. register_tool创建自定义ToolButton实例（QPushButton子类），设置icon文本、tooltip，setCheckable(True)，加入_button_group实现互斥单选
	3. 用户鼠标悬浮按钮：ToolButton.enterEvent触发，调用AnimationUtils.scale_icon(button, target_size, 200)执行图标放大动画
	4. 用户鼠标离开按钮：ToolButton.leaveEvent触发，调用AnimationUtils.scale_icon(button, original_size, 200)执行图标恢复动画
	5. 用户点击按钮：按钮置为checked状态，QSS :checked伪状态自动应用高亮样式（background-color变化 + border-left绘制左侧竖条选中指示器）
	6. 发射toolbar.tool_selected(tool_id)信号
	7. MainWindow接收tool_selected信号，根据tool_id路由执行对应逻辑（切换面板显示、更新内容区域等）
	8. 面板切换时如需淡入淡出过渡效果：AnimationUtils.cross_fade(current_widget, target_widget, 250)实现平滑视觉切换
* 数据流转：用户悬浮/点击 -> ToolButton enterEvent/clicked事件 -> AnimationUtils动效执行 -> tool_selected信号发射 -> MainWindow槽函数路由 -> 面板显示切换或内容更新
* 异常处理：
	- 快速连续点击多个按钮导致动画冲突：QPropertyAnimation在执行新动画前自动stop()停止旧动画
	- 减少动效模式开启：AnimationUtils.is_reduced_motion()返回True时所有动画时长设为0，直接跳至最终状态

#### 6. 加载指示器动画流程
* 实现步骤：
	1. 业务模块（如RightPanel._on_convert_clicked）调用loading_indicator.show()和loading_indicator.start()启动加载动画
	2. start方法启动内部QTimer，间隔interval=1000/fps（默认约33ms即30fps），同时重置QElapsedTimer开始计时
	3. QTimer超时回调中读取QElapsedTimer.elapsed()计算实际经过时间，按实际增量更新_angle（angle += elapsed_sec * 2 * pi * 0.8），调用self.update()触发重绘
	4. paintEvent中调用QPainter绘制圆弧：使用QConicalGradient设置画笔渐变颜色（从透明到accent色），QPainter.drawArc绘制约270度跨度的圆弧
	5. 圆弧起始角度由_angle决定，每帧旋转约0.15弧度（约8.6度），通过QElapsedTimer时间修正避免帧率波动导致旋转不均匀
	6. 业务操作完成或出错后调用loading_indicator.stop()停止QTimer，调用loading_indicator.hide()隐藏
	7. hideEvent中自动调用stop()确保组件隐藏时定时器不空转消耗CPU
	8. showEvent中如果之前为运行状态则自动恢复动画
* 数据流转：操作开始 -> show()+start() -> QTimer循环 -> QElapsedTimer计时 -> _angle递增 -> paintEvent绘制圆弧 -> 操作完成 -> stop()+hide()
* 异常处理：
	- QTimer在组件已删除后仍触发回调：在paintEvent首行检查self.isVisible()，不可见时自动stop()停止定时器
	- 高CPU负载导致帧率骤降：QElapsedTimer真实时间修正机制确保旋转速度恒定（基于实际时间增量而非固定帧增量）

### UI界面设计方案
* 整体布局：
	* 主窗口（QMainWindow）采用全新三栏布局结构：顶部菜单栏（QMenuBar，保留）-> 中央区域（QHBoxLayout容器，替换原有QStackedWidget）-> 底部状态栏（QStatusBar，保留）
	* 中央区域从左到右依次为：VerticalToolBar（固定窄宽度，约48-56px，按屏幕宽度4%计算）-> QSplitter三栏容器（左栏:中栏:右栏 = 3:4:3）
	* 移除原有QToolBar，其预留功能整合到VerticalToolBar和后续三栏面板中
	* 窗口初始尺寸 = 屏幕可用尺寸 x 0.618（黄金比例），居中显示于屏幕，支持用户自由缩放
	* 所有顶层布局margins = 0, spacing = 0，由各面板内部控制内部组件间距
* 组件列表：
	1. main_window（QMainWindow）：
		* 父组件：无（顶级窗口）
		* 关键属性：windowTitle="ECBM"，objectName="MainWindow"，minimumWidth=800，minimumHeight=500
		* 信号与槽：closeEvent -> 优雅退出流程处理，resizeEvent -> SizeManager.on_resize，主题切换信号 -> MainWindow._on_theme_changed
	2. menu_bar（QMenuBar）：
		* 父组件：main_window
		* 关键属性：objectName="MenuBar"（保持不变）
		* 新增菜单项：视图菜单（QMenu "view_menu"）含主题切换动作（QAction "action_toggle_theme"），文件菜单和帮助菜单保留原有实现
		* 信号与槽：action_toggle_theme.triggered -> ThemeManager.toggle_theme
	3. status_bar（QStatusBar）：
		* 父组件：main_window
		* 关键属性：objectName="StatusBar"（保持不变）
		* 信号与槽：接收SharedSignals.source_loaded信号显示"已加载: [源路径]"信息
	4. central_container（QWidget）：
		* 父组件：main_window（通过setCentralWidget设置）
		* 关键属性：objectName="CentralContainer"
		* 内部布局：QHBoxLayout，setContentsMargins(0,0,0,0)，setSpacing(0)
	5. vertical_tool_bar（VerticalToolBar）：
		* 父组件：central_container
		* 关键属性：objectName="VerticalToolBar"，setFixedWidth由SizeManager计算（约48-56px）
		* 默认注册工具按钮：文件浏览器（file_explorer，Unicode图标）、URL链接输入（url_input）、转换任务列表（convert_tasks）、设置（settings），底部固定主题切换按钮（theme_toggle，月亮/太阳Unicode图标）
		* 信号与槽：tool_selected(str) -> MainWindow._on_tool_selected(str)
	6. splitter_panels（SplitterPanels）：
		* 父组件：central_container
		* 关键属性：objectName="SplitterPanels"，orientation=Qt.Orientation.Horizontal，handleWidth=3，childrenCollapsible=True
		* 初始sizes：由current_width减去toolbar_width后按3:4:3分配
	7. left_panel（LeftPanel）：
		* 父组件：splitter_panels（addWidget索引0）
		* 关键属性：objectName="LeftPanel"，minimumWidth=200
		* 子组件结构（自上而下）：标题QLabel（objectName="PanelTitle"，文本"内容源"）、拖放区域QWidget（objectName="DropArea"，acceptDrops=True，显示"拖放文件到此处或输入URL"提示）、URL输入QLineEdit（objectName="UrlInput"，placeholderText="输入文件路径或URL..."）、提交QPushButton（objectName="UrlSubmitBtn"，文本"加载"）、历史记录QListWidget（objectName="HistoryList"）
		* 信号与槽：source_selected(str) -> SharedSignals.source_loaded.emit(str)
	8. center_panel（CenterPanel）：
		* 父组件：splitter_panels（addWidget索引1）
		* 关键属性：objectName="CenterPanel"，minimumWidth=300
		* 子组件结构：QTabWidget（objectName="EditorTabs"）包含"编辑"标签页（QPlainTextEdit，objectName="MarkdownEditor"，placeholderText="在此编辑Markdown内容..."）和"预览"标签页（QTextBrowser，objectName="MarkdownPreview"）
		* 信号与槽：content_changed(str) -> 预览页通过QTimer防抖500ms后自动刷新渲染
	9. right_panel（RightPanel）：
		* 父组件：splitter_panels（addWidget索引2）
		* 关键属性：objectName="RightPanel"，minimumWidth=200
		* 子组件结构（自上而下）：标题QLabel（objectName="PanelTitle"，文本"输出设置"）、输出路径行（QHBoxLayout内含QLineEdit objectName="OutputPath" + QPushButton objectName="BrowseBtn" 文本"浏览"）、导出格式QComboBox（objectName="FormatCombo"，选项：Markdown(.md)/HTML(.html)/纯文本(.txt)）、转换QPushButton（objectName="ConvertBtn"，文本"开始转换"）、QProgressBar（objectName="ProgressBar"，初始value=0）、状态QLabel（objectName="StatusLabel"，文本"就绪"）、LoadingIndicator（objectName="LoadingIndicator"，默认隐藏）
		* 信号与槽：convert_requested(dict) -> MainWindow分发到业务控制器处理
	10. loading_indicator（LoadingIndicator）：
		* 父组件：right_panel（按需创建，可被任意面板复用）
		* 关键属性：objectName="LoadingIndicator"，fixedWidth=32，fixedHeight=32
		* 控制方法：start()启动旋转动画，stop()停止动画，is_running()查询运行状态
* 交互逻辑：
	* 用户点击左侧工具栏按钮 -> VerticalToolBar发射tool_selected信号 -> MainWindow._on_tool_selected路由处理 -> 选中按钮高亮（左侧竖条+背景色变化+颜色过渡动画）-> 对应面板获得焦点或切换显示
	* 用户拖拽文件到左栏/输入URL后点击"加载" -> LeftPanel发射source_selected信号 -> MainWindow通知CenterPanel.load_content加载内容 -> 用户在编辑/预览标签页间切换编辑或查看Markdown渲染结果
	* 用户在右栏配置输出路径/格式后点击"开始转换" -> RightPanel发射convert_requested信号 -> MainWindow转发至业务控制器 -> 控制器创建工作线程执行转换 -> 工作线程progress信号更新RightPanel进度条 -> finished信号触发状态更新为"完成"
	* 用户点击主题切换按钮（工具栏底部）或菜单"视图->切换主题" -> ThemeManager.toggle_theme() -> theme_changed信号 -> 全局QSS替换 + 各面板update_theme -> 按钮图标在月亮/太阳Unicode字符间切换
	* 用户拖拽窗口边框缩放 -> resizeEvent -> SizeManager防抖重算 -> size_changed信号 -> 工具栏+三栏+所有面板子组件尺寸按比例更新 -> 窗口新尺寸异步写入ConfigManager

### 关键技术实现要点
#### 1. 黄金比例窗口尺寸计算
* 实现思路：首次启动通过QScreen获取屏幕可用分辨率（availableGeometry），按黄金比例0.618计算窗口宽高，应用最小/最大约束后设置；后续启动从ConfigManager读取用户已调整的保存尺寸
* 关键代码片段：

```python
def calculate_golden_window_size(screen) -> tuple[int, int]:
    geo = screen.availableGeometry()
    sw, sh = geo.width(), geo.height()
    base = min(sw, sh)
    w = round(base * 0.618)
    h = round(w * 0.618)
    w = max(800, min(w, int(sw * 0.9)))
    h = max(500, min(h, int(sh * 0.9)))
    return w, h
```

* 注意事项：QScreen.availableGeometry()会扣除任务栏/系统托盘区域，避免窗口与任务栏重叠；headless环境QScreen可能为None需回退到1920x1080预设值

#### 2. QSplitter自定义Handle绘制
* 实现思路：重写QSplitter.createHandle()返回StyledSplitterHandle子类实例，在paintEvent中使用QPainter绘制1px半透明分割线，enterEvent/leaveEvent中标记hover状态切换颜色
* 关键代码片段：

```python
class StyledSplitterHandle(QSplitterHandle):
    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        c = QColor("#6C8EBF") if self._hovered else QColor("#3A3A4A")
        w, h = self.width(), self.height()
        tw, th = (2, h) if self.orientation() == Qt.Orientation.Horizontal else (w, 2)
        p.fillRect(w // 2 - tw // 2, h // 2 - th // 2, tw, th, c)
        p.end()
```

* 注意事项：handle绘制区域较小（约3-4px宽），需设置setAttribute(Qt.WidgetAttribute.WA_Hover)确保hover事件正确触发；handle的sizeHint需返回合理的QSize确保拖动交互区域足够

#### 3. QSS占位符主题替换系统
* 实现思路：由于PyQt6 QSS不支持CSS var()语法，采用QSS文件内{{color_key}}占位符 + ThemeManager运行时Python字符串replace方案实现主题变量替换
* 关键代码片段：

```python
class ThemeManager(QObject):
    _DARK = {"bg_primary": "#1E1E2E", "bg_secondary": "#2A2A3C",
             "text_primary": "#E0E0F0", "accent": "#6C8EBF",
             "border": "#3A3A50", "separator": "#2A2A3A"}
    _LIGHT = {"bg_primary": "#F5F5F5", "bg_secondary": "#EAEAEA",
              "text_primary": "#1E1E2E", "accent": "#4A7ABF",
              "border": "#C0C0D0", "separator": "#D0D0D0"}

    def load_qss(self, theme: str) -> str:
        if theme not in self._cache:
            path = get_project_root() / "app_ui" / "styles" / f"{theme}_theme.qss"
            tpl = path.read_text(encoding="utf-8")
            p = self._DARK if theme == "dark" else self._LIGHT
            for k, v in p.items():
                tpl = tpl.replace("{{" + k + "}}", v)
            self._cache[theme] = tpl
        return self._cache[theme]
```

* 注意事项：QSS文件内所有颜色值必须使用{{color_key}}占位符格式；ThemeManager._DARK和_LIGHT必须包含完全相同的键集合；替换后检查QSS中是否残留未替换的占位符

#### 4. 防抖resize尺寸计算
* 实现思路：SizeManager内部使用QTimer.singleShot实现防抖，每次窗口resize先停止旧定时器再启动新定时器（100ms），只有最后一次尺寸被实际计算
* 关键代码片段：

```python
class SizeManager(QObject):
    size_changed = pyqtSignal(dict)

    def on_resize(self, w: int, h: int) -> None:
        if abs(w - self._window_width) < 5 and abs(h - self._window_height) < 5:
            return
        self._pending = (w, h)
        if self._throttle_timer.isActive():
            self._throttle_timer.stop()
        self._throttle_timer.start(self._throttle_ms)
```

* 注意事项：尺寸变化小于5px时跳过计算避免无效更新；窗口最大化/全屏操作时应立即计算一次跳过防抖延迟

#### 5. 工具栏按钮动画（hover缩放+选中指示器）
* 实现思路：自定义ToolButton（QPushButton子类），重写enterEvent/leaveEvent使用QPropertyAnimation动画化iconSize或font属性实现hover缩放；选中状态通过QSS :checked伪状态设置border-left实现左侧竖条指示器
* 关键代码片段：

```python
class ToolButton(QPushButton):
    def enterEvent(self, ev):
        if AnimationUtils.is_reduced_motion():
            return
        self._anim.stop()
        self._anim.setDuration(200)
        self._anim.setStartValue(self._icon_size)
        self._anim.setEndValue(self._hover_size)
        self._anim.setEasingCurve(QEasingCurve.Type.OutCubic)
        self._anim.start()
```

* 注意事项：若使用Unicode文本模拟图标则需动画化font-size属性（改用QFont + setFont方案）；每次enter/leave前必须先stop()旧动画

#### 6. 系统主题自动跟随
* 实现思路：监听QApplication.styleHints().colorSchemeChanged信号（Qt 6.5+），仅当用户设置主题模式为"system"时自动响应系统主题变化并发射theme_changed信号
* 关键代码片段：

```python
def _connect_system_theme(self):
    app = QApplication.instance()
    if app is not None:
        app.styleHints().colorSchemeChanged.connect(
            lambda: self._mode == "system" and self.theme_changed.emit(self.get_effective_theme())
        )
```

* 注意事项：colorSchemeChanged信号需Qt 6.5+支持，添加版本检查；部分Linux桌面环境可能不触发该信号，手动切换入口作为回退方案

#### 7. 减少动效支持
* 实现思路：ConfigManager提供reduce_motion布尔配置项（默认False），AnimationUtils.is_reduced_motion()读取该配置，所有动画函数在首行检查若为True则duration设为0直接跳至终态
* 关键代码片段：

```python
def is_reduced_motion() -> bool:
    return ConfigManager.get_instance().get("reduce_motion", False)
```

* 注意事项：无Qt系统级API直接获取OS层级的"减少动画"偏好设置，当前仅依赖ConfigManager用户配置项；后续可通过检测Windows注册表Accessibility键值扩展

### 测试方案设计
* 单元测试要点：
	- SizeManager.calculate_sizes测试：给定典型窗口尺寸（如1186x733），验证返回尺寸字典中各值在合理范围内（toolbar_width 48-52，title_font 14-16，body_font 12-14）
	- size_utils边界测试：极小窗口（800x500）和极大窗口（3840x2160）下各计算函数输出不出现负值或零值
	- ThemeManager单例测试：验证get_instance()多次调用返回同一实例，验证set_theme/toggle_theme/get_effective_theme逻辑正确性
	- ThemeManager颜色字典完整性测试：验证_DARK和_LIGHT包含完全相同的键集合，所有颜色值格式为合法hex颜色字符串
	- AnimationUtils减运动测试：验证is_reduced_motion()返回True时所有动画函数duration参数实际为0
	- LoadingIndicator绘制测试：模拟不同角度值下paintEvent不抛出异常
* 集成测试要点：
	- 启动流程集成测试：验证MainWindow实例化后三栏+工具栏布局正确创建，各面板不为None，窗口尺寸匹配黄金比例计算结果
	- 主题切换集成测试：模拟ThemeManager.set_theme("dark")和set_theme("light")，验证QApplication.styleSheet()正确更新，各面板update_theme被调用
	- resize响应集成测试：模拟MainWindow.resize(1200, 800)，等待防抖延迟后验证SizeManager.size_changed信号正确发射且各面板update_sizes被调用
	- 工具栏交互集成测试：模拟VerticalToolBar按钮点击，验证tool_selected信号正确路由到MainWindow处理
	- QSplitter拖拽集成测试：模拟分隔条拖拽操作，验证handle位置正确更新且各面板最小宽度约束生效
* 性能测试指标：
	- 应用冷启动到界面完全显示完成（含QSS解析+主题加载）目标 < 3秒
	- 窗口resize到size_changed信号发射总延迟目标 < 150ms（含100ms防抖）
	- 主题切换完成时间（从set_theme调用到界面完全更新）目标 < 300ms
	- LoadingIndicator单实例运行CPU占用目标 < 1%
	- 工具栏按钮hover动画帧率目标 >= 40fps（QPropertyAnimation驱动）
* 测试数据准备：
	- 测试用QSS文件（test_theme.qss）：使用{{color_key}}占位符格式的简化主题文件，含基本选择器
	- 测试用屏幕配置模拟：1920x1080、1366x768、2560x1440、3840x2160四种分辨率场景
	- 测试用Markdown内容：包含标题、列表、代码块、链接的完整Markdown示例文本，用于CenterPanel渲染测试

### 参考关联
* [官方技术文档]：Gift/Document/PyQt6Docs.md - QScreen类（屏幕尺寸获取API）、QSplitter类（分割面板容器）、QPropertyAnimation类（属性动画引擎）、QGraphicsOpacityEffect类（透明度效果）、Signals and Slots章节（信号槽通信机制）、QSS样式表选择器语法、QStyleHints.colorSchemeChanged信号
* [官方技术文档]：Gift/Document/Python3.14.4Doc.md - pathlib.Path（跨平台文件路径处理）、math模块（数学计算函数）、logging模块（日志记录）
* [优秀开源项目-unified-ui]：Gift/ReferenceProject/unified-ui/packages/unified-ui/src/components/sidebar.tsx - Sidebar系统设计，折叠为图标的布局模式，provider上下文管理模式，转化为PyQt6左侧工具栏按钮组管理方案
* [优秀开源项目-unified-ui]：Gift/ReferenceProject/unified-ui/packages/unified-ui/src/components/resizable.tsx - ResizablePanelGroup可拖拽分隔设计，对应QSplitter的handle定制逻辑
* [优秀开源项目-unified-ui]：Gift/ReferenceProject/unified-ui/packages/unified-ui/src/tokens/ - 设计令牌体系（色彩/间距/动效/阴影/排版），语义化组织结构，转化为Python字典常量定义
* [优秀开源项目-unified-ui]：Gift/ReferenceProject/unified-ui/packages/unified-ui/src/motion/presets.ts - Framer Motion动效预设（fadeIn/scaleIn/slideIn），映射为QPropertyAnimation实现方案
* [优秀开源项目-unified-ui]：Gift/ReferenceProject/unified-ui/packages/unified-ui/src/theme/customizer-store.tsx - 主题customizer状态管理模式，设计主题管理器的持久化和运行时切换机制
* [优秀开源项目-webtui]：Gift/ReferenceProject/webtui/packages/css/src/base.css - CSS @layer分层样式架构、属性驱动的样式模式、暗色/亮色CSS变量体系，应用于QSS文件组织结构设计
* [优秀开源项目-markitdown]：Gift/ReferenceProject/markitdown/ - 插件系统设计（entry_points + register_converters），预留UI面板动态注册扩展机制
* [现有项目架构]：ECBMCode/app_ui/main_window.py - 现有MainWindow类需在setup_ui()方法中重构布局结构
* [现有项目架构]：ECBMCode/app_ui/signals.py - 现有SharedSignals单例类需扩展UI相关全局信号
* [现有项目架构]：ECBMCode/app_infra/config/config_manager.py - 现有ConfigManager需新增theme_mode、window_width、window_height、reduce_motion配置项默认值
* [工具]：Gift/Tools/GetTime.bat - 系统时间获取工具

### 注意事项
* [编码规范]：所有新增Python文件首行添加"# -*- coding: utf-8 -*-"编码注释，文件名使用snake_case，类名PascalCase，函数/方法snake_case，常量UPPER_SNAKE_CASE
* [线程安全]：UI组件尺寸更新（update_sizes）和主题更新（update_theme）必须在主线程执行，不得在工作线程直接调用UI方法；跨线程通信使用pyqtSignal的自动线程安全传递机制
* [QSS加载时序]：必须在MainWindow.show()之前完成QSS样式表加载（setup_ui流程末尾），避免窗口先显示无样式或默认样式后突变至主题样式导致的视觉闪烁
* [资源路径规范]：QSS样式文件统一放置在app_ui/styles/目录（dark_theme.qss、light_theme.qss）；图标资源放置在resources/icons/目录
* [QSS占位符冲突避免]：ThemeManager.load_qss中使用{{color_key}}双花括号格式标识颜色占位符，与Python str.format()的单花括号语法彻底区分，避免意外的字符串格式化冲突
* [QSplitter Handle定制]：必须重写QSplitter.createHandle()方法返回StyledSplitterHandle子类实例，不能仅通过QSS样式表定制handle外观（QSS对QSplitterHandle的样式控制能力有限）
* [iconSize动画兼容性]：QPropertyAnimation对iconSize属性动画要求按钮必须使用QIcon.setIcon()设置图标；若使用Unicode文本模拟图标则需改用QLabel+fontSize方案或QGraphicsView方案
* [QGraphicsOpacityEffect清理]：面板切换淡入淡出动画使用QGraphicsOpacityEffect后，必须在动画finished信号的槽函数中调用widget.setGraphicsEffect(None)彻底移除效果对象，避免持续渲染导致的性能持续下降
* [防抖定时器管理]：SizeManager.on_resize中每次调用必须先检查_throttle_timer.isActive()，若活跃则stop()后再start()，确保只有最后一次窗口尺寸被实际计算处理
* [配置持久化策略]：主题偏好（theme_mode）在set_theme调用时即时持久化到ConfigManager；窗口尺寸（window_width/window_height）在防抖计算完成后异步保存到ConfigManager.set_runtime，避免阻塞resize事件正常处理
* [QPlainTextEdit主题适配]：编辑器组件的背景色和文字色需在CenterPanel.update_theme方法中通过setStyleSheet内联样式代码设置，不能仅依赖全局QSS（QPlainTextEdit对部分QSS选择器支持有限制）
* [最小栏宽保护机制]：QSplitter中setCollapsible(False)配合setMinimumWidth()确保三栏不会因用户拖拽分隔条而完全折叠消失；当窗口总宽度不足以容纳三栏最小宽度之和时，优先压缩中栏（通过调大其stretchFactor实现）
* [验收标准]：
	1. 主窗口首次启动时尺寸 = 屏幕可用区域 x 0.618（黄金比例），居中显示，后续启动使用ConfigManager已保存尺寸
	2. 左侧竖向工具栏显示4个工具按钮+1个主题切换按钮，按钮hover有缩放动效，选中状态显示左侧竖条高亮指示器
	3. 三栏按3:4:3比例正确显示，支持鼠标拖拽分隔条调整栏宽，各栏最小宽度约束生效不可完全折叠
	4. 暗色/亮色主题切换响应时间 < 300ms，切换后所有组件颜色正确更新无明显延迟
	5. 窗口resize后约0.1秒（防抖间隔）所有组件尺寸按比例重新计算并更新显示
	6. 减少动效模式开启时所有动画时长归零，界面直接呈现最终状态无过渡动画
	7. 加载指示器旋转动画平滑无卡顿（>25fps），启动/停止无闪烁，隐藏时自动停止定时器
	8. 全局异常钩子继续生效，UI组件初始化或更新过程中的异常不导致应用崩溃
* [潜在Bug风险]：QSplitter在窗口缩至极小尺寸时handle可能完全不可见导致用户无法拖拽恢复，需在SplitterPanels中重写resizeEvent检查各handle位置是否合法并在必要时自动调整sizes；QSS文件中占位符替换后若ThemeManager颜色字典缺少某个键将导致占位符残留在最终QSS字符串中引发解析错误，需在load_qss末尾添加完整性校验；QPropertyAnimation的finished信号在动画被stop()中途停止后不会触发，依赖该信号的资源清理逻辑需改用QObject.destroyed信号或额外的手动清理调用
* [性能优化建议]：ThemeManager对QSS文件内容做内存缓存（_qss_cache字典），避免每次主题切换都重复磁盘IO读取文件；SizeManager在窗口尺寸未发生实质变化（差异<5px）时跳过所有计算和信号发射避免无效UI更新；LoadingIndicator在hideEvent中自动调用stop()停止QTimer避免组件隐藏后仍持续空转消耗CPU；面板切换时先隐藏旧面板再显示新面板减少同时渲染的组件数量
---