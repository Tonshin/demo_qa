import os

import allure
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from locators.pages_locators import FormLocators
from data.data import *


class PageForm(BasePage):

    locator = FormLocators()

    def __init__(self, browser, url=None):
        super().__init__(browser, url)
        self.url = 'https://demoqa.com/automation-practice-form'

    @allure.step("Добавить имя")
    def input_first_name(self, first_name):
        self.element_is_visible(self.locator.FIRST_NAME).send_keys(first_name)

    @allure.step("Добавить фамилию")
    def input_last_name(self, last_name):
        self.element_is_visible(self.locator.LAST_NAME).send_keys(last_name)

    @allure.step("Добавить email")
    def input_email(self, email):
        self.element_is_visible(self.locator.EMAIL).send_keys(email)

    @allure.step("Выбрать мужской пол")
    def click_gender(self):
        self.element_is_visible(self.locator.GENDER).click()

    @allure.step("Добавить номер телефона")
    def input_number(self, number):
        self.element_is_visible(self.locator.NUMBER).send_keys(number)

    @allure.step("Выбрать дату")
    def select_date(self):
        self.element_is_visible(self.locator.DOB).click()
        self.element_is_visible(self.locator.MONTH_DOB).click()
        self.element_is_visible(self.locator.MONTH_CHECK_JUNE).click()
        self.element_is_visible(self.locator.YEAR_DOB).click()
        self.element_is_clickable(self.locator.YEAR_CHECK_1997).click()
        self.element_is_clickable(self.locator.DATE_THIRD_DAY).click()

    @allure.step("Выбрать предмет")
    def input_subject(self, subject):
        subjects_input = self.element_is_visible(self.locator.SUBJECT)
        subjects_input.send_keys(subject)
        subjects_input.send_keys(Keys.ENTER)

    @allure.step("Выбрать хобби")
    def select_hobbies(self):
        self.element_is_visible(self.locator.HOBBIES).click()

    @allure.step("Добавить файл")
    def input_picture(self):
        picture_input = self.element_is_clickable(self.locator.PICTURE_INPUT_BUTTON)
        file = os.path.abspath(FILE_PATH)
        picture_input.send_keys(file)

    @allure.step("Добавить адрес")
    def input_address(self, address):
        self.element_is_visible(self.locator.ADDRESS).send_keys(address)

    @allure.step("Удалить footer")
    def remove_footer_and_fixeban(self):
        self.remove_footer()
        self.remove_fixeban()

    @allure.step("Выбрать штат и город")
    def select_state_and_city(self):
        state_dropdown = self.element_is_clickable(self.locator.STATE_DROPDOWN_BUTTON)
        self.scroll_into_view_state_and_use_action()
        state_dropdown.click()
        self.element_is_clickable(self.locator.STATE_VALUE_CHOICE).click()
        city_dropdown = self.element_is_clickable(self.locator.CITY_DROPDOWN_BUTTON)
        self.scroll_into_view_city_and_use_action()
        city_dropdown.click()
        self.element_is_clickable(self.locator.CITY_VALUE_CHOICE).click()

    @allure.step("Нажать кнопку 'Submit'")
    def click_submit(self):
        submit_button = self.element_is_clickable(self.locator.SUBMIT)
        self.scroll_into_view_submit_and_use_action()
        submit_button.click()

    def check_the_results(self):
        result_txt = self.element_is_visible(self.locator.RESULT_TXT).text
        assert result_txt == "Thanks for submitting the form", "Текст не соответствует ожидаемому"

        student_name_table = self.element_is_visible(self.locator.STUDENT_NAME_TABLE)
        assert student_name_table.text == FIRST_NAME + " " + LAST_NAME, "Имя и фамилия не соответсвует ожиданию"

        email_in_table = self.element_is_visible(self.locator.EMAIL_IN_TABLE)
        assert email_in_table.text == EMAIL, "Email не соответствует ожидаемому"

        gender_in_table = self.element_is_visible(self.locator.GENDER_IN_TABLE)
        assert gender_in_table.text == "Male", "Пол не соответствует ожидаемому"

        number_in_table = self.element_is_visible(self.locator.NUMBER_IN_TABLE)
        assert number_in_table.text == NUMBER, "Номер не соответствует ожидаемому"

        date_in_table = self.element_is_visible(self.locator.DATE_IN_TABLE)
        assert date_in_table.text != "", "Дата не соответствует ожидаемому"

        subjects_in_table = self.element_is_visible(self.locator.SUBJECTS_IN_TABLE)
        assert subjects_in_table.text == SUBJECT, "Предмет не соответствует ожидаемому"

        hobbies_in_table = self.element_is_visible(self.locator.HOBBIES_IN_TABLE)
        assert hobbies_in_table.text != "", "Хобби не соответствует ожидаемому"

        picture_in_table = self.element_is_visible(self.locator.PICTURE_IN_TABLE)
        assert picture_in_table.text != "", "Файл не вложен"

        address_in_table = self.element_is_visible(self.locator.ADDRESS_IN_TABLE)
        assert address_in_table.text != "", "Адрес не соответствует ожидаемому"

        state_and_city_in_table = self.element_is_visible(self.locator.STATE_AND_CITY_IN_TABLE)
        assert state_and_city_in_table.text != "", "Штат и город не соответствует ожидаемому"
