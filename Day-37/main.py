import requests
from datetime import datetime

USERNAME = "sabbirhossain"
TOKEN = "sabbir12345hossain"

pixela_endpoints = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoints, json=user_params)
# print(response.text)

graph_endpoints = f"{pixela_endpoints}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycleing Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoints, json=graph_config, headers=headers)
# print(response.text)

post_pixel_endpoints =f"{pixela_endpoints}/{USERNAME}/graphs/graph1"

today = datetime.now()
date = today.strftime("%Y%m%d")
post_pixel = {
    "date": date,
    "quantity":input("How many kilometers did you cycle todday? "),
}
response = requests.post(post_pixel_endpoints,json=post_pixel,headers=headers)
print(response.text)

update_piexel_endpoints = f"{pixela_endpoints}/{USERNAME}/graphs/graph1/{date}"
update_piexel = {
    "date": date,
    "quantity": "13"
}
# response = requests.put(update_piexel_endpoints,json=update_piexel,headers=headers)
# print(response.text)

# pixel_delete_endpoints = f"{pixela_endpoints}/{USERNAME}/graphs/graph1/{date}"
# response = requests.delete(pixel_delete_endpoints,headers=headers)
# print(response.text)







