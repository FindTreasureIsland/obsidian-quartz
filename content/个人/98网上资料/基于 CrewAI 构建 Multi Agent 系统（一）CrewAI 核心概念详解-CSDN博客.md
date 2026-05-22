---
title: "基于 CrewAI 构建 Multi Agent 系统（一）CrewAI 核心概念详解-CSDN博客"
source: "https://blog.csdn.net/m0_56255097/article/details/144785165"
author:
published:
created: 2025-03-06
description: "文章浏览阅读1.7k次，点赞20次，收藏26次。Agent是 CrewAI 中的自主单元，具备执行任务、做出决策和与其他代理通信的能力。它们如同团队中的成员，各自承担特定角色，如研究员、作家或客户支持等，共同为实现团队目标贡献力量。在 CrewAI 框架中，任务是代理需要完成的具体工作，包含执行所需的各种细节，如清晰的描述、负责执行的代理、所需工具等。任务可以是协作性的，通过属性管理和流程编排，实现多个代理的协同工作，提升团队合作效率。_crewai"
tags:
  - "clippings"
---
```
CrewAI官网：https://www.crewai.com                                    
Github：https://github.com/joaomdmoura/crewAI  
中文文档：http://www.aidoczh.com/docs/crewai/  
```

## 1\. 引言

在人工智能领域，Multi Agent 系统正逐渐成为解决复杂问题、实现高效协作的关键技术。CrewAI 作为一款强大的多 Agent 协作工具，为开发者提供了便捷的方式来构建智能协作系统。本文将详细介绍如何基于 CrewAI 构建 Multi Agent 系统。

## 2\. CrewAI 核心概念详解

### 2.1 代理（Agent）

#### 2.1.1 Agent的定义与功能

Agent是 CrewAI 中的自主单元，具备执行任务、做出决策和与其他代理通信的能力。它们如同团队中的成员，各自承担特定角色，如研究员、作家或客户支持等，共同为实现团队目标贡献力量。

#### 2.1.2 代理属性

- **角色（Role）**：明确代理在团队中的功能定位，决定其最适合执行的任务类型。例如，研究员角色的代理擅长收集和分析信息，而作家角色的代理则专注于创作内容。
- **目标（Goal）**：指导代理的决策过程，是代理努力实现的个体目标。比如，数据分析师代理的目标可能是提取可操作的见解，以支持业务决策。
- **背景故事（Backstory）**：为代理的角色和目标提供丰富背景信息，增强互动和协作的动态性。以数据分析师为例，其背景故事可以是 “您是一家大公司的数据分析师。您负责分析数据并为业务提供见解。您目前正在进行一个项目，分析我们营销活动的表现。”
- **LLM（可选）**：表示运行代理的语言模型。若未指定，默认从`OPENAI_MODEL_NAME`环境变量中获取模型名称，否则默认为 “gpt - 4”。开发者可以根据需求选择合适的语言模型，以满足不同任务的处理要求。
- **工具（可选）**：代理可使用的一组能力或功能集，通常是与执行环境兼容的自定义类实例，默认值为空列表。这些工具能够扩展代理的能力，使其能够执行诸如网页搜索、数据分析等操作。
- **调用功能的 LLM（可选）**：指定处理该代理工具调用的语言模型，若传递则覆盖团队功能调用 LLM，默认值为`None`。通过灵活配置此属性，开发者可以更精准地控制代理的工具调用行为。
- **最大迭代次数（可选）**：代理在被强制给出最佳答案前可执行的最大迭代次数，默认值为 25。合理设置该参数有助于控制任务执行的深度和效率。
- **最大请求次数（可选）**：代理每分钟可执行的最大请求数，用于避免速率限制，默认值为`None`。开发者可根据实际情况进行设置，以确保系统稳定运行。
- **最大执行时间（可选）**：代理执行任务的最大时长，默认值为`None`，表示无最大执行时间限制。此属性可用于控制任务的执行周期，防止任务长时间占用资源。
- **详细模式（可选）**：将其设置为`True`可配置内部记录器提供详细执行日志，便于调试和监控，默认值为`False`。在开发和优化过程中，开启详细模式有助于快速定位问题。
- **允许委托（可选）**：代理之间可相互委托任务或问题，确保任务由最合适的代理处理，默认值为`True`。这一特性促进了团队内部的灵活协作，提高了任务处理的准确性和效率。
- **步骤回调（可选）**：在代理每个步骤后调用的函数，可用于记录操作或执行其他操作，会覆盖团队`step_callback`。开发者可以利用此回调函数实现自定义的监控和处理逻辑。
- **缓存（可选）**：指示代理是否使用工具使用缓存，默认值为`True`。缓存机制有助于提高任务执行效率，减少重复计算。

