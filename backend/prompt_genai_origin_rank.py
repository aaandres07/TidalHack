from google import genai
from google.genai import types
import os
from pydantic import BaseModel

client = genai.Client(api_key=os.environ.get('GOOGLE_API_KEY'))

JSONobject = "[{'originIndex': 2, 'destinationIndex': 0, 'duration': '0s'}, {'originIndex': 2, 'destinationIndex': 1, 'distanceMeters': 516, 'duration': '423s'}, {'originIndex': 0, 'destinationIndex': 1, 'distanceMeters': 1067, 'duration': '872s'}, {'originIndex': 0, 'destinationIndex': 2, 'distanceMeters': 558, 'duration': '472s'}, {'originIndex': 1, 'destinationIndex': 1, 'distanceMeters': 725, 'duration': '585s'}, {'originIndex': 0, 'destinationIndex': 0, 'distanceMeters': 1016, 'duration': '821s'}, {'originIndex': 2, 'destinationIndex': 2, 'distanceMeters': 1054, 'duration': '870s'}, {'originIndex': 1, 'destinationIndex': 0, 'distanceMeters': 1007, 'duration': '807s'}, {'originIndex': 1, 'destinationIndex': 2, 'distanceMeters': 910, 'duration': '739s'}]"

class Rankings(BaseModel):
    originIndex: int
    ranking: int 

response = client.models.generate_content(
	model="gemini-2.0-flash", 
	contents=["Given a JSON with origin, destination, and duration of travel between the two points, rank the origins based on proximity to destinations. Output as a list of dictionaries with the origin as the index and value being the rank. Higher ranks are better. Respond in the format: [{'originIndex': #, 'rank': #}]. Do not output code.", JSONobject],
	config = {
		'response_mime_type': 'application/json',
		'response_schema': list[Rankings],
	}
)

print(response.text)

