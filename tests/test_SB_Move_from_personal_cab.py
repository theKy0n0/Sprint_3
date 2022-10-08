import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import *
from cred_data import cred_data

class TestSbMoveFromPersonalCab:
    def test_move_to_personal_cab(self): # Переход к личному кабинету с главной страницы
        driver = webdriver.Chrome(executable_path='/Users/serg/PycharmProjects/Sprint_3/venv/chromedriver')
        driver.get(cred_data['sb_url'])

        driver.find_element(By.CSS_SELECTOR, MainPage.PERSONAL_CABINET).click()
        driver.find_element(By.CSS_SELECTOR, AuthPage.EMAIL_FIELD).send_keys(cred_data['my_email'])
        driver.find_element(By.CSS_SELECTOR, AuthPage.PASS_FIELD).send_keys(cred_data['valid_pass'])
        driver.find_element(By.CSS_SELECTOR, AuthPage.LOGIN_BUTTON).click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, AuthPage.PERSONAL_CABINET).click()

        time.sleep(3)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile' and driver.find_element(By.XPATH, PersonalCabinet.NAME_FIELD) and driver.find_element(By.XPATH,PersonalCabinet.LOGIN_FIELD) and driver.find_element(By.XPATH, PersonalCabinet.PASS_FIELD) and driver.find_element(By.CSS_SELECTOR, PersonalCabinet.ORDER_HISTORY_BUTTON)

        driver.quit()

    def test_move_to_constructor(self): # Переход из личного кабинета по клику на "Конструктор"
        driver = webdriver.Chrome(executable_path='/Users/serg/PycharmProjects/Sprint_3/venv/chromedriver')
        driver.get(cred_data['sb_url'])

        driver.find_element(By.CSS_SELECTOR, MainPage.PERSONAL_CABINET).click()
        driver.find_element(By.CSS_SELECTOR, AuthPage.EMAIL_FIELD).send_keys(cred_data['my_email'])
        driver.find_element(By.CSS_SELECTOR, AuthPage.PASS_FIELD).send_keys(cred_data['valid_pass'])
        driver.find_element(By.CSS_SELECTOR, AuthPage.LOGIN_BUTTON).click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, AuthPage.PERSONAL_CABINET).click()
        driver.find_element(By.XPATH, PersonalCabinet.CONSTRUCTOR_BUTTON).click()

        time.sleep(3)
        assert driver.current_url == cred_data['sb_url'] and driver.find_element(By.XPATH, MainPage.WELCOME_TITLE).is_displayed()

        driver.quit()

    def test_move_by_stellar_burger_logo(self): # Переход из личного кабинета по клику на логотип Stellar Burger
        driver = webdriver.Chrome(executable_path='/Users/serg/PycharmProjects/Sprint_3/venv/chromedriver')
        driver.get(cred_data['sb_url'])

        driver.find_element(By.CSS_SELECTOR, MainPage.PERSONAL_CABINET).click()
        driver.find_element(By.CSS_SELECTOR, AuthPage.EMAIL_FIELD).send_keys(cred_data['my_email'])
        driver.find_element(By.CSS_SELECTOR, AuthPage.PASS_FIELD).send_keys(cred_data['valid_pass'])
        driver.find_element(By.CSS_SELECTOR, AuthPage.LOGIN_BUTTON).click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, AuthPage.PERSONAL_CABINET).click()
        driver.find_element(By.CSS_SELECTOR, MainPage.LOGO).click()

        time.sleep(3)
        assert driver.current_url == cred_data['sb_url'] and driver.find_element(By.XPATH, MainPage.WELCOME_TITLE).is_displayed()

        driver.quit()