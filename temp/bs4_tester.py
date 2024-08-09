import requests
from bs4 import BeautifulSoup
import datetime
import time

if __name__ == "__main__":
    cnt = 0;
    
    while(True):
        try:
            response = requests.get('https://steamcommunity.com/market/listings/730/AK-47%20%7C%20Wasteland%20Rebel%20%28Field-Tested%29')
        except:   
            print(f"GET action failed | {datetime.datetime.now().strftime('%H:%M:%S [%d %b]')}")

        soup = BeautifulSoup(response.content, 'html.parser')
        dirty_json = soup.find_all('script')[-1].string.splitlines()[2];
        clean_json = dirty_json[dirty_json.find('{') : dirty_json.rfind('}') + 1]

        if (len(clean_json) > 20):
            print(clean_json[:20])
        else:
            print(f"Total requests {cnt} before empty responce | {datetime.datetime.now().strftime('%H:%M:%S [%d %b]')}")
            break;

        print(f"Success | {datetime.datetime.now().strftime('%H:%M:%S [%d %b]')}")

        with open("clean_json_bs4.json", "w") as file:
            file.write(clean_json)
        time.sleep(2);

        cnt += 1;

    