#### 2.1.3 创建代理

代理可以使用 crewAI 内置的委托和通信机制相互交互。这允许在团队内进行动态任务管理和问题解决。

要创建代理，通常会使用所需属性初始化`Agent`类的实例。以下是一个包含所有属性的概念示例：

```python
# 示例：创建具有所有属性的代理
from crewai import Agent  

agent = Agent(  
  role='数据分析师',
  goal='提取可操作的见解',
  backstory="""您是一家大公司的数据分析师。
  您负责分析数据并为业务提供见解。
  您目前正在进行一个项目，分析我们营销活动的表现。""",
  tools=[my_tool1, my_tool2],  # 可选，默认为空列表
  llm=my_llm,  # 可选  
  function_calling_llm=my_llm,  # 可选  
  max_iter=15,  # 可选  
  max_rpm=None, # 可选  
  verbose=True,  # 可选  
  allow_delegation=True,  # 可选  
  step_callback=my_intermediate_step_callback,  # 可选                                                                                                                                                                                                                                                              
  cache=True  # 可选  
)
```

### 2.2 任务（Task）

#### 2.2.1 任务定义与协作

在 CrewAI 框架中，任务是代理需要完成的具体工作，包含执行所需的各种细节，如清晰的描述、负责执行的代理、所需工具等。任务可以是协作性的，通过属性管理和流程编排，实现多个代理的协同工作，提升团队合作效率。

#### 2.2.2 任务的属性

- **描述（Description）**：对任务内容的清晰简明陈述，让代理明确知道需要做什么。例如 “查找并总结有关人工智能的最新和最相关新闻”。
- **代理（Agent）**：负责任务执行的代理，可以直接指定，也可由 Crew 的流程根据角色、可用性等因素分配。这确保了任务能够找到合适的执行者。
- **预期输出（Expected Output）**：对任务完成后的详细描述，使代理清楚任务的目标和期望结果。比如 “对前 5 条最重要的人工智能新闻进行项目符号列表总结”。
- **工具（可选）**：代理执行任务时使用的功能或能力，可增强任务性能和代理交互。通过选择合适的工具，代理能够更高效地完成任务。
- **异步执行（可选）**：设置后任务将异步执行，允许在不等待完成的情况下继续推进其他任务，适用于耗时较长或对后续任务执行影响不大的任务。
- **上下文（可选）**：指定输出用作此任务上下文的任务，明确任务之间的依赖关系，实现任务输出的有效传递和利用。
- **配置（可选）**：用于执行任务的代理的附加配置细节，提供了进一步定制任务执行的灵活性。
- **输出 JSON（可选）**：输出 JSON 对象，需要 OpenAI 客户端，且只能设置一种输出格式。此属性方便与其他系统进行数据交互和集成。
- **输出 Pydantic（可选）**：输出 Pydantic 模型对象，同样需要 OpenAI 客户端，且只能设置一种输出格式。开发者可根据实际需求选择合适的输出格式。
- **输出文件（可选）**：将任务输出保存到文件，若与`输出JSON`或`输出Pydantic`一起使用，可指定输出保存方式。这有助于数据的持久化和后续分析。
- **回调（可选）**：任务完成后执行的 Python 可调用函数，可用于根据任务结果触发操作或通知，如发送邮件等。
- **人工输入（可选）**：指示任务是否需要最终人工反馈，对于需要人工监督的任务非常有用，确保任务结果的准确性和可靠性。

#### 2.2.3 创建任务

创建任务涉及定义其范围、负责代理以及任何额外属性以实现灵活性：

```python
from crewai import Task

task = Task(
    description='查找并总结有关人工智能的最新和最相关新闻',
    agent=sales_agent
)
```

