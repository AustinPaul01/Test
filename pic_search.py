from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # Added import for Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the path to your webdriver (replace with the actual full path)
webdriver_path = r"chrome.exe"  # Ensure accurate path

# URL of Google Images
url = "https://images.google.com/"

# Path to your image file
image_path = "pic1.jpg"

# Function to perform the steps
def find_similar_images(image_path):
    try:
        # Create a ChromeOptions object
        options = webdriver.ChromeOptions()

        # Set up the browser (using a Service object for Selenium 4 compatibility)
        service = webdriver.chrome.service.Service(webdriver_path)
        driver = webdriver.Chrome(service=service, options=options)

        # Navigate to Google Images
        driver.get(url)

        # Find the search bar
        search_bar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )

        # Upload the image using CTRL+V
        search_bar.send_keys(Keys.CONTROL + "v")

        # Click on the search button
        search_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "MiYK0e"))
        )
        search_button.click()

        # Click on "Tools" button
        tools_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "hdtb-tls"))
        )
        tools_button.click()

        # Click on "Similar images"
        similar_images_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Similar']"))
        )
        similar_images_button.click()

        # Wait for user to explore
        input("Press Enter to close the browser...")


    finally:
        # Close the browser window (ensure driver is defined and initialized)
        if driver:  # Check if driver was successfully created
            driver.quit()

# Execute the function
find_similar_images(image_path)
