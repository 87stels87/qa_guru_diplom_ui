import allure
import pytest

from pages.film_card_page import FilmCardPage
from pages.main_page import MainPage
from pages.search_page import SearchPage

film_title = "Харбин"

film_card_page = FilmCardPage()
main_page = MainPage()
search_page = SearchPage()


@allure.epic('Тесты на карточку фильма')
@allure.label('Владелец', 'allure8')
@allure.tag('Регресс', 'веб')
class TestFilmCardPage:
    @pytest.mark.skip
    @allure.story('Карточка фильма')
    @allure.title('Отображение элементов на карточке фильма')
    @allure.feature('Отображение кнопки Купить на карточке фильма')
    @allure.severity('Critical')
    def test_visible_buy_button(self):
        main_page.open_main_page()
        main_page.click_on_search_icon()
        main_page.input_name_film_and_click_by_search_result_card(film_title)
        film_card_page.check_visible_buy_button()

    @allure.story('Карточка фильма')
    @allure.title('Отображение элементов на карточке фильма')
    @allure.feature('Отображение плеера при нажатии на кнопку Трейлер')
    @allure.severity('Critical')
    def test_open_video_player_after_click_button_trailer(self):
        main_page.open_main_page()
        main_page.click_on_search_icon()
        main_page.input_name_film_and_click_by_search_result_card(film_title)
        film_card_page.click_button_trailer()
        film_card_page.check_open_video_player()


    @allure.story('Карточка фильма')
    @allure.title('Отображение элементов на карточке фильма')
    @allure.feature('Редирект на форму регистрации при оценке фильма для незарегистрированного пользователя')
    @allure.severity('Normal')
    def test_transfer_on_registration_form_after_click_film_score(self):
        main_page.open_main_page()
        main_page.click_on_search_icon()
        main_page.input_name_film_and_click_by_search_result_card(film_title)
        film_card_page.click_film_score()
        film_card_page.check_registration_form()
