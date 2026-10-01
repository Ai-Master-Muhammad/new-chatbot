# new-chatbot
A modern, professional chatbot interface built with Streamlit that connects to a locally hosted LLM. This project provides a clean UI for interacting with models like Gemma 3 or Qwen, leveraging a streaming response system for a natural chat experience.

## 🏗 Architecture

The application follows a simple frontend-backend separation:

- **Frontend (UI):** Built with **Streamlit**, providing a responsive chat interface, session-based message history, and real-time streaming updates.
- **Backend (LLM Service):** A Python-based service (`llm_service.py`) that manages communication with a local LLM server via REST API. It handles prompt construction and streams responses back to the UI.
- **Local LLM:** The system is designed to connect to an OpenAI-compatible or Ollama-style local API (defaulting to port `11434`).

## 🚀 Requirements

### 1. Local LLM (Gemma 3)
This chatbot does **not** bundle the LLM. You must have a local LLM runner installed and the model downloaded before starting the app.

- **Recommended Runner:** [Ollama](https://ollama.com/)
- **Model:** Gemma 3 (or other compatible models like `qwen2.5-coder:3b`).
- **Status:** The LLM server must be running in the background.
  - *Example Ollama command:* `ollama run gemma3` (ensure the model name matches your `.env` configuration).

### 2. Python Environment
- **Python:** version `3.12` or higher.
- **Package Manager:** [uv](https://github.com/astral-sh/uv) (highly recommended for fast, reliable setup).

## 🛠 Installation & Setup (Windows)

Follow these exact commands for a fresh clone on Windows:

### 1. Clone the Repository
```powershell
git clone <your-repo-url>
cd new-chatbot
```

### 2. Install `uv` (if not already installed)
```powershell
powershell -ExecutionPolicy ByPass -Command "irm https://astral.sh/uv/install.ps1 | iex"
```

### 3. Initialize Environment and Install Dependencies
```powershell
uv sync
```

### 4. Configuration
Create a `.env` file in the root directory to configure your local LLM connection:

```env
# The endpoint of your local LLM server (e.g., Ollama)
LOCAL_LLM_ENDPOINT=http://localhost:11434/api/generate

# The exact name of the model installed locally
LOCAL_LLM_MODEL=gemma3
```

## 🏃 How to Run

Once your local LLM is running and your environment is configured, start the Streamlit app using `uv`:

```powershell
uv run streamlit run app.py
```

The app will typically be available at `http://localhost:8501`.

## ⚙️ Configuration Details

| Variable | Default Value | Description |
| :--- | :--- | :--- |
| `LOCAL_LLM_ENDPOINT` | `http://localhost:11434/api/generate` | The API URL for the local LLM. |
| `LOCAL_LLM_MODEL` | `qwen2.5-coder:3b` | The identifier of the local model to use. |

## 📝 Project Structure
- `app.py`: Main Streamlit application entry point.
- `src/new_chatbot/llm_service.py`: Logic for communicating with the local LLM API.
- `.env`: Environment variables for local configuration.
- `pyproject.toml`: Project dependencies and metadata.
