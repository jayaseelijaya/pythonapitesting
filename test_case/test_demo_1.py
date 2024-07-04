import requests
import random


class TestPytestDemo:
    base_url = "https://reqres.in/api/users"
    def test_get_demo(self):
        
        # send request
        # response = requests.get(url=TestPytestDemo.base_url,headers=TestPytestDemo.hearder,verify=False)
        response = requests.get(url=TestPytestDemo.base_url,params={"page":"2"},verify=False)
        # assert
        assert response.status_code == 200
        json_body = response.json()
        assert json_body["page"] == 2
        print(json_body)

    def test_post_demo(self):
        print("post request statred")
        data = {
                    "name": "morpheus",
                    "job": "leader"
                }
         
        print(data)
        # send request
        response2 = requests.post(TestPytestDemo.base_url,json=data, verify=False)
        json_body = response2.json()
        assert response2.status_code == 201
        assert json_body["name"] == data["name"]