---
title: "RAG: Retrieval Augmented Generation In-Depth with Code Implementation using Langchain, Langchain…"
source: "https://medium.com/@devmallyakarar/rag-retrieval-augmented-generation-in-depth-with-code-implementation-using-langchain-llamaindex-1f77d1ca2d33"
author:
  - "[[Devmallya Karar]]"
published: 2024-09-21
created: 2025-03-01
description: "Retrieval Augmented Generation (RAG) represents an innovative framework that combines the strengths of information retrieval and generative modelling to address complex query tasks in natural…"
tags:
  - "clippings"
---
[

![Devmallya Karar](https://miro.medium.com/v2/resize:fill:88:88/1*kOYSsZPtFM_Q5-3zKxYulQ.jpeg)

](https://medium.com/@devmallyakarar?source=post_page---byline--1f77d1ca2d33---------------------------------------)                                              

Retrieval Augmented Generation (RAG) represents an innovative framework that combines the strengths of information retrieval and generative modelling to address complex query tasks in natural language processing. It was notably developed to enhance the capabilities of sequence-to-sequence models by dynamically retrieving external documents and incorporating their information during the generation process. At its core, RAG operates by integrating a pre-trained language model with a neural retrieval mechanism. This integration allows the model to access a vast external knowledge base (typically a corpus of documents) to fetch relevant information that aids in generating more informed and accurate responses. The RAG model effectively turns the challenge of generating language from a purely predictive task into an information-grounded task.  

![](https://miro.medium.com/v2/resize:fit:2000/1*Z-cp233Br1miQjefi5ynCA.jpeg)  

The architecture of RAG can be primarily divided into two components: the retriever and the generator. The retriever is tasked with fetching relevant documents from the corpus based on the input query, while the generator, a sequence-to-sequence model, uses both the original query and the retrieved documents to produce the final output.  

## Retrieval Mechanism  

The retrieval component of RAG is typically built on a dense vector space model where both the documents in the corpus and the input query are embedded into a high-dimensional space. The similarity between the query and document vectors (often calculated using dot product or cosine similarity) determines the relevance of the documents to the query. This process can be mathematically represented as:  

***sim(q,d) = qTd  ***

where q and d are vector representations of the query and a document, respectively.  

![](https://miro.medium.com/v2/resize:fit:1400/1*NKTRRkd1KlmmKbkPENVBAg.png)

Retrieval-Augmented Generation (RAG) system integrated with a Large Language Model (LLM).

It outlines the workflow of a Retrieval-Augmented Generation (RAG) system integrated with a Large Language Model (LLM). This diagram illustrates how RAG systems enhance the capabilities of LLMs by incorporating external knowledge sources during the response generation process. Here’s a breakdown of each step in the flow:

1. **Prompt + Query**: The process begins with an initial prompt and a query. This input can be any text-based question or request for information that the user wants to address using the system.
2. **Query**: The system isolates the query from the initial input and uses it as the basis for retrieving information. The isolated query serves as a focused input for the retrieval system.
3. **Search Relevant Information**: The query is used to search through external knowledge sources. These could be databases, documents, or any organized corpus that the system has access to. The search process aims to find data that is relevant to the query.
4. **Relevant Information for Enhanced Context**: The information retrieved from the knowledge sources is then combined with the original input to create an enhanced context. This enriched context now includes both the original prompt (and/or query) and the additional relevant information fetched from external sources. This step is critical as it allows the LLM to have access to a broader and more specific context than what was originally provided.
5. **Generated Text Response**: With an enhanced context that integrates the retrieved information, the Large Language Model endpoint then generates a response. This response is expected to be more informed, accurate, and relevant, as it is based on both the original query and the additional context provided by the retrieved information.
6. **Prompt + Query + Enhanced Context → Large Language Model Endpoint**: This step in the flow represents the process of sending the enhanced input (original prompt/query plus retrieved information) to the LLM for processing. The LLM endpoint, likely a sophisticated neural network model, processes this information to generate a coherent and contextually enriched response.

This architecture demonstrates the power of combining traditional LLMs with retrieval mechanisms to significantly enhance the model’s ability to generate detailed and accurate outputs by grounding the responses in retrieved external data. This approach is particularly useful in scenarios where the LLM needs to provide responses based on factual information or when handling complex queries that require detailed understanding and background knowledge.

## Mathematical Derivation of the Retrieval Mechanism

The retrieval mechanism typically employs a dense vector space model where documents and queries are represented as high-dimensional vectors. The goal is to find document vectors that are closest to the query vector in this space, implying relevance to the query.

## Vector Representation

1. **Embedding**: Each document d in the corpus and the query q are transformed into vectors: ***d = fdoc​(d;θdoc​) q = fquery(q;θquery)***.

Here, ***fdoc***​ and ***fquery***​ are embedding functions (typically neural networks) that map the text to a high-dimensional vector space, and ***θdoc***​ and ***θquery***​ are the parameters of these functions.

2\. **Normalization**: Often, these vectors are normalized to have unit length to simplify the calculation of similarity:

![](https://miro.medium.com/v2/resize:fit:1400/1*90CUikTli1kz5Tkk_oNcjg.jpeg)

## Similarity Calculation

1. **Similarity Score**: The similarity between the query and each document is calculated using the dot product of their normalized vectors: sim(q,d)=q^Td^ This can also be computed using cosine similarity since the vectors are normalized.

## Generation Mechanism

Once the relevant documents are retrieved, the generator component, which leverages a transformer-based model like BERT or GPT, takes over. The input to this model is a combination of the input query and the contents of the retrieved documents. The generation process is governed by the conditional probability of generating a sequence of tokens y (the output) given the input sequence x and the retrieved documents D. This can be mathematically expressed as:

![](https://miro.medium.com/v2/resize:fit:1400/1*a1D3iafsWAiP4lH0tt8BGg.jpeg)

Here, y<i​ represents all tokens before position iii, ensuring that the generation of each token conditions on the preceding tokens, the input query, and the content of the retrieved documents.

## Training

Training a RAG model involves optimizing both the retriever and the generator components. The goal is to improve the relevance of the retrieved documents as well as the accuracy of the generated text. The training objective typically combines the loss functions from both retrieval and generation tasks:

1. **Retrieval Loss:** This loss measures how well the retriever is selecting relevant documents. A common approach is to use a ranking loss like triplet loss, which encourages the retriever to rank the correct document above incorrect ones.
2. **Generation Loss:** This is usually a cross-entropy loss that measures how well the generator predicts the target sequence given the input and retrieved documents.

The combined objective function is often formulated as a weighted sum of both losses:

![](https://miro.medium.com/v2/resize:fit:1400/1*mtbHsvtrxW97Bro4MgZBbA.jpeg)

where α is a hyperparameter that balances the importance of the retrieval and generation tasks.

## Issues happens with Search & Retrieval

The search and retrieval method significantly boosts the efficiency and accuracy of Large Language Models (LLMs), but it also introduces several potential challenges that could negatively affect the user experience if not addressed early.

A common issue occurs when the system receives a query that does not closely align with any of the entries in the vector store — akin to searching for a needle in a haystack and not finding the needle. This situation often results from unique or highly specific queries. As a result, the system may only be able to pull the “most similar” chunks of data, which may not be wholly relevant.

Consequently, this mismatch can lead to inadequate responses from the LLM. Since the quality of the LLM’s outputs relies heavily on the relevance of the retrieved data chunks, an inappropriate match might lead to responses that are only tangentially related to, or even completely disconnected from, the user’s original query.

![](https://miro.medium.com/v2/resize:fit:1400/1*FPFv0av16KMB-6m1MAnwJw.png)

Image by [Ariza](https://arize.com/blog-course/introduction-to-retrieval-augmented-generation/)

Irrelevant or subpar responses from the Large Language Model (LLM) can lead to user frustration, reducing their satisfaction and potentially eroding trust in both the system and the product as a whole.

To prevent these issues, it is critical to monitor three key areas:

1. **Query Density (Drift):** This refers to the coverage of user queries by the vector store. A significant drift in query density can indicate that the vector store is not fully capturing the range of user queries, leading to a lack of closely related data chunks. Regular monitoring of query density can help identify these gaps or deficiencies. With these insights, we can enhance the vector store by adding more relevant data chunks or refining existing ones, thereby improving the system’s capability to retrieve data in response to user queries.
2. **Ranking Metrics:** These metrics assess the effectiveness of the search and retrieval system in identifying the most relevant chunks. A decline in these metrics suggests that the system’s ability to differentiate between relevant and irrelevant chunks may require fine-tuning.
3. **User Feedback:** Encouraging user feedback on the quality and relevance of the LLM’s responses is crucial for measuring user satisfaction and pinpointing areas for improvement. Analyzing this feedback regularly can reveal patterns and trends, which can then inform necessary adjustments to the application.

By focusing on these areas, we can enhance the responsiveness and reliability of the LLM, ensuring that it meets user expectations and maintains their trust in the system.

## Optimization of Search & Retrieval

Optimizing the search and retrieval processes is a continuous effort that spans the entire lifecycle of your LLM-powered application, starting from the building phase through to post-production.

In the building phase, it is crucial to focus on developing a robust testing and evaluation strategy. This proactive approach helps in identifying potential issues early, allowing for optimization of strategies and laying a strong foundation for the system.

Important areas to concentrate on during this phase include:

- **Chunking Strategy:** Careful evaluation of how information is segmented and processed at this stage can illuminate areas where performance improvements are necessary.
- **Retrieval Performance:** Regular assessments of the system’s ability to fetch information will reveal whether there is a need to implement different tools or strategies, such as context ranking or utilizing HYDE.

As the application moves into the post-production phase after release, the optimization efforts must persist. With a well-defined evaluation strategy in place, it becomes feasible to proactively detect emerging issues and continually enhance the model’s performance. Strategies to consider in this phase include:

- **Expanding our Knowledge Base:** By adding more documentation, the system’s capacity to provide accurate and customized responses is significantly improved. A larger dataset enables the LLM to offer more precise responses.
- **Refining Chunking Strategy:** Further adjustments to how information is segmented and processed can result in substantial performance improvements.
- **Enhancing Context Understanding:** Implementing an additional ‘context evaluation’ step allows the system to integrate the most pertinent context into the LLM’s responses, enhancing accuracy.

## Types of Search

Vector databases, while exceptional at semantic search, are not a universal solution for all search-related challenges — they excel in certain aspects but fall short in others. Traditional keyword search, in many instances, can yield more pertinent results and enhance user satisfaction. This outcome is often attributed to the way results are ranked in vector databases; results with higher cosine similarity scores may overshadow partial matches that contain specific keywords the user is searching for, thereby reducing the perceived relevance of the results.

On the other hand, traditional keyword search comes with its own set of limitations. For example, if a user inputs a term that is semantically close to but not exactly the same as the terms stored in the database, keyword search may fail to return useful and relevant results. This limitation highlights the inherent trade-off in search methodologies, where no single approach is perfect for every scenario.

In response to these trade-offs, practical applications in search and retrieval often necessitate a combination of both keyword and vector search strategies. Vector databases play a crucial role here as they store embeddings that enable semantic similarity searches and are scalable to handle very large datasets.

To summarize the distinct features and applications of each search type:

- **Keyword Search**: This method is ideal when users have a clear understanding of what they are looking for and expect to find results that match specific phrases or exact terms from their queries. It operates independently of vector databases.
- **Vector Search**: This approach is beneficial when users are unsure of the exact terms to use or when the query is more conceptual. It relies on a vector database to find semantically relevant results.
- **Hybrid Search (Keyword + Vector)**: This method typically merges results from both keyword searches and vector searches. It then employs cross-encoder models to re-rank these results, ensuring that the most relevant outcomes from both methods are considered. This approach requires both a document database for keyword searches and a vector database for semantic searches.

This combination, or hybrid approach, leverages the strengths of each method to deliver a more robust and accurate search experience, catering to a broader range of user needs and search scenarios.

![](https://miro.medium.com/v2/resize:fit:2000/1*HcknySGWsT0wiD7kaIEe0g.png)

## Semantic Search

Semantic search aims to enhance the accuracy of search results by understanding the underlying intent and contextual meaning of a search query, rather than relying solely on lexical matches like traditional search engines. This method allows the system to recognize and retrieve synonyms and conceptually similar terms, improving the relevance of search results.

## Background

The foundational concept of semantic search involves embedding all entries in a corpus — ranging from sentences and paragraphs to entire documents — into a vector space. When a search query is received, it is also transformed into a corresponding vector within the same space. By comparing these vectors, the system identifies entries in the corpus that are semantically close to the query, ensuring a high degree of semantic overlap. This approach allows the search engine to understand content at a deeper level than simple keyword matching.

## Symmetric vs. Asymmetric Semantic Search

It is important to distinguish between symmetric and asymmetric semantic search, as they cater to different types of queries and content:

- **Symmetric Semantic Search**: This type involves queries and corpus entries that are similar in length and content depth. An example of this would be searching for questions similar in structure and intent, such as “How to learn Python online?” finding a match in “How to learn Python on the web?”. In symmetric search scenarios, it’s conceivable that the query and the corpus entries could be interchanged without losing relevance.
- **Asymmetric Semantic Search**: In this setup, queries are typically shorter — often just a question or a few keywords — while the desired results are more detailed or longer paragraphs that provide an answer. For example, the query “What is Python?” might return a detailed paragraph explaining that “Python is an interpreted, high-level and general-purpose programming language. Python’s design philosophy …”. Unlike symmetric search, in asymmetric scenarios, reversing the roles of the query and the corpus entries generally doesn’t yield useful results.

Understanding these distinctions is crucial for optimizing the design and functionality of semantic search systems, as it directly influences how queries are processed and how results are generated. This differentiation ensures that the search system can effectively handle a wide range of query types and deliver the most relevant and contextually appropriate results.

## Retrieval Algorithms

## Similarity Search (Vanilla Search) & Maximum Marginal Relevance(MMR)

When retrieving documents from a large corpus, most methods use similarity metrics like cosine similarity, Euclidean distance, or dot product to identify documents that are closest to the query or question posed. These metrics effectively pull the most similar documents based on the query, aligning well with the search intent.

However, there arises a challenge when we desire not only similarity but also diversity among the retrieved documents. This need is particularly critical when we want to avoid redundancy and provide a broad perspective on a topic. This is where the concept of Maximum Marginal Relevance (MMR) becomes invaluable.

## Understanding Maximum Marginal Relevance (MMR)

MMR is designed to balance between the relevance of the documents to the query and the diversity among the documents selected for retrieval. This approach helps ensure that the returned set of documents is both relevant and varied, providing a comprehensive view of the subject matter.

In practical applications like unsupervised learning for key phrase extraction, MMR can significantly enhance the utility and information quality. For example, consider a scenario where key phrases extracted from product reviews include terms like “Good Product,” “Great Product,” “Nice Product,” “Excellent Product,” “Easy Install,” “Nice UI,” “Lightweight.” Without MMR, the system might overly focus on similar phrases that frequently appear like “Good Product,” “Great Product,” and “Nice Product,” which all describe the same feature of the product and rank highly due to their frequency.

## Implementing MMR in Key Phrase Selection

To address this, if we only have space to display five key phrases, it’s crucial to select diverse phrases to cover a broader range of attributes, ensuring they provide varied insights into the product. MMR helps in:

- **Removing Redundant Phrases**: By using cosine similarity, MMR identifies and filters out phrases that are too similar to each other.
- **Re-ranking the Key Phrases**: MMR re-ranks the remaining phrases to prioritize those that add new information, thereby maximizing the relevance and diversity of the phrases shown.

## Example of MMR in Action

Suppose after the initial ranking, the phrases “Good Product,” “Great Product,” and “Nice Product” are all high on the list. MMR would evaluate the similarity among these phrases and likely retain only one or two while elevating others like “Easy Install” and “Lightweight,” which diversify the content presented.

## Broader Application and Future Discussion

MMR is just one of the many advanced retrieval strategies. Others include Multi Query Retrieval, Long-Context Reorder, Multi-Vector Retriever, Parent Document Retriever, Self-Querying, and Time-weighted Vector Store Retrieval. These methodologies, which offer various enhancements and optimizations for specific scenarios, will be explored in further detail in an upcoming blog post.

By integrating MMR into document retrieval and key phrase extraction processes, we ensure that the information presented is not only relevant but also diverse, thereby enriching the user’s experience and providing a fuller understanding of the topic.

## Retrieve & Re-Rank

Semantic search has greatly benefited from advancements in natural language processing, particularly through the use of models like Sentence Transformers. These models are designed to compute embeddings for texts ranging from short queries to lengthy paragraphs, making them ideal for semantic search applications where the understanding of context and meaning is crucial.

## Using Sentence Transformers in Semantic Search

Sentence Transformers generate embeddings that capture the semantic nuances of texts, enabling them to match queries with content that is contextually relevant, even if the exact keywords are not present. Here’s how it generally works:

1. **Embedding Generation**: Each piece of text — whether a query, sentence, or paragraph — is transformed into a vector (embedding) using the Sentence Transformer model. This process involves encoding the textual information into a high-dimensional space where semantically similar phrases are placed closer together.
2. **Embedding Storage**: These embeddings are then stored in a searchable format. Modern vector databases or approximate nearest neighbor (ANN) search libraries (like FAISS or Annoy) are used to manage these embeddings efficiently, allowing for quick retrieval even in large-scale datasets.
3. **Semantic Matching**: When a query is received, it is also converted into an embedding. The system then searches the vector database to find the closest embeddings (i.e., the most semantically related texts) to the query embedding.

This method enhances the capability of search systems to return more relevant and meaningful results by understanding the content’s context rather than relying solely on keyword matches.

## Enhancing Semantic Search with Retrieve & Re-Rank

For more complex search tasks, such as those found in question-answering systems, a two-step process called Retrieve & Re-Rank can significantly improve the effectiveness of the search:

1. **Retrieval Phase**: In the first phase, the system uses the query’s embedding to fetch a preliminary set of relevant documents from the corpus. This step is focused on speed and recall, aiming to gather a broad set of potentially relevant answers without yet fine-tuning for the best match.
2. **Re-Ranking Phase**: In the second phase, the system employs a more computationally intensive model to analyze the context and relevance of each retrieved document more deeply. This might involve additional features like the exactness of match, the depth of answer, and relevance to the query’s intent. Advanced models, possibly including cross-encoders or even larger transformers, evaluate the documents in relation to the query to determine the best fit.

This Retrieve & Re-Rank method allows for an efficient handling of large datasets in the initial retrieval while ensuring high accuracy in the final results through a detailed re-ranking. It balances the need for quick response times with the desire for high precision, making it particularly suitable for complex query answering tasks where both relevance and context sensitivity are critical.

Implementing these sophisticated search mechanisms not only improves user satisfaction through more accurate and relevant responses but also enhances the robustness of search systems in handling diverse and complex queries.

## Retrieve & Re-Rank Pipeline

A pipeline for information retrieval / question-answering retrieval that works well is the following. All components are provided and explained in this article:

![](https://miro.medium.com/v2/resize:fit:1400/1*Ok6J9fgm2T3uWPMvBGRXsw.jpeg)

This method is particularly effective for complex information retrieval tasks where precision is critical. Here’s a detailed look at each step involved in this search methodology:

## Step 1: Initial Retrieval

The first stage involves the use of a retrieval system to gather a large set of potential results, typically around 100, that may be relevant to the given search query. This retrieval can be conducted using one of two primary methods:

- **Lexical Search**: Utilizing traditional search engines like ElasticSearch, this method relies on keyword matching. It scans documents to find occurrences of the words included in the search query. While fast and efficient, lexical search may retrieve documents that match the query terms but miss contextual relevance or semantic similarity.
- **Dense Retrieval**: Employing a bi-encoder architecture, dense retrieval processes both the query and the documents in the corpus into dense vector representations. These embeddings are then compared (usually via cosine similarity) to identify documents whose contexts are semantically close to that of the query. This method tends to pull more contextually relevant documents compared to lexical search but may still include some less relevant results.

## Step 2: Re-Ranking with a Cross-Encoder

Once the initial list of potential hits is retrieved, the second stage of the process begins:

- **Re-Ranking**: A cross-encoder is employed to re-evaluate the relevance of each candidate document to the search query. Unlike the bi-encoder used for dense retrieval, a cross-encoder takes the pair of the query and each individual document as input and outputs a relevance score. This model is more computationally intensive because it performs a deeper analysis of the interaction between the query and document content, considering the nuances of their relationship.
- **Scoring and Ranking**: The cross-encoder scores each document for its relevance to the query. These scores are then used to sort the documents, resulting in a ranked list where the most relevant documents appear first. This refined list significantly improves the quality of the results that will be presented to the user.

## Output

The final output of this two-step process is a carefully curated list of documents, ranked by their relevance to the user’s query. This method effectively combines the speed and scalability of initial retrieval methods (either lexical or dense retrieval) with the precision of deep learning models (cross-encoder), ensuring that users receive the most accurate and contextually appropriate responses to their searches.

This dual-stage retrieval and re-ranking system is especially beneficial in environments where the accuracy of search results is paramount, such as in academic research, legal document retrieval, or any professional setting where precision and context are crucial.

![](https://miro.medium.com/v2/resize:fit:1400/1*hR0skMIH54BW8fT6H0CEWw.jpeg)

## Pre-trained Bi-Encoders (Retrieval)

The bi-encoder produces embeddings independently for your paragraphs and for your search queries. You can use it like this:

```
from sentence_transformers import SentenceTransformermodel = SentenceTransformer("multi-qa-mpnet-base-dot-v1")docs = [
    "My first paragraph. That contains information",
    "Python is a programming language.",
]
document_embeddings = model.encode(docs)query = "What is Python?"
query_embedding = model.encode(query)
```

Now let’s focus on chunking in-depth !!

## Introduction to Chunking

Chunking in Retrieval-Augmented Generation (RAG) refers to the process of splitting a large document or dataset into smaller, more manageable “chunks” before retrieving and generating relevant information. This technique is essential in RAG systems because it enables more efficient retrieval by ensuring that only pertinent parts of a document are processed, rather than the entire text.

When a user query is made, chunking allows the retriever to focus on smaller, contextually relevant sections, improving the quality of the generated response. The system retrieves chunks of text from a knowledge base and passes them to the generator model (like GPT), which synthesizes an answer.

The size of the chunk is critical: too large, and irrelevant information may get included; too small, and important context could be lost. Often, chunk sizes are determined based on token limits or the nature of the data (e.g., paragraphs, sentences). Effective chunking improves retrieval precision, minimizes unnecessary computation, and enhances overall response relevance, especially for applications like question-answering, summarization, and decision support in large corpora.

In simple way chunking is breaking down large pieces of text into smaller, more manageable chunks. This process has two main phases:

- Data Preparation: Reliable data sources are segmented into chunked documents and stored in a database. The database can be a vector store if you generate embeddings within the chunks.
- Retrieval: When a user asks a question, the system searches through the document chunks using vector search, full-text search, or a combination of both. This process identifies and retrieves the chunks most relevant to the user’s query.

## **Why Chunking is Crucial in RAG Architectures ?**

Chunking is indeed a crucial element in Retrieval-Augmented Generation (RAG) architectures, and your points capture the nuances effectively. Here’s an expanded look at why chunking matters in RAG systems:

1. **Increased Accuracy with Smaller Chunks**: When text is broken down into smaller chunks, each piece becomes more manageable for the system to search through. This leads to more accurate retrieval of relevant information. Smaller chunks allow the RAG system to avoid overloading the generative model with unnecessary context and focus on pinpointing the most relevant pieces of information based on the input query.
2. **Enhanced Contextual Generation**: Larger chunks can provide better context for generative models, making it easier for the system to generate responses that are more coherent and contextually appropriate. By balancing the size of chunks, RAG systems can make use of the additional context available from bigger chunks, leading to more nuanced answers while still maintaining relevance
3. **Scalability and Performance**: Chunking significantly reduces computational overhead by breaking large datasets into manageable pieces. These smaller chunks can be processed in parallel, allowing the RAG architecture to scale effectively while ensuring fast, efficient retrieval and generation processes. This parallelization is especially important when working with vast amounts of data or when speed is critical.
4. **Balance between Chunk Size and Retrieval Needs**: One challenge is ensuring that chunks are neither too small, which can lose context, nor too large, which can reduce retrieval precision. Therefore, an optimal chunk size is essential, balancing the trade-off between retrieval accuracy and contextual understanding.

## Techniques to Improve Chunking

Several advanced methods can be employed to refine chunking:

- **Fixed Character Sizes**: This is a simple technique where text is divided into fixed-size segments. While easy to implement, it may not always capture the semantic boundaries between ideas, which can affect retrieval and generation quality.

Here’s an example of how to implement fixed character size chunking using the code provided previously:

```
text = "This is the text I would like to chunk up. It is the example text for this exercise."
chunk_size = 35

chunks = []

for i in range(0, len(text), chunk_size):
    chunk = text[i:i + chunk_size]
    chunks.append(chunk)

print(chunks)
```

Using LangChain’s `CharacterTextSplitter` to achieve the same result:

```
from langchain.text_splitter import CharacterTextSplitter
text_splitter = CharacterTextSplitter(chunk_size=35, chunk_overlap=0, separator='', strip_whitespace=False)

documents = text_splitter.create_documents([text])

for doc in documents:
    print(doc.page_content)
```

- **Recursive Character Text Splitting**: Instead of arbitrary fixed sizes, this method uses separators like spaces, punctuation, or newlines to ensure chunks contain coherent units of information. It’s an improvement over fixed-length chunking as it considers natural language structures.

Here’s an example of how to implement recursive character text splitting in Langchain:

```
%pip install -qU langchain-text-splitters
```

Firstly install the long-chain-text-splitters library if you haven’t done this yet.

```
from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
The Olympic Games, originally held in ancient Greece, were revived in 1896 and
have since become the world’s foremost sports competition, bringing together 
athletes from around the globe.
"""

text_splitter = RecursiveCharacterTextSplitter(
    
    chunk_size=30,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False,
)
documents = text_splitter.create_documents([text])

for doc in documents:
    print(doc.page_content)
```

In this method, the text is first split by larger structures like paragraphs, and if the chunks are still too large, it further splits them using smaller structures like sentences. Each chunk maintains meaningful context and avoids cutting off vital information.

Recursive character text splitting strikes a balance between simplicity and sophistication, providing a robust method for chunking that respects the text’s inherent structure.

- **Document-Specific Splitting**: Some documents (e.g., PDFs or Markdown files) require unique chunking strategies to account for format-specific characteristics such as headers, tables, or lists. Tailoring chunking methods to document structure can help capture more meaningful chunks.

Here’s an example of how to implement document-specific splitting for Markdown and Python files:

## Markdown Splitting

```
from langchain.text_splitter import MarkdownTextSplitter

markdown_text = """
# Fun in California
## Driving
Try driving on the 1 down to San Diego
### Food
Make sure to eat a burrito while you're there
## Hiking
Go to Yosemite
"""

splitter = MarkdownTextSplitter(chunk_size=40, chunk_overlap=0)

documents = splitter.create_documents([markdown_text])

for doc in documents:
    print(doc.page_content)
```

## Python Code Splitting

```
from langchain.text_splitter import PythonCodeTextSplitter

python_text = """
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 36)
for i in range(10):
    print(i)
"""

python_splitter = PythonCodeTextSplitter(chunk_size=100, chunk_overlap=0)

documents = python_splitter.create_documents([python_text])

for doc in documents:
    print(doc.page_content)
```

Document-specific splitting preserves the document’s logical structure, making the chunks more meaningful and contextually accurate. For example, headers and sections are separated in Markdown files, while classes and functions are used in Python code.

This method enhances the system’s ability to retrieve and generate relevant responses by maintaining the integrity of different document types, thereby improving the overall performance and accuracy of the RAG system.

- **Semantic Splitting**: Using embeddings and semantic analysis allows systems to chunk based on meaning rather than structure. This advanced method ensures that each chunk contains conceptually related information, leading to more accurate retrieval.

Here’s an example of how to implement semantic splitting using embeddings.

```
from sklearn.metrics.pairwise import cosine_similarity
from langchain.embeddings import OpenAIEmbeddings
import re

text = """
One of the most important things I didn't understand about the world when I was a child is the degree to which the returns for performance are superlinear.
Teachers and coaches implicitly told us the returns were linear. "You get out," I heard a thousand times, "what you put in." They meant well, but this is rarely true. If your product is only half as good as your competitor's, you don't get half as many customers. You get no customers, and you go out of business.
It's obviously true that the returns for performance are superlinear in business. Some think this is a flaw of capitalism, and that if we changed the rules it would stop being true. But superlinear returns for performance are a feature of the world, not an artifact of rules we've invented. We see the same pattern in fame, power, military victories, knowledge, and even benefit to humanity. In all of these, the rich get richer.
"""

sentences = re.split(r'(?<=[.?!])\s+', text)
sentences = [{'sentence': x, 'index' : i} for i, x in enumerate(sentences)]

def combine_sentences(sentences, buffer_size=1):
    for i in range(len(sentences)):
        combined_sentence = ''
        for j in range(i - buffer_size, i):
            if j >= 0:
                combined_sentence += sentences[j]['sentence'] + ' '
        combined_sentence += sentences[i]['sentence']
        for j in range(i + 1, i + 1 + buffer_size):
            if j < len(sentences):
                combined_sentence += ' ' + sentences[j]['sentence']
        sentences[i]['combined_sentence'] = combined_sentence
    return sentences
sentences = combine_sentences(sentences)

oai_embeds = OpenAIEmbeddings()
embeddings = oai_embeds.embed_documents([x['combined_sentence'] for x in sentences])

for i, sentence in enumerate(sentences):
    sentence['combined_sentence_embedding'] = embeddings[i]

def calculate_cosine_distances(sentences):
    distances = []
    for i in range(len(sentences) - 1):
        embedding_current = sentences[i]['combined_sentence_embedding']
        embedding_next = sentences[i + 1]['combined_sentence_embedding']
        similarity = cosine_similarity([embedding_current], [embedding_next])[0][0]
        distance = 1 - similarity
        distances.append(distance)
        sentences[i]['distance_to_next'] = distance
    return distances, sentences
distances, sentences = calculate_cosine_distances(sentences)

import numpy as np
breakpoint_distance_threshold = np.percentile(distances, 95)
indices_above_thresh = [i for i, x in enumerate(distances) if x > breakpoint_distance_threshold]

chunks = []
start_index = 0
for index in indices_above_thresh:
    end_index = index
    group = sentences[start_index:end_index + 1]
    combined_text = ' '.join([d['sentence'] for d in group])
    chunks.append(combined_text)
    start_index = index + 1
if start_index < len(sentences):
    combined_text = ' '.join([d['sentence'] for d in sentences[start_index:]])
    chunks.append(combined_text)

for i, chunk in enumerate(chunks):
    print(f"Chunk #{i+1}:\n{chunk}\n")
```

Semantic splitting uses embeddings to create semantically similar chunks, improving retrieval accuracy and contextual generation in RAG systems. Focusing on the meaning of the text ensures that each chunk contains coherent and relevant information, enhancing the performance and reliability of the RAG application.

- **Agentic Splitting**: Leveraging large language models (LLMs) to determine the most appropriate chunking boundaries based on both content and context. This intelligent splitting can adapt dynamically to the text, ensuring that each chunk is optimal for retrieval and generation purposes.

## How Does Agentic Chunking Work?

The method of **agentic chunking** plays a vital role in improving the processing of long documents by large language models (LLMs). It addresses the limitations of both **recursive character splitting** and **semantic splitting**, which often fail to capture the coherent structure of a document. By breaking text into manageable pieces (chunks) based on **complete sentences**, agentic chunking maintains more logical integrity across the content.

## Key Features of Agentic Chunking:

1. **Evaluates Sentences Independently:** Unlike methods based on token length or semantic shifts, agentic chunking evaluates each sentence as an independent unit. This helps avoid breaking sentences mid-thought and maintains logical coherence across splits.
2. **Preserves Contextual Clarity:** When dealing with documents that may have pronouns or other references (such as “he” in your example), agentic chunking ensures that sentences are rewritten to maintain clarity. For instance, “He was leading NASA’s Apollo 11 mission” is clarified to “Neil Armstrong was leading NASA’s Apollo 11 mission.”
3. **Propositioning:** This process rewrites sentences so that they become independent propositions, complete with explicit subjects, reducing ambiguity. Each sentence, when passed to the LLM, stands alone without relying on previous sentences for understanding.

By using propositioning, sentences like:

- “On July 20, 1969, astronaut Neil Armstrong walked on the moon.”
- “Neil Armstrong was leading NASA’s Apollo 11 mission.”

are now clearer and can be chunked independently, enabling the LLM to better manage relationships between sentences, even if they are far apart in the original document.

This process significantly improves how LLMs handle texts by reducing ambiguity and enhancing the ability to chunk logically grouped sentences, ultimately improving downstream tasks such as summarization, content extraction, and question answering.

Now, the LLM can individually check every sentence and allocate it to a chunk or create one if it is irrelevant. This is possible because every sentence has a subject.

## Implementing Agentic chunking

Now, we have a rough idea of how agentic chunking works. We also know that the sentences need to be propositioned for it to work.

However, there are many different ways to implement this; no single package does it for us.

Let’s start with propositioning.

## Propositioning the text

As we now understand propositioning, we can create our own prompt to let an LLM do this for us. Fortunately, an excellent prompt is hosted in the Langchain hub.

Let’s pull the prompt template, create an LLM chain, and test it.

```
obj = hub.pull("wfh/proposal-indexing")llm = ChatOpenAI(model="gpt-4o")
class Sentences(BaseModel):
    sentences: List[str]extraction_llm = llm.with_structured_output(Sentences)
extraction_chain = obj | extraction_llm
sentences = extraction_chain.invoke(
    """
    On July 20, 1969, astronaut Neil Armstrong walked on the moon . 
    He was leading the NASA's Apollo 11 mission. 
    Armstrong famously said, "That's one small step for man, one giant leap for mankind" as he stepped onto the lunar surface.
    """
)>>['On July 20, 1969, astronaut Neil Armstrong walked on the moon.',
 "Neil Armstrong was leading NASA's Apollo 11 mission.",
 'Neil Armstrong famously said, "That\'s one small step for man, one giant leap for mankind" as he stepped onto the lunar surface.']
```

To handle large texts effectively, splitting the text into **paragraphs** and applying **propositioning** within each paragraph is a better approach. This ensures that pronouns like “he” remain contextually tied to the relevant subject within the paragraph. By doing this, we maintain clarity within smaller sections of the text, ensuring accurate chunking and extraction.

Using a **Pydantic model** to extract structured sentences after splitting by paragraphs allows for better handling of references and improves the model’s ability to infer meaning accurately.

```
paragraphs = text.split("\n\n")propositions = []for i, p in enumerate(paragraphs):
    propositions = extraction_chain.invoke(p        propositions.extend(propositions)
```

The above code snippet will create a list of propositions within each paragraph’s context.

To create chunks using an LLM agent, especially after applying propositioning, here’s how the process works:

## Step-by-Step Process:

1. **Initialize an empty dictionary** called `chunks` to store the grouped propositions.

```
{
    "12345": {
        "chunk_id": "12345",
        "propositions": [
            "The month is October.",
            "The year is 2023."
        ],
        "title": "Date & Time",
        "summary": "This chunk contains information about dates and times, including the current month and year.",
    },
    "67890": {
        "chunk_id": "67890",
        "propositions": [
            "One of the most important things that I didn't understand about the world as a child was the degree to which the returns for performance are superlinear.",
            "Teachers and coaches implicitly told us that the returns were linear.",
            "I heard a thousand times that 'You get out what you put in.'"
        ],
        "title": "Performance Returns",
        "summary": "This chunk contains information about performance returns and how they are perceived differently from reality.",
    }
}
```

As it encounters a new proposition, the agent either adds it to an existing chunk or creates a new chunk if no suitable one is found. The decision on whether an existing chunk matches is based on the incoming proposition and the chunk’s current summary.

Additionally, if new propositions are added to a chunk, the agent can update the chunk’s summary and title to reflect the new information. This ensures that the metadata stays relevant as the chunk evolves.

Let’s code them step by step.

To create chunks for the first time, we need a function that initializes a chunk when a new proposition appears. Since there are no chunks initially, this function will create the first chunk to store the initial proposition. This function will also be used anytime the agent determines that a new chunk is necessary for a different proposition. The chunks are stored outside of the function to allow continuous updates by this and other functions. When creating a chunk, we use the LLM to generate both a title and a summary based on the first proposition added to the chunk.

```
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAIllm = ChatOpenAI(temperature=0)chunks = {}def create_new_chunk(chunk_id, proposition):
    summary_llm = llm.with_structured_output(ChunkMeta)    summary_prompt_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Generate a new summary and a title based on the propositions.",
            ),
            (
                "user",
                "propositions:{propositions}",
            ),
        ]
    )    summary_chain = summary_prompt_template | summary_llm    chunk_meta = summary_chain.invoke(
        {
            "propositions": [proposition],
        }
    )    chunks[chunk_id] = {
        "summary": chunk_meta.summary,
        "title": chunk_meta.title,
        "propositions": [proposition],
    }
```

In Step II, we need a function to add new propositions to existing chunks as we continue scanning the document. When adding a new proposition to a chunk, the existing **title** and **summary** may no longer accurately represent the chunk’s content. Therefore, the function should re-evaluate these elements and update them if necessary.

To simplify this process, we use an LLM to decide whether changes are needed for the title and summary. By configuring the LLM with a **Pydantic model**, the output is structured, ensuring that the updated title and summary are organized properly, rather than just returning random text. This structured approach ensures that any changes to the chunk’s title and summary remain consistent and aligned with the content.

```
from langchain_core.pydantic_v1 import BaseModel, Fieldclass ChunkMeta(BaseModel):
    title: str = Field(description="The title of the chunk.")
    summary: str = Field(description="The summary of the chunk.")def add_proposition(chunk_id, proposition):
    summary_llm = llm.with_structured_output(ChunkMeta)    summary_prompt_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "If the current_summary and title is still valid for the propositions return them."
                "If not generate a new summary and a title based on the propositions.",
            ),
            (
                "user",
                "current_summary:{current_summary}\n\ncurrent_title:{current_title}\n\npropositions:{propositions}",
            ),
        ]
    )    summary_chain = summary_prompt_template | summary_llm    chunk = chunks[chunk_id]    current_summary = chunk["summary"]
    current_title = chunk["title"]
    current_propositions = chunk["propositions"]    all_propositions = current_propositions + [proposition]    chunk_meta = summary_chain.invoke(
        {
            "current_summary": current_summary,
            "current_title": current_title,
            "propositions": all_propositions,
        }
    )    chunk["summary"] = chunk_meta.summary
    chunk["title"] = chunk_meta.title
    chunk["propositions"] = all_propositions
```

In Step III, we need an agent that determines whether a proposition belongs to an existing chunk or if a new chunk should be created. The agent will:

1. **Check Existing Chunks**: When a new proposition arrives, the agent assesses if any of the current chunks are suitable for storing it. If a relevant chunk exists, the agent calls the `add_proposition` function, passing the chunk ID and proposition.
2. **Create New Chunk**: If no existing chunk is suitable, the agent calls the `create_new_chunk` function to start a new chunk for this proposition.
3. **LLM Decision**: The agent leverages an LLM to decide whether to push the proposition to an existing chunk or create a new one, ensuring the decision is contextually informed. Based on the LLM’s response, it triggers the appropriate function to either add or create a chunk.

This way, the agent intelligently organizes propositions into the most relevant chunks.

```
def find_chunk_and_push_proposition(proposition):    class ChunkID(BaseModel):
        chunk_id: int = Field(description="The chunk id.")    allocation_llm = llm.with_structured_output(ChunkID)    allocation_prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You have the chunk ids and the summaries"
                "Find the chunk that best matches the proposition."
                "If no chunk matches, return a new chunk id."
                "Return only the chunk id.",
            ),
            (
                "user",
                "proposition:{proposition}" "chunks_summaries:{chunks_summaries}",
            ),
        ]
    )    allocation_chain = allocation_prompt | allocation_llm    chunks_summaries = {
        chunk_id: chunk["summary"] for chunk_id, chunk in chunks.items()
    }    best_chunk_id = allocation_chain.invoke(
        {"proposition": proposition, "chunks_summaries": chunks_summaries}
    ).chunk_id    if best_chunk_id not in chunks:
        best_chunk_id = create_new_chunk(best_chunk_id, proposition)
        return    add_proposition(best_chunk_id, proposition)
```

## The Problem: Hallucinations and Errors in RAG Systems

An important issue raised which surrounds the limitations of Retrieval-Augmented Generation (RAG) systems and their susceptibility to hallucinations and logical errors, particularly in the response generation process. To address the problem more systematically, let’s break it down further:

## 1\. The Fundamental Problem:

Large Language Models (LLMs) can generate hallucinations — incorrect responses that are not grounded in the provided context or the underlying knowledge base. Even in a RAG setup where the retrieval mechanism is designed to enhance the accuracy of the model’s responses by fetching relevant data, errors can still occur during generation.

## 2\. Why Do Hallucinations Occur in RAG Systems?

The two main reasons for hallucinations in RAG systems, as you pointed out, are:

- **LLM Limitations in Reasoning Across Context:** Despite the presence of the correct information in the retrieved context, LLMs may still generate incorrect responses. This happens because the model must synthesize the answer from potentially fragmented data, often requiring reasoning that spans across multiple retrieved documents. If the model fails to do so effectively, hallucinations arise.
- **Suboptimal Retrieval:** If the retrieved context is incomplete or irrelevant (due to issues like poor document chunking or formatting, or the absence of crucial information in the knowledge base), the LLM might generate a response based on an inaccurate or inadequate context, leading to hallucinations.

## 3\. Examples of High-Impact Failures:

The case of Air Canada you mentioned highlights the real-world consequences of these hallucinations. When a chatbot generates an incorrect response, such as misrepresenting a refund policy, it can lead to reputational damage and legal repercussions, as well as a loss of trust in the system.

## 4\. Detection and Mitigation of Hallucinations:

The primary goal of any enterprise RAG system is to ensure that its responses are both accurate and reliable. Current approaches to detecting incorrect responses include:

- **Post-Response Validation:** Implementing mechanisms to verify the factual accuracy of the generated output against the retrieved context or external sources before presenting it to the user.
- **Confidence Scoring:** Leveraging confidence scores for both the retrieved context and the generated response can help determine the likelihood of an answer being incorrect.
- **Feedback Loops:** Continuous improvement of retrieval algorithms and refinement of the knowledge base to enhance retrieval accuracy and minimize the risk of hallucination.
- **AI-Powered Fact-Checkers:** Deploying additional AI models trained specifically for factual consistency checks can help reduce hallucinations in generated responses.

## 5\. Current Research Directions:

To mitigate the issue, research in the following areas is vital:

- **Improved Contextual Reasoning:** Enhancing LLMs’ ability to perform complex reasoning across multiple retrieved documents, ensuring that correct relationships between facts are understood and preserved in the response.
- **Robust Retrieval Mechanisms:** Ensuring the retrieval component can fetch not just relevant, but comprehensive and precise chunks of information to minimize the possibility of incorrect or incomplete context leading to hallucinations.
- **Real-Time Error Detection:** Development of detectors that can assess the generated response in real-time, flagging potential inaccuracies for further review before the response is delivered to users.

By focusing on these detection mechanisms and improving the retrieval process, organizations can better safeguard their RAG systems from hallucinations and ensure greater trust and reliability in the responses provided by LLMs.

## The Solution: Hallucination Detection Methods

The outlined hallucination detection methods provide a robust framework to mitigate the risks associated with LLM-generated hallucinations in high-stakes applications such as medicine, law, and finance. Here’s a deeper look at each method’s potential and implementation:

## 1\. Self-Evaluation (Self-eval):

This method capitalizes on the LLM’s own reasoning ability by prompting it to assess its own output based on a predefined confidence scale. By asking the model to explain its confidence via chain-of-thought (CoT) reasoning, it encourages deeper introspection before assigning a confidence score.

- **Advantages:**
- Simple and effective, especially when the LLM has access to the context.
- The reasoning provided by the LLM could give valuable insights into why a certain score was assigned, helping developers understand where hallucinations are likely.
- Scalable since it involves no external processes or systems.
- **Potential Challenges:**
- The LLM’s self-assessment might still be biased or flawed, especially if the LLM initially hallucinated due to misunderstanding the context.
- It may still miss subtle factual inconsistencies.

## 2\. G-Eval (from DeepEval package):

G-Eval improves upon simple self-evaluation by introducing a multi-step criterion-based evaluation. By using predefined criteria to measure the factual correctness of a response, it provides a more structured way for LLMs to reason about the accuracy of their output.

- **Advantages:**
- More rigorous than self-evaluation as it considers multi-step criteria, providing a more detailed and systematic evaluation.
- Proven correlation with human judgment on several datasets makes it a reliable method for applications where accuracy is critical.
- **Potential Challenges:**
- Complexity increases, as setting up and fine-tuning multi-step criteria for diverse use cases may require additional effort.
- May need fine-tuning based on the specific knowledge database and context format.

## 3\. Hallucination Metric (from DeepEval package):

This method uses one LLM to evaluate the degree to which another LLM’s response contradicts the retrieved context. The idea is to detect contradictions between the generated answer and the provided context, which could signal hallucination.

- **Advantages:**
- This metric focuses explicitly on contradiction detection, which is one of the main signs of hallucinations.
- Having a second LLM review the response introduces a new perspective, reducing the chance of unchecked hallucinations.
- **Potential Challenges:**
- Running multiple LLM evaluations can increase computation costs.
- Not all hallucinations are contradictions; some hallucinations may introduce new, unsupported information without direct contradiction, so it might miss such cases.

## 4\. RAGAS:

The RAG-specific evaluation suite, RAGAS, is a powerful tool that provides multiple scores, each tailored to evaluating different aspects of hallucination in RAG systems. The three key scores are:

- **Faithfulness:** Measures the fraction of claims in the response that are supported by the retrieved context.
- **Advantages:** Directly assesses how grounded the response is in the retrieved information, helping catch instances where the model “makes things up.”
- **Challenges:** May require precise context retrieval to be fully effective.
- **Answer Relevancy:** Computes the similarity between the original question and LLM-generated questions based on the response, using vector embeddings.
- **Advantages:** Ensures that the generated response is relevant to the question, filtering out irrelevant or off-topic hallucinations.
- **Challenges:** While it checks for relevancy, it might not catch factual inaccuracies if the response is relevant but wrong.
- **Context Utilization:** Assesses the degree to which the context was used in forming the response.
- **Advantages:** Identifies whether the LLM relied on the provided context, catching hallucinations due to insufficient reliance on the retrieved information.
- **Challenges:** This score alone won’t guarantee correctness; context utilization must be paired with other metrics to ensure faithfulness.

## 5\. Strategic Use Cases for Detection Methods:

- **High-Stakes Applications:** For sectors like healthcare, law, and finance, using a combination of these methods could be crucial. For example, **Self-eval** could provide a quick, scalable approach to flag potential hallucinations, while **G-Eval** or the **Hallucination Metric** could serve as more intensive, second-layer checks for higher confidence levels.
- **Cost-Optimization in RAG Systems:** Methods like **Self-eval** or **Answer Relevancy** could be used early in the retrieval pipeline to determine when a response should be trusted or whether it’s worth invoking more resource-intensive retrieval or re-querying steps. If a high confidence is obtained early, this could avoid unnecessary computational overhead.

## 6\. Combined Approach to Detection:

Each of these methods has strengths and weaknesses, but they can be combined for robust detection. A practical implementation might involve:

- **Self-eval** as a quick, lightweight first-pass filter.
- **G-Eval** or the **Hallucination Metric** as a second-pass evaluator for cases where the initial self-assessment indicates low-to-moderate confidence.
- **RAGAS scores** as a final measure for faithfulness, relevancy, and context utilization, allowing developers to fine-tune responses based on specific application needs.

By incorporating these detection methods into RAG systems, we can better ensure that LLM responses are trustworthy and avoid the detrimental effects of hallucinations in sensitive.

Here is the specific prompt template used:

```
Question: {question}
Answer: {response}Evaluate how confident you are that the given Answer is a good and accurate response to the Question.
Please assign a Score using the following 5-point scale:
1: You are not confident that the Answer addresses the Question at all, the Answer may be entirely off-topic or irrelevant to the Question.
2: You have low confidence that the Answer addresses the Question, there are doubts and uncertainties about the accuracy of the Answer.
3: You have moderate confidence that the Answer addresses the Question, the Answer seems reasonably accurate and on-topic, but with room for improvement.
4: You have high confidence that the Answer addresses the Question, the Answer provides accurate information that addresses most of the Question.
5: You are extremely confident that the Answer addresses the Question, the Answer is highly accurate, relevant, and effectively addresses the Question in its entirety.The output should strictly use the following template: Explanation: [provide a brief reasoning you used to derive the rating Score] and then write ‘Score: <rating>’ on the last line.
```

Here is the prompt template used to prompt TLM:

```
Answer the QUESTION using information only from
CONTEXT: {context}
QUESTION: {question}
```

Now we will simplify 6 types of RAG’s !!

## **Standard RAG:**

Standard RAG (Retrieval-Augmented Generation) is a framework designed to combine retrieval mechanisms with language generation models. Its main goal is to enhance the accuracy and relevance of generated text by retrieving related information from external sources and then using that retrieved data as input to a generative model, typically a large language model (LLM) like GPT or BERT.

![](https://miro.medium.com/v2/resize:fit:1400/1*BbrpYPDEmlNAHtrZmqVd_g.jpeg)

Here’s how Standard RAG works:

## 1\. Document Retrieval:

- In the first step, RAG retrieves relevant documents from an external knowledge base (like a database, a set of documents, or even the web) based on a given query or user input.
- This retrieval process is usually done using embeddings-based similarity search. A common model used for this is a dense retriever, such as **DPR (Dense Passage Retrieval)**, which converts both the query and documents into vectors and retrieves the most similar documents.

## 2\. Contextual Document Integration:

- Once the relevant documents are retrieved, they are passed along with the original user input (query) to a generative model.
- These documents act as additional context for the generative model, allowing it to provide more accurate and contextually informed responses.

## 3\. Answer Generation:

- The generative model (often based on Transformer architectures like GPT-3 or similar) combines the original user query with the retrieved documents and generates a coherent response that synthesizes the retrieved information.
- The final output is usually more precise and factually grounded compared to a purely generative model because the model has direct access to the relevant documents.

## Example Workflow of Standard RAG:

- **Query**: The user asks a question like “What is the capital of France?”
- **Retrieval**: The system retrieves documents that mention France, capital cities, and related topics.
- **Augmentation**: These retrieved documents are fed into the generative model.
- **Generation**: The model produces an answer like “The capital of France is Paris,” based on both its pre-training knowledge and the retrieved documents.

## **Corrective RAG**

Corrective RAG (Retrieval-Augmented Generation) is an extension or variation of the RAG framework that integrates a retrieval mechanism with a generative model. In Corrective RAG, the focus is on using feedback or correction loops to improve the quality and accuracy of generated responses by refining the retrieved information or adjusting the generated outputs based on errors or inconsistencies.

![](https://miro.medium.com/v2/resize:fit:1400/1*vCNrTwvCElF2SIokpVFklw.png)

Here’s how Corrective RAG generally works:

1. **Retrieval-Augmented Generation (RAG) Overview**:

- **Retrieval**: A retriever model is used to fetch relevant documents or data from a knowledge base based on the input query.
- **Generation**: A generative model (like GPT) takes both the query and the retrieved documents as input and generates a response using this augmented information.

**2\. Corrective RAG Enhancements**:

- **Initial Generation**: The initial RAG process happens where a response is generated based on retrieved information and the input query.
- **Error Detection**: A secondary system (often using another model or a human feedback loop) identifies potential errors, inconsistencies, or areas of improvement in the generated output. This could involve fact-checking, correcting grammar, or refining the relevance of the generated answer.
- **Correction Process**: Based on the detected errors, corrective feedback is provided. This could involve:
- **Re-retrieval**: Triggering the retriever to fetch more accurate or additional supporting information based on the errors.
- **Re-generation**: The generative model reprocesses the query and retrieved documents, incorporating corrections to improve accuracy and coherence.
- **Looping**: This correction loop can iterate multiple times until a satisfactory or error-free output is generated.

**3\. Feedback Integration**:

- **Human-in-the-loop**: In some cases, human feedback can be provided to improve the corrective process, either by validating the correction or suggesting modifications manually.
- **Automatic Feedback**: Alternatively, machine learning models (e.g., classifiers or ranking models) can be used to automatically assess the quality of outputs and trigger corrective actions.

**4\. Applications of Corrective RAG**:

- **Fact-checking**: Ensuring generated responses are factually accurate.
- **Error Handling in Conversational AI**: Correcting misunderstandings or inaccurate answers in chatbots or virtual assistants.
- **Improving QA Systems**: Enhancing question-answering systems by continuously refining answers through feedback and correction loops.

## **Speculative RAG**

**Speculative Retrieval-Augmented Generation (Speculative RAG)** is an advanced technique that combines retrieval-based and generative models to enhance the efficiency and effectiveness of generating factual and accurate text. The main idea is to speed up the generation process by using a retrieval system to fetch relevant information early on, allowing the generative model to focus on more specific tasks rather than generating the entire text from scratch.

![](https://miro.medium.com/v2/resize:fit:2000/1*MDau9Z9SPnAcZqw-TJ7jDg.png)

Here’s how **Speculative RAG** works:

## Key Components:

1. **Retrieval Model**: This system searches and retrieves relevant documents or information from a large corpus, such as a database or the web. The retrieved documents are the basis for the generation process, providing factual grounding to the model.
2. **Generative Model**: A large language model (LLM) generates text based on the input from the retrieval model. The model leverages the retrieved information to produce coherent and contextually accurate responses.
3. **Speculative Generation**: The generative model first predicts or “speculates” on the output based on an initial set of retrievals and its own internal knowledge. If the retrieval system finds highly relevant data, the model revises its predictions, improving accuracy. If the retrieved information is already accurate, the process continues seamlessly.
4. **Parallel Processing**: Speculative RAG accelerates the generation process by running the retrieval and generative processes in parallel. The generative model does not wait for the retrieval system to finish; instead, it begins generating based on partial or initial retrievals and adjusts its output as more relevant information becomes available.

## How It Works:

1. **Initial Query**: A user poses a question or query.
2. **Retrieval Step**: The system sends this query to the retrieval model, which searches for relevant documents or sources from a knowledge base.
3. **Speculative Generation**: Simultaneously, the generative model begins constructing a response based on partial information or its own internal knowledge.
4. **Feedback Loop**: As more relevant information is retrieved, the speculative generation is refined in real-time. The final output is a combination of generative reasoning and factual data from the retrieval system.
5. **Response**: The model delivers a faster and more factually accurate response, as the retrieval system acts as a “corrector” or “guide” for the generative model’s output.

## Benefits:

- **Faster Response Time**: Since the retrieval and generation happen simultaneously, it reduces latency compared to traditional RAG, where the generation process waits for retrieval results.
- **Improved Accuracy**: The speculative nature helps the generative model correct potential errors by using more accurate information from the retrieved documents.
- **Efficiency**: It optimizes the retrieval-augmented generation process by reducing the need for multiple interactions between the retrieval and generative systems.

Speculative RAG is useful in applications where speed and factual accuracy are crucial, such as in customer support, research assistance, and real-time data generation.

## **Fusion RAG**

**Fusion RAG (Fusion Retrieval-Augmented Generation)** is a hybrid approach that combines retrieval-based methods with generation-based techniques for enhancing the performance of AI models, particularly in tasks that involve answering complex queries or generating text. The approach is particularly useful in open-domain question answering, where the system needs to access external information to provide accurate and contextually relevant answers.

![](https://miro.medium.com/v2/resize:fit:1400/1*jp_upWrKyzfFqA0AzrIShw.png)

## How Fusion RAG Works

1. **Retrieval (R)**:

- The first step involves retrieving relevant documents or pieces of information from a large corpus (such as knowledge bases, web pages, or databases).
- This is usually done using dense retrieval models like **BERT** or **bi-encoder models**, which can efficiently search for documents most relevant to the input query.
- The retrieval model finds a set of documents or passages that are likely to contain relevant information.

**2\. Fusion (F)**:

- The retrieved information is then fused together. This step involves combining relevant sections from multiple documents.
- The fusion process enhances the richness and diversity of the information, ensuring the final result draws on a broader and more comprehensive range of knowledge.
- This can be done through techniques such as attention mechanisms or weighted aggregation of the retrieved content.

**3\. Augmented Generation (AG)**:

- After retrieving and fusing the relevant information, the model uses a **generation model** (like a Transformer-based language model) to create a response or output based on the input query and the retrieved documents.
- The generation model uses the retrieved content as an additional context, improving the accuracy and relevance of the generated response.

## Key Features

- **Hybrid Approach**: Fusion RAG leverages both retrieval-based models (for precision) and generative models (for fluency and creativity).
- **Efficient Knowledge Integration**: Instead of generating responses purely from internal parameters, the model incorporates external knowledge for better factual accuracy.
- **Scalability**: It can handle large datasets or knowledge bases, making it suitable for applications like chatbots, search engines, or even complex decision support systems.

## Benefits

- **Enhanced Accuracy**: The combination of retrieval and generation ensures that the responses are both relevant and factually correct.
- **Dynamic Knowledge Updating**: The retrieval component allows the system to use up-to-date information, unlike static language models that rely on pre-trained knowledge.
- **Versatility**: This method can be applied to various domains, including customer support, research, and even content creation, where accurate and context-aware responses are essential.

## **Agentic RAG**

**Agentic Retrieval-Augmented Generation (RAG)** is an advanced framework designed to enhance traditional Retrieval-Augmented Generation models by integrating agency, or decision-making abilities, into the workflow. Standard RAG models combine a language model (like GPT or BERT) with a retrieval system to fetch relevant documents from external databases, which are then used to generate responses. The agentic variant goes beyond this by incorporating additional decision-making components that give the system more autonomy and context-awareness in managing tasks.

![](https://miro.medium.com/v2/resize:fit:1400/1*IN8y-UPfNkmrULC4NcsKQQ.jpeg)

## Key Components of Agentic RAG

1. **Retrieval Mechanism**: Like standard RAG, Agentic RAG retrieves external knowledge from structured or unstructured databases based on a query. This could be a database, document repository, or any knowledge source.
2. **Generation Mechanism**: After retrieval, a language model generates a response that is informed by the retrieved documents. This ensures that responses are grounded in factual information.
3. **Agentic Layer (Decision-Making)**: What sets Agentic RAG apart is that it introduces an additional layer that can make decisions based on the context, retrieved information, and the user’s needs. This decision-making process allows the model to:

- **Plan** actions over multiple steps to achieve a goal.
- **Decide** which data to prioritize or retrieve.
- **Control** the flow of information, determining whether to retrieve more, generate a response, or ask for clarification.

## How Agentic RAG Works:

1. **Query Understanding**: The system first interprets the query or task provided by the user. This could be a complex request requiring multiple pieces of information from various sources.
2. **Document Retrieval**: Using a retrieval engine (like Elasticsearch or a vector-based database), the model retrieves relevant documents from a knowledge source. In Agentic RAG, this retrieval step can be optimized based on the context and agentic decision-making processes (e.g., it may choose to retrieve additional documents for better accuracy or stop if the retrieved information is sufficient).
3. **Agentic Decision-Making**: At this stage, the model decides:

- How to use the retrieved documents.
- Whether to retrieve more data.
- If a subtask (such as parsing or filtering) needs to be performed before generation.

1. The agentic system assesses whether the current data meets the requirements for generating a reliable response.
2. **Response Generation**: The model uses the retrieved information and the decisions made in the previous step to generate an accurate, coherent, and contextually relevant response. The generation step relies on large language models to synthesize information.
3. **Post-Processing and Control Flow**: If necessary, the system can engage in multi-turn dialogues, seeking clarification or additional input from the user before finalizing its response. It might also store outcomes for future learning, improving the response quality over time.

## Example Use Case:

- **Due Diligence in M&A**: In mergers and acquisitions, due diligence involves analyzing various financial and legal documents. An Agentic RAG system could autonomously retrieve relevant financial reports, analyze trends, and decide whether more information is needed. It could also summarize findings and offer recommendations based on predefined decision criteria.

## Advantages of Agentic RAG:

- **Autonomy**: By incorporating decision-making, it can handle more complex queries that require dynamic retrieval and multi-step processing.
- **Efficiency**: The agentic component optimizes the retrieval process, reducing unnecessary information fetching and focusing only on what’s needed.
- **Contextual Awareness**: It’s capable of understanding broader contexts and making informed decisions on the fly.

This approach makes Agentic RAG highly useful for complex tasks in areas like research, decision support, and automation of knowledge-heavy workflows.

## **Self RAG**

Self-Retrieval-Augmented Generation (Self-RAG) is an extension of the Retrieval-Augmented Generation (RAG) paradigm, which combines the benefits of large language models (LLMs) with external information retrieval systems to generate more accurate and grounded responses.

![](https://miro.medium.com/v2/resize:fit:2000/1*jcUR3kVzcDBSmWCYKTlNVQ.png)

## How Self-RAG Works:

1. **Initial Query Generation**: The system starts with an initial query, either provided by the user or generated by the model itself based on a given input.
2. **Self-Retrieval Step**: The model queries its own knowledge base or an external data source to retrieve relevant documents or information that can help generate a more accurate response. The retrieval system could be a traditional search engine, a dense retriever (like sentence transformers), or a vector database with embeddings.
3. **Self-Selection of Evidence**: From the retrieved information, the model selects or scores the most relevant pieces of evidence. This self-selection is crucial as it filters out unnecessary or less relevant information.
4. **Generation with Augmented Knowledge**: The LLM generates a response by incorporating the retrieved and selected information. This “augmented” generation is meant to ensure that the output is more factually grounded and contextually relevant, improving both the accuracy and the quality of the generated text.
5. **Feedback Loop (Optional)**: In some implementations, the model might perform multiple iterations, refining the query or the retrieved evidence in response to how well the previous generation matched the input prompt.

## Key Benefits:

- **Factual Accuracy**: By retrieving relevant documents, Self-RAG ensures the generated responses are grounded in reality, improving factual correctness.
- **Reduced Hallucination**: LLMs sometimes produce information that sounds plausible but is incorrect. By consulting external sources, Self-RAG reduces this risk.
- **Adaptability**: The retrieval system can be tailored to different knowledge domains, allowing Self-RAG to adapt to specific tasks or topics.

## Applications:

Self-RAG is often used in tasks like:

- Document generation based on large knowledge bases.
- Question answering, where the model needs external evidence.
- Personalized responses, where user-specific data is retrieved.

## **RAG Code Implementation :**

## Tools Used:

- **LangChain**: A framework for building applications with LLMs.
- **LlamaIndex (formerly GPT Index)**: A library to efficiently query a document using a large language model.
- **LangSmith**: A tool for observability, logging, and experimentation with large language models.
- **RetrieverQA**: A QA mechanism where the model first retrieves relevant information from a knowledge base, then uses that information to generate a response.

## Plan in Pseudocode:

1. **Set up LangChain**: Use LangChain to handle the interaction between LLM and retrievers.
2. **Configure LlamaIndex**: Build the index to enable efficient document retrieval.
3. **Set up Retriever**: Use RetrieverQA to query the document with relevant data.
4. **Connect LangSmith**: Monitor the interactions, responses, and retriever performance.
5. **Final Response Generation**: Combine the retrieved documents with LLM to generate the final answer.

## Steps:

1. **Install Required Libraries**: First, install the required libraries.

```
!pip install langchain llama-index langsmith retriever-qa
```

**Code Implementation**: Here’s how to implement the RAG framework with LangChain, LlamaIndex, and LangSmith using RetrieverQA.

```
from langchain.llms import OpenAI
from llama_index import SimpleDocument, GPTSimpleVectorIndex
from retriever_qa import RetrieverQA
from langchain.prompts import PromptTemplate
from langsmith import Client
client = Client(api_key="YOUR_LANGSMITH_API_KEY")
documents = [
    SimpleDocument("The capital of France is Paris."),
    SimpleDocument("Python is a popular programming language."),
    SimpleDocument("The human brain has 86 billion neurons.")
]
index = GPTSimpleVectorIndex.from_documents(documents)
retriever_qa = RetrieverQA(retriever=index)
llm = OpenAI(model="gpt-4", temperature=0.5)
prompt_template = PromptTemplate(
    template="You are a helpful assistant. Use the following retrieved documents to answer the question:\n{retrieved_docs}\n\nQuestion: {question}\nAnswer:",
    input_variables=["retrieved_docs", "question"]
)
def rag_retriever_qa(query):
    
    retrieved_docs = retriever_qa.retrieve(query)    
    formatted_docs = "\n".join([doc.text for doc in retrieved_docs])        
    prompt = prompt_template.format(retrieved_docs=formatted_docs, question=query)        
    answer = llm.generate(prompt)        
    client.log_interaction(
        input=prompt,
        output=answer,
        retriever=retrieved_docs,
        question=query
    )    return answer
if __name__ == "__main__":
    query = "What is the capital of France?"
    response = rag_retriever_qa(query)
    print(f"Answer: {response}")
```

## Explanation of the Code:

1. **LangChain Initialization**:

- The `OpenAI` object from `langchain.llms` initializes the connection to an OpenAI LLM (e.g., GPT-4), which is used for generating the final response based on retrieved documents.
- `temperature=0.5` is used for controlling the randomness in the output. A lower value makes the model more deterministic.

**2\. LlamaIndex**:

- The `SimpleDocument` class creates a document object. In this case, we provide three example documents that will be indexed.
- `GPTSimpleVectorIndex` builds an index from these documents. This index will later be used to retrieve relevant information.

**3\. RetrieverQA**:

- `RetrieverQA` is initialized with the retriever (i.e., the LlamaIndex) that it will use to retrieve relevant information based on the query.
- The `.retrieve()` method returns relevant documents that match the query from the index.

**4\. Prompt Template**:

- `PromptTemplate` defines the structure of the prompt that the LLM will use. It takes the retrieved documents and the user's query as inputs. The prompt asks the LLM to use the retrieved documents to answer the question.

**5\. LangSmith for Observability**:

- LangSmith’s `Client` object logs the input, output, and retrieval steps of the interaction. This helps track and debug interactions over time.
- `client.log_interaction()` captures the prompt, response, retriever details, and query to store them for analysis.

**6\. RAG Flow**:

- The `rag_retriever_qa` function executes the full RAG process. First, it retrieves relevant documents from the LlamaIndex, then uses those documents to generate a response with the OpenAI LLM. The prompt is formatted to include both the retrieved documents and the original question.

**7\. Running the Code**:

- Finally, an example query `"What is the capital of France?"` is passed to the function, and the generated answer is printed.

To implement **caching** and use a **more sophisticated vector-based search with embeddings** for better retrieval performance, we’ll enhance the code in the following ways:

## Steps:

1. **Caching**: Implement a simple caching mechanism so that frequently asked questions do not require repeated retrieval from the LLM and documents.
2. **Embeddings for Vector-based Search**: Use a language model to create embeddings for documents and the query. These embeddings will be used for efficient vector-based search.

We’ll use **OpenAIEmbeddings** (or another embedding provider) to generate the embeddings for documents and queries, and we’ll enhance the retriever to perform vector similarity search.

## Plan:

1. **Embeddings Generation**:

- Use a pre-trained model (e.g., OpenAI, Hugging Face) to generate embeddings for both the documents and the queries.
- Store these embeddings in a vector database.

**2\. Caching**:

- Use a dictionary to store the previous queries and their answers to avoid unnecessary repeated processing.

**3\. Efficient Vector Retrieval**:

- Perform similarity search using embeddings to retrieve the most relevant documents.

Let’s walk through the updated code implementation.

```
from langchain.llms import OpenAI
from llama_index import SimpleDocument, GPTSimpleVectorIndex, VectorIndexRetriever
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langsmith import Client
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict
client = Client(api_key="YOUR_LANGSMITH_API_KEY")
documents = [
    SimpleDocument("The capital of France is Paris."),
    SimpleDocument("Python is a popular programming language."),
    SimpleDocument("The human brain has 86 billion neurons.")
]
embedding_model = OpenAIEmbeddings()doc_texts = [doc.text for doc in documents]
doc_embeddings = embedding_model.embed_documents(doc_texts)
cache = defaultdict(lambda: None)
def get_top_k_similar(query_embedding, doc_embeddings, k=3):
    similarities = cosine_similarity([query_embedding], doc_embeddings)
    top_k_indices = np.argsort(similarities[0])[-k:][::-1]
    return top_k_indices
def retrieve_documents(query):
    
    if cache[query]:
        return cache[query]    
    query_embedding = embedding_model.embed_query(query)        
    top_k_indices = get_top_k_similar(query_embedding, doc_embeddings)        
    retrieved_docs = [documents[i] for i in top_k_indices]    
    cache[query] = retrieved_docs        return retrieved_docs
llm = OpenAI(model="gpt-4", temperature=0.5)
prompt_template = PromptTemplate(
    template="You are a helpful assistant. Use the following retrieved documents to answer the question:\n{retrieved_docs}\n\nQuestion: {question}\nAnswer:",
    input_variables=["retrieved_docs", "question"]
)
def rag_retriever_qa(query):
    
    retrieved_docs = retrieve_documents(query)    
    formatted_docs = "\n".join([doc.text for doc in retrieved_docs])        
    prompt = prompt_template.format(retrieved_docs=formatted_docs, question=query)        
    answer = llm.generate(prompt)        
    client.log_interaction(
        input=prompt,
        output=answer,
        retriever=retrieved_docs,
        question=query
    )    return answer
if __name__ == "__main__":
    query = "What is the capital of France?"
    response = rag_retriever_qa(query)
    print(f"Answer: {response}")
```

## Explanation of Changes:

1. **Embedding Generation**:

- We use `OpenAIEmbeddings` to generate embeddings for both the documents and queries.
- The `embed_documents()` method generates embeddings for the list of document texts, and `embed_query()` is used to create embeddings for the query.

**2\. Cosine Similarity for Vector-based Retrieval**:

- The `get_top_k_similar` function calculates the cosine similarity between the query embedding and the document embeddings using `scikit-learn`'s `cosine_similarity` function. It returns the indices of the top `k` most similar documents.
- The top documents are selected based on the highest similarity scores and returned as the retrieved documents.

**3\. Caching**:

- A `defaultdict` is used as a simple cache to store the results for each query. If the same query is made again, it returns the cached result instead of recomputing the embeddings and similarity.

**4\. Integration with LangChain**:

- Once the relevant documents are retrieved, the `formatted_docs` is passed into the prompt template, which then generates a response using the OpenAI LLM.

**5\. LangSmith Logging**:

- As before, we log each interaction (input, output, retrieved docs, and query) using `LangSmith` for observability.

## Caching and Retrieval Optimization:

- **Efficiency**: The cache avoids unnecessary calls to the embedding model and LLM, thus speeding up responses for repeated queries.
- **Accuracy**: By using embeddings and cosine similarity, we are performing more sophisticated retrieval than simple keyword matching.

## **Using LangChain Agents :**

To implement Retrieval-Augmented Generation (RAG) using **LangChain Agents**, **LlamaIndex**, **LangSmith**, and **RetrieverQA**, we’ll build a system where LangChain agents will dynamically retrieve relevant documents using LlamaIndex and handle the question-answering process with RetrieverQA. The responses and retrieval steps will be logged using LangSmith for observability.

## Steps to Implement:

1. **LangChain Agents**: We’ll use LangChain’s agent system to dynamically retrieve documents based on the user query.
2. **LlamaIndex**: This will be used to create an efficient index from documents and handle vector-based search to retrieve relevant information.
3. **RetrieverQA**: Used to handle question answering by retrieving documents based on the query and generating the final response.
4. **LangSmith**: Used for logging interactions (prompts, responses, retrieval steps) and debugging.

## Dependencies:

You need the following libraries installed:

```
!pip install langchain llama-index langsmith retriever-qa
```

## High-Level Flow:

1. **Agent Setup**: A LangChain agent will handle the question-answering flow. It will retrieve the relevant documents from LlamaIndex, use RetrieverQA to fetch answers, and then use the LLM to generate the final response.
2. **LlamaIndex for Document Retrieval**: The agent will interact with LlamaIndex to retrieve the most relevant documents from the indexed knowledge base.
3. **RetrieverQA**: The agent will use RetrieverQA to retrieve answers based on the documents retrieved from the index.
4. **Logging with LangSmith**: Each step of the retrieval and generation process will be logged using LangSmith.

## Code:

```
from langchain.agents import initialize_agent, Tool, AgentExecutor
from langchain.llms import OpenAI
from llama_index import SimpleDocument, GPTSimpleVectorIndex
from retriever_qa import RetrieverQA
from langchain.prompts import PromptTemplate
from langsmith import Client
client = Client(api_key="YOUR_LANGSMITH_API_KEY")
documents = [
    SimpleDocument("The capital of France is Paris."),
    SimpleDocument("Python is a popular programming language."),
    SimpleDocument("The human brain has 86 billion neurons.")
]
index = GPTSimpleVectorIndex.from_documents(documents)
retriever_qa = RetrieverQA(retriever=index)
llm = OpenAI(model="gpt-4", temperature=0.5)
prompt_template = PromptTemplate(
    template="You are a helpful assistant. Use the following retrieved documents to answer the question:\n{retrieved_docs}\n\nQuestion: {question}\nAnswer:",
    input_variables=["retrieved_docs", "question"]
)def retrieve_documents(query):
    
    retrieved_docs = retriever_qa.retrieve(query)        
    formatted_docs = "\n".join([doc.text for doc in retrieved_docs])        
    client.log_interaction(
        input=query,
        output=formatted_docs,
        retriever=retrieved_docs
    )        return formatted_docsdef generate_answer(query, retrieved_docs):
    
    prompt = prompt_template.format(retrieved_docs=retrieved_docs, question=query)        
    answer = llm.generate(prompt)        
    client.log_interaction(
        input=prompt,
        output=answer,
        question=query
    )        return answer
tools = [
    Tool(
        name="Document Retriever",
        func=retrieve_documents,
        description="Retrieve relevant documents based on a query."
    ),
    Tool(
        name="Answer Generator",
        func=generate_answer,
        description="Generate a final answer based on retrieved documents."
    )
]

agent = initialize_agent(
    tools=tools,
    agent_type="zero-shot-react-description",  
    llm=llm
)
def rag_with_agent(query):
    
    
    result = agent.run(query)        return result
if __name__ == "__main__":
    query = "What is the capital of France?"
    response = rag_with_agent(query)
    print(f"Answer: {response}")
```

## Detailed Explanation:

1. **LangSmith Initialization**:

- The `LangSmith` client is initialized for logging each interaction (input, output, retriever, and question). This enables observability and debugging of the RAG process.

**2\. Document Indexing** with **LlamaIndex**:

- We load some example documents (like the capital of France, programming in Python, etc.) and create an index using `GPTSimpleVectorIndex`. This index will later be used to retrieve relevant information.

**3\. RetrieverQA Setup**:

- `RetrieverQA` is initialized using the LlamaIndex as the retriever. It will handle the retrieval of relevant documents based on the user query.

**4\. LangChain LLM**:

- An OpenAI LLM (GPT-4 in this case) is instantiated. This will be used to generate the final answers based on the documents retrieved by `RetrieverQA`.

**5\. LangChain Agent and Tools**:

- We define two tools for the LangChain agent:

**Document Retriever**: This tool retrieves relevant documents from the LlamaIndex. It formats the documents and logs the interaction using LangSmith.

**Answer Generator**: This tool takes the retrieved documents and generates a final response using the LLM.

- These tools are passed into the LangChain agent using `initialize_agent`. The agent dynamically decides how to use these tools based on the descriptions.

**6\. RAG Flow**:

- In the `rag_with_agent` function, we pass the query to the agent. The agent retrieves the relevant documents using the `Document Retriever` tool and then generates the answer using the `Answer Generator` tool.
- The result is returned as the final answer.

**7\. Logging**:

- Each interaction (retrieval and answer generation) is logged using LangSmith. This is useful for observability and monitoring the performance of both the retriever and the generator.

## Example Usage:

If you run the script with the query `"What is the capital of France?"`, the system will:

1. Retrieve the relevant document about Paris from the LlamaIndex.
2. Pass this document into the LLM, which generates the final answer: `"The capital of France is Paris."`

## And here is the joke !!

Why did the Retrieval-Augmented Generation (RAG) model go to therapy?

Because it had too many *unresolved queries*! 😄