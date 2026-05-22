---
banner:
title: LangChain完整指南和教程
author: 宋志勇
summary:
  "{ summary }":
created: 2025-03-06 12:03
updated: 2025-09-27 23:14
tags:
  - clippings
---
---

LangChain指南

其核心是[LangChain](https://www.langchain.com/)是一个创新的框架，专为构建利用语言模型功能的应用程序而量身定制。这是一个为开发人员设计的工具包，用于创建具有上下文感知和复杂推理能力的应用程序。在讨论[**检索增强生成****（RAG）**]时，该框架具有高度相关性(https://nanonets.com/blog/what-is-retrieval-augmented-generation-rag/)，这一概念增强了语言模型在基于检索到的数据生成响应方面的有效性。

这意味着LangChain应用程序可以理解上下文，例如提示指令或基于内容的响应，并使用[**大型语言模型**](https://nanonets.com/blog/what-are-large-language-models/)对于复杂的推理任务，比如决定如何回应或采取什么行动。LangChain代表了一种开发智能应用程序的统一方法，通过其多样化的组件简化了从概念到执行的过程。

##了解LangChain

LangChain不仅仅是一个框架；这是一个由几个组成部分组成的成熟生态系统。

-首先，有Python和JavaScript中的LangChain库。这些库是LangChain的支柱，为各种组件提供接口和集成。它们提供了一个基本的运行时环境，用于将这些组件组合成有凝聚力的链和代理，以及可立即使用的现成实现。

这些组件共同使您能够轻松地开发、生产和部署应用程序。使用LangChain，您首先可以使用库编写应用程序，并参考模板以获取指导。然后，LangSmith帮助您检查、测试和监控您的链，确保您的应用程序不断改进并准备好部署。最后，使用LangServe，您可以轻松地将任何链转换为API，使部署变得轻而易举。

在接下来的部分中，我们将深入探讨如何设置LangChain，并开始您创建智能、语言模型驱动的应用程序的旅程。

---

##安装和设置

你准备好深入LangChain的世界了吗？设置它很简单，本指南将逐步引导您完成整个过程。

LangChain之旅的第一步是安装它。您可以使用pip或conda轻松完成此操作。在终端中运行以下命令：

```bash

---

*对于那些喜欢最新功能并喜欢更多冒险的人来说，您可以直接从源代码安装LangChain。克隆存储库并导航到`langchain/libs/langchain`目录。然后，运行：*

```bash

*对于实验功能，请考虑安装“langchain experimental”。这是一个包含尖端代码的包，用于研究和实验目的。使用以下方式安装：*

```bash

*LangChain CLI是一个方便的工具，用于处理LangChain模板和LangServe项目。要安装LangChain CLI，请使用：*

```bash

*LangServe对于将LangChain链部署为REST API至关重要。它与LangChain CLI一起安装*

---

LangChain通常需要与模型提供者、数据存储、API等集成。对于这个例子，我们将使用OpenAI的模型API。使用以下命令安装OpenAI Python包：

python

要访问API，请将OpenAI API密钥设置为环境变量：

```bash

或者，直接在python环境中传递密钥：

python

LangChain允许通过模块创建语言模型应用程序。这些模块既可以独立存在，也可以针对复杂的用例进行组合。这些模块是-

-**模型I/O**：促进与各种语言模型的交互，有效地处理它们的输入和输出。

每个模块都针对特定的开发需求，使LangChain成为创建高级语言模型应用程序的综合工具包。

除了上述组件，我们还有**LangChain表达式语言（LCEL）**，这是一种声明性的方式，可以轻松地将模块组合在一起，这使得可以使用通用的Runnable接口链接组件。

LCEL看起来像这样-

python

#示例链

现在我们已经介绍了基础知识，我们将继续：

-深入了解每个Langchain模块的细节。

让我们开始吧！

---

##模块一：模型输入/输出

在LangChain中，任何应用程序的核心元素都围绕着语言模型。该模块提供了与任何语言模型有效交互的基本构建块，确保了无缝集成和通信。

#####模型I/O的关键组件

1.**LLM和聊天模式（可互换使用）：**

-**定义**：使用语言模型作为基础但输入和输出格式不同的模型。

3.**提示**：模板化、动态选择和管理模型输入。允许创建灵活且特定于上下文的提示，以指导语言模型的响应。

#####[法学硕士](https://nanonets.com/blog/what-are-large-language-models/)

LangChain与OpenAI、Cohere和Hugging Face等大型语言模型（LLM）的集成是其功能的一个基本方面。LangChain本身不托管LLM，但提供了一个统一的接口来与各种LLM进行交互。

本节概述了在LangChain中使用OpenAI LLM包装器，也适用于其他LLM类型。我们已经在“入门”部分安装了它。让我们初始化LLM。

```bash

-LLM实现了[Runnable接口](https://python.langchain.com/docs/expression_language/interface)，[LangChain表达式语言（LCEL）]的基本构建块(https://python.langchain.com/docs/expression_language/). 这意味着它们支持“调用”、“ainvoke”、“流”、“astream”、“批处理”、“abatch”和“astream_log”调用。

让我们来看一些例子。

```bash

您也可以调用stream方法来流式传输文本响应。

```bash

#####聊天模特

LangChain与聊天模型（语言模型的一种特殊变体）的集成对于创建交互式聊天应用程序至关重要。虽然聊天模型在内部使用语言模型，但它们呈现了一个以聊天消息作为输入和输出的独特界面。本节详细概述了在LangChain中使用OpenAI的聊天模型。

python

LangChain中的聊天模型可以处理不同的消息类型，如'AIMessage'、'AHumanMessage'、'SystemMessage'、`FunctionMessage'和`ChatMessage'（带有任意角色参数）。一般来说，最常用的是“HumanMessage”、“AIMessage”和“SystemMessage”。

聊天模式主要接受“List[BaseMessage]”作为输入。字符串可以转换为“HumanMessage”，也支持“PromptValue”。

python

####提示

提示对于指导语言模型生成相关和连贯的输出至关重要。它们可以从简单的说明到复杂的少数镜头示例。在LangChain中，由于有几个专用的类和函数，处理提示可以是一个非常简化的过程。

LangChain的`PromptTemplate`类是一个用于创建字符串提示的多功能工具。它使用Python的`str.format`语法，允许动态生成提示。您可以定义一个带有占位符的模板，并根据需要用特定值填充它们。

python

#带有占位符的简单提示

#填充占位符以创建提示

对于聊天模型，提示更具结构化，涉及具有特定角色的消息。LangChain为此提供了“ChatPromptTemplate”。

python

#定义具有各种角色的聊天提示

#格式化聊天提示

这种方法允许创建具有动态响应的交互式、引人入胜的聊天机器人。

PromptTemplate和ChatPromptTemplate都与LangChain表达式语言（LCEL）无缝集成，使其能够成为更大、更复杂的工作流程的一部分。稍后我们将对此进行更多讨论。

自定义提示模板有时对于需要独特格式或特定说明的任务至关重要。创建自定义提示模板涉及定义输入变量和自定义格式方法。这种灵活性使LangChain能够满足各种特定于应用程序的要求。在这里阅读更多。

LangChain还支持少镜头提示，使模型能够从示例中学习。此功能对于需要上下文理解或特定模式的任务至关重要。很少有镜头提示模板可以从一组示例或利用示例选择器对象构建。在这里阅读更多。

#####输出分析器

输出解析器在Langchain中起着至关重要的作用，使用户能够构建语言模型生成的响应。在本节中，我们将探讨输出解析器的概念，并使用Langchain的PydanticOutputParser、SimpleJsonOutputParser，CommaSeparatedListOutputParser和XMLOutputParser提供代码示例。

**PydanticOutputParser**

Langchain提供PydanticOutputParser，用于将响应解析为Pydantic数据结构。下面是一个如何使用它的分步示例：

python

#初始化语言模型

#使用Pydantic定义所需的数据结构

@验证器（“设置”）

#设置PydanticOutputParser

#使用格式说明创建提示

#定义一个查询以提示语言模型

#结合提示、模型和解析器以获得结构化输出

#使用解析器解析输出

#结果是一个结构化对象

输出将是：

![](https://nanonets.com/blog/content/images/2023/11/image-19.png)

**SimpleJsonOutputParser**

Langchain的SimpleJsonOutputParser用于解析类似JSON的输出。这里有一个例子：

python

#创建JSON提示

 # 初始化 JSON 解析器

#使用提示、模型和解析器创建链

#浏览结果

#结果是一个类似JSON的字典列表

 ** 逗号分隔的列表输出解析器 **

当您想从模型响应中提取逗号分隔的列表时，CommaSeparatedListOutputParser非常方便。这里有一个例子：

python

#初始化解析器

#创建格式说明

#创建请求列表的提示

#定义一个查询以提示模型

#生成输出

#使用解析器解析输出

#结果是一个项目列表

**日期时间输出解析器**

Langchain的DatetimeOutputParser旨在解析日期时间信息。以下是如何使用它：

python

 # 初始化 DatetimeOutputParser

#使用格式说明创建提示

prompt=PromptTemplate.from_template(

#使用提示和语言模型创建链

#定义一个查询以提示模型

#运行链条

#使用日期时间解析器解析输出

#结果是一个日期时间对象

这些示例展示了如何使用Langchain的输出解析器来构建各种类型的模型响应，使其适用于不同的应用程序和格式。输出解析器是提高Langchain中语言模型输出的可用性和可解释性的有价值的工具。

---

##模块二：检索

LangChain中的检索在需要用户特定数据的应用程序中起着至关重要的作用，这些数据不包含在模型的训练集中。这个过程被称为[检索增强生成（RAG）](https://nanonets.com/blog/what-is-retrieval-augmented-generation-rag/)，涉及获取外部数据并将其集成到语言模型的生成过程中。LangChain提供了一套全面的工具和功能来促进这一过程，既适用于简单的应用程序，也适用于复杂的应用程序。

LangChain通过一系列组件实现检索，我们将逐一讨论。

###文档加载器

LangChain中的文档加载器允许从各种来源提取数据。它们有100多个加载器可供使用，支持各种文档类型、应用程序和源（私有s3存储桶、公共网站、数据库）。

您可以根据自己的要求选择文档加载器[此处](https://python.langchain.com/docs/integrations/document_loaders).

所有这些加载器都将数据摄取到**Document**类中。稍后我们将学习如何使用引入Document类的数据。

**文本文件加载器：**将一个简单的.txt文件加载到文档中。

```bash

loader=文本加载器（“./sample.txt”）

**CSV加载器：**将CSV文件加载到文档中。

```bash

loader=csv加载器（文件路径=“./example.data/sample.csv”）

我们可以选择通过指定字段名来定制解析-

```bash

**PDF加载器：**LangChain中的PDF加载器提供了各种方法来解析和提取PDF文件中的内容。每个加载器都满足不同的要求，并使用不同的底层库。下面是每个装载机的详细示例。

PyPDFLoader is used for basic [PDF parsing](https://nanonets.com/blog/pdf-parser/).

python

loader=PyPDFLoader（“example_data/layout解析器paper.pdf”）

MathPixLoader是提取数学内容和图表的理想选择。

python

loader=MathpixPDF加载器（“example_data/math-content.pdf”）

PyMuPDFLoader速度很快，包括详细的元数据提取。

python

loader=PyMuPDFLoader（“example_data/layout解析器paper.pdf”）

#可选地为PyMuPDF的get_text（）调用传递其他参数

PDFMiner Loader用于对文本提取进行更精细的控制。

python

loader=PDFMinerLoader（“example_data/layout解析器paper.pdf”）

AmazonTextractPDFParser利用[AWS Textract](https://nanonets.com/blog/aws-textract-teardown-pros-cons-review/)用于OCR和其他高级PDF解析功能。

python

#需要AWS帐户和配置

PDFMinerPDFasHTMLLoader从PDF生成HTML进行语义解析。

python

loader=PDFMinerPDFasHTMLLoader（“example_data/layout解析器paper.pdf”）

PDFPlumberLoader提供详细的元数据，并支持每页一个文档。

python

loader=PDFPlumberLoader（“example_data/layout解析器paper.pdf”）

**集成加载器：**LangChain提供各种自定义加载器，可以直接从您的应用程序（如Slack、Sigma、Notion、Confluence、Google Drive等）和数据库加载数据，并在LLM应用程序中使用它们。

完整列表在[此处](https://python.langchain.com/docs/integrations/document_loaders).

下面是几个例子来说明这一点-

######示例I-Slack

Slack是一个广泛使用的即时通讯平台，可以集成到LLM工作流和应用程序中。

-转到Slack工作区管理页面。

python

SLACK_WORKSPACE_URL=“https://xxx.slack.com“#替换为您的Slack URL

loader=SlackDirectoryLoader（LOCAL_ZIPFILE，SLACK_WORKSPACE_URL）

######示例二-Figma

Figma是一个流行的接口设计工具，它提供了一个用于数据集成的REST API。

-从URL格式获取Figma文件密钥：`https://www.figma.com/file/{filekey}/sampleFilename`。

python

figma_loader=FigmaFileLoader(

index=VectorstoreIndexCreator（）.from_loeaders（[figma_loeader]）

-`generate_code`函数使用Figma数据创建HTML/CSS代码。

python

#建立人工智能模型

#检索相关文档

#生成和格式化提示

返回响应

#示例用法

-执行`generate_code`函数时，会根据Figma设计输入返回HTML/CSS代码。

现在让我们用我们的知识创建一些文档集。

我们首先加载一份PDF，即BCG年度可持续发展报告。

![](https://nanonets.com/blog/content/images/2023/11/image-23.png)

我们为此使用PyPDFLoader。

```bash

loader=PyPDFLoader（“bcg-2022-年度可持续性报告-2023.pdf”）

我们现在将从Airtable获取数据。我们有一个Airtable，其中包含有关各种OCR和数据提取模型的信息-

![](https://nanonets.com/blog/content/images/2023/11/image-24.png)

让我们使用集成加载器列表中的AirtableLoader来实现这一点。

```bash

api_key=“XXXXX”

loader=AirtableLoader（api_key、table_id、base_id）

现在让我们继续学习如何使用这些文档类。

###文件转换器

LangChain中的文档转换器是我们在上一小节中创建的用于操作文档的基本工具。

它们用于将长文档拆分为更小的块、组合和过滤等任务，这些任务对于使文档适应模型的上下文窗口或满足特定的应用程序需求至关重要。

其中一个工具是RecursiveCharacterTextSplitter，这是一个多功能的文本拆分器，使用字符列表进行拆分。它允许使用块大小、重叠和起始索引等参数。以下是一个在Python中如何使用它的示例：

python

state_of_the_union=“您的长文本在这里…”

text_splitter=递归字符TextSplitter(

texts=text_splitter.create_documents（[state_of_the_union]）

另一个工具是CharacterTextSplitter，它根据指定的字符分割文本，并包括块大小和重叠的控件：

python

text_splitter=字符TextSplitter(

texts=text_splitter.create_documents（[state_of_the_union]）

HTMLHeaderTextSplitter旨在根据标题标签拆分HTML内容，保留语义结构：

python

html_string=“您的html内容在此处…”

html_splitter=HTMLHeaderTextSplitter（headers_to_split_on=headers_to.split_on）

通过将HTMLHeaderTextSplitter与另一个拆分器（如Pipelined splitter）组合，可以实现更复杂的操作：

python

url=“https://example.com"

chunk_size=500

LangChain还为不同的编程语言提供了特定的拆分器，如Python代码拆分器和JavaScript代码拆分器：

python

python_code=“”“

python_splitter=递归字符TextSplitter.from_language(

js_code=“”“

js_splitter=递归字符TextSplitter.from_language(

为了基于令牌计数拆分文本，这对具有令牌限制的语言模型很有用，我们使用了TokenTextSplitter：

python

text_splitter=TokenTextSplitter（chunk_size=10）

最后，LongContextReorder对文档进行重新排序，以防止由于长上下文导致的模型性能下降：

python

重新排序=LongContextReorder（）

这些工具演示了在LangChain中转换文档的各种方法，从简单的文本拆分到复杂的重新排序和特定语言的拆分。对于更深入和具体的用例，应参考LangChain文档和集成部分。

在我们的示例中，加载器已经为我们创建了分块文档，这部分已经处理完毕。

###文本嵌入模型

LangChain中的文本嵌入模型为OpenAI、Cohere和Hugging Face等各种嵌入模型提供商提供了一个标准化的接口。这些模型将文本转换为向量表示，实现了通过向量空间中的文本相似性进行语义搜索等操作。

要开始使用文本嵌入模型，通常需要安装特定的软件包并设置API密钥。我们已经为OpenAI完成了这项工作

在LangChain中，`embed_documents`方法用于嵌入多个文本，提供向量表示列表。例如：

python

#初始化模型

#嵌入文本列表

对于嵌入单个文本，如搜索查询，使用`embed_query`方法。这对于将查询与一组文档嵌入进行比较非常有用。例如：

python

#初始化模型

#嵌入单个查询

理解这些嵌入是至关重要的。每条文本都转换为向量，向量的维度取决于所使用的模型。例如，OpenAI模型通常产生1536维向量。然后，这些嵌入用于检索相关信息。

LangChain的嵌入功能不仅限于OpenAI，而是旨在与各种提供商合作。设置和使用可能因提供者而异，但将文本嵌入向量空间的核心概念保持不变。有关详细的使用方法，包括高级配置和与不同嵌入模型提供程序的集成，集成部分中的LangChain文档是一个宝贵的资源。

####矢量存储

LangChain中的矢量存储支持文本嵌入的高效存储和搜索。LangChain与50多个矢量商店集成，提供易于使用的标准化界面。

**示例：存储和搜索嵌入**

嵌入文本后，我们可以将它们存储在像“Chroma”这样的向量存储中，并执行相似性搜索：

python

db=色度从文本（嵌入文本）

让我们使用FAISS向量存储为文档创建索引。

```bash

pdfstore=文件失败（pdf页，

airtablestore=FAISS.from_documents（airtabledocs，

####寻回犬

LangChain中的检索器是响应非结构化查询返回文档的接口。它们比向量存储更通用，专注于检索而不是存储。虽然矢量存储可以用作检索器的骨干，但也有其他类型的检索器。

要设置Chroma检索器，您首先使用`pip install chromadb`安装它。然后，您可以使用一系列Python命令加载、拆分、嵌入和检索文档。下面是一个设置Chroma检索器的代码示例：

python

full_text=open（“state_of_the_union.txt”，“r”）.read（）

嵌入=OpenAIEmbeddings（）

retrieved_docs=retriever.invoke（“总统对凯坦吉·布朗·杰克逊说了什么？”）

MultiQueryRetriever通过为用户输入查询生成多个查询并组合结果来自动进行提示调优。以下是其简单用法的示例：

python

问题=“任务分解的方法是什么？”

unique_docs=检索器_from_llm.get_relatent_documents（查询=问题）

LangChain中的上下文压缩使用查询的上下文压缩检索到的文档，确保只返回相关信息。这涉及内容减少和过滤不太相关的文档。以下代码示例显示了如何使用上下文压缩检索器：

python

llm=OpenAI（温度=0）

compressed_docs=compression_retriever.get_relatent_documents（“总统对凯坦吉·杰克逊·布朗说了什么”）

EnsembleRetriever结合了不同的检索算法以实现更好的性能。以下代码显示了组合BM25和FAISS检索器的示例：

python

bm25_retriever=BM25Retriever.from_texts（doc_list）.set_k（2）

ensemble_receiver=集合检索器(

docs=ensemble_requirer.get_relevant_documents（“apples”）

LangChain中的MultiVector Retriever允许查询每个文档有多个向量的文档，这对于捕获文档中的不同语义方面非常有用。创建多个向量的方法包括分成更小的块、总结或生成假设问题。为了将文档分割成更小的块，可以使用以下Python代码：

```bash

loaders=[文本加载器（“file1.txt”），文本加载器（”file2.txt“）]

vectorstore=Chroma（collection_name=“full_documents”，embedding_function=OpenAIEmbeddings（））

doc_ids=[文档中_的str（uuid.uuid4（））]

retriever.vectorstore.add_documents（sub_docs）

由于内容表示更加集中，生成摘要以进行更好的检索是另一种方法。以下是生成摘要的示例：

python

chain=（lambda x:x.page_content）|ChatPromptTemplate.from_template（“总结以下文档：\n\n{doc}”）|ChatOpenAI（max_retrys=0）|StrOutputParser（）

summary_docs=[枚举（摘要）中i，s的文档（page_content=s，元数据={id_key:doc_ids[i]}）]

使用LLM生成与每个文档相关的假设问题是另一种方法。这可以通过以下代码完成：

python

chain=（lambda x:x.page_content）|ChatPromptTemplate.from_template（“生成3个假设问题：\n\n{doc}”）|ChatOpenAI（max_retrys=0）.bind（functions=functions，function_call={“name”：“hypotential_questions”}）|JsonKeyOutputFunctionsParser（key_name=“questions”）

question_docs=[文档（page_content=q，元数据={id_key:doc_ids[i]}）用于i，问题中q的枚举问题（假设问题）]

父文档检索器是另一种检索器，它通过存储小块和检索较大的父文档，在嵌入准确性和上下文保留之间取得平衡。其实施如下：

python

loaders=[文本加载器（“file1.txt”），文本加载器（”file2.txt“）]

child_splitter=递归字符TextSplitter（chunk_size=400）

retriever.add_documents（文档，ids=无）

retrieved_docs=retriever.get_relevant_documents（“query”）

自查询检索器从自然语言输入构建结构化查询，并将其应用于其底层的VectorStore。其实现如以下代码所示：

python

元数据字段信息=[AttributeInfo（名称=“流派”，描述=“…”，类型=“字符串”），…]

retriever=SelfQueryRetriever.from_llm（llm，向量库，文档内容描述，元数据字段信息）

retrieved_docs=retriever.invoke（“query”）

WebResearchRetriever根据给定的查询执行web研究-

```bash

#初始化组件

#实例化WebResearchRetriever

#检索文档

对于我们的示例，我们还可以使用已经作为向量存储对象的一部分实现的标准检索器，如下所示-

![](https://nanonets.com/blog/content/images/2023/11/image-26.png)

我们现在可以查询检索器。查询的输出将是与查询相关的文档对象。这些最终将用于在后续章节中创建相关响应。

![](https://nanonets.com/blog/content/images/2023/11/image-27.png)

![](https://nanonets.com/blog/content/images/2023/11/image-28.png)

---

##模块三：代理人

LangChain引入了一个名为“代理”的强大概念，将链的概念提升到了一个全新的水平。代理利用语言模型动态确定要执行的动作序列，使其具有令人难以置信的通用性和适应性。与传统的链不同，在传统的链中，动作被硬编码在代码中，代理使用语言模型作为推理引擎来决定采取哪些动作以及以什么顺序采取。

**Agent**是负责决策的核心组件。它利用语言模型和提示的力量来确定实现特定目标的下一步。代理的输入通常包括：

-**工具：**可用工具的描述（稍后将详细介绍）。

---

代理的输出可以是下一个**动作**（**AgentActions**）或发送给用户的最终**响应**（**AgentFinish**）。**动作**指定**工具**和该工具的**输入**。

---

###工具

工具是代理可以用来与世界交互的接口。它们使代理能够执行各种任务，例如搜索网络、运行shell命令或访问外部API。在LangChain中，工具对于扩展代理的功能并使其能够完成各种任务至关重要。

要使用LangChain中的工具，您可以使用以下代码段加载它们：

python

工具名称=[…]

某些工具可能需要基础语言模型（LLM）才能初始化。在这种情况下，你也可以通过法学硕士：

python

工具名称=[…]

此设置允许您访问各种工具并将其集成到代理的工作流中。带有使用文档的完整工具列表位于[此处](https://python.langchain.com/docs/integrations/tools).

让我们来看一些工具的例子。

######DuckDuckGo

DuckDuckGo工具使您能够使用其搜索引擎进行网络搜索。以下是如何使用它：

```bash

DataForSeo

DataForSeo工具包允许您使用DataForSeoneneneba API获取搜索引擎结果。若要使用此工具包，您需要设置API凭据。以下是如何配置凭据：

python

os.environ[“DATAFORSEO_LOGIN”] =“<您的_api_访问_用户名>”

设置凭据后，您可以创建“DataForSeoAPIWrapper”工具来访问API：

python

包装器=DataForSeoAPIWrapper（）

result=wrapper.run（“洛杉矶天气”）

`DataForSeoAPIWrapper`工具从各种来源检索搜索引擎结果。

您可以自定义JSON响应中返回的结果和字段的类型。例如，您可以指定结果类型、字段，并为要返回的顶级结果的数量设置最大计数：

python

json_result = json_wrapper.results（“比尔·盖茨”）

此示例通过指定结果类型、字段和限制结果数量来定制JSON响应。

您还可以通过向API包装器传递附加参数来指定搜索结果的位置和语言：

python

customized_result=customized_wrapper.results（“我附近的咖啡”）

通过提供位置和语言参数，您可以根据特定地区和语言定制搜索结果。

您可以灵活选择要使用的搜索引擎。只需指定所需的搜索引擎：

python

customized_result=customized_wrapper.results（“我附近的咖啡”）

在这个例子中，搜索被定制为使用Bing作为搜索引擎。

API包装还允许您指定要执行的搜索类型。例如，您可以执行地图搜索：

python

maps_search_result=maps_search.results（“我附近的咖啡”）

这将定制搜索以检索地图相关信息。

######外壳（bash）

Shell工具包为代理提供了对Shell环境的访问，允许他们执行Shell命令。此功能功能强大，但应谨慎使用，特别是在沙盒环境中。以下是如何使用Shell工具：

python

shell_tool=ShellTool（）

result=shell_tool.run（{“命令”：[“echo‘Hello World！’”，“time”]}）

在这个例子中，Shell工具运行两个Shell命令：回显“Hello World！”和显示当前时间。

![](https://nanonets.com/blog/content/images/2023/11/image-30.png)

您可以向代理提供Shell工具以执行更复杂的任务。下面是一个代理使用Shell工具从网页获取链接的示例：

python

llm=ChatOpenAI（温度=0.1）

shell_tool.description=shell_tool.description+f“args{shell_tool.args}”。替换(

在这种情况下，代理使用Shell工具执行一系列命令，从网页中获取、过滤和排序URL。

提供的示例演示了LangChain中可用的一些工具。这些工具最终扩展了代理的功能（将在下一小节中探讨），并使它们能够高效地执行各种任务。根据您的要求，您可以选择最适合项目需求的工具和工具包，并将其集成到代理的工作流程中。

###回到代理

现在让我们转向代理人。

AgentExecutor是代理的运行时环境。它负责调用代理，执行它选择的操作，将操作输出传递回代理，并重复该过程，直到代理完成。在伪代码中，AgentExecutor可能看起来像这样：

python

AgentExecutor处理各种复杂性，例如处理代理选择不存在的工具的情况、处理工具错误、管理代理生成的输出，以及在各个级别提供日志记录和可观察性。

虽然AgentExecutor类是LangChain中的主要代理运行时，但还支持其他更具实验性的运行时，包括：

-计划并执行代理

为了更好地理解代理框架，让我们从头开始构建一个基本的代理，然后继续探索预构建的代理。

在我们深入构建代理之前，有必要重新审视一些关键术语和模式：

-**代理操作：**这是一个数据类，表示代理应该采取的操作。它由“tool”属性（要调用的工具的名称）和“tool_input”属性（该工具的输入）组成。

在我们的示例中，我们将使用OpenAI函数调用来创建我们的代理。这种方法对于创建代理是可靠的。我们将首先创建一个计算单词长度的简单工具。这个工具很有用，因为语言模型在计算单词长度时有时会因标记化而出错。

首先，让我们加载用于控制代理的语言模型：

python

llm=ChatOpenAI（型号=“gpt-3.5涡轮增压”，温度=0）

让我们用字长计算来测试模型：

python

回复应注明“educa”一词中的字母数

接下来，我们将定义一个简单的Python函数来计算单词的长度：

python

@工具

我们创建了一个名为`get_word_length`的工具，它接受一个单词作为输入并返回其长度。

现在，让我们为代理创建提示。提示指示代理如何推理和格式化输出。在我们的例子中，我们使用的是OpenAI函数调用，它需要最少的指令。我们将使用占位符为用户输入和代理草稿栏定义提示：

python

prompt=ChatPromptTemplate.from_message(

现在，代理如何知道它可以使用哪些工具？我们依赖于OpenAI函数调用语言模型，这需要单独传递函数。为了向代理提供我们的工具，我们将把它们格式化为OpenAI函数调用：

python

llm_with_tools=llm.bind（函数=[工具中t的format_tool_to_openai_function（t）]）

现在，我们可以通过定义输入映射并连接组件来创建代理：

*这是LCEL语言。我们稍后将对此进行详细讨论*

python

代理=(

_函数消息(

我们已经创建了我们的代理，它理解用户输入，使用可用的工具，并格式化输出。现在，让我们与它互动：

python

代理应使用AgentAction进行响应，指示要采取的下一个操作。

我们已经创建了代理，但现在我们需要为它编写一个运行时。最简单的运行时是连续调用代理、执行操作并重复直到代理完成的运行时。这里有一个例子：

python

user_input=“educa这个词有多少个字母？”

虽然为True：

打印（最终结果）

在这个循环中，我们反复调用代理，执行操作，并更新中间步骤，直到代理完成。我们还处理循环中的工具交互。

![](https://nanonets.com/blog/content/images/2023/11/image-33.png)

为了简化这一过程，LangChain提供了AgentExecutor类，该类封装了代理执行，并提供了错误处理、早期停止、跟踪和其他改进。让我们使用AgentExecutor与代理进行交互：

python

agent_executor=代理执行器（代理=代理，工具=工具，详细信息=True）

agentexecutor.invoke（{“input”：“单词educa中有多少个字母？”}）

AgentExecutor简化了执行过程，并提供了一种与代理交互的便捷方式。

*稍后还将详细讨论内存*

到目前为止，我们创建的代理是无状态的，这意味着它不记得以前的交互。为了实现后续问题和对话，我们需要为代理添加内存。这涉及两个步骤：

1.在提示中添加一个内存变量来存储聊天历史记录。

让我们从在提示符中添加一个内存占位符开始：

python

MEMORY_KEY=“聊天历史”

现在，创建一个列表来跟踪聊天记录：

python

聊天历史=[]

在代理创建步骤中，我们还将包括内存：

python

现在，在运行代理时，请确保更新聊天历史记录：

python

这使代理能够维护对话历史记录，并根据之前的交互回答后续问题。

祝贺您已在LangChain中成功创建并执行了第一个端到端代理。要深入了解LangChain的功能，您可以探索：

-支持不同的代理类型。

######代理类型

LangChain提供各种代理类型，每种类型都适合特定的用例。以下是一些可用的代理：

-**零样本ReAct:**此代理使用ReAct框架仅根据工具的描述来选择工具。它需要对每个工具进行描述，并且用途广泛。

探索这些代理类型，在LangChain中找到最适合您需求的代理。这些代理允许您在其中绑定一组工具来处理操作并生成响应。了解更多关于[如何在此处使用工具构建自己的代理]的信息(https://www.youtube.com/watch?v=Q8JLSm-哈克）。

######预构建代理

让我们继续探索代理，重点关注LangChain中可用的预构建代理。

**Gmail**

LangChain提供Gmail工具包，允许您将LangChain电子邮件连接到Gmail API。为了开始，你需要设置你的凭据，这在Gmail API文档中有解释。一旦您下载了`credentials.json`文件，您就可以继续使用Gmail API。此外，您需要使用以下命令安装一些必需的库：

python

您可以按如下方式创建Gmail工具包：

python

toolkit=GmailToolkit（）

您还可以根据需要自定义身份验证。在幕后，使用以下方法创建googleapi资源：

python

凭据=get_gmail_credentials(

该工具包提供了可在代理中使用的各种工具，包括：

-`GmailCreateDraft`：使用指定的消息字段创建电子邮件草稿。

要在代理中使用这些工具，可以按如下方式初始化代理：

python

llm=OpenAI（温度=0）

以下是一些如何使用这些工具的示例：

1.创建Gmail草稿进行编辑：

python

1.在草稿中搜索最新电子邮件：

python

这些示例演示了LangChain的Gmail工具包在代理中的功能，使您能够以编程方式与Gmail交互。

**SQL数据库代理**

本节概述了一个旨在与SQL数据库交互的代理，特别是Chinook数据库。此代理可以回答有关数据库的一般问题并从错误中恢复。请注意，它仍在积极开发中，并非所有答案都是正确的。在敏感数据上运行它时要小心，因为它可能会在数据库上执行DML语句。

要使用此代理，您可以按如下方式对其进行初始化：

python

db=SQL数据库.from_uri（“sqlite:///../../../../../notebooks/Chinook.db")

agentexecutor=create_sql_agent(

此代理可以使用“ZERO_SHOT_REACT_DRIPTION”代理类型进行初始化。它旨在回答问题并提供描述。或者，您可以使用OPENAI的GPT-3.5-turbo模型的“OPENAI_FUNCTIONS”代理类型初始化代理，我们在早期的客户端中使用了该模型。

---

**免责声明**

-查询链可以生成插入/更新/删除查询。要小心，如果需要，可以使用自定义提示或创建没有写权限的SQL用户。

---

您可以要求代理描述一个表，例如“播放列表跟踪”表。以下是一个示例：

python

代理将提供有关表的模式和示例行的信息。

如果您错误地询问了不存在的表，代理可以恢复并提供有关最接近匹配表的信息。例如：

python

代理将找到最近的匹配表并提供有关它的信息。

您还可以要求代理在数据库上运行查询。例如：

python

代理商将执行查询并提供结果，例如总销售额最高的国家。

要获取每个播放列表中的曲目总数，可以使用以下查询：

python

代理将返回播放列表名称以及相应的曲目总数。

在代理遇到错误的情况下，它可以恢复并提供准确的响应。例如：

python

即使在遇到初始错误后，代理也会进行调整并提供正确的答案，在这种情况下，这是最畅销的三位艺术家。

 **Pandas 数据框架代理**

本节介绍一个代理，旨在与Pandas DataFrames交互以进行问答。请注意，此代理在后台使用Python代理来执行由语言模型（LLM）生成的Python代码。使用此代理时请务必小心，以防止LLM生成的恶意Python代码造成潜在危害。

您可以按如下方式初始化Pandas DataFrame代理：

python

从langchain.llms导入OpenAI

df=pd.read_csv（“titanic.csv”）

#使用ZERO_SHOT_REACT_DRIPTION代理类型

#或者，使用OPENAI_FUNCTIONS代理类型

您可以要求代理计算DataFrame中的行数：

python

代理将执行代码`df.shape[0]`并提供答案，例如“数据帧中有891行。”

您还可以要求代理根据特定条件过滤行，例如查找有3个以上兄弟姐妹的人数：

python

代理将执行代码`df[df['SibSp']>3].shape[0]`并提供答案，例如“30个人有3个以上的兄弟姐妹。”

如果你想计算平均年龄的平方根，你可以问代理人：

python

代理将使用`df['age'].mean（）`计算平均年龄，然后使用`math.sqrt（）`来计算平方根。它将提供答案，例如“平均年龄的平方根为5.449689683556195。”

让我们创建DataFrame的副本，缺失的年龄值用平均年龄填充：

python

然后，您可以使用两个DataFrames初始化代理并向其提问：

python

代理将比较两个DataFrames中的年龄列并提供答案，例如“年龄列中的177行不同”

 **使用工具包**

本节介绍如何使用Jira工具包，该工具包允许代理与Jira实例进行交互。您可以使用此工具包执行各种操作，例如搜索问题和创建问题。它使用atlasian python api库。要使用此工具包，您需要为Jira实例设置环境变量，包括Jira\_API\_TOKEN、Jira\_USERNAME和Jira\_instance\_URL。此外，您可能需要将OpenAI API键设置为环境变量。

要开始使用，请安装atlassian python api库并设置所需的环境变量：

python

导入操作系统

os.environ[“JIRA-API-TOKEN”]=“ABC”

llm=OpenAI（温度=0）

您可以指示代理在特定项目中创建一个新问题，并附上摘要和描述：

python

代理将执行必要的操作来创建问题并提供响应，例如“在项目PW中创建了一个新问题，其中包含摘要‘制作更多炒饭’和描述‘提醒制作更多炒饭‘。”

这允许您使用自然语言指令和Jira工具包与Jira实例进行交互。

---

##模块四：链条

LangChain是一个专为在复杂应用程序中使用大型语言模型（LLM）而设计的工具。它提供了创建组件链的框架，包括LLM和其他类型的组件。两个主要框架

-LangChain表达式语言（LCEL）

LangChain表达式语言（LCEL）是一种允许直观组合链的语法。它支持流式传输、异步调用、批处理、并行化、重试、回退和跟踪等高级功能。例如，您可以在LCEL中组合一个提示、模型和输出解析器，如下代码所示：

python

型号=ChatOpenAI（型号=“gpt-3.5-turbo”，温度=0）

对于runnable.stream中的chunk（{“问题”：“世界七大奇迹是什么”}）：

或者，LLMChain是一种类似于LCEL的组件组合选项。LLMChain示例如下：

python

chain=LLMChain（llm=model，prompt=prompt，output_passer=StrOutputParser（））

LangChain中的链也可以通过合并Memory对象来实现有状态。这允许跨调用的数据持久性，如本例所示：

python

会话=会话链（llm=聊天，内存=会话缓冲内存（））

LangChain还支持与OpenAI的函数调用API集成，这对于获取结构化输出和在链中执行函数非常有用。为了获得结构化输出，您可以使用Pydantic类或JsonSchema指定它们，如下所示：

python

类人员（基本模型）：

llm=ChatOpenAI（模型=“gpt-4”，温度=0）

runnable=create_structured_output_runnable（Person、llm、prompt）

对于结构化输出，还可以使用LLMChain的传统方法：

python

类人员（基本模型）：

chain=create_structured_output_chain（Person、llm、prompt、verbose=True）

LangChain利用OpenAI函数为不同目的创建各种特定链。这些包括用于提取、标记、OpenAPI和带有引用的QA的链。

在提取的背景下，该过程类似于结构化输出链，但侧重于信息或实体提取。对于标记，我们的想法是用情感、语言、风格、涵盖的主题或政治倾向等类来标记文档。

可以用Python代码演示标记在LangChain中的工作原理。该过程从安装必要的软件包和设置环境开始：

python

从langchain.chat_models导入ChatOpenAI

定义了标记模式，指定了属性及其预期类型：

python

llm=ChatOpenAI（温度=0，型号=“gpt-3.5涡轮-0613”）

使用不同输入运行标记链的示例显示了模型解释情感、语言和攻击性的能力：

```蟒蛇

“我对你很生气！我会给你应得的！”

为了进行更精细的控制，可以更具体地定义模式，包括可能的值、描述和所需的属性。下面显示了这种增强控制的示例：

python

chain=create_tagging_chain（模式，llm）

Pydantic模式也可用于定义标记标准，提供了一种Python式的方法来指定所需的属性和类型：

python

类标签（BaseModel）：

chain=create_tagging_chain_pydantic（标签，llm）

此外，LangChain的元数据标记器文档转换器可用于从LangChain文档中提取元数据，提供与标记链类似的功能，但应用于LangChain文档。

引用检索源是LangChain的另一个功能，它使用OpenAI函数从文本中提取引用。以下代码演示了这一点：

python

llm=ChatOpenAI（温度=0，型号=“gpt-3.5涡轮-0613”）

在LangChain中，大型语言模型（LLM）应用程序中的链接通常涉及将提示模板与LLM以及可选的输出解析器组合在一起。推荐的方法是通过LangChain表达式语言（LCEL），尽管也支持传统的LLMChain方法。

使用LCEL，BasePromptTemplate、BaseLanguageModel和BaseOutputParser都实现了Runnable接口，并且可以很容易地相互连接。以下是一个示例：

python

prompt=PromptTemplate.from_template(

LangChain中的路由允许创建非确定性链，其中前一步的输出决定了下一步。这有助于构建和保持与LLM交互的一致性。例如，如果你有两个针对不同类型问题优化的模板，你可以根据用户输入选择模板。

以下是如何使用LCEL和RunnableBranch来实现这一点，Runnablebranc用（condition，runnable）对列表和默认的runnable初始化：

python

general_prompt=PromptTemplate.from_template(

#设置分类器和最终链的更多代码

然后，使用各种组件（如主题分类器、提示分支和输出解析器）构建最终链，以根据输入的主题确定流：

python

final_chain=(

final_chain.invoke(

这种方法体现了LangChain在处理复杂查询和根据输入适当路由查询方面的灵活性和强大功能。

在语言模型领域，一种常见的做法是在初始调用之后进行一系列后续调用，将一个调用的输出用作下一个调用。当您希望基于之前交互中生成的信息进行构建时，这种顺序方法尤其有益。虽然LangChain表达式语言（LCEL）是创建这些序列的推荐方法，但SequentialChain方法仍因其向后兼容性而被记录在案。

为了说明这一点，让我们考虑一个场景，在这个场景中，我们首先生成一个游戏概要，然后根据该概要生成一个评论。使用Python的“langchain.thints”，我们创建了两个“PromptTemplate”实例：一个用于概要，另一个用于评论。以下是设置这些模板的代码：

python

synopsis_frompt=PromptTemplate.from_template(

review_prompt=PromptTemplate.from_template(

在LCEL方法中，我们使用“ChatOpenAI”和“StrOutputParser”将这些提示链接起来，以创建一个序列，该序列首先生成概要，然后生成评论。代码片段如下：

python

llm=ChatOpenAI（）

如果我们需要概要和评论，我们可以使用`RunnablePassthrough `为每一个创建一个单独的链，然后将它们组合在一起：

python

synopsis_chain=synopsis_front|llm|StrOutputParser（）

对于涉及更复杂序列的场景，“SequentialChain”方法开始发挥作用。这允许多个输入和输出。考虑一个案例，我们需要一个基于戏剧标题和时代的概要。以下是我们如何设置它：

python

llm=OpenAI（温度=0.7）

synopsis_template=“你是一名剧作家。鉴于该剧的标题及其所处的时代，你的工作是为该剧写一个梗概。\n\n标题：｛title｝\n背景：｛era｝\n剧作家：这是上述剧的梗概：”

review_template=“您是《纽约时报》的戏剧评论家。鉴于该剧的剧情简介，您的工作是为该剧写一篇评论。\n\n戏剧简介：\n{剧情简介}\n来自《纽约邮报》戏剧评论家对上述戏剧的评论：”

overall_chain=序列链(

overall_chain（{“title”：“海滩上日落时的悲剧”，“era”：“维多利亚时代的英格兰”}）

在您希望在整个链或链的后期维护上下文的情况下，可以使用“SimpleMemory”。这对于管理复杂的输入/输出关系特别有用。例如，在我们想根据戏剧的标题、时代、概要和评论生成社交媒体帖子的情况下，“SimpleMemory”可以帮助管理这些变量：

python

template=“你是一家戏剧公司的社交媒体经理。考虑到戏剧的标题、所处的时代、日期、时间和地点、戏剧的梗概以及戏剧的评论，

为该剧撰写社交媒体帖子是你的职责。\n\n以下是关于该剧的时间和地点的一些背景：\n日期和时间：｛time｝\n地点：｛location｝\n\n戏剧概要：\n｛概要｝\n《纽约时报》戏剧评论家对上述戏剧的评论：\n{评论}\n\n社交媒体帖子：“

overall_chain=序列链(

overall_chain（{“title”：“海滩上日落时的悲剧”，“era”：“维多利亚时代的英格兰”}）

除了顺序链之外，还有用于处理文档的专用链。这些链中的每一个都有不同的目的，从组合文档到基于迭代文档分析细化答案，再到映射和减少文档内容，以便根据评分的回复进行总结或重新排名。这些链可以用LCEL重新创建，以获得额外的灵活性和定制性。

-“StuffDocumentsChain”将一系列文档合并到一个传递给LLM的提示中。

以下是一个使用LCEL设置“MapReduceDocumentsChain”的示例：

python

llm=聊天人类学（）

map_chain=(

map_as_doc_chain=(

def format_docs（文档）：

collapse_chain=(

reduce_chain=(

map_reduce=（map_as_doc_chain.map（）| collapse | reduce_chain）。with_config（run_name=“map-reduce”）

这种配置允许对文档内容进行详细和全面的分析，利用LCEL和底层语言模型的优势。

---

##模块五：内存

在LangChain中，记忆是会话界面的一个基本方面，允许系统引用过去的交互。这是通过存储和查询信息来实现的，主要有两个动作：读取和写入。存储系统在运行过程中与链交互两次，增加用户输入并存储输入和输出以供将来参考。

**将内存构建到系统中**

1.**存储聊天消息：**LangChain内存模块集成了各种存储聊天消息的方法，从内存列表到数据库。这确保了所有聊天互动都被记录下来以供将来参考。

为了演示LangChain中内存的使用，请考虑“ConversationBufferMemory”类，这是一种将聊天消息存储在缓冲区中的简单内存形式。这里有一个例子：

python

内存=会话缓冲内存（）

在将内存集成到链中时，了解从内存返回的变量以及它们在链中的使用方式至关重要。例如，`load_memory_vables`方法有助于将从内存中读取的变量与链的期望值对齐。

**LangChain端到端示例**

考虑在LLMChain中使用ConversationBufferMemory。该链与适当的提示模板和记忆相结合，提供了无缝的对话体验。下面是一个简化的例子：

python

llm=OpenAI（温度=0）

response=对话（{“问题”：“天气怎么样？”}）

这个例子说明了LangChain的记忆系统如何与其链集成，以提供连贯和上下文感知的对话体验。

**Langchain中的内存类型**

Langchain提供了各种内存类型，可用于增强与AI模型的交互。每种内存类型都有自己的参数和返回类型，使其适用于不同的场景。让我们结合代码示例来探索Langchain中可用的一些内存类型。

1.对话缓冲存储器**

此内存类型允许您存储和提取对话中的消息。您可以将历史记录提取为字符串或消息列表。

python

内存=会话缓冲内存（）

#将历史记录提取为字符串

#将历史记录提取为消息列表

您还可以在链中使用会话缓冲存储器进行类似聊天的交互。

2.对话缓冲区窗口内存**

这种内存类型保存最近交互的列表，并使用最后K次交互，防止缓冲区变得太大。

python

内存=转换缓冲窗口内存（k=1）

{“历史”：“人类：不多你：不多”}

与对话缓冲存储器一样，您也可以在链中使用这种存储器类型进行类似聊天的交互。

3.对话实体内存**

这种内存类型会记住对话中特定实体的事实，并使用LLM提取信息。

python

llm=OpenAI（温度=0）

{“历史”：“人类：Deven和Sam正在进行一个黑客马拉松项目\nAI：听起来是个很棒的项目！他们正在进行什么样的项目？”，

4.会话知识图记忆**

这种内存类型使用知识图来重建内存。您可以从消息中提取当前实体和知识三元组。

python

llm=OpenAI（温度=0）

{“历史”：“关于萨姆：萨姆是朋友。”}

您还可以在链中使用此内存类型进行基于对话的知识检索。

5.对话摘要记忆**

这种记忆类型创建了一段时间内对话的摘要，有助于从较长的对话中提炼信息。

python

llm=OpenAI（温度=0）

{“历史”：“人类向人工智能致意，人工智能会做出回应。”}

6.对话摘要缓冲存储器**

这种内存类型结合了对话摘要和缓冲区，在最近的交互和摘要之间保持平衡。它使用令牌长度来确定何时刷新交互。

python

llm=OpenAI（）

{'历史'：'系统：\n人类说“嗨”，人工智能回答“怎么了”。\n人类：你不多\nAI：不多'

您可以使用这些内存类型来增强与Langchain中的AI模型的交互。每种内存类型都有特定的用途，可以根据您的要求进行选择。

7.对话令牌缓冲存储器**

ConversationTokenBufferMemory是另一种内存类型，用于在内存中保存最近交互的缓冲区。与之前关注交互数量的内存类型不同，这次使用令牌长度来确定何时刷新交互。

在LLM中使用内存：

python

llm=OpenAI（）

内存=会话令牌缓冲内存（llm=llm，max_token_limit=10）

memory.load_memoryvariables（{}）

{“历史”：“人类：不多你：不多”}

在这个例子中，内存被设置为根据令牌长度而不是交互次数来限制交互。

使用此内存类型时，您还可以将历史记录作为消息列表获取。

python

在链中使用：

您可以在链中使用ConversationTokenBufferMemory来增强与AI模型的交互。

python

conversation_with_summary=对话链(

在这个例子中，ConversationTokenBufferMemory在ConversationChain中用于管理对话，并根据令牌长度限制交互。

 **8。VectorStoreRetriever内存**

VectorStoreRetrieverMemory将内存存储在向量存储中，并在每次调用时查询前K个最“突出”的文档。这种内存类型不会明确跟踪交互顺序，而是使用向量检索来获取相关内存。

python

#初始化向量存储（具体取决于所选的向量存储）

embedding_size=1536#OpenAI嵌入的维度

#创建您的VectorStoreRetrieverMemory

#将上下文和相关信息保存到内存中

#根据查询从内存中检索相关信息

在这个例子中，VectorStoreRetrieverMemory用于存储和检索基于向量检索的对话中的相关信息。

您还可以在链中使用VectorStoreRetrieverMemory进行基于对话的知识检索，如前面的示例所示。

Langchain中的这些不同内存类型提供了各种方法来管理和检索对话中的信息，增强了人工智能模型理解和响应用户查询和上下文的能力。每种内存类型都可以根据应用程序的具体要求进行选择。

---

现在我们将学习如何使用LLMChain的内存。LLMChain中的内存允许模型记住之前的交互和上下文，以提供更连贯和上下文感知的响应。

要在LLMChain中设置内存，您需要创建一个内存类，例如ConversationBufferMemory。以下是如何设置它：

python

template=“”“您是一个与人类对话的聊天机器人。

{聊天历史}

prompt=PromptTemplate(

llm=OpenAI（）

llm_chain.precent（human_input=“你好，我的朋友”）

在这个例子中，ConversationBufferMemory用于存储对话历史记录。`memory_key`参数指定用于存储对话历史的密钥。

如果你使用的是聊天模型而不是完成风格模型，你可以用不同的方式组织提示，以更好地利用内存。以下是一个如何使用内存设置基于聊天模型的LLMChain的示例：

python

#创建聊天提示模板

memory=ConversationBufferMemory（memory_key=“chat_history”，return_messages=True）

llm = ChatOpenAI（）

chat_llm_chain=LLMChain(

chat_llm_chain.predict（human_input=“你好，我的朋友”）

在这个例子中，ChatPromptTemplate用于构建提示，ConversationBufferMemory用于存储和检索对话历史。这种方法对于上下文和历史起着至关重要作用的聊天式对话特别有用。

内存也可以添加到具有多个输入的链中，例如问答链。以下是一个如何在问答链中设置内存的示例：

python

#将长文档拆分为更小的块

#创建一个ElasticVectorSearch实例来索引和搜索文档块

#对文档进行提问

#为带记忆的问答链设置提示

给定一个长文档的以下摘录部分和一个问题，创建一个最终答案。

{上下文}

{聊天历史}

prompt=PromptTemplate(

#提出问题并检索答案

打印（结果）

在这个例子中，使用分割成小块的文档来回答问题。ConversationBufferMemory用于存储和检索对话历史，使模型能够提供上下文感知的答案。

向代理添加内存使其能够记住并使用之前的交互来回答问题并提供上下文感知的响应。以下是如何在代理中设置内存：

python

#创建搜索工具

#使用内存创建提示

{聊天历史}

提示=ZeroShotAgent.create_prompt(

#创建具有内存的LLMChain

#提出问题并检索答案

在加拿大？")

#提出后续问题

在这个例子中，内存被添加到代理中，使其能够记住之前的对话历史并提供上下文感知的答案。这使得代理能够根据存储在内存中的信息准确回答后续问题。

##LangChain表达式语言

在自然语言处理和机器学习领域，构建复杂的操作链可能是一项艰巨的任务。幸运的是，LangChain表达式语言（LCEL）提供了一种声明性和高效的方法来构建和部署复杂的语言处理管道。LCEL旨在简化链的组装过程，使其能够轻松地从原型制作到生产。在本博客中，我们将探讨什么是LCEL以及为什么您可能想要使用它，并提供实际的代码示例来说明它的功能。

LCEL，即LangChain表达式语言，是构建语言处理链的强大工具。它是专门为支持从原型到生产的无缝过渡而构建的，不需要大量的代码更改。无论您是构建一个简单的“提示+LLM”链，还是构建一个包含数百个步骤的复杂管道，LCEL都能满足您的需求。

以下是在语言处理项目中使用LCEL的一些原因：

1.快速令牌流：LCEL实时将令牌从语言模型传递到输出解析器，提高了响应速度和效率。

现在，让我们深入了解演示LCEL强大功能的实际代码示例。我们将探讨LCEL的常见任务和场景。

###提示+LLM

最基本的组合涉及将提示和语言模型组合在一起，以创建一个链，该链接收用户输入，将其添加到提示中，将其传递给模型，并返回原始模型输出。这里有一个例子：

python

prompt=ChatPromptTemplate.from_template（“给我讲一个关于{foo}的笑话”）

result=chain.require（{“foo”：“bears”}）

在这个例子中，链条产生了一个关于熊的笑话。

您可以将停止序列附加到链上，以控制它如何处理文本。例如：

python

当遇到换行符时，此配置会停止文本生成。

LCEL支持将函数调用信息附加到链中。这里有一个例子：

python

此示例附加函数调用信息以生成笑话。

###提示+LLM+输出解析器

您可以添加一个输出解析器，将原始模型输出转换为更可行的格式。您可以这样做：

python

chain=prompt|model|StrOutputParser（）

输出现在是字符串格式，这对下游任务更方便。

在指定要返回的函数时，您可以直接使用LCEL对其进行解析。例如：

python

链=(

此示例直接解析“joke”函数的输出。

这些只是LCEL如何简化复杂语言处理任务的几个例子。无论您是构建聊天机器人、生成内容还是执行复杂的文本转换，LCEL都可以简化您的工作流程，使您的代码更易于维护。

###RAG（检索增强生成）

LCEL可用于创建检索增强生成链，该链结合了检索和语言生成步骤。这里有一个例子：

python

从langchain.prompts导入聊天提示模板

#创建矢量存储和检索器

#定义提示模板

问题：{问题}

模型 = ChatOpenAI()

#创建检索增强生成链

result=chain.require（“哈里森在哪里

工作？")

在这个例子中，链从上下文中检索相关信息并生成对问题的响应。

###会话检索链

您可以轻松地将对话历史添加到您的链中。以下是一个会话检索链的示例：

python

从langchain.prompts.prompt导入PromptTemplate

#定义提示模板

聊天记录：

template=“”“仅根据以下上下文回答问题：

问题：{问题}

#定义输入映射和上下文

result=对话式qa_chain.invoke(

在这个例子中，链在会话上下文中处理后续问题。

###使用内存并返回源文档

LCEL还支持内存和返回源文档。以下是如何在链中使用内存：

python

#创建内存实例

#定义链的步骤

standalone_question={

已检索文档={

最终输入={

答案={

#通过组合步骤创建最终链

inputs={“问题”：“哈里森在哪里工作？”}

在这个例子中，内存用于存储和检索对话历史和源文档。

###多条链条

您可以使用Runnables将多个链串在一起。这里有一个例子：

python

从langchain.chat_models导入ChatOpenAI

prompt1=ChatPromptTemplate.from_template（“这个人来自哪个城市？”）

模型 = ChatOpenAI()

chain1=prompt1|模型|StrOutputParser（）

链2=(

result=chain2.invoke（{“人”：“奥巴马”，“语言”：“西班牙语”}）

在这个例子中，两条链被组合在一起，以特定的语言生成有关城市及其国家的信息。

###分支和合并

LCEL允许您使用RunnableMaps拆分和合并链。以下是一个分支和合并的示例：

python

从langchain.chat_models导入ChatOpenAI

规划师=(

arguments_for=(

最终响应者=(

链=(

result=chain.require（{“input”：“scrum”}）

在这个例子中，使用分支和合并链来生成一个参数，并在生成最终响应之前评估其优缺点。

###用LCEL编写Python代码

LangChain表达式语言（LCEL）的一个强大应用是编写Python代码来解决用户问题。下面是一个如何使用LCEL编写Python代码的示例：

python

template=“”“编写一些python代码来解决用户的问题。

只返回Markdown格式的python代码，例如：

python

模型 = ChatOpenAI()

def_sanitize_output（文本：str）：

chain=prompt|model|StrOutputParser（）|_sanitize_output|PythonREPL（）.run

result=chain.require（{“input”：“2加2等于多少”}）

在这个例子中，用户提供输入，LCEL生成Python代码来解决问题。然后使用Python REPL执行代码，并以Markdown格式返回生成的Python代码。

请注意，使用Python REPL可以执行任意代码，因此请谨慎使用。

###为链添加内存

在许多会话式AI应用中，内存是必不可少的。以下是如何向任意链添加内存：

python

模型=聊天OpenAI（）

内存=转换缓冲内存（返回消息=真）

#初始化内存

链=(

inputs={“input”：“嗨，我是Bob”}

#将对话保存在内存中

#加载内存以查看对话历史记录

在这个例子中，内存用于存储和检索对话历史，使聊天机器人能够维护上下文并做出适当的响应。

###在Runnables中使用外部工具

LCEL允许您将外部工具与Runnables无缝集成。以下是使用DuckDuckGo搜索工具的示例：

python

搜索 = DuckDuckGoSearchRun()

template=“”“将以下用户输入转换为搜索引擎的搜索查询：

｛input｝“”“

模型=聊天OpenAI（）

chain=提示|模型|StrOutputParser（）|搜索

search_result=chain.require（{“input”：“我想知道今晚有什么游戏”}）

在这个例子中，LCEL将DuckDuckGo搜索工具集成到链中，使其能够根据用户输入生成搜索查询并检索搜索结果。

LCEL的灵活性使您可以轻松地将各种外部工具和服务整合到您的语言处理管道中，从而增强它们的能力和功能。

###向LLM申请添加审核

为了确保您的LLM应用程序遵守内容策略并包括审核保障，您可以将审核检查集成到您的链中。以下是如何使用LangChain添加审核：

python

moded=OpenAIModerationChain（）

模型=OpenAI（）

链=提示|模型

#未经审核的原始回复

moderated_chain=链|中等

#适度后的反应

在这个例子中，`OpenAIModerationChain`用于为LLM生成的响应添加审核。审核链检查违反OpenAI内容策略的内容的响应。如果发现任何违规行为，它将相应地标记响应。

###语义相似性路由

LCEL允许您根据用户输入的语义相似性实现自定义路由逻辑。以下是一个如何根据用户输入动态确定链逻辑的示例：

python

physics_template=“”“你是一位非常聪明的物理学教授\

这里有一个问题：

math_template=“”“你是一位非常优秀的数学家。你擅长回答数学问题\

这里有一个问题：

嵌入=OpenAIEmbeddings（）

def prompt_router（输入）：

链=(

print（chain.invoke（{“query”：“什么是黑洞”}））

在这个例子中，`prompt_router`函数计算用户输入与物理和数学问题的预定义提示模板之间的余弦相似度。基于相似性得分，链动态选择最相关的提示模板，确保聊天机器人对用户的问题做出适当的回应。

###使用代理和可运行程序

LangChain允许您通过组合Runnables、提示、模型和工具来创建代理。下面是一个构建代理并使用它的示例：

python

model=聊天人类学（model=“claude-2”）

@工具

tool_list=[搜索]

#获取使用提示

#从中间步骤到字符串传递到模型的逻辑

#将工具转换为字符串以进入提示的逻辑

代理=(

agent_executor=代理执行器（代理=代理，工具=工具列表，详细信息=True）

result=agentexecutor.invoke（{“问题”：“纽约的天气怎么样？”}）

在这个例子中，通过组合模型、工具、提示和用于中间步骤和工具转换的自定义逻辑来创建代理。然后执行代理，提供对用户查询的响应。

###查询SQL数据库

您可以使用LangChain查询SQL数据库，并根据用户问题生成SQL查询。这里有一个例子：

python

template=“”“根据下面的表架构，编写一个SQL查询来回答用户的问题：

问题：{问题}

从langchain.utilities导入SQLDatabase

#初始化数据库（本例需要Chinook示例数据库）

def get_schema（_）：

def run_query（查询）：

从langchain.chat_models导入ChatOpenAI

模型=聊天OpenAI（）

sql_response=(

result=sql_response.require（{“问题”：“有多少员工？”}）

template=“”“根据下表模式、问题、SQL查询和SQL响应，编写一个自然语言响应：

问题：{问题}

全链=(

response=full_chain.invoke（{“问题”：“有多少员工？”}）

在这个例子中，LangChain用于根据用户问题生成SQL查询，并从SQL数据库中检索响应。提示和响应被格式化，以提供与数据库的自然语言交互。

---

##使用LangServe进行部署

LangServe帮助开发人员将LangChain可运行文件和链部署为REST API。该库与FastAPI集成，并使用pydantic进行数据验证。此外，它还提供了一个客户端，可用于调用部署在服务器上的可运行文件，LangChainJS中还提供了JavaScript客户端。

**特点**

-输入和输出模式是从LangChain对象中自动推断出来的，并在每个API调用中强制执行，并带有丰富的错误消息。

**局限性**

-对于源自服务器的事件，尚不支持客户端回调。

使用LangChain CLI快速引导LangServe项目。要使用langchain CLI，请确保安装了最新版本的langchain CLI。您可以使用pip install-U langchain cli安装它。

python

使用LangChain模板快速启动您的LangServe实例。有关更多示例，请参阅模板索引或示例目录。

这是一个部署了OpenAI聊天模型、Anthropic聊天模型和一个使用Anthropic模型讲述主题笑话的链的服务器。

python

app=FastAPI(

add_routes(

add_routes(

model=ChatAnthropic（）

如果__name__==“__main__”：

run（应用程序，主机=“localhost”，端口=8000）

部署上述服务器后，您可以使用以下命令查看生成的OpenAPI文档：

```bash

确保添加/docs后缀。

python

openai=可远程运行（“http://localhost:8000/openai/")

joke_chain.invoke（{“主题”：“鹦鹉”}）

#或异步

提示=[

#支持astream

prompt=ChatPromptTemplate.from_message(

#可以定义自定义链

chain.batch（〔{“主题”：“鹦鹉”}，{“话题”：“猫”}）

在TypeScript中（需要LangChain.js版本0.0.166或更高版本）：

```打字稿

const链=新的远程可运行({

Python使用请求：

python

你也可以使用curl：

```bash

以下代码：

python

将这些端点添加到服务器：

-POST/my\_runnable/recall-在单个输入上调用runnable

你可以在/my unnunable/party找到一个适合你跑步的操场页面。这提供了一个简单的UI，用于配置和调用具有流式输出和中间步骤的可运行文件。

对于客户端和服务器：

```bash

或者pip安装“langserve\[client\]”作为客户端代码，pip安装“langserve\[server\]”用于服务器代码。

如果您需要向服务器添加身份验证，请参考FastAPI的安全文档和中间件文档。

您可以使用以下命令部署到GCP Cloud Run：

```bash

LangServe为Pydantic 2提供支持，但有一些限制。使用Pydantic V2时，不会为invoke/batch/stream/stream\_log生成OpenAPI文档。Fast API不支持混合使用pydantic v1和v2名称空间。LangChain在Pydantic v2中使用v1命名空间。请阅读以下指南，以确保与LangChain的兼容性。除了这些限制之外，我们希望API端点、游乐场和任何其他功能都能按预期工作。

LLM应用程序通常处理文件。有不同的架构可以用来实现文件处理；在高层次上：

-文件可以通过专用端点上传到服务器，并使用单独的端点进行处理。

您应该确定应用程序的适当架构。目前，要按值将文件上传到可运行文件，请对文件使用base64编码（尚不支持多部分/表单数据）。

这里有一个[示例](https://github.com/langchain-ai/langserve/tree/main/examples/file_processing)它显示了如何使用base64编码将文件发送到远程可运行文件。请记住，您始终可以通过引用（例如s3 url）上传文件，也可以将它们作为多部分/表单数据上传到专用端点。

输入和输出类型在所有可运行文件上定义。您可以通过输入\_schema和输出\_schemas属性访问它们。LangServe使用这些类型进行验证和记录。如果要覆盖默认的推断类型，可以使用with\_types方法。

这里有一个玩具示例来说明这个想法：

python

应用程序 = FastAPI()

def函数（x:任意）->int：

runnable=RunnableLambda（函数）。with_types(

add_routes（应用程序，可运行）

如果您希望数据反序列化为复制模型而不是等效的字典表示，请继承CustomUserType。目前，这种类型仅在服务器端工作，用于指定所需的解码行为。如果从该类型继承，服务器将把解码后的类型保留为复制模型，而不是将其转换为字典。

python

应用程序 = FastAPI()

自定义Foo（自定义用户类型）：

def函数（foo:foo）->int：

add_routes（应用程序，RunnableLambda（函数），路径=“/foo”）

游乐场允许您从后端为可运行的程序定义自定义小部件。小部件在字段级别指定，并作为输入类型的JSON模式的一部分提供。小部件必须包含一个名为type的键，其值是众所周知的小部件列表之一。其他小部件键将与描述JSON对象中路径的值相关联。

总体架构：

```javascript

类型小部件={

允许在UI游乐场中为以base64编码字符串上传的文件创建文件上传输入。这是完整的例子。

python

从langserve导入CustomUserType

#注意：否则继承CustomUserType而不是BaseModel

#额外字段用于指定游乐场UI的小部件。

---

##LangSmith简介

LangChain使LLM应用程序和代理的原型制作变得容易。然而，将LLM应用程序交付到生产环境可能看起来很困难。您可能需要对提示、链和其他组件进行大量定制和迭代，以创建高质量的产品。

为了帮助这一过程，引入了LangSmith，这是一个用于调试、测试和监控LLM应用程序的统一平台。

这什么时候有用？当您想快速调试新链、代理或一组工具，可视化组件（链、llms、检索器等）的关系和使用方式，评估单个组件的不同提示和LLM，在数据集上多次运行给定链以确保其始终符合质量标准，或捕获使用痕迹并使用llms或分析管道生成见解时，您可能会发现它很有用。

先决条件：

1.创建一个LangSmith帐户并创建一个API密钥（请参见左下角）。

现在，让我们开始吧！

首先，配置环境变量以告诉LangChain记录跟踪。这是通过将LANGCHAIN\_TRACING\_V2环境变量设置为true来实现的。您可以通过设置LangChain\_project环境变量来告诉LangChain要登录到哪个项目（如果没有设置，运行将记录到默认项目中）。如果项目不存在，这将自动为您创建项目。您还必须设置LANgcHAI\_ENDPOINT和LANGCHAIN\_API\_KEY环境变量。

注意：您还可以在python中使用上下文管理器，通过以下方式记录跟踪：

python

启用跟踪_v2_（项目名称=“我的项目”）：

然而，在这个例子中，我们将使用环境变量。

python

导入操作系统

unique_id=uuid4（）.十六进制[0:8]

#本教程中的代理使用

创建LangSmith客户端以与API交互：

python

客户端=客户端（）

创建LangChain组件并将运行记录到平台。在这个例子中，我们将创建一个ReAct风格的代理，可以访问通用搜索工具（DuckDuckGo）。可以在Hub中查看代理的提示：

python

#获取此提示的最新版本

llm=ChatOpenAI(

工具=[

llm_with_tools=llm.bind（函数=[工具中t的format_tool_to_openai_function（t）]）

runnable_agent=(

AgentExecutor=代理执行器(

我们正在多个输入上并发运行代理，以减少延迟。运行会在后台记录到LangSmith，因此执行延迟不受影响：

python

results=agent_executor.batch（[{“input”：x}表示输入中的x]，return_exceptions=True）

结果[：2]

假设您已成功设置环境，您的代理跟踪应显示在应用程序的“项目”部分。恭喜！

不过，看起来代理并没有有效地使用这些工具。让我们评估一下，这样我们就有了一个基线。

除了记录运行外，LangSmith还允许您测试和评估LLM应用程序。

在本节中，您将利用LangSmith创建基准数据集，并在代理上运行人工智能辅助评估器。您将通过几个步骤完成此操作：

-创建LangSmith数据集：

下面，我们使用LangSmith客户端从上面的输入问题和列表标签创建数据集。稍后，您将使用这些指标来衡量新代理的性能。数据集是一组示例的集合，它们只不过是可以用作应用程序测试用例的输入输出对：

python

dataset_name=f“代理qa-{unique_id}”

数据集=client.create_dataset(

对于查询，请在zip中回答（输入、输出）：

-初始化新代理以进行基准测试：

LangSmith允许您评估任何LLM、链、代理，甚至自定义函数。会话代理是有状态的（它们有内存）；为了确保此状态不会在数据集运行之间共享，我们将传入一个链式工厂(

也称为构造函数）函数，用于为每次调用初始化：

python

-配置评估：

在UI中手动比较链的结果是有效的，但可能很耗时。使用自动化指标和人工智能辅助反馈来评估组件的性能可能会有所帮助：

python

evaluation_config=RunEvalConfig(

-运行代理和评估器：

使用run\_on\_dataset（或异步arun\_on\ _dataset）函数来评估您的模型。这将：

1.从指定的数据集中提取示例行。

结果将在LangSmith应用程序中显示：

python

现在我们有了测试运行结果，我们可以对代理进行更改并对其进行基准测试。让我们用不同的提示再试一次，看看结果：

python

chain_results=run_on_dataset(

LangSmith允许您直接在web应用程序中将数据导出为CSV或JSONL等常见格式。您还可以使用客户端获取运行以进行进一步分析，存储在自己的数据库中，或与他人共享。让我们从评估运行中获取运行跟踪：

python

#一段时间后，这些将被填充。

这是一个快速入门指南，但还有更多方法可以使用LangSmith来加快开发流程并产生更好的结果。

有关如何充分利用LangSmith的更多信息，请查看LangSmith文档。

##使用Nanonets升级

虽然LangChain是将语言模型（LLM）与您的应用程序和工作流集成的有价值的工具，但在企业用例方面可能会面临局限性。

1.**数据连接**：对各种业务应用程序和数据格式的支持有限。

输入[纳米网](https://nanonets.com/)工作流程！

###利用工作流自动化的力量：现代企业的游戏规则改变者

在当今快节奏的商业环境中，工作流自动化是一项至关重要的创新，为各种规模的公司提供了竞争优势。将自动化工作流程整合到日常业务运营中不仅仅是一种趋势；这是一种战略需要。除此之外，LLM的出现为手动任务和流程的自动化开辟了更多的机会。

欢迎来到Nanonets工作流自动化，人工智能驱动的技术使您和您的团队能够在几分钟内自动化手动任务并构建高效的工作流。利用自然语言轻松创建和管理与您的所有文档、应用程序和数据库无缝集成的工作流。

<iframe src=“https://player.vimeo.com/video/886199923?app_id=122963“width=”426“height=”240“frameborder=”0“allow=”自动播放；全屏；picture in picture“title=”Nanonets工作流自动化“></iframe>

我们的平台不仅为统一的工作流程提供无缝的应用程序集成，而且能够构建和利用自定义的大型语言模型应用程序，在您的应用程序中进行复杂的文本写作和回复发布。始终确保数据安全是我们的首要任务，严格遵守GDPR、SOC 2和HIPAA合规标准​.

为了更好地理解Nanonets工作流自动化的实际应用，让我们深入研究一些现实世界的例子。

-**自动化客户支持和参与流程**

<iframe src=“https://player.vimeo.com/video/886204564?app_id=122963“width=”426“height=”228“frameborder=”0“allow=”自动播放；全屏；picture in picture“title=”自动化客户支持和参与流程“></iframe>

-**工单创建–Zendesk**：当客户在Zendesk中提交新的支持工单，表示他们需要产品或服务方面的帮助时，工作流会被触发。

-**自动问题解决流程**

 ！[]（https://nanonets.com/blog/content/images/2023/11/Screen_Recording_2023-11-19_at_6.51.20_PM_V4.gif ）

1.**初始触发-Slack消息**：当客户服务代表在Slack的专用通道中收到新消息时，工作流程开始，表明需要解决的客户问题。

-**自动会议日程安排流程**

 ！[]（https://nanonets.com/blog/content/images/2023/11/Screen_Recording_2023-11-19_at_6.53.40_PM_V2.gif ）

1.**首次联系–LinkedIn**：当一个专业联系人在LinkedIn上发送了一条新消息，表示有兴趣安排会议时，工作流程就会启动。LLM解析传入的消息，如果它认为该消息是潜在求职者的会议请求，则触发工作流。

-[**发票处理**](https://nanonets.com/blog/invoice-processing/)**在应付账款中**

![](https://www.youtube.com/watch?v=PHGT7DGW7hA)

-**发票收据-Gmail**：发票通过电子邮件收到或上传到系统。

-**内部知识库协助**

![](https://nanonets.com/blog/content/images/2023/11/652ceeb94be5f658cde2b59d_chat-with-data--1--2.gif)

-**初步询问–Slack**：团队成员Smith在#chat with data Slack频道中询问遇到QuickBooks集成问题的客户。

####企业效率的未来

[纳米网](https://nanonets.com/)Workflows是一个安全、多用途的工作流自动化平台，可自动化您业务中的手动任务和工作流。它提供了一个易于使用的用户界面，使个人和组织都可以访问。

首先，您可以安排与我们的一位人工智能专家通话，他们可以根据您的特定用例提供定制的Nanonets工作流的个性化演示和试用。 

设置后，您可以使用自然语言设计和执行由LLM支持的复杂应用程序和工作流，与您的应用程序和数据无缝集成。

 ！[]（https://nanonets.com/blog/content/images/2023/11/Screen_Recording_2023-11-15_at_1.36.18_PM_V5.gif ）

使用Nanonets工作流增强您的团队，使他们能够专注于真正重要的事情。

---