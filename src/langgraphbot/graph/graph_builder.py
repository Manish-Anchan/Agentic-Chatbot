from langgraph.graph import StateGraph, START, END
from src.langgraphbot.state.state import State
from src.langgraphbot.node.chatbot_node import ChatbotNode



class GraphBuilder:
    def __init__(self, model):
        self.model = model
        self.graph_builder = StateGraph(State)

    def chatbot_build_graph(self):
        self.chatbot_node = ChatbotNode(self.model)

        self.graph_builder.add_node("chatbot", self.chatbot_node.chatbot)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)


    def setup_graph(self, usecase: str):
        if usecase == "Basic Chatbot":
            self.chatbot_build_graph()
        return self.graph_builder.compile()