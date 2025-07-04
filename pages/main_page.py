import allure
from selene import browser, have, be
from selene.support.conditions.be import enabled
from selene.support.conditions.not_ import visible
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

url_by_subscription = "https://id.sber.ru/?scope=openid%20api%2Fv1%2Fuserdata%20avatar%20email%20mobile%20gender%20name%20birthdate%20offline_access%20prime_subscription%20bonus_balance%20mapp_sso%20email_confirmed%20verified&"
expected_email = "partnership@okko.tv"
section_name = "Новое в магазине"


class MainPage:

    def open_main_page(self):
        try:
            with allure.step('Открыть главную страницу'):
                browser.open(browser.config.base_url)
            with allure.step('Закрытие баннера при наличии'):
                if browser.element('[test-id="banner-pop-up-cancel-action-button"]').click().wait_until(be.visible):
                    browser.element('[test-id="banner-pop-up-cancel-action-button"]').click()
        except Exception as e:
            print(f"Произошла ошибка при закрытии баннера: {e}")

    def check_search_button_promo_code_be_visible(self):
        with allure.step('Убедиться в наличии кнопки Ввести промокод'):
            s('nav_promo').should(visible)

    def check_url_after_click_on_subscribe_button(self):
        with allure.step('Убедиться в корректности урла после клика на кнопку с подпиской'):
            browser.element('[test-id="nav_subscribe"]').click()
            browser.should(have.url_containing(url_by_subscription))

    def click_on_search_icon(self):
        with allure.step('Клик по иконке поиска на главной станице'):
            s('[test-id="nav_search"]').click()

    def input_name_film_and_click_by_search_result_card(self, film_name):
        with allure.step('Ввод наименования фильма и клик по результату поиска'):
            s('[data-testid="nav_search_input"]').type(film_name)
            # s(f'(.//*[text()="{film_name}"])[1]').click()
            s('(.//*[@test-id="search_collection_element"])[1]').click()

    def click_on_store_icon(self):
        with allure.step('Клик по ссылке Магазин на главной странице'):
            s('[test-id="store"]').click()

    def check_section_new(self):
        with allure.step('Проверка секции Новое в магазине '):
            s('[test-id="card_rail_header"]').should(have.text(section_name))

    def click_on_promos_link(self):
        with allure.step('Клик по ссылке Акции и предложения'):
            s('[href="/promos"]').click()

    def check_visible_mail_in_promos_section(self):
        with allure.step('Проверка наличия почты в разделе промоакции'):
            s('[href="mailto: partnership@okko.tv"]').should(enabled)
            s('[href="mailto: partnership@okko.tv"]').should(have.text(expected_email))