from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load building data
with open("buildings.json") as f:
    building_data = json.load(f)

# Placeholder function to rank apartments/dorms
def rank_locations(preferences, building_data):
    # TODO: Replace with your actual ranking logic
    dorms = building_data["dorms"]
    ranked = sorted(dorms, key=lambda d: d["building_name"])  # Dummy sort

    top_3 = ranked[:3]

    # Simulated map data: return dorms and most frequent buildings (dummy example)
    map_data = {
        "top_3": top_3,
        "highlighted_buildings": [
            {"building_code": "ZACH", "count": 5},
            {"building_code": "ETB", "count": 3},
        ]
    }

    return map_data

@app.route('/api/recommend', methods=['POST'])
def recommend():
    preferences = request.json

    if not preferences:
        return jsonify({"error": "Missing input"}), 400

    results = rank_locations(preferences, building_data)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
