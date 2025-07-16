
# 🤖 Chat Bot Agent Using n8n and Google Generative AI

This project demonstrates how to build an intelligent chat bot agent using [n8n](https://n8n.io/), Google Generative AI, and a memory component for contextual conversations.

![Workflow Screenshot](Chat%20Bot%20Agent%20Using%20n8n.png)

## 📌 Overview

This chatbot is created in **n8n**, a powerful workflow automation platform. The bot listens for incoming messages, processes them using Google’s AI model, and maintains conversation context using a simple memory tool.

---

## 🧠 Key Features

- **Event-driven Chat Trigger**
- **AI-powered Response Generation** using Google Generative AI
- **Simple Memory Tool** for maintaining chat history
- **Reusable Workflow** for chatbot agents
- **Live Logging and Debugging** support in n8n

---

## ⚙️ Workflow Components

| Component                    | Description                                                   |
|-----------------------------|---------------------------------------------------------------|
| `When chat message received`| Trigger to initiate the flow                                  |
| `AI Agent`                  | Main handler for message processing                           |
| `Google Generative AI Chat` | Language model to generate human-like responses               |
| `Simple Memory`             | Stores and retrieves previous messages for better context     |
| `Logs & Output`             | Shows execution tokens, timing, and generated replies         |

---

## 🚀 How to Use

1. **Install n8n**:  
   Follow installation instructions from [n8n Docs](https://docs.n8n.io/).

2. **Create a New Workflow**:  
   - Open n8n.
   - Create a project named `First Chat Bot Agent`.

3. **Add Nodes**:
   - Add `Trigger → AI Agent → Google Generative AI Model`
   - Attach a `Simple Memory` node to the AI Agent.
   - Configure the API Key for Google Generative AI.

4. **Test It**:
   - Send a chat message.
   - The bot replies with context-aware answers.

---

## 🔐 Prerequisites

- Google Generative AI API Key
- n8n account or local instance
- Internet access for model calls

---

## 📦 Example Output

```plaintext
"Despite these challenges, the development of agentic AI represents a significant leap towards more capable and autonomous artificial intelligence systems."
```



