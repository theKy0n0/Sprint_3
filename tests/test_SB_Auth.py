import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import *
from cred_data import cred_data

class TestSbAuth:
    def test_login_by_button_on_main_page(self): # Вход по кнопке «Войти в аккаунт» на главной
        driver = webdriver.Chrome(executable_path='/Users/serg/PycharmProjects/Sprint_3/venv/chromedriver')
        driver.get(cred_data['sb_url'])

        driver.find_element(By.XPATH, MainPage.LOGIN_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, AuthPage.EMAIL_FIELD).send_keys(cred_data['my_email'])
        driver.find_element(By.CSS_SELECTOR, AuthPage.PASS_FIELD).send_keys(cred_data['valid_pass'])
        driver.find_element(By.CSS_SELECTOR, AuthPage.LOGIN_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, AuthPage.PERSONAL_CABINET).click()

        time.sleep(2)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile' and driver.find_element(By.XPATH, PersonalCabinet.NAME_FIELD) and driver.find_element(By.XPATH, PersonalCabinet.LOGIN_FIELD) and driver.find_element(By.XPATH, PersonalCabinet.PASS_FIELD)

        driver.quit()

    def test_login_by_personal_cab_button(self): # Вход через кнопку «Личный кабинет»
        driver = webdriver.Chrome(executable_path='/Users/serg/PycharmProjects/Sprint_3/venv/chromedriver')
        driver.get(cred_data['sb_url'])

        driver.find_element(By.CSS_SELECTOR, MainPage.PERSONAL_CABINET).click()
        driver.find_element(By.CSS_SELECTOR, AuthPage.EMAIL_FIELD).send_keys(cred_data['my_email'])
        driver.find_element(By.CSS_SELECTOR, AuthPage.PASS_FIELD).send_keys(cred_data['valid_pass'])
        driver.find_element(By.CSS_SELECTOR, AuthPage.LOGIN_BUTTON).click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, AuthPage.PERSONAL_CABINET).click()

        time.sleep(3)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile' and driver.find_element(By.XPATH, PersonalCabinet.NAME_FIELD) and driver.find_element(By.XPATH,PersonalCabinet.LOGIN_FIELD) and driver.find_element(By.XPATH, PersonalCabinet.PASS_FIELD)

        driver.quit()

    def test_login_by_registration_page_button(self): # Вход через кнопку в форме регистрации
        driver = webdriver.Chrome(executable_path='/Users/serg/PycharmProjects/Sprint_3/venv/chromedriver')
        driver.get(cred_data['sb_reg_url'])

        driver.find_element(By.XPATH, RegPage.REG_ENTER_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, AuthPage.EMAIL_FIELD).send_keys(cred_data['my_email'])
        driver.find_element(By.CSS_SELECTOR, AuthPage.PASS_FIELD).send_keys(cred_data['valid_pass'])
        driver.find_element(By.CSS_SELECTOR, AuthPage.LOGIN_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, AuthPage.PERSONAL_CABINET).click()

        time.sleep(2)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile' and driver.find_element(By.XPATH, PersonalCabinet.NAME_FIELD) and driver.find_element(By.XPATH,PersonalCabinet.LOGIN_FIELD) and driver.find_element(By.XPATH, PersonalCabinet.PASS_FIELD)

        driver.quit()

    def test_login_by_recovery_pass_page(self): # Вход через кнопку в форме восстановления пароля
        driver = webdriver.Chrome(executable_path='/Users/serg/PycharmProjects/Sprint_3/venv/chromedriver')
        driver.get(cred_data['sb_recovery_pass_url'])

        driver.find_element(By.XPATH, RecoveryPage.RECOVERY_ENTER_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, AuthPage.EMAIL_FIELD).send_keys(cred_data['my_email'])
        driver.find_element(By.CSS_SELECTOR, AuthPage.PASS_FIELD).send_keys(cred_data['valid_pass'])
        driver.find_element(By.CSS_SELECTOR, AuthPage.LOGIN_BUTTON).click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, AuthPage.PERSONAL_CABINET).click()

        time.sleep(2)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile' and driver.find_element(By.XPATH, PersonalCabinet.NAME_FIELD) and driver.find_element(By.XPATH,PersonalCabinet.LOGIN_FIELD) and driver.find_element(By.XPATH, PersonalCabinet.PASS_FIELD)

        driver.quit()