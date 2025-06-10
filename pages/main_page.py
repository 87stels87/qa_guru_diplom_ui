
from selene import browser, be, have
from selene.core.match import browser_has_url
from selene.support.conditions.be import enabled
from selene.support.conditions.not_ import visible
from selene.support.shared.jquery_style import s
from selenium.webdriver.support.expected_conditions import url_to_be
import allure
from selene.support.shared import browser


def open_main_page():
    with allure.step('Открыть главную страницу'):
        # browser.open('https://okko.tv/')
        browser.open(browser.config.base_url)



def check_search_button_promo_code_be_visible():
    with allure.step('Убедиться в наличии кнопки Ввести промокод'):
        s('nav_promo').should(visible)


def check_url_after_click_on_subscribe_button():
    with allure.step('Убедиться в корректности урла после клика на кнопку с подпиской'):
        browser.element('[test-id="nav_subscribe"]').click()
        browser.should(have.url_containing(
            'https://id.sber.ru/?scope=openid%20api%2Fv1%2Fuserdata%20avatar%20email%20mobile%20gender%20name%20birthdate%20offline_access%20prime_subscription%20bonus_balance%20mapp_sso%20email_confirmed%20verified&'))


def click_on_search_icon():
    with allure.step('Клик по иконке поиска на главной станице'):
        s('[test-id="nav_search"]').click()

def input_name_film_and_click_by_search_resalt_card(film_name):
    with allure.step('Ввод наименования фильма и клик по результату поиска'):
        s('[test-id="nav_search_input"]').type(film_name)
        s(f'.//*[text()="{film_name}"]').click()


def click_on_store_icon():
    with allure.step('Клик по ссылке Магазин на главной странице'):
        s('[test-id="store"]').click()


def check_section_new():
    with allure.step('Проверка секции Новое в магазине '):
        s('[test-id="card_rail_header"]').should(have.text("Новое в магазине"))


def click_on_promos_link():
    with allure.step('Клик по ссылке Акции и предложения'):
        # browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        s('[href="/promos"]').click()


def check_visible_mail_in_promos_section():
    with allure.step('Проверка наличия почты в разделе промоакции'):
        s('[href="mailto: partnership@okko.tv"]').should(enabled)
        s('[href="mailto: partnership@okko.tv"]').should(have.text("partnership@okko.tv"))
