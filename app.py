from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Dummy crop recommendation logic (replace with ML later)
def recommend_crop(N, P, K, ph, rainfall, temp, humidity):
    crops = ["Rice", "Wheat", "Maize", "Sugarcane", "Cotton", "Millets", "Pulses"]
    return random.choice(crops)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    N = float(request.form["nitrogen"])
    P = float(request.form["phosphorus"])
    K = float(request.form["potassium"])
    ph = float(request.form["ph"])
    rainfall = float(request.form["rainfall"])
    temp = float(request.form["temperature"])
    humidity = float(request.form["humidity"])

    crop = recommend_crop(N, P, K, ph, rainfall, temp, humidity)

    # Pass values to result page
    return render_template("result.html", 
                           crop=crop,
                           values=[N, P, K, ph, rainfall, temp, humidity])

if __name__ == "__main__":
    app.run(debug=True)