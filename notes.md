## Команды для клнсоли
`mkdir personal_website`

`uv run django-admin startproject mysite personal_website` - создание проекта 

`uv run personal_website/manage.py runserver` - запуск проекта на локальном сервере

`uv run personal_website/manage.py startapp blog` - создание приложения

`uv run personal_website/manage.py makemigrations blog` - активация моделей 

`uv run personal_website/manage.py migrate` - создание таблиц в базе данных

`uv run personal_website/manage.py createsuperuser` - создание админки

## Работа с python
`blog/views.py` - тут создать view

`blog/urls.py` - сюда добавить путь к view

`mysite/urls.py/urlpatterns` - сюда добавить path("", include("blog.urls"))

`mysite/settings.py/TIME_ZONE = 'Europe/Moscow'` - смена часовог пояса

