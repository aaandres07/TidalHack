curl -X POST -d '{
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
  ]
}' \
-H 'Content-Type: application/json' -H 'X-Goog-Api-Key: AIzaSyBZnHYQDxQb8-yODVQMkkvGtKm788TytwM' \
-H 'X-Goog-FieldMask: originIndex,destinationIndex,duration,distanceMeters' \
'https://routes.googleapis.com/distanceMatrix/v2:computeRouteMatrix'