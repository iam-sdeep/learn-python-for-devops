# Devops Engineer - Developer has an API(Application Programmable Inreface)

import requests

def get_api_data():
    demo_url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url=demo_url)
    return response.json()
#print(response)
#print(dir(response))
#print(response.json())
#print(type((response.json())))
#print(response.json()[2])

get_api_data()