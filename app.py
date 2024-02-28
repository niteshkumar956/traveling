from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data (replace this with a database in a real application)
itineraries = [
    {"id": 1, "destination": "Paris", "dates": "2022-08-15 to 2022-08-20", "activities": ["Eiffel Tower", "Louvre Museum"]},
    {"id": 2, "destination": "New York", "dates": "2022-09-10 to 2022-09-15", "activities": ["Central Park", "Times Square"]}
]

@app.route('/')
def home():
    return render_template('index.html', itineraries=itineraries)

@app.route('/add_itinerary', methods=['POST'])
def add_itinerary():
    if request.method == 'POST':
        destination = request.form['destination']
        dates = request.form['dates']
        activities = request.form['activities'].split(',')

        # Replace this with database storage in a real application
        new_id = len(itineraries) + 1
        new_itinerary = {"id": new_id, "destination": destination, "dates": dates, "activities": activities}
        itineraries.append(new_itinerary)

        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
