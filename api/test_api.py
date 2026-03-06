#this page is trying to communicate/request data from my api's
import requests


# Keep the base URL clean
BASE_URL = 'https://geo.api.gouv.fr/communes' 

params = {
    'codePostal' : '49000'
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    print(response.json())
else:('Failed to load data')
   

#BASE_URL = 'http://127.0.0.1:8000/api/livre'
        



