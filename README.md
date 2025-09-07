Chaya: Conversational AI Agent
Chaya is a conversational AI assistant built with LangChain that can chat and search the web for information. This agent is designed to remember the context of the conversation and can dynamically decide whether to answer a question using its own knowledge or by using an internet search tool.

Features
Conversational Memory: Remembers past interactions to maintain a continuous and meaningful conversation.

Intelligent Decision-Making: The agent can choose when to use its language model to answer directly and when to perform an internet search for up-to-date or specific information.

Customizable: Easily swap out the language model and add more tools to extend the agent's capabilities.

Requirements
Before running the application, make sure you have the following installed:

Python 3.8+

Ollama: A tool for running open-source language models locally. Download Ollama here.

An Ollama model: The script is configured to use the gemma3:1b model.

A Tavily API Key: Required for the internet search functionality.