“任务分配”：直接为分配指定一个 `代理`，或者让 `分层` 的 CrewAI 流程根据角色、可用性等决定。

#### 2.2.4 使用工具创建任务

```python
import os
os.environ["OPENAI_API_KEY"] = "Your Key"
os.environ["SERPER_API_KEY"] = "Your Key" # serper.dev API key

from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool

research_agent = Agent(
  role='研究员',
  goal='查找并总结最新的人工智能新闻',
  backstory="""您是一家大公司的研究员。
  您负责分析数据并为业务提供见解。""",
  verbose=True
)

search_tool = SerperDevTool()

task = Task(
  description='查找并总结最新的人工智能新闻',
  expected_output='对前 5条最重要的人工智能新闻进行项目符号列表总结',
  agent=research_agent,
  tools=[search_tool]
)

crew = Crew(
    agents=[research_agent],
    tasks=[task],
    verbose=2
)

result = crew.kickoff()
print(result)
```

#### 2.2.5 任务依赖

在 crewAI 中，一个任务的输出会自动传递到下一个任务，当有一个任务依赖于另一个任务的输出，但并非立即在其后执行时，这将非常有用。这通过任务的 `上下文` 属性完成：

```python
# ...

research_ai_task = Task(
    description='查找并总结最新的人工智能新闻',
    expected_output='对前 5条最重要的人工智能新闻进行项目符号列表总结',
    async_execution=True,
    agent=research_agent,
    tools=[search_tool]
)

research_ops_task = Task(
    description='查找并总结最新的人工智能运营新闻',
    expected_output='对前 5条最重要的人工智能运营新闻进行项目符号列表总结',
    async_execution=True,
    agent=research_agent,
    tools=[search_tool]
)

write_blog_task = Task(
    description="撰写一篇关于人工智能重要性及其最新新闻的完整博客文章",
    expected_output='4段长的完整博客文章',
    agent=writer_agent,
    context=[research_ai_task, research_ops_task]
)

#...
```

#### 2.2.6 异步执行

任务以异步方式执行，意味着 Crew 不会等待其完成才继续下一个任务。这对于需要很长时间完成的任务或对下一个任务执行不是至关重要的任务非常有用。可以使用 `上下文` 属性在将来的任务中定义，它应等待异步任务的输出完成。

```python
#...

list_ideas = Task(
    description="探索有关人工智能文章的 5个有趣想法。",
    expected_output="一份包含 5个文章想法的项目符号列表。",
    agent=researcher,
    async_execution=True # 将以异步方式执行
)

list_important_history = Task(
    description="研究人工智能的历史，并告诉我 5个最重要的事件。",
    expected_output="包含 5个重要事件的项目符号列表。",
    agent=researcher,
    async_execution=True # 将以异步方式执行
)

write_article = Task(
    description="撰写一篇关于人工智能、其历史和有趣想法的文章。",
    expected_output="一篇关于人工智能的 4段文章。",
    agent=writer,
    context=[list_ideas, list_important_history] # 将等待两个任务的输出完成
)

#...
```

#### 2.2.7 回调机制

在任务完成后执行回调函数，允许根据任务结果触发操作或通知。

```python
# ...

def callback_function(output: TaskOutput):
    # 任务完成后执行某些操作
    # 例如：向经理发送电子邮件
    print(f"""
        任务完成！
        任务：{output.description}
        输出：{output.raw_output}
    """)

research_task = Task(
    description='查找并总结最新的人工智能新闻',
    expected_output='对前 5条最重要的人工智能新闻进行项目符号列表总结',
    agent=research_agent,
    tools=[search_tool],
    callback=callback_function
)

#...
```

#### 2.2.8 访问特定任务输出

一组 Crew 运行完成后，可以通过使用任务对象的 `output` 属性访问特定任务的输出：

```python
# ...
task1 = Task(
    description='查找并总结最新的人工智能新闻',
    expected_output='对前 5条最重要的人工智能新闻进行项目符号列表总结',
    agent=research_agent,
    tools=[search_tool]
)

#...

crew = Crew(
    agents=[research_agent],
    tasks=[task1, task2, task3],
    verbose=2
)

result = crew.kickoff()

# 返回一个 TaskOutput 对象，其中包含任务的描述和结果
print(f"""
    任务完成！
    任务：{task1.output.description}
    输出：{task1.output.raw_output}
""")
```

