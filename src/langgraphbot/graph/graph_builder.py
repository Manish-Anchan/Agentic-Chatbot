from langgraph.graph import StateGraph, START, END
from src.langgraphbot.state.state import State
from src.langgraphbot.nodes.chatbot_node import ChatbotNode
from src.langgraphbot.tools.search_tool import get_tools, create_tool_node
from src.langgraphbot.nodes.chatbot_with_tool_node import ChatbotWithToolNode
from langgraph.prebuilt import tools_condition



class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def chatbot_build_graph(self):
        self.chatbot_node = ChatbotNode(self.llm)

        self.graph_builder.add_node("chatbot", self.chatbot_node.chatbot)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def chatbot_with_tool(self):
        tools = get_tools()
        tool_node = create_tool_node(tools)

        llm = self.llm

        obj_chatbot_with_node=ChatbotWithToolNode(llm)
        chatbot_node=obj_chatbot_with_node.create_chatbot(tools)

        self.graph_builder.add_node("chatbot",chatbot_node)
        self.graph_builder.add_node("tools",tool_node)
      
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tools_condition)
        self.graph_builder.add_edge("tools","chatbot")
        


    def setup_graph(self, usecase: str):
        if usecase == "Basic Chatbot":
            self.chatbot_build_graph()
        if usecase == "Chatbot With Web":
            self.chatbot_with_tool()
        return self.graph_builder.compile()