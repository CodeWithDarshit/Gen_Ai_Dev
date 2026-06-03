from dotenv import load_dotenv

import os

load_dotenv()

from langchain_google_genai  import ChatGoogleGenerativeAI



model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite",temperature=0.9, max_tokens=20)


response = model.invoke("write a poem ai  ")

print(response.content)