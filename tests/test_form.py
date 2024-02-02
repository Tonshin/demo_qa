import allure

from pages.page_form import PageForm
from data.data import FIRST_NAME, LAST_NAME, NUMBER, SUBJECT, ADDRESS, EMAIL


@allure.title("Проверить отправку валидно заполненной формы")
@allure.description("""
    Цель: Проверить отправку валидно заполненной формы
    Шаги:
    1. Заполнить все поля формы валидными данными
    2. Нажать на кнопку "Submit"
    3. Проверить окно с отправленными данными
    """)
def test_form_submit_success(browser):
    page_form = PageForm(browser)
    page_form.open()
    page_form.input_first_name(FIRST_NAME)
    page_form.input_last_name(LAST_NAME)
    page_form.input_email(EMAIL)
    page_form.click_gender()
    page_form.input_number(NUMBER)
    page_form.select_date()
    page_form.input_subject(SUBJECT)
    page_form.select_hobbies()
    page_form.input_picture()
    page_form.input_address(ADDRESS)
    page_form.remove_footer_and_fixeban()
    page_form.select_state_and_city()
    page_form.click_submit()
    page_form.check_the_results()
