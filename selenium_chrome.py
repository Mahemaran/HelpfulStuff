from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager  # You can install this library for automatic driver management
import time

# Set up the webdriver using ChromeDriverManager
service = Service(ChromeDriverManager().install())  # Automatically download and use the correct chromedriver

# Initialize the Chrome driver
driver = webdriver.Chrome(service=service)

# Open YouTube homepage
# driver.get("https://www.youtube.com/")
driver.get("https://www.youtube.com/@MaheMaran-s9y")

# Wait for the page to load
time.sleep(10)  # Wait for 3 seconds to ensure the page is loaded
input("Press Enter after logging into YouTube...")
# Find all video titles
video_titles = driver.find_elements(By.XPATH, '//a[@id="video-title"]')

# Print all video titles
for title in video_titles:
    print(title.get_attribute('title'))

# Close the driver
driver.quit()
