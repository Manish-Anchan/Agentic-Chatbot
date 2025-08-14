from src.langgraphbot.state.state import State


class ChatbotWithToolNode:
    def __init__(self, model):
        self.llm = model

    def chatbot(self, state: State):
        user_input =  state["messages"][-1] if state["messages"] else ""
        llm_response = self.llm.invoke([{"role" : "user", "content": user_input}])

        tool_response = f"Tool integration for : {user_input}"

        return {"messages":[llm_response, tool_response]}
    


    def create_chatbot(self, tools):
        system_prompt = "Do not call any tools unless the user explicitly asks for a web search or up-to-date information."

        llm_with_tools = self.llm.bind_tools(tools, tool_choice="auto")

        def chatbot_node(state: State):
            # prepend the system prompt so the model sees the rule every call
            messages = [{"role": "system", "content": system_prompt}] + state["messages"]
            resp = llm_with_tools.invoke(messages)
            return {"messages": state["messages"] + [resp]}

        return chatbot_node


