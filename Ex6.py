import requests

response = requests.post("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)

print("Количество редиректов: ", response.history.__len__())
finish_response = response.history[-1]
print("Последний редирект происходит на url: ", finish_response.url)