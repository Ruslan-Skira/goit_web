"""I will test here /notes"""

import json
import requests

expected_result = {'title': 'Running', 'description': '30 minutess', 'status': False}

data = {
  "title": "Running",
  "description": "30 minutess",
  "done": False
}
headers = {"Content-type": 'application/json'}

response =  requests.post("http://127.0.0.1:8000/notes", data=json.dumps(data), headers=headers)


assert expected_result == response.json()