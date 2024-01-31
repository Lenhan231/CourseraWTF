import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep


# Create Chrome options and configure them
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Set up the ChromeDriver with options and service
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

# Navigate to LinkedIn login page
driver.get("https://www.linkedin.com/login")
time.sleep(2)
# Find the email field and enter the email
email_field = driver.find_element(By.ID, "username")  
email_field.send_keys("nhanle221199@gmail.com")
time.sleep(2)
# Find the password field and enter the password
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("0la1thangtop256")
time.sleep(2)
# Find the login button and click on it
login_button = driver.find_element(By.XPATH, "//*[@id='organic-div']/form/div[3]/button")
login_button.click()
time.sleep(2)
# Alternatively, you can use single quotes around the XPath string to avoid escaping
# login_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
# login_button.click()

search_field = driver.find_element(By.XPATH, "//*[@id=\"global-nav-typeahead\"]/input")
search_field.send_keys("Software Engineer people")
search_field.send_keys(Keys.RETURN)






password_field.send_keys(Keys.RETURN)
driver.quit()
