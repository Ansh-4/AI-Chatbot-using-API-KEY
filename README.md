# AI-Chatbot-using-API-KEY
A lightweight Python chatbot powered by the Mistral AI API, featuring real-time console interaction and secure API key handling. Ideal for experimenting with AI responses and building your own conversational assistant.
# 🤖 Mistral Python Chatbot

A simple command-line chatbot built using the **Mistral AI API**. This project enables real-time conversational interaction with an elegant and calm assistant style.

---

## 🚀 Features

* Powered by `mistral-small-latest`
* Maintains full conversation history
* Adjustable response creativity (`temperature`)
* Secure API handling using `.env`
* Easy to run in any terminal
* Exit anytime using `quit` or `exit`

---

## 🛠️ Tech Stack

* **Python**
* **mistralai**
* **python-dotenv**

---

## 📂 Structure

```
mistral-chatbot/
│
├─ chatbot.py
├─ .env (not tracked)
├─ .gitignore
└─ requirements.txt
```

---

## 🔐 Setup

1. Clone the repository:

```bash
git clone https://github.com/<Ansh-4>/<AI Chatbot using API-KEY>.git
cd <AI Chatbot using API-KEY>
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add:

```
API_KEY=your_mistral_api_key_here(not including mine for clear reasons)
```

---

## ▶️ Run

```bash
python chatbot.py
```

Example interaction:

```
You: Hello
Assistant: Hello! How may I assist you?
```

---

## 🌱 Future Improvements

* GUI version (Tkinter / Streamlit)
* Telegram / Discord bot integration
* Voice input + output
* Chat memory database


