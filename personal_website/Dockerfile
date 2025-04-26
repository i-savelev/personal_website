# Базовый образ Python
FROM python:3.12-slim

# Установка рабочей директории внутри контейнера
WORKDIR /app

# Копирование файлов проекта в контейнер
COPY . /app/

# Установка зависимостей
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Открытие порта для Django-приложения
EXPOSE 8000

# Команда для запуска сервера разработки
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--forwarded-allow-ips='*'", "mysite.wsgi:application"]