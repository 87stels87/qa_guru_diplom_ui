import allure
from selene import have, be
from selene.support.conditions.be import visible, empty
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def check_visible_collection_often_search():
    with allure.step('Проверка отображения секции Часто ищут'):
        s('[test-id="nav_search_collection_title"]').should(visible)
        s('[test-id="nav_search_collection_title"]').should(have.text('Часто ищут'))


def check_search_by_name_film(film_name):
    with allure.step('Проверка нахождения фильма по наименованию'):
        s('[test-id="nav_search_input"]').type(film_name)
        s('[test-id="nav_search_collection_element"]').should(visible)
        s('[test-id="nav_search_collection_element"]').should(be.not_.blank)


def check_search_by_last_name_director(last_name_director):
    with allure.step('Проверка нахождения фильма по фамилии режиссера'):
        s('[test-id="nav_search_input"]').type(last_name_director)
        s('[test-id="nav_search_collection_element"]').should(visible)
        s('[test-id="nav_search_collection_element"]').should(have.text(last_name_director))


