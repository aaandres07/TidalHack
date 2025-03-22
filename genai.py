
from google import genai
import os

client = genai.Client(api_key=os.environ.get('GOOGLE_API_KEY'))

address = input(['A', 'B', 'C'])

response = client.models.generate_content(
	model="gemini-2.0-flash", contents="Explain how AI works in a few words"
)
print(response.text)

