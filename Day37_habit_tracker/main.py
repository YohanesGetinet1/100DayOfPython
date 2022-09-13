import requests
from datetime import datetime
USER_NAME = "yohanesgetinet"
TOKEN = "jif54ojo65ko6565"

PIXELA_END_POINT = "https://pixe.la/v1/users"
PARAMETER = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
response = requests.post(PIXELA_END_POINT, json=PARAMETER)


GRAPH_END_POINT = f"{PIXELA_END_POINT}/{USER_NAME}/graphs"
GRAPH_PARAMETER = {
    "id": "habit1",
    "name": "graph1",
    "unit": "commits",
    "type": "int",
    "color": "ajisai",
}
header = {
    "X-USER-TOKEN": TOKEN,
}

graph = requests.post(url=GRAPH_END_POINT, json=GRAPH_PARAMETER, headers=header)

pixel_end_point = f"{PIXELA_END_POINT}/{USER_NAME}/graphs/habit1"
today = datetime.now()

para = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1"
}
graph_post = requests.post(url=pixel_end_point, json=para, headers=header)

parame = {
    "quantity": "10",
}
graph_put = requests.put(url=f"{PIXELA_END_POINT}/{USER_NAME}/graphs/habit1/20220912", headers=header, json=parame)
parameter = {
    "X-USER-TOKEN": TOKEN,
}
graph_delete = requests.delete(url=f"{PIXELA_END_POINT}/{USER_NAME}/graphs/habit1/20220912", headers=header)
print(graph_delete.text)
