import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
def get_order_sheet():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)
    sheet_id = os.getenv("GOOGLE_SHEET_ID")

    sheet = client.open_by_key(sheet_id).sheet1

    return sheet

def find_order_status(order_id):
    sheet = get_order_sheet()
    records = sheet.get_all_records()

    for row in records:
        if str(row.get("OrderID", "")).strip() == str(order_id).strip():
            status = row.get("Status", "Unknown").strip()
            carrier = row.get("Carrier", "").strip()

            # Build response based on status
            if status.lower() == "cancelled":
                return f"⚠️ Order #{order_id} has been *cancelled*. If you believe this is incorrect, please contact our support team."
            elif status.lower() == "pending":
                return f"⏳ Order #{order_id} is *pending* and not yet shipped."
            elif status.lower() == "shipped":
                return f"✅ Order #{order_id} has been *shipped* via {carrier}."
            else:
                return f"ℹ️ Order #{order_id} is currently marked as *{status}*."

    # If no order match found
    return None

