from google import genai
from google.genai import types
import os
import PIL.Image

client = genai.Client(api_key=os.environ.get('GOOGLE_API_KEY'))

image = PIL.Image.open("Please enter the file path to your schedule: ")

response = client.models.generate_content(
	model="gemini-2.0-flash", 
    contents=["Parse this image of a university schedule and make a JSON containing: class name, class code, class time, and class location.", image]
)
print(response.text)

