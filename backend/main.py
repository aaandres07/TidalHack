
from google import genai
import os
import requests
import json

client = genai.Client(api_key=os.environ.get('GOOGLE_API_KEY'))

response = client.models.generate_content(
	model="gemini-2.0-flash", contents="Explain how AI works in a few words"
)
print(response.text)


def compute_request_matrix(courses):
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
			},
			{
				"waypoint": {
					"address": "225 Discovery Dr, College Station, TX 77843"
				}
			}
		],
		"destinations": [],
		"travelMode": "WALK"
	}

	with open('buildings.json', 'r') as file:	
		buildings = json.load(file)
		for building in buildings['classes']:
			if building['building_code'] in courses:
				data['destinations'].append({
					"waypoint": {
						"address": building['address']
					}
				})

	url = "https://routes.googleapis.com/distanceMatrix/v2:computeRouteMatrix"
	headers = {
		"Content-Type": "application/json",
		"X-Goog-Api-Key": os.environ.get('GOOGLE_API_KEY'),
		"X-Goog-FieldMask": "originIndex,destinationIndex,duration,distanceMeters"
	}

	response = requests.post(url, headers=headers, data=json.dumps(data))
	return response

print(compute_request_matrix(['ZACH', 'BLOC', 'HELD']).json())