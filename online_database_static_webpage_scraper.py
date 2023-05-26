import requests
from bs4 import BeautifulSoup
import pandas as pd

# Create lists to store the extracted data
data_column1 = []
data_column2 = []

for n in range(2, 249):

    print(n)

    try:
        # URL of the website
        url = f"https://www.website.com/page={n}"

        # Send a GET request to the website
        response = requests.get(url)

        # Get the HTML content from the response
        html_content = response.text

        # Create a BeautifulSoup object to parse the HTML
        soup = BeautifulSoup(html_content, "html.parser")

        # Find all list items with the role 'listitem'
        list_items = soup.find_all("li", attrs={"role": "listitem", "class": "generic-class"})

        # Loop over each list item
        for item in list_items:
            try:
                # Find all divs with the class 'summary-list-row'
                divs = item.find_all("div", class_="summary-list-row")

                # Extract the text from the first three divs and concatenate them
                column1_text = "".join(
                    [div.find("dd", class_="summary-list-value").get_text(strip=True) for div in divs[:3]])

                # Extract the text from the fourth div
                column2_text = divs[3].find("dd", class_="summary-list-value").get_text(strip=True)

                # Append the extracted data to the respective lists
                data_column1.append(column1_text)
                data_column2.append(column2_text)
            except:
                pass
    except:
        pass

# Create a dataframe from the extracted data
df = pd.DataFrame({"Column1": data_column1, "Column2": data_column2})

df.to_csv('hmrc.csv')
