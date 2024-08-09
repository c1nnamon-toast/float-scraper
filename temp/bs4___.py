import requests
from bs4 import BeautifulSoup
import datetime

if __name__ == "__main__":
    try:
        response = requests.get('https://steamcommunity.com/market/listings/730/AK-47%20%7C%20Wasteland%20Rebel%20%28Field-Tested%29')
    except:   
        print(f"GET action failed | {datetime.datetime.now().strftime('%H:%M:%S [%d %b]')}")
        
    soup = BeautifulSoup(response.content, 'html.parser')
    dirty_json = soup.find_all('script')[-1].string.splitlines()[2];
    clean_json = dirty_json[dirty_json.find('{') : dirty_json.rfind('}') + 1]
    
    print(f"Success | {datetime.datetime.now().strftime('%H:%M:%S [%d %b]')}")

    with open("clean_json_bs4.json", "w") as file:
        file.write(clean_json)