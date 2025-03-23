from flask import Flask, render_template, request, redirect, url_for, session
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Make sure to set a secret key for session management

# Placeholder data for apartments and dorms (replace with actual data or API calls)
apartments = [
    {'name': 'Best Apartment 1', 'location': {'lat': 30.618, 'lng': -96.341}, 'price': 1500},
    {'name': 'Best Apartment 2', 'location': {'lat': 30.616, 'lng': -96.342}, 'price': 1800},
    {'name': 'Best Apartment 3', 'location': {'lat': 30.617, 'lng': -96.343}, 'price': 1200},
]

dorms = [
    {'name': 'Best Dorm 1', 'location': {'lat': 30.619, 'lng': -96.340}, 'price': 800},
    {'name': 'Best Dorm 2', 'location': {'lat': 30.617, 'lng': -96.341}, 'price': 750},
    {'name': 'Best Dorm 3', 'location': {'lat': 30.616, 'lng': -96.342}, 'price': 700},
]

# Route for the Apartment Finder form
@app.route('/apartment', methods=['GET', 'POST'])
def apartment():
    if request.method == 'POST':
        # Get form data
        preferences = {
            'beds': request.form.get('beds'),
            'baths': request.form.get('baths'),
            'budget_min': request.form.get('budget-min'),
            'budget_max': request.form.get('budget-max'),
            'major': request.form.get('major'),
            'transport_mode': request.form.get('transport-mode'),
        }

        # Store preferences in session
        session['preferences'] = preferences

        # Redirect to map page with apartment results
        return redirect(url_for('apartment_map'))

    return render_template('apartment.html')

# Route for the Dorm Finder form
@app.route('/dorm', methods=['GET', 'POST'])
def dorm():
    if request.method == 'POST':
        # Get form data
        preferences = {
            'beds': request.form.get('beds'),
            'baths': request.form.get('baths'),
            'budget_min': request.form.get('budget-min'),
            'budget_max': request.form.get('budget-max'),
            'transport_mode': request.form.get('transport-mode'),
        }

        # Store preferences in session
        session['preferences'] = preferences

        # Redirect to map page with dorm results
        return redirect(url_for('dorm_map'))

    return render_template('dorm.html')

# Route for apartment map page
@app.route('/apartment_map')
def apartment_map():
    preferences = session.get('preferences', {})

    # Filter apartments based on preferences
    filtered_apartments = [apt for apt in apartments
                           if int(apt['price']) >= int(preferences.get('budget_min', 0)) and
                           int(apt['price']) <= int(preferences.get('budget_max', 2500))]

    # Render map with results
    return render_template('apartment_map.html', apartments=filtered_apartments)

# Route for dorm map page
@app.route('/dorm_map')
def dorm_map():
    preferences = session.get('preferences', {})

    # Filter dorms based on preferences
    filtered_dorms = [dorm for dorm in dorms
                      if int(dorm['price']) >= int(preferences.get('budget_min', 0)) and
                      int(dorm['price']) <= int(preferences.get('budget_max', 2500))]

    # Render map with results
    return render_template('dorm_map.html', dorms=filtered_dorms)

if __name__ == '__main__':
    app.run(debug=True)
