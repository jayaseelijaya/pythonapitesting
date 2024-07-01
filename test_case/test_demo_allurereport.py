import requests
import random
import pytest


class TestPytestDemo:
    base_url = "https://gorest.co.in/public/v2/users"
    Authorization_token = "Bearer a9236691775171d6d264f6cb619cd12b019997aadbc776ab5fc5ccec6b026361"
    hearder = {"Authorization":Authorization_token}
    #GET api 

    def test_getapi(self):
    
        response = requests.get(TestPytestDemo.base_url, headers=TestPytestDemo.hearder, verify=False)
        assert response.status_code == 200
        Jsonvalue = response.text
        #print("User details",response.text)
        json_body = response.json()
        print(json_body)

    def test_postapi(self):
        random_num = random.randint(108897,4565578)
        print("post request statred")
        data = {
            "id": 13576,
            "name": "jaya" + str(random_num) ,
            "email": "jaya"+str(random_num)+"@arreichert.test",
            "gender": "female",
            "status": "inactive"
        }
        response2 = requests.post(TestPytestDemo.base_url,json=data, headers=TestPytestDemo.hearder, verify=False)
        assert response2.status_code == 201
        value = response2.json()
        print("------------",value)
        assert value["name"] == "jaya" + str(random_num)




