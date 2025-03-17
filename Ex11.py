import requests
class TestEx11:
    def test_ex11(self):
        response1 = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        some_cookie = response1.cookies
        print(some_cookie)
        assert response1.status_code == 200, "Wrong response code"

        assert "HomeWork" in some_cookie, "There is no field 'HomeWork' in the response"