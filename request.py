import requests
url = 'http://localhost:5000/api'
r = requests.post(url,json={'anosDeExperiencia':0.5,})
print(r.json())
