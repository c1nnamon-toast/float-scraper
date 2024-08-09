import requests
import datetime
import time
import json


if __name__ == "__main__":
    cnt = 0;
    
    while(True):
        try:
            response = requests.get('https://steamcommunity.com/market/listings/730/AK-47%20%7C%20Wasteland%20Rebel%20%28Field-Tested%29/render?start=0&count=20&currency=3&language=english&format=json')
        except:   
            print(f"GET action failed | {datetime.datetime.now().strftime('%H:%M:%S [%d %b]')}")
            break;
        
        response_json = response.json();

        # try:
        #     response_json = response.json()
        # except:
        #     print(f"Failed to decode JSON | {datetime.datetime.now().strftime('%H:%M:%S [%d %b]')}")
        #     break;

        if (response_json == None) or ("success" not in response_json) or (response_json["success"] is False):
            print(f"Total requests {cnt} before unsuccessful read | {datetime.datetime.now().strftime('%H:%M:%S [%d %b]')}")
            break;

        print(response_json);

        print(f"Success | {datetime.datetime.now().strftime('%H:%M:%S [%d %b]')}")

        with open("clean_json_requests.json", "w", encoding="utf-8") as file:
            json.dump(response_json, file, indent=4)  # pretty printing to the file
        time.sleep(2);

        cnt += 1;
