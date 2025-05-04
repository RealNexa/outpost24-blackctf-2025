import requests
import json
import time

BASE_URL = "http://134.122.88.8:5002"
TOKEN = "/api/token" #POST
EXPLORE = "/api/tomb/{tomb_id}?token={token}"

def get_token():
    response = requests.post(BASE_URL+TOKEN)

    if response.status_code != 200:
        raise Exception(f"Failed to get token: {response.text}")

    json_data = json.loads(response.text)

    return json_data["token"]


def main():
    token = get_token()
    for tomb_id in range(1, 10001):
        print(f"ID: {tomb_id}\r", end="")
        explore_uri = EXPLORE.format(tomb_id=tomb_id, token=token)
        response = requests.get(BASE_URL+explore_uri)
        
        response_json = json.loads(response.text)

        if "is empty!" not in response_json["content"]:
            print("=====")
            print(tomb_id)
            print(response_json)
            break




    



if __name__ == "__main__":
    main()
