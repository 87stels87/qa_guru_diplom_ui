import allure
import pytest

from pages.main_page import MainPage

main_page = MainPage()


@allure.epic('Тесты на главную страницу')
@allure.story('Отображение маркетинговых элементов')
@allure.feature('Маркетинговые элементы')
@allure.label('Владелец', 'allure8')
@allure.tag('Регресс', 'веб')
class TestMainPage:
    @pytest.mark.skip
    @allure.title('Отображение кнопки Ввести промокод')
    @allure.severity('Critical')
    def test_visible_promo_code_button(self):
        main_page.open_main_page()
        main_page.check_search_button_promo_code_be_visible()

    @pytest.mark.skip
    @allure.title('Проверка урла после редиректа на форму авторизации по кнопке Подписка')
    @allure.severity('Critical')
    def test_url_after_click_on_subscribe_button(self):
        main_page.open_main_page()
        main_page.check_url_after_click_on_subscribe_button()

    @pytest.mark.skip
    @allure.story('Отображение маркетинговых элементов')
    @allure.title('Проверка наименования электронной почты при нажатии на ссылку Акции и предложения')
    @allure.severity('Normal')
    def test_should_mail_in_promos(self):
        main_page.open_main_page()
        main_page.click_on_promos_link()
        main_page.check_visible_mail_in_promos_section()

    @pytest.mark.skip
    @allure.story('Отображение секции Новое в магазине при клике на ссылку Магазин')
    @allure.title('Отображение секции Новое в магазине')
    @allure.severity('Normal')
    def test_check_section_new_in_store(self):
        main_page.open_main_page()
        main_page.click_on_store_icon()
        main_page.check_section_new()