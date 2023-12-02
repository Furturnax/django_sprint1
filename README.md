# Проект "Blogicum v. 1.0"
Реализация социальной сети **Blogicum**. 

Основные возможности:
- чтение публикаций. 

Проект является учебным. Основная польза в приобретении понимания реализации проекта через фреймворк `Django`, а именно: 
- развёртывание `Django` проекта;
- установка приложений и их регистрация;
- настройка локализации и часового пояса;
- описание маршрутов `URL`;
- создание `html` шаблонов всех страниц в отдельной директории `templates`;
- подключение `css` файла, иконок в виде статических материалов из отдельной директории `static` ; 
- реализация view-функций, позволяющих рендерить страницы, на основе `base.html`;
- запуск интегрированного в `Django` сервера, через который доступен текущий продукт.

<br>

## Технологический стек:
- Python 3.11.5
- Django 3.2.16
- Pytest 7.4.2

<br>

## Как запустить проект :shipit: :
+ Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone git@github.com:Furturnax/django_sprint1.git
```

```bash
cd django_sprint1/
```

+ Cоздать и активировать виртуальное окружение (Windows/Bash):
```bash
python -m venv venv
```

```bash
source venv/Scripts/activate
```

+ Установить зависимости из файла requirements.txt:
```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

+ Перейти в директорию с manage.py:
```bash
cd blogicum/
```

+ Выполнить миграции:
```bash
python manage.py migrate
```

+ Запустить проект:
```bash
python manage.py runserver
```

<br>

## Просмотр контента:
Перейти по адресу http://127.0.0.1:8000/. На данный момент доступно несколько записей, загруженных непосредственно во view-функцию. 

<br>

## Тестирование проекта:
Тестирование реализовано с использованием библиотеки Pytest. 

+ Запустить тесты из основной директории проекта:
```bash
pytest
```

<br>

## Авторство
Автор проекта - Yandex Practicum | [GitHub](https://github.com/yandex-praktikum)

Разработчик - Andrew Fedorchenko | [GitHub](https://github.com/Furturnax) [Telegram](https://t.me/furturnax)

Ревьюер - Evgeniy Salahutdinov | [GitHub](https://github.com/EugeneSal)
