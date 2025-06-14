import os
import openai
from openai import OpenAI
from google_doc_utils import get_doc_text

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_gpt(question):
    context = get_doc_text()

    messages = [
        {"role": "system", "content": """
         
         You are a helpful customer support agent. Answer accurately based on the company knowledge base. - Redirect off-topic questions back to NovaWare-related subjects. 
        If the user asks for an order status, do not guess — assume order lookups are handled separately.
        - If anything is not clear -  DO NOT MAKE UP THE ANSWER AND always  suggest them contacting our dedicated sales or technical support team and make sure to use use below information:"""},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"}
    ]

    response = client.chat.completions.create(
        model="gpt-4.1-nano",  # or "gpt-4" if you have access
        messages=messages,
        temperature=0.5
    )

    return response.choices[0].message.content.strip()
