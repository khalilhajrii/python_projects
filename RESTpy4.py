import requests

#API key pour l'access
api_key_v4="eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxN2VhZThlNDgwZTJhMjcwODRhYjVmZmUxYzE0Y2M4MSIsInN1YiI6IjYwMTdkYmYyYWFmZWJkMDA0MGRkMGFhZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.E4iTISWZbGUJKjjEN0bRheqEoCwAyVcFvFMXma7aBKI"
 
#endpoint ou URL
movie_id=501
api_version=4
api_url=f"https://api.themoviedb.org/{api_version}"
url_path=f"/movie/{movie_id}"
endpoint=f"{api_url}{url_path}"

headers={
    'Authorization': f'Bearer {api_key_v4}',
    'Content-Type': 'application/json;charset=utf-8'
    }

#affichage de URL API
print(endpoint)

#methode HTTP (POST, GET, UPDATE, DELETE, PUT, PATCH)
request=requests.get(endpoint, headers=headers)



#generateur des status en cas d'erreur ou success
print(request.status_code,"OK")
#l'affichage des données de notre API 
print(request.text)