import allure

from pages.main_page import open_main_page, check_search_button_promo_code_be_visible, \
    check_url_after_click_on_subscribe_button, click_on_store_icon, check_section_new, click_on_promos_link, \
    check_visible_mail_in_promos_section


@allure.epic('Тесты на главную страницу')
@allure.story('Отображение маркетинговых элементов')
@allure.title('Отображение кнопки Ввести промокод')
@allure.feature('Маркетинговые элементы')
@allure.label('Владелец', 'allure8')
@allure.tag('Регресс', 'веб')
@allure.severity('Critical')
def test_visible_promo_code_button(setup_browser):
    open_main_page()
    check_search_button_promo_code_be_visible()


@allure.epic('Тесты на главную страницу')
@allure.story('Отображение маркетинговых элементов')
@allure.title('Проверка урла после редиректа на форму авторизации по кнопке Подписка')
@allure.feature('Маркетинговые элементы')
@allure.label('Владелец', 'allure8')
@allure.tag('Регресс', 'веб')
@allure.severity('Critical')
def test_url_after_click_on_subscribe_button(setup_browser):
    open_main_page()
    check_url_after_click_on_subscribe_button()


@allure.epic('Тесты на главную страницу')
@allure.story('Отображение маркетинговых элементов')
@allure.title('Проверка наименования электронной почты при нажатии на ссылку Акции и предложения')
@allure.feature('Маркетинговые элементы')
@allure.label('Владелец', 'allure8')
@allure.tag('Регресс', 'веб')
@allure.severity('Normal')
def test_should_mail_in_promos(setup_browser):
    open_main_page()
    click_on_promos_link()
    check_visible_mail_in_promos_section()


@allure.epic('Тесты на главную страницу')
@allure.story('Отображение секции Новое в магазине при клике на ссылку Магазин')
@allure.title('Отображение секции Новое в магазине')
@allure.feature('Маркетинговые элементы')
@allure.label('Владелец', 'allure8')
@allure.tag('Регресс', 'веб')
@allure.severity('Normal')
def test_check_section_new_in_store(setup_browser):
    open_main_page()
    click_on_store_icon()
    check_section_new()
