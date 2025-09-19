import time
import subprocess
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set the current working directory
cwd = r"C:\Users\LENOVO\youtu"

# Directly invoke the Python interpreter and Django's manage.py
django_command = "python manage.py runserver 127.0.0.1:8005"
process = subprocess.Popen(django_command, cwd=cwd, shell=True)

# Selenium Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("--app=http://127.0.0.1:8005")

# WebDriver setup
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://127.0.0.1:8005")

# Loop to keep the driver active and check the page title
try:
    while True:
        time.sleep(2)
        print(driver.title)  # Prints the page title to monitor the process
except KeyboardInterrupt:
    print("\nProcess interrupted by user.")
finally:
    driver.quit()  # Gracefully closes the browser
    process.terminate()  # Stops the Django development server
