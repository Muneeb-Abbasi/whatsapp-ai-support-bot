from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import os

def get_doc_text():
    scope = ["https://www.googleapis.com/auth/documents.readonly"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    service = build("docs", "v1", credentials=creds)
    doc = service.documents().get(documentId=os.getenv("GOOGLE_DOC_ID")).execute()
    text = ""
    for content in doc.get("body").get("content"):
        if "paragraph" in content:
            for el in content["paragraph"].get("elements", []):
                text += el.get("textRun", {}).get("content", "")
    return text.strip()
