from src.langgraphbot.state.state import State


class ChatbotNode:
    def __init__(self, model):
        self.llm = model

    def chatbot(self, state: State) -> dict:

        return {"messages" : self.llm.invoke(state["messages"])}