#### 2.2.9 工具覆盖机制

在任务中指定工具允许动态调整代理能力，突出了 CrewAI 的灵活性。

#### 2.2.10 错误处理和验证机制

在创建和执行任务时，存在某些验证机制，以确保任务属性的健壮性和可靠性。这些验证包括但不限于：

- 确保每个任务仅设置一种输出类型，以保持清晰的输出期望。
- 防止手动分配 `id` 属性，以维护唯一标识符系统的完整性。

这些验证有助于在 crewAI 框架内维护任务执行的一致性和可靠性。

### 2.3 工具（Tool）

#### 2.3.1 工具的作用与类型

CrewAI 工具赋予代理多种能力，包括网页搜索、数据分析、内容生成和任务委派等，使代理能够执行各种复杂操作，实现从简单搜索到复杂互动以及有效团队合作的跨越。

#### 2.3.2 工具的关键特征

- **实用性（Utility）**：专为任务设计，涵盖了多个领域的功能需求，如网页搜索、数据分析、内容生成等，满足代理在不同场景下的工作需求。
- **集成性（Integration）**：能够无缝集成到工作流程中，与代理和任务紧密配合，提升代理的整体能力，实现高效协作。
- **可定制性（Customizability）**：提供了灵活性，开发者既可以开发定制工具满足特定需求，也可以利用现有工具，根据代理的实际需求进行个性化配置。
- **错误处理（Error Handling）**：具备强大的错误处理机制，确保工具在运行过程中遇到异常时能够优雅地处理，保证系统的平稳运行。
- **缓存机制（Caching Mechanism）**：具有智能缓存功能，可优化性能，减少冗余操作。开发者还可以通过`cache_function`属性对缓存机制进行更精细的控制，进一步提高效率。

#### 2.3.3 使用 crewAI 工具

要通过 crewAI 工具增强代理的能力，需要先安装额外工具包：

```
pip install 'crewai[tools]'
```

下面是使用案例

```python
import os
from crewai import Agent, Task, Crew

# 导入 crewAI 工具
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    SerperDevTool,
    WebsiteSearchTool
)
# 设置 API 密钥
os.environ["SERPER_API_KEY"] = "Your Key" # serper.dev API 密钥
os.environ["OPENAI_API_KEY"] = "Your Key"

# 实例化工具
docs_tool = DirectoryReadTool(directory='./blog-posts')
file_tool = FileReadTool()
search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()

# 创建代理
researcher = Agent(
    role='市场研究分析师',
    goal='提供关于人工智能行业最新市场分析',
    backstory='一位对市场趋势敏锐的专家分析师。',
    tools=[search_tool, web_rag_tool],
    verbose=True
)

writer = Agent(
    role='内容撰写人员',
    goal='撰写有关人工智能行业的引人入胜的博客文章',
    backstory='一位对技术充满激情的熟练撰稿人。',
    tools=[docs_tool, file_tool],
    verbose=True
)
# 定义任务
research = Task(
    description='研究人工智能行业的最新趋势并提供摘要。',
    expected_output='关于人工智能行业前三个热门发展的摘要，并对其重要性提供独特视角。',
    agent=researcher
)
write = Task(
    description='根据研究分析师的摘要撰写一篇引人入胜的博客文章。从目录中最新的博客文章中汲取灵感。',
    expected_output='一篇以 markdown 格式排版的四段博客文章，内容引人入胜、信息丰富且易懂，避免使用复杂术语。',
    agent=writer,
    output_file='blog-posts/new_post.md'  # 最终的博客文章将保存在此处
)

# 组建团队
crew = Crew(
    agents=[researcher, writer],
    tasks=[research, write],
    verbose=2
)

# 执行任务
crew.kickoff()
```

#### 2.3.3 可用的 CrewAI 工具

CrewAI 提供了丰富的工具，如`CodeDocsSearchTool`（搜索代码文档和相关技术文档的 RAG 工具）、`CSVSearchTool`（在 CSV 文件中搜索的 RAG 工具，处理结构化数据）、`DirectorySearchTool`（用于目录搜索，浏览文件系统）等众多工具，每个工具都有其特定的用途和优势，可根据任务需求选择合适的工具。

