import base64
from logging import exception
import json
import requests

client_id='1f4b663f5eaa4295ada9bd822be1e72b'
client_secret='eddc5e6c0b3e42019a1283694558d541'

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


def get_new_release():
    try:
        token = access_token()
        header = {'Authorization': f'Bearer {token}'}
        Param = {'limit': 50}
        response = requests.get('https://api.spotify.com/v1/browse/new-releases',
                                headers=header, params=Param)
        if response.status_code == 200:
            # print(response.json())
            data = response.json()
            albums = data['albums']['items']
            for album in albums:
                info = {
                    'album_name':album['name'],
                    'artist_name':album['artists'][0]['name'],
                    'release_date':album['release_date'],
                    'album_type':album['album_type'],
                    'total_tracks':album['total_tracks'],
                    'spotify_url':album['external_urls']['spotify'],
                    'album_image':album['images'][0]['url'] if album['images'] else None
                }
                print(json.dumps(info,indent=2))
    except Exception as e:
        print("Error in latest release data fetching ..",e)

get_new_release()