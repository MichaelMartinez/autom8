from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
from selenium.webdriver import Chrome
from selenium import webdriver
import os

# Create a directory to save the downloaded files
os.makedirs("downloaded_files", exist_ok=True)

# Set up the Chrome webdriver (you need to have Chrome and chromedriver installed)
driver = webdriver.Chrome()

# Navigate to the webpage
url = "https://hero.page/samir/ai-prompts-for-frontend-development-jobs-prompt-library"
driver.get(url)
driver.implicitly_wait(10)
# Find all the links with the specific class
links = driver.find_elements(By.TAG_NAME, "a")
for link in links:
    print(f"working on %{link.text}")
    href = link.get_attribute("href")
    print(href)
    if href:
        driver.get(href)
        filename = "downloaded_files/" + href.split("/")[-1] + ".html"
        with open(filename, "wb") as file:
            file.write(driver.page_source.encode("utf-8"))

# Close the browser
driver.quit()
