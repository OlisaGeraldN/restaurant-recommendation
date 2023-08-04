from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual Yelp API key
API_KEY = 'il7pdj2B4mvvMmTvkHYeUx-yTdmzclSNOQ1cLoVfK-MriLwxZ90W7-MSguVUESn6hT4BFDUqd83yFtRdnA4gqAcuASQ2RAOD0rT3YohzlNJM5CDfe8p4itXssCTIZHYx'

# Yelp API endpoint for searching businesses
YELP_API_URL = 'https://api.yelp.com/v3/businesses/search'

def get_restaurant_recommendations(location, cuisine):
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }

    params = {
        'location': location,
        'term': cuisine,
        'limit': 10  # Number of results to retrieve
    }

    response = requests.get(YELP_API_URL, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'businesses' in data:
            return data['businesses']
    return []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form['location']
        cuisine = request.form['cuisine']
        restaurants = get_restaurant_recommendations(location, cuisine)
        return render_template('results.html', restaurants=restaurants)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
