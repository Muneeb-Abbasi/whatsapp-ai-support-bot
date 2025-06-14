# whatsapp-ai-support-bot
AI-powered WhatsApp customer support bot with OpenAI GPT, Google Sheets/Docs integration, and Twilio webhook using Flask.

WhatsApp AI Customer Support Bot
A production-inspired AI chatbot that connects to WhatsApp using Twilio, answers customer queries via OpenAI GPT, and tracks order status using Google Sheets — with company knowledge served from a Google Doc.

✨ Features

- Order tracking via WhatsApp using Order ID (e.g. #1234)
- Natural language Q&A using OpenAI GPT and Google Docs
- Google Sheets integration for order lookup
- Company knowledge base served from a Google Doc
- Live testing using LocalTunnel + Twilio Sandbox
- Smart fallback logic to route messages to correct handler (order vs GPT)

📚 Tech Stack

- Backend: Python + Flask
- AI: OpenAI (GPT-4.1-Nano)
- Messaging: Twilio WhatsApp Sandbox
- Data Sources: Google Sheets (Orders), Google Docs (FAQs)
- Auth & Config: .env + credentials.json (Google Cloud service account)
- Dev Tunneling: LocalTunnel

🛠️ Setup Instructions

1. Clone the Repository
   git clone https://github.com/yourusername/whatsapp-ai-support-bot.git
   cd whatsapp-ai-support-bot

2. Install Dependencies
   python -m venv venv
   venv\Scripts\activate (or source venv/bin/activate)
   pip install -r requirements.txt

🔐 Environment Configuration

Create a .env file by copying the sample:
   cp .env.example .env
Fill in your credentials inside .env.

🔑 Google Cloud Setup

1. Go to https://console.cloud.google.com/
2. Create a project
3. Enable:
   - Google Sheets API
   - Google Docs API
   - Google Drive API
4. Create a Service Account and download JSON Key as credentials.json
5. Share your Google Sheet and Google Doc with the service account email (editor access)

💬 Twilio Setup (WhatsApp Sandbox)

1. Sign in to Twilio Console
2. Join the WhatsApp Sandbox
3. Set your webhook to https://<your-subdomain>.loca.lt/bot
4. Copy SID and Auth Token to .env

🚀 Run the App Locally

1. Run the Flask app: python app.py
2. Start LocalTunnel: npx localtunnel --port 5000 --subdomain yoursubdomain
3. Set webhook in Twilio Console to: https://yoursubdomain.loca.lt/bot

📂 Folder Structure

/whatsapp-ai-support-bot
├── app.py
├── google_sheets_utils.py
├── google_doc_utils.py
├── openai_utils.py
├── .env.example
├── requirements.txt
└── credentials.json (not committed)

🔄 Future Enhancements

- Migrate backend from Flask to FastAPI
- Replace Google Sheets with PostgreSQL
- Add live human-agent escalation
- Add session memory and customer recognition
- Deploy to cloud (Render, Railway, AWS)

🙋‍♂️ Author

Muneeb Ahmed Abbasi
AI Engineer | 
LinkedIn: https://www.linkedin.com/in/muneebahmedabbasi /