#### 2.3.4 创建自己的工具

需要先安装工具包

```
pip install 'crewai[tools]'
```

- **子类化`BaseTool`**：通过继承`BaseTool`类，开发者可以创建自定义工具。需要定义工具的名称、描述，并实现`_run`方法来定义工具的具体功能逻辑。例如：

```python
from crewai_tools import BaseTool

class MyCustomTool(BaseTool):
    name: str = "我的工具名称"
    description: str = "清晰描述此工具用于什么，您的代理将需要这些信息来使用它。"
    def _run(self, argument: str) -> str:
        # 实现在这里
        return "自定义工具的结果"
```

- **利用`tool`装饰器**：使用`tool`装饰器可以更简洁地创建自定义工具。只需定义函数，在函数上方添加`@tool`装饰器，并提供工具名称和描述即可。例如：

```python
from crewai_tools import tool

@tool("我的工具名称")
def my_tool(question: str) -> str:
    """清晰描述此工具用于什么，您的代理将需要这些信息来使用它。"""
    # 函数逻辑在这里
    return "您的自定义工具的结果"
```

- **自定义缓存机制**：工具可以选择实现`cache_function`来微调缓存行为。根据特定条件确定何时缓存结果，提供对缓存逻辑的细粒度控制。例如：

```python
from crewai_tools import tool

@tool
def multiplication_tool(first_number: int, second_number: int) -> str:
    """当您需要将两个数字相乘时有用。"""
    return first_number * second_number

def cache_func(args, result):
    # 在这种情况下，仅在结果是2的倍数时才缓存结果
    cache = result % 2 == 0
    return cache

multiplication_tool.cache_function = cache_func
```

#### 2.3.5 使用 LangChain 工具

CrewAI 与 LangChain 的工具包无缝集成，开发者可以利用 LangChain 提供的内置工具，如`GoogleSerperAPIWrapper`等，通过简单的配置将其集成到 CrewAI 系统中，扩展代理的能力。例如：

```python
from crewai import Agent
from langchain.agents import Tool
from langchain.utilities import GoogleSerperAPIWrapper

# 设置API密钥
os.environ["SERPER_API_KEY"] = "Your Key"
search = GoogleSerperAPIWrapper()

# 创建并将搜索工具分配给代理
serper_tool = Tool(
  name="中级答案",
  func=search.run,
  description="用于基于搜索的查询的工具"
)

agent = Agent(
  role='研究分析师',
  goal='提供最新的市场分析',
  backstory='一位对市场趋势敏锐的专家分析师。',
  tools=[serper_tool]
)
```

### 2.4 流程（Process）

#### 2.4.1 流程实现方式

- **顺序执行（Sequential）**：任务按照预先定义的顺序依次执行，一个任务的输出作为下一个任务的上下文，确保任务执行的有序性和连贯性。
- **分级（Hierarchical）**：将任务组织在管理层级中，通过指定管理语言模型（`manager_llm`）启用该流程。管理者代理负责监督任务执行，包括规划、委派和验证任务，任务根据代理能力分配，而非预分配。
- **共识流程（计划中）**：旨在实现代理之间在任务执行上的协作决策，引入民主的任务管理方式，目前尚未在代码库中实施，但体现了 CrewAI 对持续发展和创新的追求。

#### 2.4.2 流程在团队合作中的作用

流程使个体代理能够作为一个有凝聚力的整体运作，简化协作努力，以高效、协调的方式实现共同目标。通过合理的流程设计，团队能够更好地应对复杂任务，提高整体工作效率。

#### 2.4.3 将流程分配给manager

在创建manager时，开发者可以指定流程类型来设置执行策略。对于分级流程，必须为管理者代理定义`manager_llm`。例如：

```python
from crewai import Crew
from crewai.process import Process
from langchain_openai import ChatOpenAI

# 顺序流程
crew = Crew(
    agents=my_agents,
    tasks=my_tasks,
    process=Process.sequential
)

# 分级流程，确保提供manager_llm
crew = Crew(
    agents=my_agents,
    tasks=my_tasks,
    process=Process.hierarchical,
    manager_llm=ChatOpenAI(model="gpt - 4")
)
```

