import allure
import pytest

from pages.film_card_page import FilmCardPage
from pages.main_page import MainPage
from pages.search_page import SearchPage

film_card_page = FilmCardPage()
main_page = MainPage()
search_page = SearchPage()

name_director = "Квентин Тарантино"
film_title = "Твин Пикс"


@allure.epic('Тесты на поиск')
@allure.feature('Поиск')
@allure.label('Владелец', 'allure8')
@allure.tag('Регресс', 'веб')
class TestSearchPage:
    @pytest.mark.skip
    @allure.story('Отображение дополнительных секций')
    @allure.title('Отображение секции Часто ищут')
    @allure.severity('Critical')
    def test_visible_collection_often_search(self):
        main_page.open_main_page()
        main_page.click_on_search_icon()
        search_page.check_visible_collection_often_search()

    @allure.story('Поиск фильма')
    @allure.title('Поиск фильма по наименованию')
    @allure.severity('Critical')
    def test_search_by_name_film(self):
        main_page.open_main_page()
        main_page.click_on_search_icon()
        search_page.check_search_by_name_film(film_title)

    @allure.story('Поиск фильма')
    @allure.title('Поиск фильма по фамилии и имени режиссера')
    @allure.severity('Critical')
    def test_search_by_last_name_director(self):
        main_page.open_main_page()
        main_page.click_on_search_icon()
        search_page.check_search_by_last_name_director(name_director)