import os
from typing import Annotated
from typing_extensions import TypedDict
from dotenv import load_dotenv

from langchain_core.messages import BaseMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode

load_dotenv()

# Enable LangSmith Tracing explicitly
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


model = ChatOpenAI(model="gpt-4o-mini-2024-07-18", temperature=0)


# Define tools at module level to prevent serialization issues
@tool
def add(a: float, b: float) -> float:
    """Adds two numbers."""
    return a + b


tools = [add]
tool_node = ToolNode(tools)
model_with_tools = model.bind_tools(tools)


def make_alternative_graph():
    """Make a tool-calling agent"""

    def call_model(state: State):
        response = model_with_tools.invoke(state["messages"])
        return {"messages": [response]}

    def should_continue(state: State):
        last_message = state["messages"][-1]
        if hasattr(last_message, "tool_calls") and last_message.tool_calls:
            return "tools"
        return END

    graph_workflow = StateGraph(State)

    graph_workflow.add_node("agent", call_model)
    graph_workflow.add_node("tools", tool_node)

    graph_workflow.add_edge(START, "agent")
    graph_workflow.add_conditional_edges("agent", should_continue)
    graph_workflow.add_edge("tools", "agent")

    return graph_workflow.compile()


agent = make_alternative_graph()