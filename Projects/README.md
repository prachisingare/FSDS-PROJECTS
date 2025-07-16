# 📅 Daily Planner Chatbot Using n8n + Google Sheets + Gemini AI

This project demonstrates a chatbot workflow built using [n8n](https://n8n.io/) that acts as a **Daily Planner Assistant**. It integrates:
- **Google Gemini (Generative AI)** for intelligent chat responses
- **Google Sheets** for managing and retrieving task data
- **Memory tools** to enable contextual and personalized planning

![Workflow Screenshot](Daily%20Planner%20using%20n8n.png)

---

## 🧠 Key Features

- 📩 **Chat Trigger**: Activated when a chat message is received
- 🤖 **AI Agent**: Google Gemini model processes and responds intelligently
- 📊 **Google Sheets Integration**: Reads rows containing daily tasks, time slots, and priorities
- 🧠 **Memory Tool**: Maintains user context
- 📋 **Planner Summary**: Provides formatted daily schedules in natural language

---

## 🔗 Workflow Structure

| Node | Function |
|------|----------|
| `When chat message received` | Starts the workflow when a message is received |
| `AI Agent` | Central logic using Google Gemini & memory |
| `Google Sheets - Get Rows` | Fetches tasks from a spreadsheet |
| `Google Gemini Chat Model` | Converts data into a conversational reply |
| `Memory Tool` | Maintains session memory |

---

## 💡 Example Output

```plaintext
Here is the data from your Google Sheet:

• Time Slot: 6.00 - 7.00 AM, Task/ACTIVITY: YOGA/EXERCISE, Priority: low
• Time Slot: 7.00 - 8.00 AM, Task/ACTIVITY: COOKING
• Time Slot: 8.00 - 9.00 AM, Task/ACTIVITY: BREAKFAST
...
```

---

## 📦 How to Use

1. **Install and Set up n8n**  
   Follow: https://docs.n8n.io/hosting/

2. **Create a Google Sheet**  
   - Include columns like `Time Slot`, `Task/ACTIVITY`, and `Priority`.

3. **Set up the Workflow**
   - Add a trigger: `When chat message received`
   - Connect an AI Agent with Google Gemini Chat and memory
   - Connect Google Sheets (OAuth) and map sheet columns

4. **Run & Test**  
   - Start the workflow
   - Type: “Show my plan for today”
   - Bot replies with tasks from the sheet

---

## 🔐 Requirements

- n8n Account or local instance
- Google Cloud Project (for Gemini API access)
- Google Sheet with planner data
- OAuth credentials for Sheets API

---

## 🚀 Future Enhancements

- Add buttons for marking tasks as complete
- Integrate with Google Calendar
- Support daily reminders or Slack messages

---
