import base64
from logging import exception
from  dotenv import load_dotenv
import os
import requests

load_dotenv('env')
client_id=os.getenv('client_id')
client_secret=os.getenv('client_secret')

def access_token():
    try:
        credentials = f"{client_id}:{client_secret}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()

        response = requests.post(
            "https://accounts.spotify.com/api/token",
            headers={'authorization': f'Basic {encoded_credentials}'},
            data={'grant_type':'client_credentials'})
        print(response)

        print("token granted successfully")
        return response.json()['access_token']
    except Exception as e:
        print("error in token ",e)
