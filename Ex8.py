import requests
import json
import time

response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
token1 = response1.json().get('token')
time1 = response1.json().get('seconds')

start_result = "Job is NOT ready"
finish_result = "Job is ready"

method = {"token": token1}
response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=method)
print(response2.text)
status1 = response2.json().get('status')
if status1 == "Job is NOT ready":
    print("Status is right")
elif status1 == "Job is ready":
    print("Status is wrong")

time.sleep(time1)

response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=method)
print(response3.text)
status = response3.json().get('status')
result = response3.json().get('result')

if status == "Job is NOT ready":
    print("Status is wrong")
elif (status == "Job is ready") & (result is not None):
    print("Status is right")

