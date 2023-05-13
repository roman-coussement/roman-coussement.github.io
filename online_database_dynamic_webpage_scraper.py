from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import selenium
import time
import csv
import os

data_list = []

# set chromedriver.exe path
service = Service("<PATH_TO_CHROMEDRIVER>")
driver = webdriver.Chrome(service=service)

for page in range(2124):
    try:
        URL = f"<PLACEHOLDER_URL>{page}<PLACEHOLDER_URL>"

        # implicit wait
        driver.implicitly_wait(0.5)
        # maximize browser
        driver.maximize_window()
        # launch URL
        driver.get(URL)

        clicked_links = []

        # loop through relevant elements
        for btn in driver.find_elements(By.PARTIAL_LINK_TEXT, '<PLACEHOLDER_TEXT>'): #find all rulings
            link_text = btn.text
            try:
                if link_text not in clicked_links:
                    btn.click() # click hyperlink
                    content = driver.find_elements(By.ID, "<PLACEHOLDER_ID>")
                    for ruling in content:
                        data_list.append(ruling.text)
            except:
                pass
    except:
        pass
# close browser
driver.quit()

print(type(data_list))
for s in data_list:
    print(type(s))

data_list = [s.splitlines() for s in data_list]

data_list = [" ".join(s) for s in data_list]

data_list = list(dict.fromkeys(data_list))

print(len(data_list))

with open('<PLACEHOLDER_FILENAME>.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for ruling in data_list:
        try:
            writer.writerow([ruling])
        except:
            pass
file.close()
