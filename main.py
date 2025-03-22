
from google import genai
import os
import requests
import json

client = genai.Client(api_key=os.environ.get('GOOGLE_API_KEY'))

response = client.models.generate_content(
	model="gemini-2.0-flash", contents="Explain how AI works in a few words"
)
print(response.text)


def compute_request_matrix(data):
	url = "https://routes.googleapis.com/distanceMatrix/v2:computeRouteMatrix"
	headers = {
		"Content-Type": "application/json",
		"X-Goog-Api-Key": os.environ.get('GOOGLE_API_KEY'),
		"X-Goog-FieldMask": "originIndex,destinationIndex,duration,distanceMeters,status,condition"
	}

	response = requests.post(url, headers=headers, data=json.dumps(data))
	return response

data = {
	"origins": [
		{
			"waypoint": {
				"address": "722 Lubbock St, College Station, TX 77843"
			}
		},
		{
			"waypoint": {
				"address": "306 University Dr, College Station, TX 77843"
			}
		}
	],
	"destinations": [
		{
			"waypoint": {
				"address": "466 Nagle St, College Station, TX 77843"
			}
		},
		{
		"waypoint": {
			"address": "632 Penberthy Bl, College Station, TX 77843"
			}
		}
	],
	"travelMode": "WALK",
}
print(compute_request_matrix(data).json())