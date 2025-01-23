from together import Together
from dotenv import load_dotenv
import os

load_dotenv()

client = Together(api_key=os.getenv("API_KEY"))

getDescriptionPrompt = "You are a UX/UI designer. Describe the attached screenshot or UI mockup in detail. I will feed in the output you give me to a coding model that will attempt to recreate this mockup, so please think step by step and describe the UI in detail. Pay close attention to background color, text color, font size, font family, padding, margin, border, etc. Match the colors and sizes exactly. Make sure to mention every part of the screenshot including any headers, footers, etc. Use the exact text from the screenshot."

imageUrl = "https://encrypted-tbn3.gstatic.com/licensed-image?q=tbn:ANd9GcT49ffQTaN3OJwECYvdmBeIdbj_EhMso90dbvn5w8TKmIDC0BzhAjkqhCqBEoGkw-mHH_2kpNA7unbke98"


stream = client.chat.completions.create(
    model="meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": getDescriptionPrompt},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": imageUrl,
                    },
                },
            ],
        }
    ],
    stream=True,
)

for chunk in stream:
    print(chunk.choices[0].delta.content)
