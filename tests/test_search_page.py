import allure

from pages.main_page import open_main_page, click_on_search_icon
from pages.search_page import check_search_by_last_name_director, check_visible_collection_often_search, \
    check_search_by_name_film

name_director = "Квентин Тарантино"
film_title = "Твин Пикс"

@allure.epic('Тесты на поиск')
@allure.story('Отображение дополнительных секций')
@allure.title('Отображение секции Часто ищут')
@allure.feature('Поиск')
@allure.label('Владелец', 'allure8')
@allure.tag('Регресс', 'веб')
@allure.severity('Critical')
def test_visible_collection_often_search(setup_browser):
    open_main_page()
    click_on_search_icon()
    check_visible_collection_often_search()


@allure.epic('Тесты на поиск')
@allure.story('Поиск фильма')
@allure.title('Поиск фильма по наименованию')
@allure.feature('Поиск')
@allure.label('Владелец', 'allure8')
@allure.tag('Регресс', 'веб')
@allure.severity('Critical')
def test_search_by_name_film(setup_browser):
    open_main_page()
    click_on_search_icon()
    check_search_by_name_film(film_title)


@allure.epic('Тесты на поиск')
@allure.story('Поиск фильма')
@allure.title('Поиск фильма по фамилии и имени режиссера')
@allure.feature('Поиск')
@allure.label('Владелец', 'allure8')
@allure.tag('Регресс', 'веб')
@allure.severity('Critical')
def test_search_by_last_name_director(setup_browser):
    open_main_page()
    click_on_search_icon()
    check_search_by_last_name_director(name_director)
