import requests
import json
api_url = "https://dpgw.dc.turkuamk.fi:5000/login?protocol=json"
request_data = {'username':'course-api-user', 'password':'K54cahYli3g89'}
response = requests.post(api_url, data = request_data) # a) gets the access token

api_access_token = response.json()['access_token'] # b) stores the access token

search_url = "https://dpgw.dc.turkuamk.fi:5000/data/search/blobs" 
headers = {'Token': api_access_token}
search_response = requests.get(search_url, headers=headers ) # c) Gets all the blobs

jsonified_response = search_response.json() # Turns the response to json
readable_json = json.dumps(jsonified_response, indent=2) # makes that json readable by a human

print(readable_json)