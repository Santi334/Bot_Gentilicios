from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/query": {"origins": "*"}})  # Allow access from any origin

# Dictionary with South American capitals and demonyms in English
data = {
    "Ecuador": {"capital": "Quito", "gentilic": "Ecuadorians"},
    "Argentina": {"capital": "Buenos Aires", "gentilic": "Argentinians"},
    "Brazil": {"capital": "Brasilia", "gentilic": "Brazilians"},
    "Uruguay": {"capital": "Montevideo", "gentilic": "Uruguayans"},
    "Chile": {"capital": "Santiago", "gentilic": "Chileans"},
    "Peru": {"capital": "Lima", "gentilic": "Peruvians"},
    "Colombia": {"capital": "Bogotá", "gentilic": "Colombians"},
    "Venezuela": {"capital": "Caracas", "gentilic": "Venezuelans"},
    "Paraguay": {"capital": "Asunción", "gentilic": "Paraguayans"},
    "Bolivia": {"capital": "Sucre", "gentilic": "Bolivians"}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    country = request.json.get("country", "").strip().title()  # Normalize country name
    if country in data:
        response = {
            "message": f"The capital of {country} is {data[country]['capital']} and its inhabitants are {data[country]['gentilic']}."
        }
    else:
        response = {"message": "I'm sorry, I can only answer about South American capitals and gentilic."}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Enable network access