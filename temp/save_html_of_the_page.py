from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


def load(drive, link):
    drive.get(link);

def close(drive):
    drive.quit();

def save(drive, file_name):

    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(drive.page_source)

    time.sleep(2);



if __name__ == "__main__":

    driver = webdriver.Chrome()
    link = ('https://steamcommunity.com/market/listings/730/AWP%20%7C%20Chromatic%20Aberration%20%28Field-Tested%29');

    load(driver, link);

    save(driver, "./flex/raw_html.html");

    close(driver);