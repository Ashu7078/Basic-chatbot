import nltk
from nltk.chat.util import Chat, reflections
import tkinter as tk
from tkinter import scrolledtext

# Define chatbot patterns and responses
pairs = [
    [
        r"hi|hello|hey", 
        ["Hello!", "Hey there!", "Hi! How can I help you?"]
    ],
    [
        r"how are you?", 
        ["I'm a bot, but I'm doing well! How about you?", "I'm just a program, but thanks for asking!"]
    ],
    [
        r"what is your name?", 
        ["I'm a chatbot created by you!", "I don't have a name, but you can call me ChatBot."]
    ],
    [
        r"(.*) your name?", 
        ["I am just a simple chatbot."]
    ],
    [
        r"quit", 
        ["Goodbye! Have a great day!", "Bye! Take care."]
    ],
    [
        r"(.*)", 
        ["I'm not sure I understand. Can you rephrase that?", "Interesting! Tell me more."]
    ]
]

def send_message():
    user_input = user_entry.get()
    chat_response = chat.respond(user_input)
    chat_display.insert(tk.END, "You: " + user_input + "\n", "user")
    chat_display.insert(tk.END, "Bot: " + chat_response + "\n\n", "bot")
    user_entry.delete(0, tk.END)

def chatbot():
    global chat, chat_display, user_entry
    
    root = tk.Tk()
    root.title("Chatbot")
    root.configure(bg="#222222")
    
    chat_display = scrolledtext.ScrolledText(root, width=50, height=20, bg="#333333", fg="#FFFFFF", font=("Arial", 12))
    chat_display.tag_configure("user", foreground="cyan")
    chat_display.tag_configure("bot", foreground="yellow")
    chat_display.pack(pady=10)
    
    user_entry = tk.Entry(root, width=40, bg="#444444", fg="#FFFFFF", font=("Arial", 12))
    user_entry.pack(pady=5)
    
    send_button = tk.Button(root, text="Send", command=send_message, bg="#555555", fg="#FFFFFF", font=("Arial", 12, "bold"))
    send_button.pack()
    
    chat = Chat(pairs, reflections)
    
    root.mainloop()

if __name__ == "__main__":
    chatbot()
#run hog    python chatbot.py

