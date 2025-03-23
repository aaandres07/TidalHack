from flask import Flask, render_template

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def homepage():
    return render_template('homepage.html')

# Route for the map page
@app.route('/apartment')
def apartment():
    return render_template('apartment.html')

@app.route('/apartment-map')
def apartment_map():
    return render_template('apartment_map.html')
    
@app.route('/dorm')
def dorm():
    return render_template('dorm.html')

@app.route('/dorm-map')
def dorm_map():
    return render_template('dorm_map.html')
    
if __name__ == '__main__':
    app.run(debug=True)
