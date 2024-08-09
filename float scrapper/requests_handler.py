from selenium import webdriver
import time
import json

def fetch_and_save_json():
    browser = webdriver.Edge()
    
    url = "https://steamcommunity.com/market/listings/730/P2000%20%7C%20Lifted%20Spirits%20%28Factory%20New%29/render?start=0&count=30&currency=3&language=english&format=json"
    browser.get(url)

    time.sleep(5)

    page_content = browser.page_source
    browser.quit()

    start_index = page_content.find('{"success":true')
    end_index = page_content.rfind('}', start_index) + 1  # find the last occurrence of '}' from start_index
    json_content = page_content[start_index:end_index].strip()
    #print(json_content)

    parsed_json = json.loads(json_content)
    with open("float scrapper/output.json", "w", encoding="utf-8") as file:
        json.dump(parsed_json, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    fetch_and_save_json()
