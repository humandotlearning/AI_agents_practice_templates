from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import AnyMessage, HumanMessage, AIMessage
from langgraph.prebuilt import ToolNode
from langgraph.graph import START, StateGraph
from langgraph.prebuilt import tools_condition
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from retriever import guest_info_tool
from data import docs

from dotenv import load_dotenv
import os

class AgenticRAGAgent:
    def __init__(self):
        load_dotenv()
        HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
        self.llm = HuggingFaceEndpoint(
            repo_id="Qwen/Qwen2.5-Coder-32B-Instruct",
            huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
        )
        self.chat = ChatHuggingFace(llm=self.llm, verbose=True)
        self.tools = [guest_info_tool]
        self.chat_with_tools = self.chat.bind_tools(self.tools)
        self.alfred = self._build_graph()

    class AgentState(TypedDict):
        messages: Annotated[list[AnyMessage], add_messages]

    def assistant(self, state: 'AgenticRAGAgent.AgentState'):
        return {
            "messages": [self.chat_with_tools.invoke(state["messages"])],
        }

    def _build_graph(self):
        builder = StateGraph(self.AgentState)
        builder.add_node("assistant", self.assistant)
        builder.add_node("tools", ToolNode(self.tools))
        builder.add_edge(START, "assistant")
        builder.add_conditional_edges(
            "assistant",
            tools_condition,
        )
        builder.add_edge("tools", "assistant")
        return builder.compile()

    def ask(self, user_message: str):
        messages = [HumanMessage(content=user_message)]
        response = self.alfred.invoke({"messages": messages})
        return response['messages'][-1].content

def main():
    print("Hello from agentic-rag-agent!")
    agent = AgenticRAGAgent()
    result = agent.ask("Tell me about our guest named 'Lady Ada Lovelace'.")
    print("🎩 Alfred's Response:")
    print(result)

if __name__ == "__main__":
    main()
