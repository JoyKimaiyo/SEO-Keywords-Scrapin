import csv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

list_of_keywords = ['Artificial Intelligence', 'machine learning', 'data science', 'data analyst', 'data engineering']
number_of_times = 10
result_dict = {}

# Setting up Chrome driver
chrome_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service)

# Wait for the search box element to become clickable
search_box = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.NAME, "q"))
)

for keyword in list_of_keywords:
    result_dict[keyword] = []

    print(keyword)
    for _ in range(number_of_times):
        driver.get("https://www.google.com")
        search_box = driver.find_element_by_name("q")
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)

        # Scraping organic search results
        organic_results = driver.find_elements_by_css_selector('.tF2Cxc')

        for result in organic_results:
            snippet = result.find_element_by_css_selector('.aCOpRe').text
            result_dict[keyword].append(snippet)
            print(snippet)

    print('------------------------------------------')

# Writing results to CSV
with open('search_results.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Keyword', 'Snippet'])
    for keyword, snippets in result_dict.items():
        for snippet in snippets:
            writer.writerow([keyword, snippet])

driver.quit()
