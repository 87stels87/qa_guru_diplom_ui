import allure

from pages.film_card_page import check_visible_buy_button, click_button_trailer, check_open_video_player, \
    click_film_score, check_registration_form
from pages.main_page import open_main_page, click_on_search_icon, input_name_film_and_click_by_search_resalt_card

@allure.epic('Тесты на карточку фильма')
@allure.story('Карточка фильма')
@allure.title('Отображение элементов на карточке фильма')
@allure.feature('Отображение кнопки Купить на карточке фильма')
@allure.label('Владелец', 'allure8')
@allure.tag('Регресс', 'веб')
@allure.severity('Critical')
def test_visible_buy_button(setup_browser):
    open_main_page()
    click_on_search_icon()
    input_name_film_and_click_by_search_resalt_card("Харбин")
    check_visible_buy_button()

@allure.epic('Тесты на карточку фильма')
@allure.story('Карточка фильма')
@allure.title('Отображение элементов на карточке фильма')
@allure.feature('Отображение плеера при нажатии на кнопку Трейлер')
@allure.label('Владелец', 'allure8')
@allure.tag('Регресс', 'веб')
@allure.severity('Critical')
def test_open_video_player_after_click_button_trailer(setup_browser):
    open_main_page()
    click_on_search_icon()
    input_name_film_and_click_by_search_resalt_card("Харбин")
    click_button_trailer()
    check_open_video_player()

@allure.epic('Тесты на карточку фильма')
@allure.story('Карточка фильма')
@allure.title('Отображение элементов на карточке фильма')
@allure.feature('Редирект на форму регистрации при оценке фильма для незарегистрированного пользователя')
@allure.label('Владелец', 'allure8')
@allure.tag('Регресс', 'веб')
@allure.severity('Normal')
def test_transfer_on_registration_form_after_click_film_score(setup_browser):
    open_main_page()
    click_on_search_icon()
    input_name_film_and_click_by_search_resalt_card("Харбин")
    click_film_score()
    check_registration_form()


