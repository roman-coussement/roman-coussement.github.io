from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import selenium
import time
import csv
import os

all_rulings = []

print(os.getcwd())
#set chromodriver.exe path

service = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=service)

#PATH = "C:\Program Files (x86)\chromedriver.exe"
#driver = webdriver.Chrome(PATH)

for page in range(2124):
    try:
        URL = f"https://rulings.cbp.gov/search?term=0%20OR%201%20OR%202%20OR%203%20OR%204%20OR%205%20OR%206%20OR%207%20OR%208%20" \
            "OR%209%20OR%2010%20OR%2011%20OR%2012%20OR%2013%20OR%2014%20OR%2015%20OR%2016%20OR%2017%20OR%2018%20OR%2019%20OR%" \
            f"2020%20OR%2021%20OR%2022&collection=ALL&sortBy=RELEVANCE&pageSize=100&page={page}&showDetail=true"

        #implicit wait
        driver.implicitly_wait(0.5)
        #maximize browser
        driver.maximize_window()
        #launch URL
        driver.get(URL)

        clicked_links = []

        #loop through relevant elements
        for btn in driver.find_elements(By.PARTIAL_LINK_TEXT, 'NY'): #find all rulings
            link_text = btn.text
            try:
                if link_text not in clicked_links:
                    btn.click() # click hyperlink
                    content = driver.find_elements(By.ID, "ruling-detail-content")
                    for ruling in content:
                        all_rulings.append(ruling.text)
            except:
                pass
    except:
        pass
#close browser
driver.quit()



print(type(all_rulings))
for s in all_rulings:
    print(type(s))

all_rulings = [s.splitlines() for s in all_rulings]

all_rulings = [" ".join(s) for s in all_rulings]

all_rulings = list(dict.fromkeys(all_rulings))

print(len(all_rulings))

with open('all_rulings.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for ruling in all_rulings:
        try:
            writer.writerow([ruling])
        except:
            pass
file.close()