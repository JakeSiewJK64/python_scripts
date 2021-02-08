import requests

BASE = "http://127.0.0.1/5000/" # base url
VIDEO_URL = "http://127.0.0.1:5000/"


data = [
    {"name":"Jake", "views":1000000, "likes":1000},
    {"name":"Luke",  "views":1000, "likes":10},
    {"name":"John", "views":10, "likes":2}
]

# for i in range(len(data)):
    # response = requests.put(VIDEO_URL + "Video/" + str(i), data[i])
    # print(response.json())
    
diction = str({"name":"William", "views":300, "likes":555})
response = requests.patch(VIDEO_URL + "Video/2", {"name":"William", "views":2000, "likes":5000})
input()

response = requests.get(VIDEO_URL + "Video/2")
print(response.json())    


