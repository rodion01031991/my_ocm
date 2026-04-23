# OCM - OneClickMoney

+ Структура проекта


my_ocm/<br>
├── pages/ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ# Папка с классами страниц  <br>
│   ├── first_step_of_registration_page.py ㅤㅤ# Класс первой страницы регистрацииㅤ<br>
│   ├── lodin_page.py ㅤㅤㅤㅤ# Класс страницы входа<br>
│   └── third_step_of_registration_page.py ㅤㅤ# Класс третьей страницы регистрации<br>
├── tests/ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ# Папка с тестами страниц<br>
│   ├── first_step_of_registration_page.py ㅤㅤㅤㅤㅤㅤ # Тесты для первой страницы регистрации<br>
│   ├── test_lodin.py ㅤㅤㅤㅤㅤ# Тесты для страницы входа<br>
│   └── test_third_step_of_registration_page.py ㅤㅤ# Тесты для третьей страницы регистрации<br>
├── common functions.py ㅤㅤㅤㅤ# общие функции <br>
├── conftest.py ㅤㅤㅤㅤㅤㅤㅤㅤㅤ# общие фикстуры <br>
├──requirements.txt ㅤㅤㅤㅤㅤㅤ # зависимости проекта<br>

Запуск тестов для 3 страницы python -m pytest tests/test_third_step_of_registration.py