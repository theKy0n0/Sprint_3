from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import *
from cred_data import cred_data

class TestSbMovingToConstructorSections:
    def test_moving_to_bulki_section(self): # Переход к разделу булки
        driver = webdriver.Chrome(executable_path='/Users/serg/PycharmProjects/Sprint_3/venv/chromedriver')
        driver.get(cred_data['sb_url'])

        assert driver.find_element(By.XPATH, ConstructorPage.BULKA_SECTION).is_displayed()

        for bulki in driver.find_elements(By.XPATH, ConstructorPage.BULKA_ELEMENTS):
            assert bulki.is_displayed()

        driver.quit()

    def test_moving_to_sous(self): # Переход к разделу с соусами
        driver = webdriver.Chrome(executable_path='/Users/serg/PycharmProjects/Sprint_3/venv/chromedriver')
        driver.get(cred_data['sb_url'])

        driver.find_element(By.XPATH, ConstructorPage.SOUSI_SECTION_TAB).click()

        assert driver.find_element(By.XPATH, ConstructorPage.SOUSI_SECTION).is_displayed()
        for sousi in driver.find_elements(By.XPATH, ConstructorPage.SOUSI_ELEMENTS):
            assert sousi.is_displayed()

        driver.quit()

    def test_moving_to_nachinka(self): # Переход к разделу с начинками
        driver = webdriver.Chrome(executable_path='/Users/serg/PycharmProjects/Sprint_3/venv/chromedriver')
        driver.get(cred_data['sb_url'])

        driver.find_element(By.XPATH, ConstructorPage.NACHINKA_SECTION_TAB).click()

        assert driver.find_element(By.XPATH, ConstructorPage.NACHINKA_SECTION).is_displayed()
        assert driver.find_element(By.CSS_SELECTOR, ConstructorPage.NACHINKA_FIRST).is_displayed()

        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.CSS_SELECTOR, ConstructorPage.NACHINKA_LAST))

        assert driver.find_element(By.CSS_SELECTOR, ConstructorPage.NACHINKA_LAST).is_displayed()

        driver.quit()