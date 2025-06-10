# Пример проекта автотестов для онлан-кинотеатра [Okko.tv](https://okko.tv/)
>Окко - российский онлайн-кинотеатр, позволяющий смотреть фильмы и телевизионные сериалы различных жанров в высоком качестве.
>Среди возможностей сервиса выделяются следующие:
>1) ТВ-каналы: Okko предлагает около 20 основных и десятков дополнительных эфирных каналов.
>2) Раздел «Спорт»: просмотр футбольных матчей, баскетбольных турниров, хоккея, биатлона, боёв МMA и даже киберспорта (например, Counter Strike 2 и Dota 2).
>4) Детский профиль: предусмотрена фильтрация контента по возрастному принципу, позволяющая подобрать подходящие материалы для детей.
>5) Мультипрофиль: возможность создать отдельные аккаунты для каждого члена семьи, добавив до пяти индивидуальных профилей с собственной историей просмотров.


![main page screenshot](images/screen/okko.png)


###  Используемые технологии
<p align="center">
  <code><img src="images/logo/python-original.svg" width="40" height="40" title="Python"></code>
  <code><img src="images/logo/pytest-original.svg" width="40" height="40" title="PyTest"></code>
  <code><img src="images/logo/selene.png" width="40" height="40" title="Selene"></code>
  <code><img src="images/logo/pycharm.png" width="40" height="40"vtitle="PyCharm"></code>
  <code><img src="images/logo/jenkins-original.svg" width="40" height="40" title="Jenkins"></code>
  <code><img src="images/logo/selenoid.png" width="40" height="40" title="Selenoid"></code>
  <code><img src="images/logo/Allure_Report.png" width="40" height="40" title="Allure Report"></code>
  <code><img src="images/logo/AllureTestOps.png" width="40" height="40" title="Allure TestOps"></code>
  <code><img src="images/logo/tg.png" width="40" height="40" title="Telegram Bot"></code>
  <code><img src="images/logo/docker.png" width="40" height="40" title="Docker"></code>
</p>

## Покрываемый функционал
- Авторизация пользователя 
- Проверка валидации полей логина
- Проверка возможности сбросить пароль


## Запуск тестов
#### Все UI тесты запускаются удалённо (Jenkins), но их можно запустить и локально

### Локально
Важно! Перед запуском нужно создать файл .env.selenoid_credentials и указать там selenoid_login 
и selenoid password

Для запуска тестов локально, нужно выполнить следующие шаги
1. Склонировать репозиторий
2. Открыть проект в PyCharm
3. Ввести в териминале следующие команды
``` 
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
context=web pytest -m web  
```

### С помощью [Jenkins](https://jenkins.autotests.cloud/job/C07_suprun_diploma/)
#### Для запуска автотестов необходимо:
 - Открыть [джобу](https://jenkins.autotests.cloud/job/C07_suprun_diploma/) в jenkins
 - Нажать на кнопку Build with Parameters
 - Выбрать необходимые значения параметров TESTS_TYPE и CONTEXT согласно инструкции 
 - Нажать на Build

<img src="images/screenshots/Jenkins_build.png">

## Отчет о прохождении тестов (Allure)
### Локально
Для получения отчета нужно ввести команду 
```
allure serve allure-results
``` 
Ниже представлен пример allure отчета 
<img src="images/screenshots/allure_report_example_web.png">

Подробные инструкции по работе с allure можно найти по [ссылке](https://allurereport.org/docs/).
### Если тесты запускались в Jenkins

Для получения отчета нужно нажать на иконку allure report'a в строке билда  
У него будет точно такой же формат, как и при получении локально
<img src="images/screenshots/allure_report_from_jenkins.png">

### В проекте реализована интеграция с Allure TestsOps
<img src="images/screenshots/allure_test_ops.png">

### В проекте настроена отправка краткого отчета в Telegram
<img src="images/screenshots/tg_web_allure.png">
