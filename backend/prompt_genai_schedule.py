from google import genai
from google.genai import types
import os
import PIL.Image
from pydantic import BaseModel

client = genai.Client(api_key=os.environ.get('GOOGLE_API_KEY'))

image = PIL.Image.open(input("Please enter the file path to your schedule: "))

class parse_schedule(BaseModel):
    class_name: str
    class_code: str
    class_time: str
    class_location: str

response = client.models.generate_content(
	model="gemini-2.0-flash", 
    contents=["Parse this image of a university schedule and make a JSON containing: class_name, class_code, class_time, and class_location.", image],
    config = {
        'response_mime_type': 'application/json',
		'response_schema': list[parse_schedule],
    }
)

print(response.text)

