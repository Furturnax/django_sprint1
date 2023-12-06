## Запуск проекта:
+ Клонировать репозиторий и перейти в него в командной строке:
```shell script
git clone git@github.com:Furturnax/django_sprint1.git
```

```shell script
cd django_sprint1/
```

+ Cоздать и активировать виртуальное окружение (Windows/Bash):
```shell script
python -m venv venv
```

```shell script
source venv/Scripts/activate
```

+ Установить зависимости из файла requirements.txt:
```shell script
python -m pip install --upgrade pip
```

```shell script
pip install -r requirements.txt
```

+ Перейти в директорию с manage.py:
```shell script
cd blogicum/
```

+ Выполнить миграции:
```shell script
python manage.py migrate
```

+ Запустить проект:
```shell script
python manage.py runserver
```

<br>

## Просмотр контента:
Перейти по адресу http://127.0.0.1:8000/. На данный момент доступно несколько записей, загруженных непосредственно во view-функцию. 

<br>

## Тестирование проекта:
Тестирование реализовано с использованием библиотеки Pytest. 

+ Запустить тесты из основной директории проекта:
```shell script
pytest
```
