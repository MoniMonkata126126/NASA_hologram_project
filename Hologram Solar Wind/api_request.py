import requests
import json
from datetime import date, timedelta

# Api key:
API_KEY = 'SsDY2Ocy4NU36Y6HoV6JFSOsvYiFLKkRbVapFTsA'

# Api url:
API_URL = 'https://api.nasa.gov/DONKI/RBE?'


def read_api():
    # Set parameter for today
    today = date.today()

    # Set parameter for yesterday
    yesterday = date.today() - timedelta(days = 1)
    
    # Set the parameters needed for the request
    parameters = {
        'startDate': yesterday, # Set startDate to yesterday
        'endDate': today, # Set endDate to today
        'api_key': API_KEY
    }
    
    # Make the request
    response = requests.get(API_URL, params = parameters)

    # Make it a readable dictionary or list of dictionaries
    json_data = json.loads(response.text)

    # Find and return the times and class of the last event
    if isinstance(json_data, list):
        return [json_data[-1]['beginTime'], json_data[-1]['peakTime'], json_data[-1]['endTime'], json_data[-1]['classType']]

    else: return [json_data['beginTime'], json_data['peakTime'], json_data['endTime'], json_data['classType']]
    
