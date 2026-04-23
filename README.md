# Homework-4

Local Mac LLM with Python GUI
A private, local Large Language Model (LLM) interface built for macOS using Python, Ollama, and Tkinter. This project allows you to run an AI assistant entirely on your own hardware—no API keys or internet required.
🚀 Features
GUI Interface: A clean, easy-to-use window for chatting.
Streaming Responses: Real-time text generation (text appears as it's "thought" of).
Persistent Memory: Conversations are saved to chat_history.json and reloaded automatically.
Privacy Focused: Everything stays on your Mac.
Multithreaded: The GUI remains responsive while the AI is processing.
🛠️ Prerequisites
Before running the code, ensure you have the following installed:
Ollama: Download Ollama for Mac
Thonny (or Python 3.x): Download Thonny
📦 Setup Instructions
1. Start the LLM Engine
Once Ollama is installed, open your Terminal and download the model (we use Llama 3.2 3B by default):
code
Bash
ollama run llama3.2
(Once it finishes downloading, you can type /exit to leave the terminal chat.)
2. Install Python Library
In Thonny, go to Tools > Manage packages... and search for:
ollama
Click Install.
3. Project Structure
Your folder should look like this:
ai_gui.py (The main application code)
README.md (This file)
chat_history.json (Generated automatically to store your chats)
🖥️ How to Run
Ensure the Ollama app is running (check your Mac menu bar).
Open ai_gui.py in Thonny.
Click the Run (Green Arrow) button.
Type your message and hit Enter.
⚙️ Configuration
You can change the model by editing the MODEL variable at the top of ai_gui.py:
code
Python
MODEL = "llama3.2" # You can change this to "phi3", "mistral", etc.
📝 Troubleshooting
Connection Error: Ensure the Ollama icon is visible in your Mac's top menu bar.
Slow Performance: If you have an Intel Mac, try using a smaller model like llama3.2:1b.
Memory Reset: To clear the AI's memory, simply delete the chat_history.json file in the project folder.
