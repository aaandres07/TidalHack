
from google import genai
from google.maps import routing_v2
import os

client = genai.Client(api_key=os.environ.get('GOOGLE_API_KEY'))

response = client.models.generate_content(
	model="gemini-2.0-flash", contents="Explain how AI works in a few words"
)
print(response.text)


def sample_compute_routes():
	# Create a client
	maps_client = routing_v2.RoutesClient(credentials=os.environ.get('GOOGLE_API_KEY'))

	# Initialize request argument(s)
	request = routing_v2.ComputeRouteMatrixRequest(
		origins=[routing_v2.RouteMatrixOrigin(routing_v2.Waypoint(address="722 Lubbock St, College Station, TX 77843"))],
		destinations=[routing_v2.RouteMatrixDestination(routing_v2.Waypoint(address="466 Nagle St, College Station, TX 77843"))]
	)

	# Make the request
	response = maps_client.compute_routes(request=request)

	# Handle the response
	print(response)

sample_compute_routes()