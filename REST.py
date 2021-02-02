import requests
import pprint

#API key pour l'access
api_key="17eae8e480e2a27084ab5ffe1c14cc81"
 
#endpoint ou URL
movie_id=500
api_version=3
api_url=f"https://api.themoviedb.org/{api_version}"
url_path=f"/movie/{movie_id}"
endpoint=f"{api_url}{url_path}?api_key={api_key}"

#methode HTTP (POST, GET, UPDATE, DELETE, PUT, PATCH)
request=requests.get(endpoint)

#affichage de l'URL API
print(endpoint)

#generateur des status en cas d'erreur ou success
print(request.status_code)
#l'affichage des données de notre API 
print(request.text)

#------------------------------------------------------------------------------

#recherche d'un film 
api_url=f"https://api.themoviedb.org/{api_version}"
url_path=f"/search/movie"
endpoint=f"{api_url}{url_path}?api_key={api_key}&query=Endgame"

#methode HTTP (POST, GET, UPDATE, DELETE, PUT, PATCH)
request=requests.get(endpoint)

#affichage de l'URL API
pprint.pprint(request.json())