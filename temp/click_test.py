from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

if __name__ == "__main__":

    drive = webdriver.Chrome()
    drive.get('https://alza.sk')
    
    # Wait up to 10 seconds for the element to be present and visible
    element_to_click = WebDriverWait(drive, 10).until(
        EC.element_to_be_clickable((By.ID, 'litp18902954'))
    )

    # Click on the element
    element_to_click.click()

    time.sleep(10)

    drive.quit()