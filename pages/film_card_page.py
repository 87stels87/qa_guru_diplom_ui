import allure
from selene import have, be
from selene.support.conditions.not_ import visible, enabled
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

text_on_film_card = "Купить и смотреть"

expected_url = "https://id.sber.ru/?scope=openid%20api%2Fv1%2Fuserdata%20avatar%20email%20mobile%20gender%20name%20birthdate%20offline_access%20prime_subscription%20bonus_balance%20mapp_sso%20email_confirmed%20verified&"


class FilmCardPage:
    def check_visible_buy_button(self):
        with allure.step('Проверка наличия кнопки Купить и смотреть на карточке фильма'):
            s('[test-id="action_purchase"]').should(have.text(text_on_film_card))

    def click_button_trailer(self):
        with allure.step('Клик по кнопке Трейлер на карточке фильма'):
            s('[test-id="play_trailer"]').click()

    def check_open_video_player(self):
        with allure.step('Проверка открытия плеера'):
            s('[id="videoElementContainer"]').should(be.enabled)

    def click_film_score(self):
        with allure.step('Клик по оценке за фильм'):
            s('//span[text()="5"]').click()

    def check_registration_form(self):
        with allure.step('Проверка открытия формы регистрации'):
            s('[data-testid="phoneNumber-input"]').should(be.enabled)
            browser.should(have.url_containing(expected_url))
