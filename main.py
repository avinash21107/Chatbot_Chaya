# import ollama
#
# print("Chaya is online! 💬")
#
#
# conversation_history = [
#     {"role": "system", "content": "You are Chaya, a friendly chatbot."}
# ]
#
# def generate_response(user_input):
#     """
#     Generates a response from the LLaMA 3 model running locally via Ollama.
#     """
#
#     conversation_history.append({"role": "user", "content": user_input})
#
#     # Pass the whole history so the model remembers past context
#     response = ollama.chat(
#         model="gemma3:1b",
#         messages=conversation_history
#     )
#
#     reply = response['message']['content']
#
#
#     conversation_history.append({"role": "assistant", "content": reply})
#
#     return reply
#
#
# if __name__ == "__main__":
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["exit", "quit"]:
#             print("Chaya: Goodbye Avinash 👋")
#             break
#
#         reply = generate_response(user_input)
#         print(f"Chaya: {reply}")
from dotenv import load_dotenv
# --------------------------------------------------------------------------------------------------

# from langchain_ollama import ChatOllama
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.runnables.history import RunnableWithMessageHistory
# from langchain.memory import ChatMessageHistory
# from langchain_community.tools.tavily_search import TavilySearchResults
#
# print("Chaya is online! 💬")
#
# # Use the new Ollama wrapper
# llm = ChatOllama(model="gemma3:1b")
#
# # Define a simple prompt template
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are Chaya, a friendly chatbot."),
#     ("human", "{input}")
# ])
#
# # Combine prompt + LLM
# chain = prompt | llm
#
# # Set up memory
# history = ChatMessageHistory()
# runnable = RunnableWithMessageHistory(
#     chain,
#     lambda session_id: history,
#     input_messages_key="input",
#     history_messages_key="history"
# )
#
# if __name__ == "__main__":
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["exit", "quit"]:
#             print("Chaya: Goodbye Avinash 👋")
#             break
#
#         reply = runnable.invoke(
#             {"input": user_input},
#             config={"configurable": {"session_id": "chat-1"}}
#         )
#         print(f"Chaya: {reply.content}")
#------------------------------------------------------------------------------------------------------


from langchain_ollama import ChatOllama
from langchain_ollama import ChatOllama
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.agents import initialize_agent, AgentType
from langchain_tavily import TavilySearch
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

print("Chaya is online! 💬")
load_dotenv()
# === LLM (Ollama) ===
llm = ChatOllama(model="gemma3:1b")

# === Memory for ongoing conversation ===
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# === Tools (Tavily Search) ===
api_key = os.getenv("API_KEY")
search_tool = TavilySearch(max_results=2, tavily_api_key=api_key)

# === Agent Setup ===
tools = [search_tool]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,
    memory=memory  # 🔥 now your agent remembers the conversation
)


def generate_response(user_input: str) -> str:
    """
    Uses an agent: Chaya decides when to use tools vs. LLM.
    """
    try:
        return agent.invoke(user_input)["output"]
    except Exception as e:
        return f"Sorry this cannot be processed:{e}"


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chaya: Goodbye Avinash 👋")
            break

        reply = generate_response(user_input)
        print(f"Chaya: {reply}")
