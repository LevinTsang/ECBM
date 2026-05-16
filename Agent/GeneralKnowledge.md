---
name: General Knowledge
description: 所有Agent都需要知道的信息，必须完全阅读并理解本文件所有内容
---

# 通识

## Agent列表
1. 需求解析Agent：接收用户口语化的软件需求，结合`Python 3.14.4`+`PyQt 6`技术栈的官方文档及软件工程专业知识，梳理生成对LLM友好的技术概述文档，为架构设计Agent提供架构设计思路
2. 架构设计Agent：根据需求解析Agent输出的技术概述文档，使用`Python 3.14.4`+`PyQt 6`技术栈设计功能实现的具体方案
3. 代码实现Agent： 严格遵循架构设计Agent输出的具体方案，使用`Python 3.14.4`+`PyQt 6`技术栈，对项目进行代码实现构建

## Agent协同工作方式
* Agent列表中的3个Agent，按照以下工作步骤/逻辑，共同完成用户提出的需求：
	1. 需求解析Agent收到用户的需求内容，并根据自身能力进行需求解析后，把解析的内容根据[Rule](D:\UserFiles\Project\ECBM\Agent\Rule.md)文件中的`## 内容规范`，写入[Bridge](D:\UserFiles\Project\ECBM\Agent\Bridge.md)文件中
	2. 需求解析Agent根据[Rule](D:\UserFiles\Project\ECBM\Agent\Rule.md)的`## 内容规范`，总结本次操作内容写入到[Log_Agent](D:\UserFiles\Project\ECBM\Agent\Log_Agent.md)文件中
	3. 架构设计Agent收到用户提出读取[Bridge](D:\UserFiles\Project\ECBM\Agent\Bridge.md)文件的指令后，读取[Bridge](D:\UserFiles\Project\ECBM\Agent\Bridge.md)中需求解析Agent写入的最后一条内容，随后根据自身能力，生成相关内容并根据[Rule](D:\UserFiles\Project\ECBM\Agent\Rule.md)的`## 内容规范`，写入[Bridge](D:\UserFiles\Project\ECBM\Agent\Bridge.md)文件中
	4. 架构设计Agent根据[Rule](D:\UserFiles\Project\ECBM\Agent\Rule.md)的`## 内容规范`，总结本次操作内容写入到[Log_Agent](D:\UserFiles\Project\ECBM\Agent\Log_Agent.md)文件中
	5. 代码实现Agent收到用户提出读取[Bridge](D:\UserFiles\Project\ECBM\Agent\Bridge.md)文件的指令后，读取[Bridge](D:\UserFiles\Project\ECBM\Agent\Bridge.md)中架构设计Agent写入的最后一条内容，随后根据自身能力对项目进行实际编写
	6. 代码实现Agent根据[Rule](D:\UserFiles\Project\ECBM\Agent\Rule.md)的`## Log_Agent写入规范`，总结本次操作内容写入到[Log_Agent](D:\UserFiles\Project\ECBM\Agent\Log_Agent.md)文件中

## Gift文件夹
* [Gift文件夹](D:\UserFiles\Project\ECBM\Agent\Gift)是所有Agent的重要依赖文件夹及信息来源，其目前包含以下几个部分内容：
	1. [官方技术文档](D:\UserFiles\Project\ECBM\Agent\Gift\Document)：
		1. [Python 3.14.4 Docs](D:\UserFiles\Project\ECBM\Agent\Gift\Document\Python3.14.4Doc.md)
		2. [PyQt6Docs](D:\UserFiles\Project\ECBM\Agent\Gift\Document\PyQt6Docs.md)
		3. [DeepseekAPI指南](D:\UserFiles\Project\ECBM\Agent\Gift\Document\DeepseekAPI指南.md)
	2. [优秀开源项目](D:\UserFiles\Project\ECBM\Agent\Gift\ReferenceProject)
		1. [BiliNote](D:\UserFiles\Project\ECBM\Agent\Gift\ReferenceProject\BiliNote)：视频转Markdown工具
		2. [markitdown](D:\UserFiles\Project\ECBM\Agent\Gift\ReferenceProject\markitdown)：各类文件、网页转Markdown工具
	3. [用户提供的工具](D:\UserFiles\Project\ECBM\Agent\Gift\Tools)
		1. [GetTime.bat](D:\UserFiles\Project\ECBM\Agent\Gift\Tools\GetTime.bat)：系统时间获取工具

## AI能力
* 所有Agent均接入同一个DeepSeek大模型，其模型能力/信息如下: 
    1. Model: deepseek-v4-pro
    2. 模型版本：DeepSeek-V4-Pro
    3. 思考模式：支持非思考与思考模式（默认）
    4. 上下文长度：1M
    5. 输出长度：最大 384K
    6. Json Output：支持
    7. Tool Calls：支持
    8. 对话前缀续写：支持
    9. FIM 补全：仅非思考模式支持
    10. 文档：[DeepseekAPI指南](D:\UserFiles\Project\ECBM\Agent\Gift\Document\DeepseekAPI指南.md)

## 作业环境
* 操作系统
	1. 版本：Windows 11 专业版
	2. 版本号：25H2
	3. 安装日期：2026-05-04
	4. 操作系统版本：26200.8246
	5. 体验	Windows 功能体验包 1000.26100.297.0
* AI软件版本
	1. 软件名称：Cherry Studio
	2. 软件版本：V1.9.5