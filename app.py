from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
import re

from google_sheets_utils import find_order_status
from openai_utils import ask_gpt

load_dotenv()
app = Flask(__name__)

@app.route("/bot", methods=["POST"])
def bot():
    msg = request.form.get("Body", "").strip()
    print("Incoming message:", msg)

    response = MessagingResponse()

    match = re.search(r'#?(\d{4,})', msg)
    if match:
        order_id = match.group(1)
        order_reply = find_order_status(order_id)

        if order_reply:
            print("✅ Order found. Responding with:", order_reply)
            response.message(order_reply)
            return str(response)
        else:
            # Order not found
            not_found_msg = (
                f"❌ Order #{order_id} was not found in our system.\n"
                "Please make sure your order number is correct, or contact support:\n"
                "📧 help@novaware.io\n"
                "📞 +1-888-NOVA-247"
            )
            response.message(not_found_msg)
            return str(response)

    # No order ID found, use GPT
    try:
        gpt_reply = ask_gpt(msg)
        print("💬 GPT Reply:", gpt_reply)
        response.message(gpt_reply)
    except Exception as e:
        print("❌ GPT error:", str(e))
        response.message("Sorry, I couldn’t process that right now. Please try again later.")

    return str(response)


if __name__ == "__main__":
    app.run(debug=True, port=5000)  # Set debug=True for development; remove in production