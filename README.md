# LangGraph AgenticAI Application

A powerful, modular AI application built with LangGraph and Streamlit that supports multiple use cases including basic chatbot functionality, web-enabled chatbot, and AI news processing workflows.

## 🚀 Features

- **Multi-Modal AI Workflows**: Support for different AI use cases through a unified graph-based architecture
- **Interactive Streamlit UI**: User-friendly web interface for seamless interaction
- **Flexible LLM Integration**: Built with Groq LLM integration with configurable parameters
- **Modular Graph Architecture**: Clean separation of concerns with individual nodes for different functionalities
- **Tool Integration**: Web search capabilities and external tool integration
- **Real-time Processing**: Stream-based processing with session state management

## 🛠️ Use Cases

### 1. Basic Chatbot
Simple conversational AI with direct question-answer capability.

### 2. Chatbot with Web Search
Enhanced chatbot with web search tools for real-time information retrieval and fact-checking.

### 3. AI News Processing
Automated news fetching, summarization, and result storage workflow.

## 📁 Project Structure

```
src/
├── langgraphbot/
│   ├── graph/
│   │   └── graph_builder.py      # Core graph construction logic
│   ├── state/
│   │   └── state.py              # State management
│   ├── nodes/
│   │   ├── chatbot_node.py       # Basic chatbot functionality
│   │   ├── chatbot_with_tool_node.py  # Tool-enabled chatbot
│   │   └── ai_news_node.py       # News processing workflows
│   ├── tools/
│   │   └── search_tool.py        # Web search and tool integration
│   ├── LLMs/
│   │   └── groqllm.py           # Groq LLM configuration
│   └── ui/
│       └── streamlitapp/
│           ├── loadui.py         # UI loading logic
│           └── displayresult.py  # Result display handling
└── main.py                       # Application entry point
```

## 🔧 Installation

1. **Clone the repository**
```bash
git clone <your-repository-url>
cd langgraph-agenticai-app
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

Required packages include:
- `streamlit`
- `langgraph`
- `groq` (for LLM integration)
- Additional dependencies as specified in your requirements.txt

4. **Set up environment variables**
Create a `.env` file with your API keys:
```bash
GROQ_API_KEY=your_groq_api_key_here
# Add other required API keys
```

## 🚀 Usage

### Running the Application

Start the Streamlit application:
```bash
streamlit run main.py
```

The application will be available at `http://localhost:8501`

### Using Different Workflows

1. **Basic Chatbot**: Select this option for simple Q&A interactions
2. **Chatbot with Web**: Choose this for chatbot with real-time web search capabilities
3. **AI News**: Use this workflow for automated news processing

### Configuration Options

The application supports various configuration parameters through the UI:
- LLM model selection
- Use case selection
- Custom parameters for each workflow

## 🏗️ Architecture

### Graph Builder (`GraphBuilder`)

The core component that constructs different workflow graphs based on the selected use case:

- **`chatbot_build_graph()`**: Creates a simple chatbot workflow
- **`chatbot_with_tool()`**: Builds a chatbot with web search tools
- **`ai_news_builder_graph()`**: Constructs an AI news processing pipeline
- **`setup_graph(usecase)`**: Main method that compiles and returns the appropriate graph

### State Management

Uses LangGraph's `StateGraph` for managing conversation state and workflow progression across different nodes.

### Node Architecture

- **ChatbotNode**: Handles basic conversational AI functionality
- **ChatbotWithToolNode**: Extends chatbot with external tool capabilities
- **AINewsNode**: Manages news fetching, summarization, and storage

## 🔧 Customization

### Adding New Use Cases

1. Create a new node class in the `nodes/` directory
2. Add the corresponding graph building method in `GraphBuilder`
3. Update the `setup_graph()` method to handle the new use case
4. Add UI options in the Streamlit interface

### Extending Tool Functionality

1. Add new tools in the `tools/` directory
2. Update the tool node creation in the graph builder
3. Configure tool conditions for proper workflow routing

## 🐛 Error Handling

The application includes comprehensive error handling:
- UI input validation
- LLM model initialization checks
- Graph setup error management
- Session state error handling

## 📝 API Reference

### GraphBuilder Methods

- `__init__(model)`: Initialize with LLM model
- `setup_graph(usecase)`: Main entry point for graph creation
- `chatbot_build_graph()`: Basic chatbot graph
- `chatbot_with_tool()`: Tool-enabled chatbot graph
- `ai_news_builder_graph()`: News processing graph

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📄 License

[Add your license information here]

## 🙏 Acknowledgments

- Built with [LangGraph](https://langchain-ai.github.io/langgraph/)
- UI powered by [Streamlit](https://streamlit.io/)
- LLM integration via [Groq](https://groq.com/)

## 📞 Support

For issues and questions:
- Create an issue in the GitHub repository
- [Add contact information if applicable]

---

**Note**: Make sure to configure your environment variables and API keys before running the application.