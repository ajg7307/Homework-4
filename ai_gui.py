import tkinter as tk
from tkinter import scrolledtext
import ollama
import threading
import json
import os

# --- SETTINGS ---
MODEL = "llama3.2"
HISTORY_FILE = "chat_history.json"

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title(f"Local LLM - {MODEL}")
        self.root.geometry("600x700")

        # Load history
        self.messages = self.load_history()

        # UI Layout
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', font=("Arial", 12))
        self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.input_frame = tk.Frame(root)
        self.input_frame.pack(padx=10, pady=10, fill=tk.X)

        self.user_input = tk.Entry(self.input_frame, font=("Arial", 14))
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.user_input.bind("<Return>", lambda event: self.send_message())

        self.send_button = tk.Button(self.input_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)

        # Show existing history in the window
        self.display_existing_history()

    def load_history(self):
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, "r") as f:
                return json.load(f)
        return [{"role": "system", "content": "You are a helpful assistant."}]

    def save_history(self):
        with open(HISTORY_FILE, "w") as f:
            json.dump(self.messages, f, indent=4)

    def display_existing_history(self):
        for msg in self.messages:
            if msg["role"] != "system":
                role = "You" if msg["role"] == "user" else "AI"
                self.append_to_chat(f"{role}: {msg['content']}\n\n")

    def append_to_chat(self, text):
        self.chat_display.configure(state='normal')
        self.chat_display.insert(tk.END, text)
        self.chat_display.configure(state='disabled')
        self.chat_display.see(tk.END)

    def send_message(self):
        prompt = self.user_input.get().strip()
        if not prompt:
            return

        self.user_input.delete(0, tk.END)
        self.append_to_chat(f"You: {prompt}\n\n")
        self.messages.append({"role": "user", "content": prompt})
        
        # Start the AI in a separate thread to prevent GUI freezing
        threading.Thread(target=self.get_ai_response, daemon=True).start()

    def get_ai_response(self):
        self.append_to_chat("AI: ")
        full_response = ""
        
        try:
            stream = ollama.chat(model=MODEL, messages=self.messages, stream=True)
            for chunk in stream:
                content = chunk['message']['content']
                full_response += content
                # Update the GUI safely from a thread
                self.root.after(0, self.update_ai_text, content)
            
            self.append_to_chat("\n\n")
            self.messages.append({"role": "assistant", "content": full_response})
            self.save_history()
        except Exception as e:
            self.root.after(0, self.append_to_chat, f"\nError: {e}\n\n")

    def update_ai_text(self, content):
        self.chat_display.configure(state='normal')
        self.chat_display.insert(tk.END, content)
        self.chat_display.configure(state='disabled')
        self.chat_display.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()