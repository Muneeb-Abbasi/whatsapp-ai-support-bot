# test_google_doc.py

import os
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build

# Load environment variables
load_dotenv()

# Define Google API scopes
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

# Load service account credentials
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', SCOPES)

# Build the Docs API service
service = build('docs', 'v1', credentials=creds)

# Get Document ID from .env
doc_id = os.getenv('GOOGLE_DOC_ID')

# Fetch the document
try:
    doc = service.documents().get(documentId=doc_id).execute()
    print("✅ Document title:", doc.get("title"))
    print("\n📄 Full Text Content:\n" + "-"*40)

    # Extract and print all text content
    for element in doc.get('body', {}).get('content', []):
        if 'paragraph' in element:
            for text_run in element['paragraph'].get('elements', []):
                text = text_run.get('textRun', {}).get('content', '')
                print(text, end='')

except Exception as e:
    print("❌ Error accessing Google Doc:")
    print(str(e))
