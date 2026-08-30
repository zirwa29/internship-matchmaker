from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return "Internship Matchmaker API is running!"


@app.route("/recommendations")
def recommendations():

    internships = pd.read_csv("data/recommended_internships.csv")

    return jsonify(internships.to_dict(orient="records"))


if __name__ == "__main__":
    app.run(debug=True)