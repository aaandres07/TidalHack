from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/apartment', methods=['GET', 'POST'])
def apartment():
    if request.method == 'POST':
        # Get the data from the form (this will depend on your form fields)
        major = request.form['major']
        beds = request.form['beds']
        baths = request.form['baths']
        budget = request.form['budget']
        transportation = request.form['transportation']
        
        # Logic to find the best apartment based on the user's choices
        # For now, we just send dummy data
        apartment_result = [
            {"name": "Apartment A", "address": "123 Main St", "price": 800},
            {"name": "Apartment B", "address": "456 Oak St", "price": 850},
            {"name": "Apartment C", "address": "789 Pine St", "price": 900}
        ]
        
        return render_template('apartment.html', apartments=apartment_result)
    
    return render_template('apartment_form.html')

@app.route('/dorm', methods=['GET', 'POST'])
def dorm():
    if request.method == 'POST':
        # Get the data from the form (this will depend on your form fields)
        major = request.form['major']
        beds = request.form['beds']
        baths = request.form['baths']
        budget = request.form['budget']
        transportation = request.form['transportation']
        
        # Logic to find the best dorm based on the user's choices
        # For now, we just send dummy data
        dorm_result = [
            {"name": "Dorm A", "address": "101 Campus Ave", "price": 500},
            {"name": "Dorm B", "address": "102 Campus Ave", "price": 550},
            {"name": "Dorm C", "address": "103 Campus Ave", "price": 600}
        ]
        
        return render_template('dorm.html', dorms=dorm_result)

    return render_template('dorm_form.html')

@app.route('/apartment_map')
def apartment_map():
    # Dummy map data for apartment locations (replace with actual data)
    apartment_map_data = [
        {"name": "Apartment A", "latitude": 30.627, "longitude": -96.336},
        {"name": "Apartment B", "latitude": 30.628, "longitude": -96.337},
        {"name": "Apartment C", "latitude": 30.629, "longitude": -96.338}
    ]
    return render_template('apartment_map.html', apartments=apartment_map_data)

@app.route('/dorm_map')
def dorm_map():
    # Dummy map data for dorm locations (replace with actual data)
    dorm_map_data = [
        {"name": "Dorm A", "latitude": 30.630, "longitude": -96.340},
        {"name": "Dorm B", "latitude": 30.631, "longitude": -96.341},
        {"name": "Dorm C", "latitude": 30.632, "longitude": -96.342}
    ]
    return render_template('dorm_map.html', dorms=dorm_map_data)

if __name__ == '__main__':
    app.run(debug=True)
