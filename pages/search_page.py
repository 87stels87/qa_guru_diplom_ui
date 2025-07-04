import allure
from selene.support.conditions.be import visible, enabled
from selene.support.shared.jquery_style import s

text_in_section_often_search = "Часто ищут"


class SearchPage:
    def check_visible_collection_often_search(self):
        with allure.step('Проверка отображения секции Часто ищут'):
            s('[test-id="search_collection_element"]').should(visible)
            # s('[test-id="nav_search_collection_title"]').should(have.text(text_in_section_often_search))

    def check_search_by_name_film(self, film_name):
        with allure.step('Проверка нахождения фильма по наименованию'):
            s('[data-testid="nav_search_input"]').type(film_name)
            s('(.//*[@test-id="search_collection_element"])[1]').should(enabled)

    def check_search_by_last_name_director(self, last_name_director):
        with allure.step('Проверка нахождения фильма по фамилии режиссера'):
            s('[data-testid="nav_search_input"]').type(last_name_director)
            s('(.//*[@test-id="search_collection_element"])[1]').should(enabled)