import requests
import json
import time

response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
obj = json.loads(response1.text)
token1 = obj["token"]
time1 = obj["seconds"]

start_result = "Job is NOT ready"
finish_result = "Job is ready"

method = {"method": "GET", "token": token1}
response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=method)
print(response2.text)
obj1 = json.loads(response2.text)
status1 = obj1["status"]
if status1 == "Job is NOT ready":
    print("Status is right")
elif status1 == "Job is ready":
    print("Status is wrong")

time.sleep(time1)

response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=method)
print(response3.text)

obj2 = json.loads(response3.text)
status = obj2["status"]
result = obj2["result"]

if status == "Job is NOT ready":
    print("Status is wrong")
elif status == "Job is ready":
    print("Status is right")

