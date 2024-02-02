# Тестовое задание
## Предварительно необходимо установить Allure, Selenium GRID
## Установка и запуск
1. Склонировать репозиторий с Github:
````
git clone https://github.com/Tonshin/demo_qa.git
````
2. Перейти в директорию проекта
3. Создать виртуальное окружение:
````
python -m venv venv
````
4. Активировать окружение: 
````
venv\Scripts\activate
````
5. Установка зависимостей:
```
pip install -r requirements.txt
```
6. Запустить тест:
```
pytest ./tests/test_form.py --alluredir=allure-results
```
7. Запустить просмотр отчетов:
```
allure serve ./allure-results
```
