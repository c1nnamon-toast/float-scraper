from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time
import glob

def fetch_float_value(drive, link):
    # Find the input element and clear any previous value
    input_element = browser.find_element(By.ID, "mat-input-1")
    input_element.clear()

    # Send the inspect link to the input field
    input_element.send_keys(link)

    #button = browser.find_element(By.CSS_SELECTOR, "button[mat-button]") 
    #button.click()

    # WebDriverWait(drive, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "market_listing_item_img_container")));
    time.sleep(3);

    float_element = browser.find_element(By.CSS_SELECTOR, 'span[mattooltipposition="above"].mat-tooltip-trigger.ng-star-inserted') 
    return float_element.text

if __name__ == "__main__":
    browser = webdriver.Chrome()
    browser.get("https://csfloat.com/checker")

    list_of_inspect_links = glob.glob('**/inspect_links*.txt', recursive=True)


    for inspect_links_filename in list_of_inspect_links:
        with open(inspect_links_filename, 'r') as file:
            inspect_links = [line.strip() for line in file.readlines()]
    
        links_n_floats = []

        for link in inspect_links:
            links_n_floats.append(link + ' ' + fetch_float_value(browser, link))
    
        #print(inspect_links_filename)

        print('\n'.join(links_n_floats))

        with open(inspect_links_filename, 'w', encoding='utf-8') as file:
            file.write('\n'.join(links_n_floats))

    browser.quit()