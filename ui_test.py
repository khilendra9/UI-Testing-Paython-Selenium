from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options
chrome_options = Options()
# Uncomment this line to see the browser
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--blink-settings=imagesEnabled=false")  # Disable images

# Set up the Chrome WebDriver using WebDriverManager with options
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Open the URL
    driver.get('https://conceptsandbeyond.com/')

    # Wait for a specific element that indicates the page is fully loaded
    wait = WebDriverWait(driver, 20)  # Wait up to 20 seconds
    wait.until(EC.visibility_of_element_located((By.XPATH, "//body")))  # Adjust this to target a specific element on your page

    # Wait for 5 seconds before closing the browser
    time.sleep(5)

    # After ensuring the page is fully loaded, wait for the element containing the text to be present
    text_to_find = "Navigating the Agile"
    
    # Find the element containing the text
    element = wait.until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{text_to_find}')]")))
    
    # Take a screenshot to see the highlighted text
    driver.save_screenshot('screenshot_before.png')

    # Wait for 2 seconds before closing the browser
    time.sleep(2)

    # Highlight the text by executing JavaScript
    driver.execute_script("arguments[0].style.backgroundColor = 'yellow';", element)

    print("Passed: '"+text_to_find+"' text found and highlighted.")

except (NoSuchElementException, TimeoutException):
    print("Failed: '"+text_to_find+"' text not found.")

finally:

    # Wait for 1 seconds before closing the browser
    time.sleep(1)

    # Take a screenshot to see the highlighted text
    driver.save_screenshot('screenshot_after.png')
    
    # Close the browser after the wait
    driver.quit()
