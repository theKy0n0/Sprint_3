import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import *
from cred_data import cred_data

class TestSbLogoutFromPersonalCabinet:
    def test_logout_from_personal_cabinet(self): # Логаут со страницы личного кабинета
        driver = webdriver.Chrome(executable_path='/Users/serg/PycharmProjects/Sprint_3/venv/chromedriver')
        driver.get(cred_data['sb_url'])

        driver.find_element(By.CSS_SELECTOR, MainPage.PERSONAL_CABINET).click()
        driver.find_element(By.CSS_SELECTOR, AuthPage.EMAIL_FIELD).send_keys(cred_data['my_email'])
        driver.find_element(By.CSS_SELECTOR, AuthPage.PASS_FIELD).send_keys(cred_data['valid_pass'])
        driver.find_element(By.CSS_SELECTOR, AuthPage.LOGIN_BUTTON).click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, AuthPage.PERSONAL_CABINET).click()
        time.sleep(2)
        driver.find_element(By.XPATH, PersonalCabinet.LOGOUT_BUTTON).click()

        time.sleep(2)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login' and driver.find_element(By.CSS_SELECTOR, AuthPage.EMAIL_FIELD).is_displayed() and driver.find_element(By.CSS_SELECTOR, AuthPage.PASS_FIELD).is_displayed() and driver.find_element(By.CSS_SELECTOR, AuthPage.LOGIN_BUTTON).is_displayed()

        driver.quit()