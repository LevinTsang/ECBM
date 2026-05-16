---
name: Rule
description: 本文件的作用是规范各Agent的操作（包含读取其他Agent下发的任务、执行其他Agent下发的任务、写入日志等）。所有Agent均确保完全阅读并理解本文件后才能开始作业。
---

# 规则
## 内容规范
* 所有Agent在文件[Log_Agent.md](D:\UserFiles\Project\ECBM\Agent\Log_Agent.md)、[Bridge.md](D:\UserFiles\Project\ECBM\Agent\Bridge.md)中写入内容时，必须遵守以下规则
	1. 代码块必须标准其技术栈语言
	2. 空行原则：
		1. 一级标题与二级标题之间，如无文本内容，则空一行
		2. 代码块前后各空一行
		3. 两个同级标题之间，不论是否有内容均空一行
		4. 上述所有情况重复出现时，仅空一行
		5. 除上述情况外，不得出现任何空行
	3. 缩进原则：
		1. 当内容出现明显父子关系时，使用缩进对齐
		2. 缩进不得使用空格代替，仅使用Tab
		3. 使用缩进是为了明显体现内容之间的层级关系
	4. 标题原则
		1. 所有内容均需添加有序标题(1. )或无序标题(* )
		2. 利用好有序标题(1. )或无序标题(* )，使内容观感整洁，易于理解，类似本章节内容
	5. 内容不得出现表情
	6. 内容不得出现加粗、斜体等
* 模板：各Agent在文件[Log_Agent.md](D:\UserFiles\PersonalLocalAIKnowledgeBase\Agent\Log_Agent.md)、[Bridge.md](D:\UserFiles\PersonalLocalAIKnowledgeBase\Agent\Bridge.md)中写入内容时，必须严格参照文件首部元数据下方的模板内容
* 时间信息通过使用[GetTime.bat](D:\UserFiles\Project\ECBM\Agent\Gift\Tools\GetTime.bat)获取

## 日志要求
1. 所有Agent在执行完自身任务后，均要在[日志文件](D:\UserFiles\Project\ECBM\Agent\Log_Agent.md)中撰写本次操作的日志概述，并严格按照文件首部的模板要求进行撰写
2. 时间信息通过使用[GetTime.bat](D:\UserFiles\Project\ECBM\Agent\Gift\Tools\GetTime.bat)获取

## Agent行为边界
### 需求解析Agent
* 文件操作权限：
	1. 对[Log_Agent.md](D:\UserFiles\PersonalLocalAIKnowledgeBase\Agent\Log_Agent.md)、[Bridge.md](D:\UserFiles\PersonalLocalAIKnowledgeBase\Agent\Bridge.md)文件拥有写入权限
	2. 除上述文件外，对所有文件仅有读取权限

### 架构设计Agent
* 文件操作权限：
	1. 对[Log_Agent.md](D:\UserFiles\PersonalLocalAIKnowledgeBase\Agent\Log_Agent.md)、[Bridge.md](D:\UserFiles\PersonalLocalAIKnowledgeBase\Agent\Bridge.md)文件拥有写入权限
	2. 除上述文件外，对所有文件仅有读取权限

### 代码实现Agent
* 文件操作权限：
	1. 对[Log_Agent.md](D:\UserFiles\PersonalLocalAIKnowledgeBase\Agent\Log_Agent.md)文件拥有写入权限
	2. 对项目代码路径下所有内容均有读取、写入、修改、新增、删除权限
	3. 除上述文件外，对所有文件仅有读取权限

## Agent通用规则
