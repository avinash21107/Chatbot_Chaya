Key Components:
The code uses several libraries to build the agent:

langchain_ollama: This library connects the agent to a language model (LLM) running locally via Ollama. In this case, it's using the "gemma3:1b" model.

langchain_tavily: This provides a tool for the agent to perform internet searches using the Tavily Search API.

langchain.memory: This component, specifically ConversationBufferMemory, allows the agent to remember the conversation history. It stores the user's and the agent's past messages, which helps the agent maintain context.

langchain.agents: This is the core of the program. It initializes the agent itself, which acts as the decision-maker. It decides whether to answer a question directly using the LLM's knowledge or to use one of the available tools, like the Tavily search tool, to find information.

dotenv: This library loads environment variables from a .env file, which is a common practice for securely handling sensitive information like API keys.

How It Works
Initialization: The code first sets up the necessary components: the language model (llm), the memory buffer, and the search tool.

Agent Creation: It then uses initialize_agent to create the conversational agent. The agent is given access to the tools (in this case, just the search tool) and is configured to remember the conversation using the memory object.

User Interaction: The if __name__ == "__main__": block starts a loop that prompts the user for input.

generate_response Function: When the user provides input, this function is called. The agent.invoke() method is the key part of this process. The agent analyzes the user's input:

If the input requires a search (e.g., "What's the weather in Paris?"), the agent will use the TavilySearch tool.

If the input is a general conversation question (e.g., "Hello, how are you?"), the agent will respond using the gemma3:1b language model and its memory of the conversation.

Output: The agent's response is printed to the console. The loop continues until the user types "exit" or "quit," ending the conversation.

In essence, this program creates a smart chatbot that can both chat and perform real-time searches to provide up-to-date or specific information to the user.







give me a readme file for the same


Here's a README.md file for the Python script you provided.

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
