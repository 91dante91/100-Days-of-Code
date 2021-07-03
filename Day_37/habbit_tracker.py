import requests
from datetime import datetime

USER_NAME = "murat91"
TOKEN = "wolfman1991"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Python",
    "unit": "Min",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = datetime.now()
pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you codding today? ")
}
response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

pixel_update_endpoint = f"{pixel_endpoint}/20210704"

pixel_update_config = {
    "quantity": "210"
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_config, headers=headers)
# print(response.text)

delete_pixel_endpoint = pixel_update_endpoint
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)
