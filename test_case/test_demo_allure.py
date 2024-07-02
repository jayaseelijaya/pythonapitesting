import random
import allure
import requests
import json


@allure.feature("Test example API endpoints")
class TestPytestAllureDemo:
    
    @allure.story("Test example get endpoint")
    @allure.title("Verify the get API")
    @allure.description("verify the get API response status code and data")
    @allure.severity("blocker")
    def test_get_example_endpoint_allure(self, env_config, env_request_data, env_response_data):
        host = env_config["url"]
        Authorization_token = env_config["token"]
        get_api_request_data = env_request_data["getAPI"]
        print(env_config)
        get_api_response_data = env_response_data["getAPI"]
        print(get_api_response_data)
        # send get request
        response = requests.get(url=host,headers={"Authorization":Authorization_token},verify=False)
        # assert
        print("response status code is" + str(response.status_code))
        assert response.status_code == 200
        print("response data is" + str(response.json()))
        #assert response.json() == get_api_response_data

    @allure.story("Test example POST API")
    @allure.title("Verify the POST API")
    @allure.description("verify the POST API response status code and data")
    @allure.severity("Critical")
    def test_post_example_endpoint_allure(self, env_config, env_request_data, env_response_data):
        host = env_config["url"]
        Authorization_token = env_config["token"]
        post_api = env_config["postAPI"]
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
        print("response status code is" + str(response.status_code))
        assert response.status_code == 201
        print("response data is" + str(response.json()))
