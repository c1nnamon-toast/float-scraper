from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

if __name__ == "__main__":

    drive = webdriver.Chrome()
    drive.get('https://alza.sk')
    
    # Wait up to 10 seconds for the element to be present and visible
    element_to_hover_over = WebDriverWait(drive, 10).until(
        EC.presence_of_element_located((By.ID, 'litp18902954'))
    )

    # Hover over the element
    hover = ActionChains(drive).move_to_element(element_to_hover_over)
    hover.perform()

    time.sleep(3)  # Wait for 3 seconds

    drive.quit()