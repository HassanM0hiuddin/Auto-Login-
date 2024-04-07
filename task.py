import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the URL of the login page
login_url = "Enter Your site address here "

# Set your login credentials
username = "Enter Your User Name here  "
password = "Enter Your password here "

def login():
    # Set up the Chrome driver
    driver = webdriver.Chrome()

    while True:
        try:
            driver.get(login_url)
            # Wait for the page to load completely
            time.sleep(5)  # Adjust the wait time as needed
            # Find the input elements for username and password
            wait = WebDriverWait(driver, 10)
            username_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="text"]')))
            password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="password"]')))
            # Enter username and password
            username_input.send_keys(username)
            password_input.send_keys(password)
            # Find and click the submit button
            submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
            submit_button.click()
            # Check if login was successful
            if "Dashboard" in driver.title:
                print("Login successful. Time:", time.strftime("%Y-%m-%d %H:%M:%S"))
            else:
                print("Login failed. Time:", time.strftime("%Y-%m-%d %H:%M:%S"))
            
            # Wait for 10 minutes before attempting to login again
            time.sleep(600)  # 600 seconds = 10 minutes
        
        except Exception as e:
            print("An error occurred:", str(e))
        
        finally:
            # Close the browser window to prevent resource leaks
            driver.quit()

# Call the login function
login()