#### 2.4.4 附加任务特性

- **异步执行（Asynchronous Execution）**：允许任务异步执行，实现并行处理，提高船员整体生产力。开发者可以根据任务特点灵活选择同步或异步执行方式。
- **人工输入审查（Human Input Review）**：提供可选的人工审查任务输出功能，在最终确定任务结果前确保质量和准确性，引入了额外的监督层，保障任务执行的可靠性。
- **输出定制（Output Customization）**：任务支持多种输出格式，如 JSON（`output_json`）、Pydantic 模型（`output_pydantic`）和文件输出（`output_file`），满足不同需求，方便数据的处理和利用。

### 2.5 团队（Crews）

#### 2.5.1 团队属性

- **任务（Tasks）**：分配给团队的任务列表，明确团队需要完成的工作内容。
- **代理（Agents）**：属于团队的代理列表，确定团队成员构成，每个代理都有其独特的角色和能力。
- **流程（可选）**：团队遵循的流程类型，如顺序或分层流程，决定任务执行的顺序和方式。
- **详细程度（可选）**：执行过程中日志记录的详细程度，便于开发者在调试和监控时获取足够信息。
- **经理 LLM（可选，分层流程必需）**：分层流程中经理代理使用的语言模型，用于管理任务执行过程。
- **功能调用 LLM（可选）**：若传递，团队将使用此 LLM 为所有代理进行工具的功能调用，开发者可根据需求灵活配置。
- **配置（可选）**：团队的可选配置设置，以`Json`或`Dict[str, Any]`格式提供，用于进一步定制团队行为。
- **最大 RPM（可选）**：团队执行过程中每分钟可执行的最大请求数，避免速率限制，可覆盖个别代理的`max_rpm`设置。
- **语言（可选）**：团队使用的语言，默认为英语，可根据实际需求进行调整。
- **语言文件（可选）**：用于团队的语言文件路径，方便进行多语言支持。
- **内存（可选）**：用于存储执行记忆（短期、长期、实体记忆），增强团队的执行能力和学习能力。
- **缓存（可选）**：指定是否使用缓存存储工具执行结果，提高流程效率。
- **嵌入器（可选）**：团队使用的嵌入器配置，主要用于内存功能，影响数据的嵌入和检索方式。
- **完整输出（可选）**：决定团队是否返回包含所有任务输出的完整输出或仅最终输出，满足不同的结果获取需求。
- **步骤回调（可选）**：在每个代理的每个步骤后调用的函数，用于记录操作或执行其他操作，不覆盖特定于代理的`step_callback`。
- **任务回调（可选）**：在每个任务完成后调用的函数，用于监控或执行任务后的其他操作。
- **共享团队（可选）**：是否与 CrewAI 团队共享完整的团队信息和执行情况，以改进库并允许训练模型。
- **输出日志文件（可选）**：是否创建包含完整团队输出和执行情况的文件，可指定文件路径和名称。

#### 2.5.2 创建团队示例

以下是一个组建团队的示例，展示如何将具有互补角色和工具的代理结合在一起，分配任务并选择流程：

```python
from crewai import Crew, Agent, Task, Process
from langchain_community.tools import DuckDuckGoSearchRun

# 定义具有特定角色和工具的代理
researcher = Agent(
    role='高级研究分析师',
    goal='发现创新的人工智能技术',
    tools=[DuckDuckGoSearchRun()]
)

writer = Agent(
    role='内容撰稿人',
    goal='撰写有关人工智能发现的引人入胜的文章',
    verbose=True
)

# 为代理创建任务
research_task = Task(
    description='识别突破性人工智能技术',
    agent=researcher
)
write_article_task = Task(
    description='撰写关于最新人工智能技术的文章',
    agent=writer
)

# 使用顺序流程组装团队
my_crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_article_task],
    process=Process.sequential,
    full_output=True,
    verbose=True,
)
```

#### 2.5.3 团队执行流程

