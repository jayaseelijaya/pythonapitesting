import random
import requests
import json

# get config file from config.json

with open("config/config.json", "r") as json_file:
    config = json.load(json_file)

# get request_data from data folder
with open('data/request_data.json', 'r') as json_file:
    request_data = json.load(json_file)

# get response_data from data folder
with open('data/response_data.json', 'r') as json_file:
    response_data = json.load(json_file)


class TestPytestDataDrivingDemo:

    def test_get_demo_data_driving(self):
        host = config.get("url")
        Authorization_token = config.get("token")
        
        # send request
        response = requests.get(url=host,headers={"Authorization":Authorization_token},verify=False)
        get_api_request_data = request_data["getAPI"]
        get_api_response_data = response_data["getAPI"]
        print(get_api_response_data)
        # send get request
       
        # assert
        assert response.status_code == 200
        #assert response.json() == get_api_response_data

    def test_post_demo_data_driving(self):
        host = config["url"]
        Authorization_token = config["token"]
        post_api = config["postAPI"]
        random_num = random.randint(12345,40965)
        
        print("post request statred")
        data = {
            "id": 13576,
            "name": "jaya" + str(random_num) ,
            "email": "jaya"+str(random_num)+"@namreichert.test",
            "gender": "female",
            "status": "inactive"
        }
        # send request
        response = requests.post(host,json=data, headers={"Authorization":Authorization_token}, verify=False)
        
        # assert
        assert response.status_code == 201
      
