# LangGraph Chatbot with Memory

A conversational AI chatbot application built with **LangGraph** that maintains conversation memory and context using a state-graph architecture. The app features a clean web interface powered by Streamlit and leverages Groq's language models for fast, efficient responses.

## 🎯 About This Project

This project demonstrates how to build intelligent chatbots using **LangGraph**, a powerful framework for building stateful, agentic applications. The key features include:

- **Conversation Memory**: Maintains full conversation history within a session using LangGraph's checkpoint system
- **State-Based Architecture**: Uses LangGraph's StateGraph to manage message state and flow
- **Streaming Responses**: Real-time response streaming for better UX
- **LLM Integration**: Powered by Groq's high-performance language models
- **Web Interface**: Clean, interactive UI built with Streamlit

### Tech Stack

- **LangGraph**: Framework for building graph-based LLM applications
- **LangChain**: Core library for building language model applications
- **Groq**: LLM provider (fast inference)
- **Streamlit**: Web application framework
- **LangChain-Groq**: Integration between LangChain and Groq

## 📁 Folder Structure

```
langgraph/
├── README.md                              # Project documentation
├── requirements.txt                       # Python dependencies
└── simple_chatbot_with_memory/
    ├── __init__.py                        # Package initialization
    ├── app.py                             # Streamlit web application
    └── chatbot_with_memory.py             # Core chatbot logic with LangGraph
```

### File Descriptions

- **`app.py`**: Main Streamlit application that provides the user interface. Handles:
  - Chat message display and input
  - Session state management for conversation history
  - Streaming responses from the chatbot
  - Message history visualization

- **`chatbot_with_memory.py`**: Core chatbot implementation featuring:
  - LangGraph StateGraph definition
  - Chat node that processes messages through the LLM
  - Memory checkpoint system for conversation persistence
  - LLM initialization with Groq

- **`requirements.txt`**: All Python package dependencies needed to run the project

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- Groq API key (get one at [console.groq.com](https://console.groq.com))

### Step 1: Clone the Repository

```bash
git clone https://github.com/Vishal-Yadav-001/langgraph.git
cd langgraph
```

### Step 2: Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

**Activate the virtual environment:**

- **On Windows:**
  ```bash
  venv\Scripts\activate
  ```

- **On macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables

Create a `.env` file in the root directory with your Groq API key:

```
GROQ_API_KEY=your_groq_api_key_here
```

You can get your Groq API key from [console.groq.com](https://console.groq.com/keys)

### Step 5: Run the Application

Navigate to the chatbot directory and start the Streamlit app:

```bash
cd simple_chatbot_with_memory
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

## 💬 How to Use

1. **Open the App**: Once running, you'll see the "Agetic Chatbot with Langgraph" interface
2. **Type Your Message**: Enter any question or message in the input field at the bottom
3. **Get Responses**: The chatbot will respond with streaming text
4. **Conversation History**: Your entire conversation history is maintained and displayed

## 🏗️ How It Works

### Architecture Overview

```
User Input (Streamlit UI)
        ↓
    app.py
        ↓
stream_generator() → chatbot.stream()
        ↓
chatbot_with_memory.py (LangGraph)
        ↓
StateGraph:
  - START → chat_with_llm → END
        ↓
ChatGroq (Groq LLM)
        ↓
Response → Memory Checkpoint
        ↓
Stream back to UI
```

### Key Components

1. **StateGraph**: Defines the conversation flow
   - **State**: Contains list of messages with automatic message handling
   - **Node**: `chat_with_llm` processes messages through the LLM
   - **Edges**: Connect START to the chat node and chat node to END

2. **Memory Checkpoint**: Uses `MemorySaver` to persist conversation state
   - Thread-based configuration tracks separate conversations
   - Enables resuming conversations with full context

3. **Message Streaming**: Real-time response generation for better UX

## 🔧 Configuration

### Changing the LLM Model

In `chatbot_with_memory.py`, you can change the model:

```python
llm = ChatGroq(model="openai/gpt-oss-120b")  # Current model
# Other available models:
# - "groq/mixtral-8x7b-32768"
# - "groq/llama-3-70b-versatile"
# - "groq/llama-3-8b-instant"
```

### Modifying Thread ID

To use different conversation threads, modify the `thread` variable and update `CONFIG`:

```python
thread = "your_unique_thread_id"
config = {"configurable": {"thread_id": thread}}
```

## 📦 Dependencies

The project uses the following main packages:

- `langgraph` - Core framework for building graph-based LLM apps
- `langgraph-prebuilt` - Pre-built components and agents
- `langgraph-sdk` - SDK utilities
- `langchain-groq` - Groq integration
- `streamlit` - Web UI framework
- `langsmith` - Monitoring and evaluation
- `langchain-openai` - OpenAI integration (optional)

See `requirements.txt` for the complete list.

## 🛠️ Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'langgraph'"

**Solution**: Make sure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### Issue: "GROQ_API_KEY not found"

**Solution**: Ensure your `.env` file exists in the root directory and contains your Groq API key:
```
GROQ_API_KEY=your_actual_api_key
```

### Issue: Streamlit app not opening

**Solution**: Try running with:
```bash
streamlit run app.py --logger.level=debug
```

## 📝 Example Usage

```
User: "Hello, what can you help me with?"
Assistant: "I'm an AI chatbot powered by LangGraph and Groq. I can help you with..."

User: "Tell me about LangGraph"
Assistant: "LangGraph is a framework for building stateful, agentic applications..."
```

## 🔗 Useful Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [Groq Console](https://console.groq.com)
- [LangChain Documentation](https://python.langchain.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)

## 📄 License

This project is open source. Please refer to the repository for license details.

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests.

## 📧 Support

For issues and questions, please create an issue in the GitHub repository.

---

**Happy chatting! 🚀**
