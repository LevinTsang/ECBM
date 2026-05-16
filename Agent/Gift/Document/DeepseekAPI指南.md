# 首次调用 API | DeepSeek API Docs
* 源 URL: https://api-docs.deepseek.com/zh-cn/
* 生成日期: 2026-05-16 15:09
* 页面数: 17

---

## 目录
* [首次调用 API | DeepSeek API Docs](#首次调用-api--deepseek-api-docs)
	* [Token 用量计算](#token-用量计算)
	* [限速](#限速)
	* [错误码](#错误码)
	* [接入 Agent 工具](#接入-agent-工具)
* [API 指南](#api-指南)
	* [多轮对话](#多轮对话)
	* [对话前缀续写（Beta）](#对话前缀续写beta)
	* [FIM 补全（Beta）](#fim-补全beta)
	* [JSON Output](#json-output)
	* [Tool Calls](#tool-calls)
	* [上下文硬盘缓存](#上下文硬盘缓存)
	* [Anthropic API](#anthropic-api)
* [API 文档](#api-文档)
* [新闻](#新闻)
* [常见问题](#常见问题)
* [更新日志](#更新日志)

---

# 首次调用 API
* DeepSeek API 使用与 OpenAI/Anthropic 兼容的 API 格式，通过修改配置，您可以使用 OpenAI/Anthropic SDK 来访问 DeepSeek API，或使用与 OpenAI/Anthropic API 兼容的软件。

| PARAM | VALUE |
| --- | --- |
| base\_url (OpenAI) | `https://api.deepseek.com` |
| base\_url (Anthropic) | `https://api.deepseek.com/anthropic` |
| api\_key | apply for an [API key](https://platform.deepseek.com/api_keys) |
| model\* | `deepseek-v4-flash` `deepseek-v4-pro` `deepseek-chat` (将于 2026/07/24 弃用) `deepseek-reasoner` (将于 2026/07/24 弃用) |
* \* deepseek-chat 与 deepseek-reasoner 两个模型名将于 2026/07/24 弃用。出于兼容考虑，二者分别对应 deepseek-v4-flash 的非思考与思考模式。

## 接入 Agent 工具[​](#接入-agent-工具 "接入 Agent 工具的直接链接")
* DeepSeek API 已接入多种主流 AI Agent 与编程助手工具。如果你使用 Claude Code、GitHub Copilot、OpenCode 等工具，可以直接将 DeepSeek 作为后端模型，无需编写代码即可开始使用。
* 详见 [Agent 工具接入指南](#接入-agent-工具)。

## 调用对话 API[​](#调用对话-api "调用对话 API的直接链接")
* 在创建 API key 之后，你可以使用以下样例脚本，通过 OpenAI API 格式来访问 DeepSeek 模型。样例为非流式输出，您可以将 stream 设置为 true 来使用流式输出。
* Anthropic API 格式的访问样例，请参考[Anthropic API](#anthropic-api)。
* curl
* python
* nodejs

```bash
curl https://api.deepseek.com/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${DEEPSEEK_API_KEY}" \
  -d '{
        "model": "deepseek-v4-pro",
        "messages": [
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": "Hello!"}
        ],
        "thinking": {"type": "enabled"},
        "reasoning_effort": "high",
        "stream": false
      }'
```

```python
# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}}
)

print(response.choices[0].message.content)
```

```python
// Please install OpenAI SDK first: `npm install openai`

import OpenAI from "openai";

const openai = new OpenAI({
        baseURL: 'https://api.deepseek.com',
        apiKey: process.env.DEEPSEEK_API_KEY,
});

async function main() {
  const completion = await openai.chat.completions.create({
    messages: [{ role: "system", content: "You are a helpful assistant." }],
    model: "deepseek-v4-pro",
    thinking: {"type": "enabled"},
    reasoning_effort: "high",
    stream: false,
  });

  console.log(completion.choices[0].message.content);
}

main();
```
* [接入 Agent 工具](#接入-agent-工具)
* [调用对话 API](#调用对话-api)

---

# Token 用量计算
* token 是模型用来表示自然语言文本的基本单位，也是我们的计费单元，可以直观的理解为“字”或“词”；通常 1 个中文词语、1 个英文单词、1 个数字或 1 个符号计为 1 个 token。

* 一般情况下模型中 token 和字数的换算比例大致如下：
* 1 个英文字符 ≈ 0.3 个 token。
* 1 个中文字符 ≈ 0.6 个 token。
* 但因为不同模型的分词不同，所以换算比例也存在差异，每一次实际处理 token 数量以模型返回为准，您可以从返回结果的 `usage` 中查看。

## 离线计算 Tokens 用量[​](#离线计算-tokens-用量 "离线计算 Tokens 用量的直接链接")
* 您可以通过如下压缩包中的代码来运行 tokenizer，以离线计算一段文本的 Token 用量。
* [deepseek\_tokenizer.zip](https://cdn.deepseek.com/api-docs/deepseek_v3_tokenizer.zip)
* [离线计算 Tokens 用量](#离线计算-tokens-用量)

---

# 限速
* DeepSeek API 会根据负载情况，动态限制用户并发量。当您到达并发上限时，会立即收到 HTTP 429 返回。
* 您的请求发出后，可能需要等待一段时间才能获取服务器的响应。在这段时间里，您的 HTTP 请求会保持连接，并持续收到如下格式的返回内容：
* 非流式请求：持续返回空行
* 流式请求：持续返回 SSE keep-alive 注释（`: keep-alive`）
* 这些内容不影响对响应的 JSON body 的解析。如果您在自己解析 HTTP 响应，请注意处理这些空行或注释。
* 如果 10 分钟后，请求仍未开始推理，服务器将关闭连接。

---

# 错误码
* 您在调用 DeepSeek API 时，可能会遇到以下错误。这里列出了相关错误的原因及其解决方法。

| 错误码 | 描述 |
| --- | --- |
| 400 - 格式错误 | 原因：请求体格式错误   解决方法：请根据错误信息提示修改请求体 |
| 401 - 认证失败 | 原因：API key 错误，认证失败   解决方法：请检查您的 API key 是否正确，如没有 API key，请先 [创建 API key](https://platform.deepseek.com/api_keys) |
| 402 - 余额不足 | 原因：账号余额不足   解决方法：请确认账户余额，并前往 [充值](https://platform.deepseek.com//top_up) 页面进行充值 |
| 422 - 参数错误 | 原因：请求体参数错误   解决方法：请根据错误信息提示修改相关参数 |
| 429 - 请求速率达到上限 | 原因：请求速率（TPM 或 RPM）达到上限   解决方法：请合理规划您的请求速率。 |
| 500 - 服务器故障 | 原因：服务器内部故障   解决方法：请等待后重试。若问题一直存在，请联系我们解决 |
| 503 - 服务器繁忙 | 原因：服务器负载过高   解决方法：请稍后重试您的请求 |

---

# 接入 Claude Code
* Claude Code 是一个运行在终端内的 AI 编程助手。

## 从现有安装中迁移到 DeepSeek[​](#从现有安装中迁移到-deepseek "从现有安装中迁移到 DeepSeek的直接链接")
* 如果你已经安装了 Claude Code，只需修改以下环境变量，其中 API Key 在 获取。
* Linux / Mac 用户，直接在终端中执行：

```bash
export ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropic
export ANTHROPIC_AUTH_TOKEN=<你的 DeepSeek API Key>
export ANTHROPIC_MODEL=deepseek-v4-pro[1m]
export ANTHROPIC_DEFAULT_OPUS_MODEL=deepseek-v4-pro[1m]
export ANTHROPIC_DEFAULT_SONNET_MODEL=deepseek-v4-pro[1m]
export ANTHROPIC_DEFAULT_HAIKU_MODEL=deepseek-v4-flash
export CLAUDE_CODE_SUBAGENT_MODEL=deepseek-v4-flash
export CLAUDE_CODE_EFFORT_LEVEL=max
```
* Windows 用户，在 Powershell 中执行：

```bash
$env:ANTHROPIC_BASE_URL="https://api.deepseek.com/anthropic"
$env:ANTHROPIC_AUTH_TOKEN="<你的 DeepSeek API Key>"
$env:ANTHROPIC_MODEL="deepseek-v4-pro[1m]"
$env:ANTHROPIC_DEFAULT_OPUS_MODEL="deepseek-v4-pro[1m]"
$env:ANTHROPIC_DEFAULT_SONNET_MODEL="deepseek-v4-pro[1m]"
$env:ANTHROPIC_DEFAULT_HAIKU_MODEL="deepseek-v4-flash"
$env:CLAUDE_CODE_SUBAGENT_MODEL="deepseek-v4-flash"
$env:CLAUDE_CODE_EFFORT_LEVEL="max"
```
* 配置完成后，执行（其中 `/path/to/my-project` 替换为你的项目路径）：

```bash
cd /path/to/my-project
claude
```

## 从零安装 Claude Code[​](#从零安装-claude-code "从零安装 Claude Code的直接链接")
### 1. 安装 Claude Code[​](#1-安装-claude-code "1. 安装 Claude Code的直接链接")
* 安装 [Node.js](https://nodejs.org/zh-cn/download/) 18+。
* Windows 用户需安装 [Git for Windows](https://git-scm.com/download/win)。
* 在命令行界面，执行以下命令安装 Claude Code：

```bash
npm install -g @anthropic-ai/claude-code
```
* 安装结束后，执行以下命令，若显示版本号则安装成功：

```
claude --version
```
### 2. 配置环境变量[​](#2-配置环境变量 "2. 配置环境变量的直接链接")
* Linux / Mac 用户执行以下命令配置 [DeepSeek Anthropic API](https://api.deepseek.com/anthropic) 环境变量，其中 API Key 在 获取：

```bash
export ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropic
export ANTHROPIC_AUTH_TOKEN=<你的 DeepSeek API Key>
export ANTHROPIC_MODEL=deepseek-v4-pro[1m]
export ANTHROPIC_DEFAULT_OPUS_MODEL=deepseek-v4-pro[1m]
export ANTHROPIC_DEFAULT_SONNET_MODEL=deepseek-v4-pro[1m]
export ANTHROPIC_DEFAULT_HAIKU_MODEL=deepseek-v4-flash
export CLAUDE_CODE_SUBAGENT_MODEL=deepseek-v4-flash
export CLAUDE_CODE_EFFORT_LEVEL=max
```
* Windows 用户执行：

```bash
$env:ANTHROPIC_BASE_URL="https://api.deepseek.com/anthropic"
$env:ANTHROPIC_AUTH_TOKEN="<你的 DeepSeek API Key>"
$env:ANTHROPIC_MODEL="deepseek-v4-pro[1m]"
$env:ANTHROPIC_DEFAULT_OPUS_MODEL="deepseek-v4-pro[1m]"
$env:ANTHROPIC_DEFAULT_SONNET_MODEL="deepseek-v4-pro[1m]"
$env:ANTHROPIC_DEFAULT_HAIKU_MODEL="deepseek-v4-flash"
$env:CLAUDE_CODE_SUBAGENT_MODEL="deepseek-v4-flash"
$env:CLAUDE_CODE_EFFORT_LEVEL="max"
```
### 3. 进入项目目录，执行 `claude` 命令，即可开始使用了。[​](#3-进入项目目录执行-claude-命令即可开始使用了 "3-进入项目目录执行-claude-命令即可开始使用了的直接链接")

```bash
cd /path/to/my-project
claude
```
* [从现有安装中迁移到 DeepSeek](#从现有安装中迁移到-deepseek)
* [从零安装 Claude Code](#从零安装-claude-code)

---

# API 指南 {#api-指南}

# 思考模式
* DeepSeek 模型支持思考模式：在输出最终回答之前，模型会先输出一段思维链内容，以提升最终答案的准确性。

## 思考模式开关与思考强度控制[​](#思考模式开关与思考强度控制 "思考模式开关与思考强度控制的直接链接")

|  |  |  |
| --- | --- | --- |
|  | 控制参数（OpenAI 格式） | 控制参数（Anthropic 格式） |
| 思考模式开关(1) | `{"thinking": {"type": "enabled/disabled"}}` | |
| 思考强度控制(2)(3) | `{"reasoning_effort": "high/max"}` | `{"output_config": {"effort": "high/max"}}` |
* (1) 默认思考开关为 `enabled`
* (2) 思考模式下，对普通请求，默认 effort 为 high；对一些复杂 Agent 类请求（如 Claude Code、OpenCode），effort 自动设置为 `max`
* (3) 思考模式下，出于兼容考虑 `low`、`medium` 会映射为 `high`, `xhigh` 会映射为 `max`
* 您在使用 OpenAI SDK 设置 `thinking` 参数时，需要将 `thinking` 参数传入 `extra_body` 中：

```python
response = client.chat.completions.create(
  model="deepseek-v4-pro",
  # ...
  reasoning_effort="high",
  extra_body={"thinking": {"type": "enabled"}}
)
```

## 输入输出参数[​](#输入输出参数 "输入输出参数的直接链接")
* 思考模式不支持 `temperature`、`top_p`、`presence_penalty`、`frequency_penalty` 参数。请注意，为了兼容已有软件，设置参数不会报错，但也不会生效。
* 在思考模式下，思维链内容通过 `reasoning_content` 参数返回，与 `content` 同级。在后续的轮次的拼接中，可以选择性地返回 `reasoning_content` 给 API：
* 在两个 `user` 消息之间，如果模型未进行工具调用，则中间 `assistant` 的 `reasoning_content` 无需参与上下文拼接，在后续轮次中将其传入 API 会被忽略。详见[多轮对话拼接](#%E5%A4%9A%E8%BD%AE%E5%AF%B9%E8%AF%9D%E6%8B%BC%E6%8E%A5)。
* 在两个 `user` 消息之间，如果模型进行了工具调用，则中间 `assistant` 的 `reasoning_content` 需参与上下文拼接，在后续所有 user 交互轮次中必须回传给 API。详见[工具调用](#%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8)。

## 多轮对话拼接[​](#多轮对话拼接 "多轮对话拼接的直接链接")
* 在每一轮对话过程中，模型会输出思维链内容（`reasoning_content`）和最终回答（`content`）。如果没有工具调用，则在下一轮对话中，之前轮输出的思维链内容不会被拼接到上下文中，如下图所示：

![](/zh-cn/img/deepseek_r1_multiround_example_cn.jpeg)

### 样例代码[​](#样例代码 "样例代码的直接链接")
* 下面的代码以 Python 语言为例，展示了如何访问思维链和最终回答，以及如何在多轮对话中进行上下文拼接。
* 非流式
* 流式

```python
from openai import OpenAI
client = OpenAI(api_key="<DeepSeek API Key>", base_url="https://api.deepseek.com")

# Turn 1
messages = [{"role": "user", "content": "9.11 and 9.8, which is greater?"}]
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=messages,
    reasoning_effort="high"
    extra_body={"thinking": {"type": "enabled"}},
)

reasoning_content = response.choices[0].message.reasoning_content
content = response.choices[0].message.content

# Turn 2

# The reasoning_content will be ignored by the API
messages.append(response.choices[0].message)
messages.append({'role': 'user', 'content': "How many Rs are there in the word 'strawberry'?"})
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=messages,
    reasoning_effort="high"
    extra_body={"thinking": {"type": "enabled"}},
)
# ...
```

```python
from openai import OpenAI
client = OpenAI(api_key="<DeepSeek API Key>", base_url="https://api.deepseek.com")

# Turn 1
messages = [{"role": "user", "content": "9.11 and 9.8, which is greater?"}]
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=messages,
    stream=True,
    reasoning_effort="high"
    extra_body={"thinking": {"type": "enabled"}},
)

reasoning_content = ""
content = ""

for chunk in response:
    if chunk.choices[0].delta.reasoning_content:
        reasoning_content += chunk.choices[0].delta.reasoning_content
    else:
        content += chunk.choices[0].delta.content

# Turn 2

# The reasoning_content will be ignored by the API
messages.append({"role": "assistant", "reasoning_content": reasoning_content, "content": content})
messages.append({'role': 'user', 'content': "How many Rs are there in the word 'strawberry'?"})
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=messages,
    stream=True,
    reasoning_effort="high"
    extra_body={"thinking": {"type": "enabled"}},
)
# ...

```

## 工具调用[​](#工具调用 "工具调用的直接链接")
* DeepSeek 模型的思考模式支持工具调用功能。模型在输出最终答案之前，可以进行多轮的思考与工具调用，以提升答案的质量。其调用模式如下图所示：

![](/zh-cn/img/thinking_with_tools.jpg)
* 请注意，区别于思考模式下的未进行工具调用的轮次，进行了工具调用的轮次，在后续所有请求中，必须完整回传 `reasoning_content` 给 API。
* 若您的代码中未正确回传 `reasoning_content`，API 会返回 400 报错。正确回传方法请您参考下面的样例代码。

### 样例代码[​](#样例代码-1 "样例代码的直接链接")

下面是一个简单的在思考模式下进行工具调用的样例代码：

```python
import os
import json
from openai import OpenAI
from datetime import datetime

# The definition of the tools
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_date",
            "description": "Get the current date",
            "parameters": { "type": "object", "properties": {} },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather of a location, the user should supply the location and date.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": { "type": "string", "description": "The city name" },
                    "date": { "type": "string", "description": "The date in format YYYY-mm-dd" },
                },
                "required": ["location", "date"]
            },
        }
    },
]

# The mocked version of the tool calls
def get_date_mock():
    return datetime.now().strftime("%Y-%m-%d")

def get_weather_mock(location, date):
    return "Cloudy 7~13°C"

TOOL_CALL_MAP = {
    "get_date": get_date_mock,
    "get_weather": get_weather_mock
}

def run_turn(turn, messages):
    sub_turn = 1
    while True:
        response = client.chat.completions.create(
            model='deepseek-v4-pro',
            messages=messages,
            tools=tools,
            reasoning_effort="high",
            extra_body={ "thinking": { "type": "enabled" } },
        )
        messages.append(response.choices[0].message)
        reasoning_content = response.choices[0].message.reasoning_content
        content = response.choices[0].message.content
        tool_calls = response.choices[0].message.tool_calls
        print(f"Turn {turn}.{sub_turn}\n{reasoning_content=}\n{content=}\n{tool_calls=}")
        # If there is no tool calls, then the model should get a final answer and we need to stop the loop
        if tool_calls is None:
            break
        for tool in tool_calls:
            tool_function = TOOL_CALL_MAP[tool.function.name]
            tool_result = tool_function(**json.loads(tool.function.arguments))
            print(f"tool result for {tool.function.name}: {tool_result}\n")
            messages.append({
                "role": "tool",
                "tool_call_id": tool.id,
                "content": tool_result,
            })
        sub_turn += 1
    print()

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url=os.environ.get('DEEPSEEK_BASE_URL'),
)

# The user starts a question
turn = 1
messages = [{
    "role": "user",
    "content": "How's the weather in Hangzhou Tomorrow"
}]
run_turn(turn, messages)

# The user starts a new question
turn = 2
messages.append({
    "role": "user",
    "content": "How's the weather in Guangzhou Tomorrow"
})
run_turn(turn, messages)

```

在 Turn 1 的每个子请求中，都携带了该 Turn 下产生的 `reasoning_content` 给 API，从而让模型继续之前的思考。`response.choices[0].message` 携带了 `assistant` 消息的所有必要字段，包括 `content`、`reasoning_content`、`tool_calls`。简单起见，可以直接用如下代码将消息 append 到 messages 结尾：

```python
messages.append(response.choices[0].message)

```

这行代码等价于：

```python
messages.append({
    'role': 'assistant',
    'content': response.choices[0].message.content,
    'reasoning_content': response.choices[0].message.reasoning_content,
    'tool_calls': response.choices[0].message.tool_calls,
})

```

且在 Turn 2 的请求中，我们仍然携带着 Turn1 所产生的 `reasoning_content` 给 API。

该代码的样例输出如下：

```text
Turn 1.1
reasoning_content="The user is asking about the weather in Hangzhou tomorrow. I need to get tomorrow's date first, then call the weather function."
content="Let me check tomorrow's weather in Hangzhou for you. First, let me get tomorrow's date."
tool_calls=[ChatCompletionMessageFunctionToolCall(id='call_00_kw66qNnNto11bSfJVIdlV5Oo', function=Function(arguments='{}', name='get_date'), type='function', index=0)]
tool result for get_date: 2026-04-19

Turn 1.2
reasoning_content="Today is 2026-04-19, so tomorrow is 2026-04-20. Now I'll call the weather function for Hangzhou."
content=''
tool_calls=[ChatCompletionMessageFunctionToolCall(id='call_00_H2SCW6136vWJGq9SQlBuhVt4', function=Function(arguments='{"location": "Hangzhou", "date": "2026-04-20"}', name='get_weather'), type='function', index=0)]
tool result for get_weather: Cloudy 7~13°C

Turn 1.3
reasoning_content='The weather result is in. Let me share this with the user.'
content="Here's the weather forecast for **Hangzhou tomorrow (April 20, 2026)**:\n\n- 🌤 **Condition:** Cloudy  \n- 🌡 **Temperature:** 7°C ~ 13°C (45°F ~ 55°F)\n\nIt'll be on the cooler side, so you might want to bring a light jacket if you're heading out! Let me know if you need anything else."
tool_calls=None

Turn 2.1
reasoning_content='The user is asking about the weather in Guangzhou tomorrow. Today is 2026-04-19, so tomorrow is 2026-04-20. I can directly call the weather function.'
content=''
tool_calls=[ChatCompletionMessageFunctionToolCall(id='call_00_8URkLt5NjmNkVKhDmMcNq9Mo', function=Function(arguments='{"location": "Guangzhou", "date": "2026-04-20"}', name='get_weather'), type='function', index=0)]
tool result for get_weather: Cloudy 7~13°C

Turn 2.2
reasoning_content='The weather result for Guangzhou is the same as Hangzhou. Let me share this with the user.'
content="Here's the weather forecast for **Guangzhou tomorrow (April 20, 2026)**:\n\n- 🌤 **Condition:** Cloudy  \n- 🌡 **Temperature:** 7°C ~ 13°C (45°F ~ 55°F)\n\nIt'll be cool and cloudy, so a light jacket would be a good idea if you're going out. Let me know if there's anything else you'd like to know!"
tool_calls=None

```

---

# 多轮对话
* 本指南将介绍如何使用 DeepSeek `/chat/completions` API 进行多轮对话。
* DeepSeek `/chat/completions` API 是一个“无状态” API，即服务端不记录用户请求的上下文，用户在每次请求时，需将之前所有对话历史拼接好后，传递给对话 API。

* 下面的代码以 Python 语言，展示了如何进行上下文拼接，以实现多轮对话。

```python
from openai import OpenAI
client = OpenAI(api_key="<DeepSeek API Key>", base_url="https://api.deepseek.com")

# Round 1
messages = [{"role": "user", "content": "What's the highest mountain in the world?"}]
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=messages
)

messages.append(response.choices[0].message)
print(f"Messages Round 1: {messages}")

# Round 2
messages.append({"role": "user", "content": "What is the second?"})
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=messages
)

messages.append(response.choices[0].message)
print(f"Messages Round 2: {messages}")
```
* 在第一轮请求时，传递给 API 的 `messages` 为：

```
[
    {"role": "user", "content": "What's the highest mountain in the world?"}
]
```
* 在第二轮请求时：
* 1. 要将第一轮中模型的输出添加到 `messages` 末尾
* 2. 将新的提问添加到 `messages` 末尾
* 最终传递给 API 的 `messages` 为：

```
[
    {"role": "user", "content": "What's the highest mountain in the world?"},
    {"role": "assistant", "content": "The highest mountain in the world is Mount Everest."},
    {"role": "user", "content": "What is the second?"}
]
```

---

# 对话前缀续写（Beta）
* 对话前缀续写沿用 [Chat Completion API](/zh-cn/api/create-chat-completion)，用户提供 assistant 开头的消息，来让模型补全其余的消息。

## 注意事项[​](#注意事项 "注意事项的直接链接")
* 1. 使用对话前缀续写时，用户需确保 `messages` 列表里最后一条消息的 `role` 为 `assistant`，并设置最后一条消息的 `prefix` 参数为 `True`。
* 2. 用户需要设置 `base_url="https://api.deepseek.com/beta"` 来开启 Beta 功能。

## 样例代码[​](#样例代码 "样例代码的直接链接")
* 下面给出了对话前缀续写的完整 Python 代码样例。在这个例子中，我们设置 `assistant` 开头的消息为 ```` "```python\n" ```` 来强制模型输出 python 代码，并设置 `stop` 参数为 ```` ['```'] ```` 来避免模型的额外解释。

```python
from openai import OpenAI

client = OpenAI(
    api_key="<your api key>",
    base_url="https://api.deepseek.com/beta",
)

messages = [
    {"role": "user", "content": "Please write quick sort code"},
    {"role": "assistant", "content": "```python\n", "prefix": True}
]
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=messages,
    stop=["```"],
)
print(response.choices[0].message.content)
```

---

# FIM 补全（Beta）
* 在 [FIM (Fill In the Middle) 补全](/zh-cn/api/create-completion)中，用户可以提供前缀和后缀（可选），模型来补全中间的内容。FIM 常用于内容续写、代码补全等场景。

## 注意事项[​](#注意事项 "注意事项的直接链接")
* 1. 模型的最大补全长度为 4K。
* 2. 用户需要设置 `base_url="https://api.deepseek.com/beta"` 来开启 Beta 功能。

## 样例代码[​](#样例代码 "样例代码的直接链接")
* 下面给出了 FIM 补全的完整 Python 代码样例。在这个例子中，我们给出了计算斐波那契数列函数的开头和结尾，来让模型补全中间的内容。

```python
from openai import OpenAI

client = OpenAI(
    api_key="<your api key>",
    base_url="https://api.deepseek.com/beta",
)

response = client.completions.create(
    model="deepseek-v4-pro",
    prompt="def fib(a):",
    suffix="    return fib(a-1) + fib(a-2)",
    max_tokens=128
)
print(response.choices[0].text)
```

## 配置 Continue 代码补全插件[​](#配置-continue-代码补全插件 "配置 Continue 代码补全插件的直接链接")
* [Continue](https://continue.dev) 是一款支持代码补全的 VSCode 插件，您可以参考[这篇文档](https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/continue/README_cn.md)来配置 Continue 以使用代码补全功能。

---

# JSON Output
* 在很多场景下，用户需要让模型严格按照 JSON 格式来输出，以实现输出的结构化，便于后续逻辑进行解析。
* DeepSeek 提供了 JSON Output 功能，来确保模型输出合法的 JSON 字符串。

## 注意事项[​](#注意事项 "注意事项的直接链接")
* 1. 设置 `response_format` 参数为 `{'type': 'json_object'}`。
* 2. 用户传入的 system 或 user prompt 中必须含有 `json` 字样，并给出希望模型输出的 JSON 格式的样例，以指导模型来输出合法 JSON。
* 3. 需要合理设置 `max_tokens` 参数，防止 JSON 字符串被中途截断。
* 4. 在使用 JSON Output 功能时，API 有概率会返回空的 content。我们正在积极优化该问题，您可以尝试修改 prompt 以缓解此类问题。

## 样例代码[​](#样例代码 "样例代码的直接链接")
* 这里展示了使用 JSON Output 功能的完整 Python 代码：

```python
import json
from openai import OpenAI

client = OpenAI(
    api_key="<your api key>",
    base_url="https://api.deepseek.com",
)

system_prompt = """
The user will provide some exam text. Please parse the "question" and "answer" and output them in JSON format.

EXAMPLE INPUT:
Which is the highest mountain in the world? Mount Everest.

EXAMPLE JSON OUTPUT:
{
    "question": "Which is the highest mountain in the world?",
    "answer": "Mount Everest"
}
"""

user_prompt = "Which is the longest river in the world? The Nile River."

messages = [{"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}]

response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=messages,
    response_format={
        'type': 'json_object'
    }
)

print(json.loads(response.choices[0].message.content))
```
* 模型将会输出：

```json
{
    "question": "Which is the longest river in the world?",
    "answer": "The Nile River"
}
```

---

# Tool Calls
* Tool Calls 让模型能够调用外部工具，来增强自身能力。

## 非思考模式[​](#非思考模式 "非思考模式的直接链接")
### 样例代码[​](#样例代码 "样例代码的直接链接")
* 这里以获取用户当前位置的天气信息为例，展示了使用 Tool Calls 的完整 Python 代码。
* Tool Calls 的具体 API 格式请参考[对话补全](/zh-cn/api/create-chat-completion/)文档。

```python
from openai import OpenAI

def send_messages(messages):
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=messages,
        tools=tools
    )
    return response.choices[0].message

client = OpenAI(
    api_key="<your api key>",
    base_url="https://api.deepseek.com",
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather of a location, the user should supply a location first.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    }
                },
                "required": ["location"]
            },
        }
    },
]

messages = [{"role": "user", "content": "How's the weather in Hangzhou, Zhejiang?"}]
message = send_messages(messages)
print(f"User>\t {messages[0]['content']}")

tool = message.tool_calls[0]
messages.append(message)

messages.append({"role": "tool", "tool_call_id": tool.id, "content": "24℃"})
message = send_messages(messages)
print(f"Model>\t {message.content}")
```
* 这个例子的执行流程如下：
* 1. 用户：询问现在的天气
* 2. 模型：返回 function `get_weather({location: 'Hangzhou'})`
* 3. 用户：调用 function `get_weather({location: 'Hangzhou'})`，并传给模型。
* 4. 模型：返回自然语言，"The current temperature in Hangzhou is 24°C."
* 注：上述代码中 `get_weather` 函数功能需由用户提供，模型本身不执行具体函数。

---

## 思考模式[​](#思考模式 "思考模式的直接链接")
* 从 DeepSeek-V3.2 开始，API 支持了思考模式下的工具调用能力，详见[思考模式](/zh-cn/guides/thinking_mode#%E5%B7%A5%E5%85%B7%E8%B0%83%E7%94%A8)。

---

## `strict` 模式（Beta）[​](#strict-模式beta "strict-模式beta的直接链接")
* 在 `strict` 模式下，模型在输出 Function 调用时会严格遵循 Function 的 JSON Schema 的格式要求，以确保模型输出的 Function 符合用户的定义。在思考与非思考模式下的工具调用，均可使用 `strict` 模式。
* 要使用 `strict` 模式，需要：
* 1. 用户需要设置 `base_url="https://api.deepseek.com/beta"` 来开启 Beta 功能
* 2. 在传入的 `tools` 列表中，所有 `function` 均需设置 `strict` 属性为 `true`
* 3. 服务端会对用户传入的 Function 的 JSON Schema 进行校验，如不符合规范，或遇到服务端不支持的 JSON Schema 类型，将返回错误信息

以下是 `strict` 模式下 tool 的定义样例：

```json
{
    "type": "function",
    "function": {
        "name": "get_weather",
        "strict": true,
        "description": "Get weather of a location, the user should supply a location first.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, CA",
                }
            },
            "required": ["location"],
            "additionalProperties": false
        }
    }
}

```

---

### `strict` 模式支持的 JSON Schema 类型[​](#strict-模式支持的-json-schema-类型 "strict-模式支持的-json-schema-类型的直接链接")
* object
* string
* number
* integer
* boolean
* array
* enum
* anyOf

#### object 类型[​](#object-类型 "object 类型的直接链接")
* object 定义一个包含键值对的深层结构，其中 properties 定义了对象中每个键（属性）的 schema。**每个 `object` 的所有属性均需设置为 `required`，且 `object` 中 `additionalProperties` 属性必须为 `false`**。
* 示例：

```json
{
    "type": "object",
    "properties": {
        "name": { "type": "string" },
        "age": { "type": "integer" }
    },
    "required": ["name", "age"],
    "additionalProperties": false
}
```

#### string 类型[​](#string-类型 "string 类型的直接链接")
* 支持的参数：
	+ pattern：使用正则表达式来约束字符串的格式
	+ format：使用预定义的常见格式进行校验，目前支持：
		- email：电子邮件地址
		- hostname：主机名
		- ipv4：IPv4 地址
		- ipv6：IPv6 地址
		- uuid：uuid
* 不支持的参数
	+ minLength
	+ maxLength
* 示例：

```json
{
    "type": "object",
    "properties": {
        "user_email": {
            "type": "string",
            "description": "The user's email address",
            "format": "email"
        },
        "zip_code": {
            "type": "string",
            "description": "Six digit postal code",
            "pattern": "^\\d{6}$"
        }
    }
}
```

#### number/integer 类型[​](#numberinteger-类型 "number/integer 类型的直接链接")
* 支持的参数
	+ const：固定数字为常数
	+ default：数字的默认值
	+ minimum：最小值
	+ maximum：最大值
	+ exclusiveMinimum：不小于
	+ exclusiveMaximum：不大于
	+ multipleOf：数字输出为这个值的倍数
* 示例：

```json
{
    "type": "object",
    "properties": {
        "score": {
            "type": "integer",
            "description": "A number from 1-5, which represents your rating, the higher, the better",
            "minimum": 1,
            "maximum": 5
        }
    },
    "required": ["score"],
    "additionalProperties": false
}
```

---

#### array 类型[​](#array-类型 "array 类型的直接链接")
* 不支持的参数
	+ minItems
	+ maxItems
* 示例：

```json
{
    "type": "object",
    "properties": {
        "keywords": {
            "type": "array",
            "description": "Five keywords of the article, sorted by importance",
            "items": {
                "type": "string",
                "description": "A concise and accurate keyword or phrase."
            }
        }
    },
    "required": ["keywords"],
    "additionalProperties": false
}
```

#### enum[​](#enum "enum的直接链接")
* enum 可以确保输出是预期的几个选项之一，例如在订单状态的场景下，只能是有限几个状态之一。
* 样例：

```json
{
    "type": "object",
    "properties": {
        "order_status": {
            "type": "string",
            "description": "Ordering status",
            "enum": ["pending", "processing", "shipped", "cancelled"]
        }
    }
}
```

#### anyOf[​](#anyof "anyOf的直接链接")
* 匹配所提供的多个 schema 中的任意一个，可以处理可能具有多种有效格式的字段，例如用户的账户可能是邮箱或者手机号中的一个：

```json
{
    "type": "object",
    "properties": {
    "account": {
        "anyOf": [
            { "type": "string", "format": "email", "description": "可以是电子邮件地址" },
            { "type": "string", "pattern": "^\\d{11}$", "description": "或11位手机号码" }
        ]
    }
  }
}
```

#### $ref 和 $def[​](#ref-和-def "$ref 和 $def的直接链接")
* 可以使用 $def 定义模块，再用 $ref 引用以减少模式的重复和模块化，此外还可以单独使用 $ref 定义递归结构。

```json
{
    "type": "object",
    "properties": {
        "report_date": {
            "type": "string",
            "description": "The date when the report was published"
        },
        "authors": {
            "type": "array",
            "description": "The authors of the report",
            "items": {
                "$ref": "#/$def/author"
            }
        }
    },
    "required": ["report_date", "authors"],
    "additionalProperties": false,
    "$def": {
        "author": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "author's name"
                },
                "institution": {
                    "type": "string",
                    "description": "author's institution"
                },
                "email": {
                    "type": "string",
                    "format": "email",
                    "description": "author's email"
                }
            },
            "additionalProperties": false,
            "required": ["name", "institution", "email"]
        }
    }
}
```

---

# 上下文硬盘缓存
* DeepSeek API 上下文硬盘缓存技术对所有用户默认开启，用户无需修改代码即可享用。

* 用户的每一个请求都会触发硬盘缓存的构建。若后续请求与之前的请求在前缀上存在重复，则重复部分只需要从缓存中拉取，计入“缓存命中”。

## 缓存落盘与命中规则[​](#缓存落盘与命中规则 "缓存落盘与命中规则的直接链接")
* 缓存命中的前提是相应前缀已被“落盘”（写入硬盘缓存）。受 Sliding Window Attention 机制的影响，缓存前缀的存取与判别与之前有所不同。每条缓存前缀是一个独立的完整单元。后续请求只有在完整匹配缓存前缀单元时，才能命中缓存。

### 缓存前缀落盘时机：[​](#缓存前缀落盘时机 "缓存前缀落盘时机：的直接链接")
* 1. 请求结束位置落盘：每次请求的用户输入结束位置与模型输出结束位置，会产生两个缓存前缀单元。后续请求若完整匹配了它们，则可命中。
* 2. 公共前缀检测落盘：当系统检测到多次请求之间存在公共前缀时，会将该公共前缀作为一个独立的缓存前缀单元进行落盘。后续请求若完整复用了该缓存前缀单元，则可命中。
* 3. 按固定 token 间隔落盘：在长输入或长输出中，系统会以一定的 token 数量为间隔，截取缓存前缀单元，避免长前缀因迟迟未达到结束位置而完全无法被缓存。
* 举例 1：用户第一轮请求内容为 `A + B`，第二轮请求内容为 `A + B + C`，则第二轮请求能完整匹配 `A + B` 这个缓存前缀单元，可以命中 `A + B` 的缓存。详见下文例一。
* 举例 2：用户第一轮请求的内容为 `A + B`，第二轮请求的内容为 `A + C`，则第二轮请求无法命中缓存，因为 `A + C` 不能完整匹配第一轮的缓存前缀单元（`A + B`）。但此时系统会识别到两轮请求存在公共前缀 `A`，并将 `A` 作为缓存前缀单元落盘。当第三轮请求 `A + D` 到来时，能完整匹配 `A` 这个缓存前缀单元，可以命中 `A` 的缓存。详见下文例二。

### 例一：多轮对话[​](#例一多轮对话 "例一：多轮对话的直接链接")
* 第一次请求

```python
messages: [
    {"role": "system", "content": "你是一位乐于助人的助手"},
    {"role": "user", "content": "中国的首都是哪里？"}
]
```
* 第二次请求

```python
messages: [
    {"role": "system", "content": "你是一位乐于助人的助手"},
    {"role": "user", "content": "中国的首都是哪里？"},
    {"role": "assistant", "content": "中国的首都是北京。"},
    {"role": "user", "content": "美国的首都是哪里？"}
]
```
* 在上例中，第二次请求可以完整复用第一次请求的缓存前缀单元，这部分会计入“缓存命中”。

### 例二：长文本问答[​](#例二长文本问答 "例二：长文本问答的直接链接")
* 第一次请求

```python
messages: [
    {"role": "system", "content": "你是一位资深的财报分析师..."}
    {"role": "user", "content": "<财报内容>\n\n请总结一下这份财报的关键信息。"}
]
```
* 第二次请求

```python
messages: [
    {"role": "system", "content": "你是一位资深的财报分析师..."}
    {"role": "user", "content": "<财报内容>\n\n请分析一下这份财报的盈利情况。"}
]
```
* 第三次请求

```python
messages: [
    {"role": "system", "content": "你是一位资深的财报分析师..."}
    {"role": "user", "content": "<财报内容>\n\n请分析一下公司收入与支出占比。"}
]
```
* 在上例中，前两次请求不会命中缓存。前两次请求完成后，系统会识别出 `system` 消息 + `user` 消息中的<财报内容>为缓存前缀单元，并进行落盘。在第三次请求中，由于完整匹配了前面落盘的缓存前缀单元，则可命中缓存。

## 查看缓存命中情况[​](#查看缓存命中情况 "查看缓存命中情况的直接链接")
* 在 DeepSeek API 的返回中，我们在 `usage` 字段中增加了两个字段，来反映请求的缓存命中情况：
* 1. `prompt_cache_hit_tokens`：本次请求的输入中，缓存命中的 tokens 数
* 2. `prompt_cache_miss_tokens`：本次请求的输入中，缓存未命中的 tokens 数

## 硬盘缓存与输出随机性[​](#硬盘缓存与输出随机性 "硬盘缓存与输出随机性的直接链接")
* 硬盘缓存只匹配到用户输入的前缀部分，输出仍然是通过计算推理得到的，仍然受到 temperature 等参数的影响，从而引入随机性。其输出效果与不使用硬盘缓存相同。

## 其它说明[​](#其它说明 "其它说明的直接链接")
* 1. 缓存系统是“尽力而为”，不保证 100% 缓存命中
* 2. 缓存构建耗时为秒级。缓存不再使用后会自动被清空，时间一般为几个小时到几天

---

# Anthropic API
* 为了满足大家对 Anthropic API 生态的使用需求，我们的 API 新增了对 Anthropic API 格式的支持，其 `base_url` 为 `https://api.deepseek.com/anthropic`。
* 通过简单的配置，即可将 DeepSeek 的能力，接入到 Anthropic API 生态中。

## 将 DeepSeek 模型接入 Claude Code[​](#将-deepseek-模型接入-claude-code "将 DeepSeek 模型接入 Claude Code的直接链接")
* 请参考[接入 Agent 工具](/zh-cn/guides/coding_agents)

## 通过 Anthropic API 调用 DeepSeek 模型[​](#通过-anthropic-api-调用-deepseek-模型 "通过 Anthropic API 调用 DeepSeek 模型的直接链接")
* 1. 安装 Anthropic SDK

```bash
pip install anthropic
```
* 2. 配置环境变量

```bash
export ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropic
export ANTHROPIC_API_KEY=${YOUR_API_KEY}
```
* 3. 调用 API

```python
import anthropic

client = anthropic.Anthropic()

message = client.messages.create(
    model="deepseek-v4-pro",
    max_tokens=1000,
    system="You are a helpful assistant.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Hi, how are you?"
                }
            ]
        }
    ]
)
print(message.content)
```
* 注意：当您给 DeepSeek 的 Anthropic API 传入不支持的模型名时，API 后端会自动将其映射到 `deepseek-v4-flash` 模型。

## Anthropic API 兼容性细节[​](#anthropic-api-兼容性细节 "Anthropic API 兼容性细节的直接链接")

### HTTP Header[​](#http-header "HTTP Header的直接链接")

| Field | Support Status |
| --- | --- |
| anthropic-beta | Ignored |
| anthropic-version | Ignored |
| x-api-key | Fully Supported |

### Simple Fields[​](#simple-fields "Simple Fields的直接链接")

| Field | Support Status |
| --- | --- |
| model | Use DeepSeek Model Instead |
| max\_tokens | Fully Supported |
| container | Ignored |
| mcp\_servers | Ignored |
| metadata | Ignored |
| service\_tier | Ignored |
| stop\_sequences | Fully Supported |
| stream | Fully Supported |
| system | Fully Supported |
| temperature | Fully Supported (range [0.0 ~ 2.0]) |
| thinking | Supported (`budget_tokens` is ignored) |
| output\_config | Only `effort` is supported |
| top\_k | Ignored |
| top\_p | Fully Supported |

### Tool Fields[​](#tool-fields "Tool Fields的直接链接")

#### tools[​](#tools "tools的直接链接")

| Field | Support Status |
| --- | --- |
| name | Fully Supported |
| input\_schema | Fully Supported |
| description | Fully Supported |
| cache\_control | Ignored |

#### tool\_choice[​](#tool_choice "tool_choice的直接链接")

| Value | Support Status |
| --- | --- |
| none | Fully Supported |
| auto | Supported (`disable_parallel_tool_use` is ignored) |
| any | Supported (`disable_parallel_tool_use` is ignored) |
| tool | Supported (`disable_parallel_tool_use` is ignored) |

### Message Fields[​](#message-fields "Message Fields的直接链接")

| Field | Variant | Sub-Field | Support Status |
| --- | --- | --- | --- |
| content | string |  | Fully Supported |
| array, type="text" | text | Fully Supported |
| cache\_control | Ignored |
| citations | Ignored |
| array, type="image" |  | Not Supported |
| array, type = "document" |  | Not Supported |
| array, type = "search\_result" |  | Not Supported |
| array, type = "thinking" |  | Supported |
| array, type="redacted\_thinking" |  | Not Supported |
| array, type = "tool\_use" | id | Fully Supported |
| input | Fully Supported |
| name | Fully Supported |
| cache\_control | Ignored |
| array, type = "tool\_result" | tool\_use\_id | Fully Supported |
| content | Fully Supported |
| cache\_control | Ignored |
| is\_error | Ignored |
| array, type = "server\_tool\_use" |  | Not Supported |
| array, type = "web\_search\_tool\_result" |  | Not Supported |
| array, type = "code\_execution\_tool\_result" |  | Not Supported |
| array, type = "mcp\_tool\_use" |  | Not Supported |
| array, type = "mcp\_tool\_result" |  | Not Supported |
| array, type = "container\_upload" |  | Not Supported |

---

# API 文档 {#api-文档}
* Version: 1.0.0

# Deepseek API
* 使用 DeepSeek API 之前，请先 [创建 API 密钥](https://platform.deepseek.com/api_keys)。

## Authentication[​](#authentication "Authentication的直接链接")
* HTTP: Bearer Auth

|  |  |
| --- | --- |
| Security Scheme Type: | http |
| HTTP Authorization Scheme: | bearer |

### Contact
* DeepSeek 技术支持: api-service@deepseek.com

### Terms of Service
* [<https://cdn.deepseek.com/policies/zh-CN/deepseek-open-platform-terms-of-service.html>](https://cdn.deepseek.com/policies/zh-CN/deepseek-open-platform-terms-of-service.html)

### License
* [MIT](https://opensource.org/license/mit/)

---

# 新闻 {#新闻}

# DeepSeek-V4 预览版：迈入百万上下文普惠时代
* 今天，我们全新系列模型 DeepSeek-V4 的预览版本正式上线并同步开源。
* DeepSeek-V4 拥有百万字超长上下文，在 Agent 能力、世界知识和推理性能上均实现国内与开源领域的领先。模型按大小分为两个版本：

![](/zh-cn/img/v4-spec.png)

* 即日起登录官网 chat.deepseek.com 或官方App，即可与最新的 DeepSeek-V4 对话，探索 1M 超长上下文记忆的全新体验。API 服务已同步更新，通过修改 model\_name 为 deepseek-v4-pro 或 deepseek-v4-flash 即可调用。

---

## DeepSeek-V4-Pro：性能比肩顶级闭源模型[​](#deepseek-v4-pro性能比肩顶级闭源模型 "DeepSeek-V4-Pro：性能比肩顶级闭源模型的直接链接")

![](/zh-cn/img/v4-benchmark.png)

* Agent 能力大幅提高：相比前代模型，DeepSeek-V4-Pro 的 Agent 能力显著增强。在 Agentic Coding 评测中，V4-Pro 已达到当前开源模型最佳水平，并在其他 Agent 相关评测中同样表现优异。目前 DeepSeek-V4 已成为公司内部员工使用的 Agentic Coding 模型，据评测反馈使用体验优于 Sonnet 4.5，交付质量接近 Opus 4.6 非思考模式，但仍与 Opus 4.6 思考模式存在一定差距。
* 丰富的世界知识：DeepSeek-V4-Pro 在世界知识测评中，大幅领先其他开源模型，仅稍逊于顶尖闭源模型 Gemini-Pro-3.1。
* 世界顶级推理性能：在数学、STEM、竞赛型代码的测评中，DeepSeek-V4-Pro 超越当前所有已公开评测的开源模型，取得了比肩世界顶级闭源模型的优异成绩。

![](/zh-cn/img/v4-benchmark-2.png)

---

## DeepSeek-V4-Flash：更快捷高效的经济之选[​](#deepseek-v4-flash更快捷高效的经济之选 "DeepSeek-V4-Flash：更快捷高效的经济之选的直接链接")

* 相比 DeepSeek-V4-Pro，DeepSeek-V4-Flash 在世界知识储备方面稍逊一筹，但展现出了接近的推理能力。而由于模型参数和激活更小，相较之下 V4-Flash 能够提供更加快捷、经济的 API 服务。
* 在 Agent 测评中，DeepSeek-V4-Flash 在简单任务上与 DeepSeek-V4-Pro 旗鼓相当，但在高难度任务上仍有差距。

---

## 结构创新和超高上下文效率[​](#结构创新和超高上下文效率 "结构创新和超高上下文效率的直接链接")
* DeepSeek-V4 开创了一种全新的注意力机制，在 token 维度进行压缩，结合 DSA 稀疏注意力（DeepSeek Sparse Attention），实现了全球领先的长上下文能力，并且相比于传统方法大幅降低了对计算和显存的需求。从现在开始，1M（一百万）上下文将是 DeepSeek 所有官方服务的标配。

![](/zh-cn/img/v4-efficiency.png)

---

## Agent 能力专项优化[​](#agent-能力专项优化 "Agent 能力专项优化的直接链接")

DeepSeek-V4 针对 Claude Code 、OpenClaw、OpenCode、CodeBuddy 等主流的 Agent 产品进行了适配和优化，在代码任务、文档生成任务等方面表现均有提升。下图为 V4-Pro 在某 Agent 框架下生成的 PPT 内页示例：

![](/zh-cn/img/v4-ppt.png)

---

## API 访问[​](#api-访问 "API 访问的直接链接")
* 目前，DeepSeek API 已同步上线 V4-Pro 与 V4-Flash，支持 OpenAI ChatCompletions 接口与 Anthropic 接口。访问新模型时，base\_url 不变, model 参数需要改为 deepseek-v4-pro 或 deepseek-v4-flash。

![](/zh-cn/img/v4-price.png)

* V4-Pro 与 V4-Flash 最大上下文长度为 1M，均同时支持非思考模式与思考模式，其中思考模式支持 reasoning\_effort 参数设置思考强度（high/max）。对于复杂的 Agent 场景建议使用思考模式，并设置强度为 max。模型调用与参数调整方法请参考 [API 文档](#api-指南)。

请大家注意：旧有的 API 接口的两个模型名 deepseek-chat 与deepseek-reasoner 将于三个月后（2026-07-24）停止使用。当前阶段内，这两个模型名分别指向deepseek-v4-flash 的非思考模式与思考模式。

## 开源权重和本地部署[​](#开源权重和本地部署 "开源权重和本地部署的直接链接")

* DeepSeek-V4 模型开源链接：

<https://huggingface.co/collections/deepseek-ai/deepseek-v4>

<https://modelscope.cn/collections/deepseek-ai/DeepSeek-V4>

* DeepSeek-V4 技术报告：

<https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf>

---

# 常见问题 {#常见问题}
# 常见问题

## 账号问题[​](#账号问题 "账号问题的直接链接")
### 账号无法登录[​](#账号无法登录 "账号无法登录的直接链接")
* 如您在登录时，收到提示“你的账号已被临时停用”，该提示意味着账号因可能违反平台使用规范，触发了系统的停用规则。

若您对此存有异议，可以填写[「账号停用申诉」](https://trtgsjkv6r.feishu.cn/share/base/form/shrcn13OBmQ3oXJKYLdHjUfeDHh)表单与我们取得联系。我们将尽快郑重评估并认真审核您的申诉。大部分请求的审核用时为 3 个工作日，一旦通过，您将可以立即正常登录和使用。感谢您的耐心等待与理解！

### 邮箱无法注册[​](#邮箱无法注册 "邮箱无法注册的直接链接")

如果您在注册时，收到错误提示“注册失败，暂不支持该邮箱域名注册。”，您当前使用的邮箱域名暂不在支持列表中，建议使用Gmail、Outlook、Hotmail、Yahoo 等国际通用邮箱进行注册。

如仍有问题，请联系 service@deepseek.com。

### 注销账号[​](#注销账号 "注销账号的直接链接")

您可以通过以下路径申请注销账号：

[「个人信息」](https://platform.deepseek.com/profile)→「注销」。

重要提示：此注销操作，会连同该账号下的 chat 平台一同注销，所有对话记录将被永久清空。若您在开放平台账户中尚有未消费的余额，将被视为自愿放弃，请您谨慎操作。

---

## 实名认证及商务问题[​](#实名认证及商务问题 "实名认证及商务问题的直接链接")

### 个人实名认证与企业实名认证有什么区别？[​](#个人实名认证与企业实名认证有什么区别 "个人实名认证与企业实名认证有什么区别？的直接链接")

个人实名认证账号与企业实名认证账号在用户权益和产品功能上目前没有区别，但认证方式和所需材料有所不同。根据合规要求，请以您账号的实际使用情况进行认证。

### 个人认证账号可以更改为企业实名账号吗？[​](#个人认证账号可以更改为企业实名账号吗 "个人认证账号可以更改为企业实名账号吗？的直接链接")

可以，您可以通过以下路径变更认证：

[「充值」](https://platform.deepseek.com/top_up)页面 →「对公汇款」→「企业实名认证」→「去变更」。

变更不会影响账户余额和当前正常使用。

### 企业实名账号可以更改为个人账号吗？[​](#企业实名账号可以更改为个人账号吗 "企业实名账号可以更改为个人账号吗？的直接链接")

已完成企业实名认证的账号，其认证类型不可变更为个人认证或其他企业认证。

### 实名认证失败[​](#实名认证失败 "实名认证失败的直接链接")

认证失败常见原因如下：

* 该身份证号码已绑定其他平台账号。
* 身份证号连续输错次数较多，认证功能会被暂时锁定。

如需进一步协助，欢迎联系 service@deepseek.com。

### 是否支持签订合作协议[​](#是否支持签订合作协议 "是否支持签订合作协议的直接链接")

DeepSeek API 主要通过自助及标准化的方式提供服务，若确有线下合作协议签订需求，如应用程序备案或企业入库，您可填写[合作协议申请工单](https://trtgsjkv6r.feishu.cn/share/base/form/shrcn99HCMzQYKjO2r44fd3ACob)，提交相关信息，我们将协助您处理。

注：所提供的协议为标准化框架协议，暂不支持条款修改，如需查看请登录[「对公汇款」](https://platform.deepseek.com/top_up)页面下载参考模版。

### 是否有限速更高的套餐[​](#是否有限速更高的套餐 "是否有限速更高的套餐的直接链接")

目前我们实行统一的 API 收费标准，暂无分级套餐。具体价格详情请查阅 [API 价格页面](https://api-docs.deepseek.com/zh-cn/quick_start/pricing)。

---

## 财务问题[​](#财务问题 "财务问题的直接链接")

### 如何充值？[​](#如何充值 "如何充值？的直接链接")

* 在线充值：完成实名认证后，您可以在[「充值」](https://platform.deepseek.com/top_up)页面使用支付宝/微信进行在线充值。您可以在[「账单」](https://platform.deepseek.com/transactions)页面查询充值结果。
* 对公汇款：对公汇款仅支持企业用户。完成企业实名认证后，可获取专属汇款账号，向专属汇款账号进行打款。为保证汇款顺利进行，请确保汇款方开户名称与开放平台实名认证名称一致。我方银行账户到账后，汇款金额将在 10 分钟- 1 小时左右自动转入您的开放平台账户，如未及时收到，请联系我们。

### 余额是否会过期？[​](#余额是否会过期 "余额是否会过期？的直接链接")

您的充值余额永久有效，不会过期。赠送余额的有效期您可以在[「账单」](https://platform.deepseek.com/transactions)页面查看。

### 如何申请发票？[​](#如何申请发票 "如何申请发票？的直接链接")

请访问[账单](https://platform.deepseek.com/transactions)页，点击发票管理，申请发票。企业用户开具发票时，发票抬头需要与实名认证信息一致，目前开发票的周期为 7 个工作日左右。

### 是否可以退款[​](#是否可以退款 "是否可以退款的直接链接")

未消费金额支持退款。

* 在线支付：您可登录开放平台，在[「账单」](https://platform.deepseek.com/transactions)页面点击「退款管理」自助操作退款。
* 企业对公转账：需填写[工单](https://trtgsjkv6r.feishu.cn/share/base/form/shrcnhcHE4A6lQaQ3v0raCXmBAg)，选择「申请退款」选项，按照指引提交相关信息。

### 如何申请发票？[​](#如何申请发票-1 "如何申请发票？的直接链接")

请访问[「账单」](https://platform.deepseek.com/transactions)页面，点击「发票管理」即可提交开票申请。企业用户开具发票时，发票抬头需要与实名认证信息一致。

### 开票是否能增加使用明细[​](#开票是否能增加使用明细 "开票是否能增加使用明细的直接链接")

登录开放平台后，进入[「账单」](https://platform.deepseek.com/transactions)页面，点击「发票管理」，在「备注信息」栏，填入相关信息。

### 如何分 key 查看用量[​](#如何分-key-查看用量 "如何分 key 查看用量的直接链接")

查看各 API Key 的详细用量步骤如下：

1. 登录开放平台，进入[「用量信息」](https://platform.deepseek.com/usage)页面。
2. 选择对应月份，点击「导出」按钮。
3. 下载并解压用量信息压缩包，您将看到两个 CSV 文件。
4. 其中标题为 amount 的文件，即包含了分 Key 统计的用量明细。

### 充值余额金额不对？[​](#充值余额金额不对 "充值余额金额不对？的直接链接")

余额异常时，请您依次确认：

* 您充值的账号与当前登录的账号是否为同一账。
* 如果您有 Google 账号，可尝试用 Google 登录方式检查充值记录是否存在于该账号下。
* 如果您注销过账号后，重新注册，则新旧账号相互独立，原账号余额无法在新账号使用。如需处理，请填写[工单](https://trtgsjkv6r.feishu.cn/share/base/form/shrcnhcHE4A6lQaQ3v0raCXmBAg)，选择「申请退款」选项，按照指引提交相关信息。

---

## API 调用问题[​](#api-调用问题 "API 调用问题的直接链接")

### 调用模型时的并发限制是多少？是否可以提高账号的并发上限？[​](#调用模型时的并发限制是多少是否可以提高账号的并发上限 "调用模型时的并发限制是多少？是否可以提高账号的并发上限？的直接链接")

当前阶段，我们没有按照用户设置硬性并发上限。在系统总负载量较高时，基于系统负载和用户短时历史用量的动态限流模型可能会导致用户收到 503 或 429 错误码。

目前暂不支持针对单个账号提高并发上限，感谢您的理解。

### 为什么我感觉 API 返回比网页端慢[​](#为什么我感觉-api-返回比网页端慢 "为什么我感觉 API 返回比网页端慢的直接链接")

网页端默认使用流式输出（stream=true），即模型每输出一个字符，都会增量地显示在前端。

API 默认使用非流式输出（stream=false），即模型在所有内容输出完后，才会返回给用户。您可以通过开启 API 的 stream 模式来提升交互性。

### 为什么调用 API 时，持续返回空行？[​](#为什么调用-api-时持续返回空行 "为什么调用 API 时，持续返回空行？的直接链接")

为了保持 TCP 连接不会因超时中断，我们会在请求等待调度过程中，持续返回空行（非流式请求）或 SSE keep-alive 注释（`: keep-alive`，流式请求）。如果您在自己解析 HTTP 响应，请注意处理这些空行或注释。

### 是否支持 LangChain？[​](#是否支持-langchain "是否支持 LangChain？的直接链接")

支持。LangChain 支持 OpenAI API 接口，而 DeepSeek API 接口与 OpenAI 兼容。您可以下载以下代码文件并替换代码中的 API Key，实现在 LangChain 中调用 DeepSeek API。

[deepseek\_langchain.py](https://cdn.deepseek.com/api-docs/deepseek_langchain.py)

### 如何离线计算 Tokens 用量？[​](#如何离线计算-tokens-用量 "如何离线计算 Tokens 用量？的直接链接")

请参考 [Token 用量计算](#token-用量计算)

---

# 更新日志

## 时间: 2026-04-24[​](#时间-2026-04-24 "时间: 2026-04-24的直接链接")
### DeepSeek-V4[​](#deepseek-v4 "DeepSeek-V4的直接链接")
* DeepSeek API 已支持 V4-Pro 与 V4-Flash，支持 OpenAI ChatCompletions 接口与 Anthropic 接口。访问新模型时，base\_url 不变, model 参数需要改为 `deepseek-v4-pro` 或 `deepseek-v4-flash`。

旧有的 API 接口的两个模型名 `deepseek-chat` 与 `deepseek-reasoner` 将于三个月后（2026-07-24）停止使用。当前阶段内，这两个模型名分别指向 `deepseek-v4-flash` 的非思考模式与思考模式。

详细更新内容请[参阅文档](#新闻)

---

## 时间: 2025-12-01[​](#时间-2025-12-01 "时间: 2025-12-01的直接链接")

### DeepSeek-V3.2[​](#deepseek-v32 "DeepSeek-V3.2的直接链接")

`deepseek-chat` 和 `deepseek-reasoner` 都已升级为 DeepSeek-V3.2.

* `deepseek-chat` 对应 DeepSeek-V3.2 的非思考模式
* `deepseek-reasoner` 对应 DeepSeek-V3.2 的思考模式

### DeepSeek-V3.2-Speciale[​](#deepseek-v32-speciale "DeepSeek-V3.2-Speciale的直接链接")

我们非正式部署了 DeepSeek-V3.2-Speciale 的 API 服务，API 用户可以通过设置 `base_url="https://api.deepseek.com/v3.2_speciale_expires_on_20251215"` 访问该模型。该模型 API 价格不变，只支持思考模式下的对话功能，不支持工具调用等功能，最大输出长度默认为 128K，支持时间截止至北京时间 2025-12-15 23:59。

详细更新内容请[参阅文档](/zh-cn/news/news251201)

---

## 时间: 2025-09-29[​](#时间-2025-09-29 "时间: 2025-09-29的直接链接")

### DeepSeek-V3.2-Exp[​](#deepseek-v32-exp "DeepSeek-V3.2-Exp的直接链接")

`deepseek-chat` 和 `deepseek-reasoner` 都已经升级为 DeepSeek-V3.2-Exp。

* `deepseek-chat` 对应 DeepSeek-V3.2-Exp 的非思考模式
* `deepseek-reasoner` 对应 DeepSeek-V3.2-Exp 的思考模式

详细更新内容请[参阅文档](/zh-cn/news/news250929)

---

## 时间: 2025-09-22[​](#时间-2025-09-22 "时间: 2025-09-22的直接链接")

### DeepSeek-V3.1-Terminus[​](#deepseek-v31-terminus "DeepSeek-V3.1-Terminus的直接链接")

`deepseek-chat` 和 `deepseek-reasoner` 都已经升级为 DeepSeek-V3.1-Terminus。`deepseek-chat` 对应 DeepSeek-V3.1-Terminus 的非思考模式，`deepseek-reasoner` 对应 DeepSeek-V3.1-Terminus 的思考模式。

此次更新在保持模型原有能力的基础上，针对用户反馈的问题进行了改进，包括：

* 语言一致性：缓解了中英文混杂、偶发异常字符等情况；
* Agent能力：进一步优化了 Code Agent 与 Search Agent 的表现。

---

## 时间: 2025-08-21[​](#时间-2025-08-21 "时间: 2025-08-21的直接链接")

### DeepSeek-V3.1[​](#deepseek-v31 "DeepSeek-V3.1的直接链接")

`deepseek-chat` 和 `deepseek-reasoner` 都已经升级为 DeepSeek-V3.1。`deepseek-chat` 对应 DeepSeek-V3.1 的非思考模式，`deepseek-reasoner` 对应 DeepSeek-V3.1 的思考模式。

* DeepSeek-V3.1 包含以下主要变化：
  + 混合推理架构：一个模型同时支持思考模式与非思考模式
  + 更高的思考效率：相比 DeepSeek-R1-0528，DeepSeek-V3.1-Think 能在更短时间内给出答案
  + 更强的 Agent 能力：通过 Post-Training 优化，新模型在工具使用与智能体任务中的表现有较大提升
    - SWE-bench Verified: 66.0
    - SWE-bench Multilingual: 54.5
    - Terminal-bench: 31.3

---

## 时间: 2025-05-28[​](#时间-2025-05-28 "时间: 2025-05-28的直接链接")

### deepseek-reasoner[​](#deepseek-reasoner "deepseek-reasoner的直接链接")

`deepseek-reasoner` 模型升级为 DeepSeek-R1-0528：

* 推理能力增强
  + 基准测试提升显著（Pass@1）
    - AIME 2025: 70.0→ 87.5 (+17.5)
    - GPQA: 71.5 → 81.0 (+9.5)
    - LCB\_v6: 63.5 → 73.3 (+9.8)
    - Aider: 57.0 → 71.6 (+14.6)
  + 注：复杂推理问题相比老版本R1会使用更多tokens
* Web前端开发能力优化
  + 生成的网页与游戏更加美观
* 幻觉降低
  + 极大程度抑制了老版本R1所存在的幻觉问题
* Json Output与Function Calling 支持
  + Function call性能
    - Tau-bench score: 53.5 (Airline)/63.9 (Retail)

---

## 时间: 2025-03-24[​](#时间-2025-03-24 "时间: 2025-03-24的直接链接")

### deepseek-chat[​](#deepseek-chat "deepseek-chat的直接链接")

`deepseek-chat` 模型升级为 DeepSeek-V3-0324：

* 推理能力增强
  + 基准测试提升显著
    - MMLU-Pro: 75.9 → 81.2 (+5.3)
    - GPQA: 59.1 → 68.4 (+9.3)
    - AIME: 39.6 → 59.4 (+19.8)
    - LiveCodeBench: 39.2 → 49.2 (+10.0)
* Web前端开发能力优化
  + 代码生成准确率提升
  + 生成的网页与游戏前端更加美观
* 中文写作能力升级
  + 风格与内容优化
    - 实现与R1写作风格对齐
    - 中长篇写作内容质量提升
* 功能增强
  + 多轮交互式改写能力提升
  + 翻译质量与书信写作优化
* 中文搜索能力优化
  + 报告分析类请求优化，输出内容详实
* Function Calling 能力改进
  + Function Calling 准确率提升，修复 V3 之前的问题

---

## 时间: 2025-01-20[​](#时间-2025-01-20 "时间: 2025-01-20的直接链接")

### deepseek-reasoner[​](#deepseek-reasoner-1 "deepseek-reasoner的直接链接")

* `deepseek-reasoner` 是我们的新模型 DeepSeek-R1. 可以通过指定 `model=deepseek-reasoner` 调用。
* 详细更新，请参考: [DeepSeek-R1 正式发布](/zh-cn/news/news250120)
* 调用指南，请参考: [推理模型](#api-指南)

---

## 时间: 2024-12-26[​](#时间-2024-12-26 "时间: 2024-12-26的直接链接")

### deepseek-chat[​](#deepseek-chat-1 "deepseek-chat的直接链接")

* `deepseek-chat` 模型升级为 DeepSeek-V3，接口不变，可以通过指定 `model=deepseek-chat` 调用。
* 详细更新，请参考：[DeepSeek-V3 正式发布](/zh-cn/news/news1226)

---

## 时间：2024-12-10[​](#时间2024-12-10 "时间：2024-12-10的直接链接")

### deepseek-chat[​](#deepseek-chat-2 "deepseek-chat的直接链接")

deepseek-chat 模型升级为 DeepSeek-V2.5-1210，模型各项能力提升，相关基准测试：

* 数学能力：在 MATH-500 基准测试中的表现从 74.8% 提升至 82.8%
* 代码能力：在 LiveCodebench (08.01 - 12.01) 基准测试中的准确率从 29.2% 提升至 34.38%
* 中文写作与推理能力：在内部测试集中表现也有相应提升

与此同时，全新版本的模型对文件上传和网页总结功能的用户体验进行了优化。

---

## 时间：2024-09-05[​](#时间2024-09-05 "时间：2024-09-05的直接链接")

### `deepseek-coder` & `deepseek-chat` 升级为 DeepSeek V2.5 模型[​](#deepseek-coder--deepseek-chat-升级为-deepseek-v25-模型 "deepseek-coder--deepseek-chat-升级为-deepseek-v25-模型的直接链接")

DeepSeek V2 Chat 和 DeepSeek Coder V2 两个模型已经合并升级，升级后的新模型为 DeepSeek V2.5。

为向前兼容，API 用户通过 `deepseek-coder` 或 `deepseek-chat` 均可以访问新的模型。

新模型在通用能力、代码能力上，都显著超过了旧版本的两个模型。

新模型更好的对齐了人类的偏好，在写作任务、指令跟随等多方面进行了优化：

* ArenaHard winrate从 68.3% 提升至 76.3%
* AlpacaEval 2.0 LC winrate从 46.61% 提升至 50.52%
* MT-Bench 分数从 8.84 提升至 9.02
* AlignBench 分数从 7.88 提升至 8.04

新模型在原Coder模型的基础上进一步提升了代码生成能力，对常见编程应用场景进行了优化，并在标准测试集上取得了以下成绩：

* HumanEval: 89%
* LiveCodeBench (1-9月): 41%

---

## 时间：2024-08-02[​](#时间2024-08-02 "时间：2024-08-02的直接链接")

### API 上线硬盘缓存技术[​](#api-上线硬盘缓存技术 "API 上线硬盘缓存技术的直接链接")

DeepSeek API 创新采用硬盘缓存，价格再降一个数量级

更新详情请跳转文档 [API 上线硬盘缓存 2024/08/02](/zh-cn/news/news0802)

---

## 时间：2024-07-25[​](#时间2024-07-25 "时间：2024-07-25的直接链接")

### API 接口更新[​](#api-接口更新 "API 接口更新的直接链接")

* 更新接口 `/chat/completions`
  + JSON 输出
  + Function 调用
  + 对话前缀续写（Beta）
  + 8K 最长输出（Beta）
* 新增接口 `/completions`
  + FIM 补全（Beta）

更新详情请跳转文档 [API 升级新功能 2024/07/25](/zh-cn/news/news0725)

---

## 时间：2024-07-24[​](#时间2024-07-24 "时间：2024-07-24的直接链接")

### deepseek-coder[​](#deepseek-coder "deepseek-coder的直接链接")

deepseek-coder 模型升级为 DeepSeek-Coder-V2-0724。

---

## 时间：2024-06-28[​](#时间2024-06-28 "时间：2024-06-28的直接链接")

### deepseek-chat[​](#deepseek-chat-3 "deepseek-chat的直接链接")

`deepseek-chat` 模型升级为 DeepSeek-V2-0628，模型推理能力提升，相关基准测试：

* 代码，HumanEval Pass@1 79.88% -> 84.76%
* 数学，MATH ACC@1 55.02% -> 71.02%
* 推理，BBH 78.56% -> 83.40%

在 Arena-Hard 测评中，与 GPT-4-0314 的对战胜率从 41.6% 提升到了 68.3%。

模型角色扮演能力显著增强，可以在对话中按要求扮演不同角色。

---

## 时间：2024-06-14[​](#时间2024-06-14 "时间：2024-06-14的直接链接")

### deepseek-coder[​](#deepseek-coder-1 "deepseek-coder的直接链接")

`deepseek-coder` 模型升级为 DeepSeek-Coder-V2-0614，代码能力显著提升，在代码生成、代码理解、代码修复和代码补全上达到了 GPT-4-Turbo-0409 的水平，并拥有卓越的数学和推理能力，其通用能力与 DeepSeek-V2-0517 持平。

---

## 时间：2024-05-17[​](#时间2024-05-17 "时间：2024-05-17的直接链接")

### deepseek-chat[​](#deepseek-chat-4 "deepseek-chat的直接链接")

`deepseek-chat` 模型升级为 DeepSeek-V2-0517，模型在指令跟随方面的性能得到了显著提升，IFEval Benchmark Prompt-Level 准确率从 63.9% 跃升至 77.6%。此外，我们对API端的“system”区域指令跟随能力进行了优化，显著增强了沉浸式翻译、RAG 等任务的用户体验。

模型对于 JSON 格式输出的准确性得到了提升。在内部测试集中，JSON 解析率从 78% 提高到了85%。通过引入恰当的正则表达式，JSON 解析率进一步提高至 97%。


* ![WeChat QRcode](https://cdn.deepseek.com/official_account.jpg)

---
