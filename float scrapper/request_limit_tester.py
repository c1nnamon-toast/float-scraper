from selenium import webdriver
import time
import json
import datetime

def fetch_and_save_json():
    browser = webdriver.Edge()
    
    url = "https://steamcommunity.com/market/listings/730/P2000%20%7C%20Lifted%20Spirits%20%28Factory%20New%29/render?start=0&count=40&currency=3&language=english&format=json"
    url2 = "https://steamcommunity.com/market/listings/730/AWP%20%7C%20Chromatic%20Aberration%20%28Field-Tested%29/render?start=0&count=40&currency=3&language=english&format=json"

    urls = [url, url2];

    req_cnt = 0
    json_content = 'more'

    while(True):
        browser.get(urls[req_cnt % 2])
        time.sleep(2)
        page_content = browser.page_source
        start = page_content.find('{"success":true')

        if start == -1:
            break;
        
        end = page_content.rfind('}', start) + 1  
        json_content = page_content[start:end].strip()

        parsed_json = json.loads(json_content)
        with open("float scrapper/output.json", "w", encoding="utf-8") as file:
            json.dump(parsed_json, file, ensure_ascii=False, indent=4)
        
        req_cnt += 1
        print(f"Request #{req_cnt:<3}", end=" | ")
        print(datetime.datetime.now().strftime('%H:%M:%S'))

    browser.quit()

    line = '-'*40;

    print(f"Maximum number of requests: {req_cnt}\n{line}\n{datetime.datetime.now().strftime('%H:%M:%S')}")

if __name__ == "__main__":
    fetch_and_save_json()