- **顺序流程（Sequential）**：任务依次执行，工作线性流动，简单直观，适用于任务之间有明确先后顺序的场景。
- **分层流程（Hierarchical）**：经理代理协调团队，委派任务并在继续之前验证结果。此流程需要`manager_llm`，适用于复杂任务的管理和分配，确保任务的高效执行和质量控制。
- **启动团队**：使用`kickoff()`方法启动团队工作流程，根据定义的流程开始执行任务，获取任务执行结果。例如：

```python
# 启动团队的任务执行
result = my_crew.kickoff()
print(result)
```

### 2.6 记忆（Memory）

#### 2.6.1 记忆系统组成部分

- **短期记忆（Short - term Memory）**：暂时存储最近的互动和结果，使代理能够迅速回忆和利用与当前情境紧密相关的信息，从而在对话或任务序列中保持连贯性，做出更贴合实际情况的决策和回应。
- **长期记忆（Long - term Memory）**：犹如一个知识宝库，保留从过往执行中积累的宝贵见解和学习成果。随着时间的推移，代理能够不断从中汲取经验，逐步构建和完善自身的知识体系，进而提升未来决策和问题解决的能力，以更好地应对复杂多变的任务场景。
- **实体记忆（Entity Memory）**：专注于捕获和组织在任务执行过程中遇到的各类实体信息，涵盖人、地点、概念等。这有助于代理深入理解复杂信息之间的内在联系，通过对实体关系的精准映射，更高效地处理和整合相关知识，为解决问题提供更全面、深入的视角。
- **上下文记忆（Context Memory）**：致力于维护互动过程中的上下文信息，确保代理在一系列任务或连续对话中，能够始终保持响应的连贯性和相关性。即使在长时间的交互过程中，也能准确理解任务背景和意图，避免出现信息断层或误解，从而提供更加准确、合理的输出。

#### 2.6.2 记忆系统如何赋能代理

- **上下文意识增强**：借助短期记忆和上下文记忆的协同作用，代理能够在对话或任务的演进过程中，牢牢把握上下文脉络。无论是多轮对话中的信息关联，还是任务序列中的逻辑延续，代理都能依据存储的上下文信息，生成更加连贯、一致且符合情境的回应，极大地提升了交互体验的流畅性和逻辑性。
- **经验积累与学习加速**：长期记忆为代理提供了一个不断成长和进化的平台。通过存储和回顾过去的行动及结果，代理能够从中总结经验教训，发现规律和模式，进而不断优化自身的决策策略和问题解决方法。这种经验积累的过程使得代理在面对类似问题时，能够迅速做出更明智、更高效的决策，显著提高工作效率和质量。
- **实体理解与信息处理优化**：实体记忆赋予代理识别和记忆关键实体的能力，使其在处理复杂信息时能够快速聚焦核心要点，理清信息之间的相互关系。这不仅有助于代理更准确地理解任务需求，还能在面对海量信息时，迅速筛选出有价值的内容，提高信息处理的速度和精度，从而更有效地应对复杂任务和多样化的问题场景。

#### 2.6.3 在团队中实施记忆

在配置团队时，开发者可以根据团队目标和任务性质，灵活启用和定制每个记忆组件。默认情况下，记忆系统处于关闭状态，通过在团队配置中设置`memory = True`，即可激活记忆功能，为团队注入强大的记忆能力。记忆默认使用 OpenAI Embeddings，但开发者也可以通过调整`embedder`参数，将其设置为其他模型，如 Google AI、Azure OpenAI、GPT4ALL、Vertex AI 或 Cohere 等，以满足不同场景下的需求。例如：

```python
from crewai import Crew, Agent, Task, Process

# 使用具有记忆功能的团队，采用默认的OpenAI Embeddings
my_crew = Crew(
    agents=[...],
    tasks=[...],
    process=Process.sequential,
    memory=True,
    verbose=True
)

# 使用具有记忆功能的团队，切换为Google AI嵌入
my_crew = Crew(
    agents=[...],
    tasks=[...],
    process=Process.sequential,
    memory=True,
    verbose=True,
    embedder={
        "provider": "google",
        "config":{
            "model": 'models/embedding - 001',
            "task_type": "retrieval_document",
            "title": "Embeddings for Embedchain"
        }
    }
)
```

#### 2.6.4 使用 CrewAI 记忆系统的好处

