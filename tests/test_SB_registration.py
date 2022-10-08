import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import *
from cred_data import cred_data


class TestSbReg:
    def test_with_correct_entities(self): # Логин с корректными данными
        driver = webdriver.Chrome(executable_path='/Users/serg/PycharmProjects/Sprint_3/venv/chromedriver')
        driver.get(cred_data['sb_url']) # Передаем браузеру адрес сайта и открываем его

        driver.find_element(By.XPATH, MainPage.LOGIN_BUTTON).click() # Находим на странице кнопку "Войти в аккаунт" и кликаем на нее
        driver.find_element(By.CSS_SELECTOR, AuthPage.REG_NEW_USER_BUTTON).click() # Находим на странице кнопку "Зарегистрироваться" и кликаем на нее
        driver.find_element(By.CSS_SELECTOR, RegPage.NAME_FIELD).send_keys(cred_data['my_name']) # Находим на странице поле ввода имени и вставляем значение имени из словаря
        driver.find_element(By.CSS_SELECTOR, RegPage.EMAIL_FIELD).send_keys(cred_data['my_email']) # Находим на странице поле ввода email и вставляем значение из email из словаря
        driver.find_element(By.CSS_SELECTOR, RegPage.PASS_FIELD).send_keys(cred_data['valid_pass']) # Находим на странице поле ввода пароля и вставляем значение пароля из словаря
        driver.find_element(By.XPATH, RegPage.REG_BUTTON).click() # Находим кнопку "Зарегистрироваться" и кликаем на нее

        time.sleep(2)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login' and driver.find_element(By.CSS_SELECTOR, AuthPage.REG_NEW_USER_BUTTON).text == 'Зарегистрироваться' # Проверяем страницу на которой находимся и наличие на этой странице кнопки с надписью "Зарегистрироваться"

        driver.quit()

    def test_with_incorrect_pass(self): # Логин с некорректным паролем
        driver = webdriver.Chrome(executable_path='/Users/serg/PycharmProjects/Sprint_3/venv/chromedriver')
        driver.get(cred_data['sb_url'])  # Передаем браузеру адрес сайта и открываем его

        driver.find_element(By.XPATH,MainPage.LOGIN_BUTTON).click()  # Находим на странице кнопку "Войти в аккаунт" и кликаем на нее
        driver.find_element(By.CSS_SELECTOR,AuthPage.REG_NEW_USER_BUTTON).click()  # Находим на странице кнопку "Зарегистрироваться" и кликаем на нее
        driver.find_element(By.CSS_SELECTOR, RegPage.NAME_FIELD).send_keys(cred_data['my_name'])  # Находим на странице поле ввода имени и вставляем значение имени из словаря
        driver.find_element(By.CSS_SELECTOR, RegPage.EMAIL_FIELD).send_keys(cred_data['my_email'])  # Находим на странице поле ввода email и вставляем значение из email из словаря
        driver.find_element(By.CSS_SELECTOR, RegPage.PASS_FIELD).send_keys(cred_data['invalid_pass'])  # Находим на странице поле ввода пароля и вставляем значение пароля из словаря
        driver.find_element(By.XPATH, RegPage.REG_BUTTON).click() # Находим кнопку "Зарегистрироваться" и кликаем на нее

        time.sleep(2)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register' and driver.find_element(By.CSS_SELECTOR, RegPage.REG_ERROR_POPUP).text == 'Некорректный пароль'

        driver.quit()
