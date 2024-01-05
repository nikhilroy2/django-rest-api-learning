import json
import requests
def get_json_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return json.loads(response.text)

