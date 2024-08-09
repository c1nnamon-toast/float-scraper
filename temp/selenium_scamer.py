from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

import time


def load(drive, link, RtW=False):
    drive.get(link);

    if RtW:
        reject_all_span = WebDriverWait(drive, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//span[text()='Reject All']")));
        reject_all_span.click();

if __name__ == "__main__":
    link = 'https://steamcommunity.com/market/listings/730/AWP%20%7C%20Chromatic%20Aberration%20%28Field-Tested%29'
    drive = webdriver.Chrome();
    
    load(drive, link, True)

    # myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.TAG_NAME, 'script')))  


    number_of_pages = 3;
    
    
    for i in range(number_of_pages):
        pages = drive.find_elements(By.XPATH, "//span[@class='market_paging_pagelink']")
        # print(pages);
        last_script = drive.find_elements(By.TAG_NAME, 'script')[-1].get_attribute('outerHTML');

        dirty_json = last_script.splitlines()[2]; # var g_rgAssets
        clean_json = dirty_json[ dirty_json.find('{')  :  dirty_json.rfind('}') + 1 ];

        with open(f"./float scrapper/clean_json_selenium{i}.json", "w") as file:
            file.write(clean_json);
        
        if( i != number_of_pages -1):
            pages[i].click();
            time.sleep(4);
    
    drive.quit();




'''
⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿
⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⣿
⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠜⣿
⣿⣿⣿⣿⠿⠿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿
⣿⣿⡏⠁⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⣶⣶⣶⣶⣦⣤⡄⠀⠀⠀⠀⢀⣴⣿
⣿⣿⣷⣄⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡧⠇⢀⣤⣶
⣿⣿⣿⣿⣿⣿⣾⣮⣭⣿⡻⣽⣒⠀⣤⣜⣭⠐⢐⣒⠢⢰
⣿⣿⣿⣿⣿⣿⣿⣏⣿⣿⣿⣿⣿⣿⡟⣾⣿⠂⢈⢿⣷⣞
⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣷⣶⣾⡿⠿⣿⠗⠈⢻⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠻⠋⠉⠑⠀⠀⢘⢻
⣿⣿⣿⣿⣿⣿⣿⡿⠟⢹⣿⣿⡇⢀⣶⣶⠴⠶⠀⠀⢽
⣿⣿⣿⣿⣿⣿⡿⠀⠀⢸⣿⣿⠀⠀⠣⠀⠀⠀⠀⠀⡟⢿⣿
⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠹⣿⣧⣀⠀⠀⠀⠀⡀⣴⠁⢘⡙
⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⠗⠂⠄⠀⣴⡟⠀⠀⡃
'''
    