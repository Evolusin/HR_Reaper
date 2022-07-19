from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
import time
# Get Chrome driver ready
browser = webdriver.Chrome(ChromeDriverManager().install())
# Set waiter that we will use wait till that shitty site will load buttons to click
wait = WebDriverWait(browser, 10)


def loginwebiste():
    # Open site
    browser.get('https://hrnest.io/Account/LogOn')
    # Your HR credentials
    hr_name = "test"
    hr_pass = "test"
    # Fill credentials
    browser.find_element(By.NAME, 'UserName').send_keys(hr_name)
    browser.find_element(By.NAME, 'Password').send_keys(hr_pass)
    # Click Log In
    browser.find_element(By.NAME, 'btn').click();


def website(data1):
    browser.get('https://hrnest.io/create-request')
    # browser.fullscreen_window()

    # Change button value to HomeOffice
    # Version 2
    browser.find_element(By.CSS_SELECTOR, "button[title='Niedostępność']").click()
    button = "div[class='col-sm-7 field'] li:nth-child(3) a:nth-child(1) span:nth-child(1)"
    time.sleep(1)
    b_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, button)))
    time.sleep(1)
    b_element.click()
    time.sleep(1)

    # Set 'date from'
    data_start_r = "#u_Requests_StartDate"
    data_end_r = "#u_Requests_EndDate"
    browser.find_element(By.CSS_SELECTOR, data_start_r).click()
    e_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, data_start_r)))
    e_element.clear()
    e_element.send_keys(data1)
    time.sleep(1)
    # Set 'date to'
    browser.find_element(By.CSS_SELECTOR, data_end_r).click()
    g_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, data_end_r)))
    g_element.clear()
    g_element.send_keys(data1)

    # time.sleep(5)

    # Wyślij wniosek
    browser.find_element(By.CSS_SELECTOR,"input[value='Utwórz wniosek']").click();


# od której daty ma liczyć 7 dni (wstawi zdalną od 14.07)

first_date = "07.10.2022"
loginwebiste()

# wykonaj X powtórzeń
powtorzen = 10
for x in range(powtorzen):
    start_date = first_date
    date_1 = datetime.strptime(start_date, "%d.%m.%Y")
    add_date = date_1 + timedelta(days=7)
    end_date = add_date.strftime("%d.%m.%Y")
    website(end_date)
    first_date = end_date
