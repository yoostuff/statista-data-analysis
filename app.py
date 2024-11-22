from flask import Flask, request, jsonify, render_template  # Flask modules for API and rendering HTML
from flask_cors import CORS  # Enable Cross-Origin Resource Sharing for frontend-backend interaction
import requests  # For making HTTP requests to the Statista API
import matplotlib.pyplot as plt  # For creating charts
import pandas as pd  # For handling data analysis and manipulation
import os  # For file handling and accessing environment variables
from dotenv import load_dotenv  # For loading environment variables from a .env file

# Load environment variables from the .env file
load_dotenv()

# Initialize the Flask app and enable CORS
app = Flask(__name__)
CORS(app)

# API Configuration: Read API key and base URL from the .env file
API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")

# HTTP headers for API requests
HEADERS = {
    "x-api-key": API_KEY
}

# Create a directory to store generated charts if it doesn't exist
if not os.path.exists("charts"):
    os.makedirs("charts")

@app.route('/')
def home():
    """
    Home route to render the index.html file.
    Provides the main UI for category selection, chart generation, and CSV download.
    """
    return render_template('index.html')

@app.route('/get_categories', methods=['GET'])
def get_categories():
    """
    Fetches categories dynamically from the Statista API and returns them as JSON.
    Categories are used to populate the dropdown in the frontend.
    """
    try:
        # Make a request to the Statista API to get categories
        response = requests.get(BASE_URL, headers=HEADERS)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Extract categories from the API response
        data = response.json()
        categories = [{'name': item['title'], 'description': item['description']} for item in data['items']]
        return jsonify(categories)  # Return the list of categories as JSON

    except requests.exceptions.HTTPError as err:
        # Handle HTTP errors and return appropriate error messages
        return jsonify({"error": f"HTTP error occurred: {err}"}), response.status_code
    except requests.exceptions.RequestException as err:
        # Handle other request-related errors
        return jsonify({"error": f"Request error occurred: {err}"}), 500
    except KeyError:
        # Handle cases where the API response format is not as expected
        return jsonify({"error": "Unexpected data format from API"}), 500

@app.route('/analyze_data', methods=['POST'])
def analyze_data():
    """
    Fetches data for a selected category and generates a chart.
    Chart type (pie, bar, line) and premium content inclusion are configurable.
    """
    # Extract parameters from the request
    category_id = request.json.get('category_id')
    chart_type = request.json.get('chart_type', 'pie')  # Default chart type is pie
    include_premium = request.json.get('premium', False)  # Default: exclude premium content

    if not category_id or not isinstance(category_id, str):
        # Validate the category ID
        return jsonify({"error": "Valid category ID is required"}), 400

    # API request parameters
    params = {"q": category_id, "premium": include_premium}
    response = requests.get(BASE_URL, headers=HEADERS, params=params)

    if response.status_code == 200:
        # Process the data if the API request is successful
        data = response.json()
        df = pd.DataFrame(data['items'])

        if 'value' not in df.columns or df.empty:
            # Handle cases where no valid data is returned
            return jsonify({"error": "No valid data found for the selected category."}), 404

        df['value'] = pd.to_numeric(df['value'], errors='coerce').fillna(0)  # Convert 'value' column to numeric

        try:
            # Generate the chart and return the file path
            chart_path = create_chart(df, chart_type)
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

        return jsonify({"chart_url": chart_path})  # Return the chart URL

    else:
        # Handle API request errors
        return jsonify({"error": f"Unable to fetch data: {response.text}"}), response.status_code

@app.route('/download_csv', methods=['POST'])
def download_csv():
    """
    Generates a CSV file for the analyzed data and returns the file path.
    Allows users to download data for further offline analysis.
    """
    # Extract parameters from the request
    category_id = request.json.get('category_id')
    include_premium = request.json.get('premium', False)

    if not category_id:
        # Validate the category ID
        return jsonify({"error": "Category ID is required"}), 400

    # API request parameters
    params = {"q": category_id, "premium": include_premium}
    response = requests.get(BASE_URL, headers=HEADERS, params=params)

    if response.status_code == 200:
        # Process the data if the API request is successful
        data = response.json()
        df = pd.DataFrame(data['items'])

        if df.empty:
            # Handle cases where no data is available for download
            return jsonify({"error": "No data available for download."}), 404

        # Save the data as a CSV file
        csv_path = os.path.join("charts", f"{category_id}_data.csv")
        df.to_csv(csv_path, index=False)
        return jsonify({"csv_url": csv_path})  # Return the CSV file path

    else:
        # Handle API request errors
        return jsonify({"error": f"Unable to fetch data: {response.text}"}), response.status_code

def create_chart(df, chart_type='pie'):
    """
    Generates a chart based on the provided DataFrame and chart type.
    Supported chart types: pie, bar, line.
    """
    plt.figure(figsize=(10, 6))  # Set the figure size

    if chart_type == 'pie':
        # Generate a pie chart
        df.groupby('title')['value'].sum().plot(kind='pie', autopct='%1.1f%%')
        plt.ylabel("")  # Remove y-axis label
    elif chart_type == 'bar':
        # Generate a bar chart
        df.groupby('title')['value'].sum().plot(kind='bar', color='skyblue')
        plt.xlabel("Categories")
        plt.ylabel("Values")
    elif chart_type == 'line':
        # Generate a line chart
        df.groupby('title')['value'].sum().plot(kind='line', marker='o')
        plt.xlabel("Categories")
        plt.ylabel("Values")
    else:
        # Handle unsupported chart types
        raise ValueError("Unsupported chart type. Please select 'pie', 'bar', or 'line'.")

    plt.title("Data Distribution")  # Add a title to the chart
    chart_path = os.path.join("charts", f"{chart_type}_chart.png")
    plt.savefig(chart_path)  # Save the chart as a PNG file
    plt.close()  # Close the plot to free resources
    return chart_path

# Run the Flask application in debug mode
if __name__ == '__main__':
    app.run(debug=True)