- **自适应学习与持续优化**：随着时间的推移和任务的不断执行，团队能够逐渐适应新的信息和任务要求，不断完善处理任务的方法和策略。记忆系统使代理能够从过往经验中学习，自动调整行为模式，从而在面对新情况时更加从容，团队整体效率也会随着经验的积累而不断提升。
- **个性化体验提升**：记忆功能使代理能够记录和识别用户的偏好、历史互动等信息，从而为用户提供更加个性化的服务和体验。无论是在内容推荐、问题解答还是交互方式上，代理都能够根据用户的个性化特征进行精准回应，满足用户的特定需求，增强用户与系统之间的粘性和满意度。
- **问题解决能力强化**：丰富的记忆存储库为代理提供了强大的知识后盾，使其在解决问题时能够充分借鉴过去的学习成果和上下文信息。通过快速检索和利用相关经验，代理能够更全面地分析问题，发现潜在的解决方案，做出更明智、更准确的决策，从而有效提升解决复杂问题的能力，为团队的成功运作提供有力支持。

---

## 如何系统学习掌握AI大模型？

AI大模型作为人工智能领域的重要技术突破，正成为推动各行各业创新和转型的关键力量。抓住AI大模型的风口，掌握AI大模型的知识和技能将变得越来越重要。

学习AI大模型是一个系统的过程，需要从基础开始，逐步深入到更高级的技术。

> 这里给大家精心整理了**一份`全面的AI大模型学习资源`，包括：AI大模型全套学习路线图（从入门到实战）、精品AI大模型学习书籍手册、视频教程、实战学习、面试题等，`资料免费分享`！**

![](https://img-blog.csdnimg.cn/img_convert/3f148c655f218bc2965ab56fc9b9c206.png)

### 1\. 成长路线图&学习规划

要学习一门新的技术，作为新手一定要**先学习成长路线图**，**方向不对，努力白费**。

这里，我们为新手和想要进一步提升的专业人士准备了一份详细的学习成长路线图和规划。可以说是最科学最系统的学习成长路线。  
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/b2e9d9b8d3244782977a5bece8cadfbf.png#pic_center)

### 2\. 大模型经典PDF书籍

书籍和学习文档资料是学习大模型过程中必不可少的，我们精选了一系列深入探讨大模型技术的书籍和学习文档，**它们由领域内的顶尖专家撰写，内容全面、深入、详尽，为你学习大模型提供坚实的理论基础**。**（书籍含电子版PDF）**

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/3095a9078ce24db69abf285b5652ee53.png#pic_center)

### 3\. 大模型视频教程

对于很多自学或者没有基础的同学来说，书籍这些纯文字类的学习教材会觉得比较晦涩难以理解，因此，我们**提供了丰富的大模型视频教程**，以动态、形象的方式展示技术概念，**帮助你更快、更轻松地掌握核心知识**。

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/d7b864768a9346cfb5de052b851947b6.png#pic_center)

### 4\. 2024行业报告

行业分析主要包括对不同行业的现状、趋势、问题、机会等进行系统地调研和评估，以了解哪些行业更适合引入大模型的技术和应用，以及在哪些方面可以发挥大模型的优势。

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/c11b60bcfd524446a917ced9e492b012.png#pic_center)

### 5\. 大模型项目实战

**学以致用** ，当你的理论知识积累到一定程度，就需要通过项目实战，**在实际操作中检验和巩固你所学到的知识**，同时为你找工作和职业发展打下坚实的基础。

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/f2f79ffa09034d96b2f7aec1f58afcbf.png#pic_center)

### 6\. 大模型面试题

面试不仅是技术的较量，更需要充分的准备。

在你已经掌握了大模型技术之后，就需要开始准备面试，我们将提供精心整理的大模型面试题库，涵盖当前面试中可能遇到的各种技术问题，让你在面试中游刃有余。

![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/b3703bef006543de963beb642ae787ea.png#pic_center)

> **全套的AI大模型学习资源已经整理打包，有需要的小伙伴可以`微信扫描下方CSDN官方认证二维码`，免费领取【`保证100%免费`】**

![](https://img-blog.csdnimg.cn/img_convert/2c74f8ae683a20dc159a85f384036825.png)