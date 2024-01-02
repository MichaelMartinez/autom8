from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc


def get_elements_with_class(driver, class_name):
    # Extract web elements with a specific class name
    return driver.find_elements_by_class_name(class_name)


def scrape_page_links(driver, url):
    driver.get(url)

    # Wait for the page to load (you can adjust the wait time as needed)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Find all the links on the page
    links = driver.find_elements(By.TAG_NAME, "a")

    # Click on each link and collect elements with the specified class
    elements_with_class = []
    for link in links:
        link.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        elements = soup.find_all("div", class_="oTLo85")
        elements_with_class.extend(elements)

    return elements_with_class


if __name__ == "__main__":
    # Set up Selenium WebDriver with Chrome
    options = Options()
    options.add_argument("--no-sandbox")  # Run Chrome in headless mode (without GUI)
    driver = uc.Chrome(
        executable_path="C:\\chromedriver-win64\\chromedriver.exe",
        options=options,
        use_subprocess=True,
    )

    # URL to scrape (replace with the desired website)
    target_url = "https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?zip=85743&inventorySearchWidgetType=AUTO&sortDir=ASC&sourceContext=carGurusHomePageModel&sortType=DEAL_RATING_RPL&entitySelectingHelper.selectedEntity=d2475&distance=500"

    try:
        result = scrape_page_links(driver, target_url)
        # print driver errors to the console

        for elem in result:
            print(elem)

    finally:
        driver.quit()
