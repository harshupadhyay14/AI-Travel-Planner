from flask import Flask, render_template, request
from main import TripCrew
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__,
            template_folder='templates',
            static_folder='static')

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # disables CSS caching

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        origin = request.form.get("origin")
        cities = request.form.get("cities")
        date_range = request.form.get("date_range")
        interests = request.form.get("interests")
        try:
            trip = TripCrew(origin, cities, date_range, interests)
            result = trip.run()
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)