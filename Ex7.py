import requests

response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print("1. В этом случае будет выводиться текст: ", response1.text)

method1 = {"method": "HEAD"}
response2 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method1)
print("2. В этом случае будет выводиться: ", response2.text)

method2 = {"method": "GET"}
response3 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=method2)
print("3. В этом случае будет выводиться: ", response3.text)

parameters_methods = [{"method":"GET"}, {"method":"POST"}, {"method":"PUT"}, {"method":"DELETE"}]
m = 0
print("4. Ответ на 4 вопрос:")
while m < 4:
    result = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=parameters_methods[m])
    print(f"Метод GET с params={parameters_methods[m]} возвращает {result} со статус кодом {result.text}")
    result = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=parameters_methods[m])
    print(f"Метод POST с data={parameters_methods[m]} возвращает {result} со статус кодом {result.text}")
    result = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=parameters_methods[m])
    print(f"Метод PUT с data={parameters_methods[m]} возвращает {result} со статус кодом {result.text}")
    result = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=parameters_methods[m])
    print(f"Метод DELETE с data={parameters_methods[m]} возвращает {result} со статус кодом {result.text}")
    m += 1
