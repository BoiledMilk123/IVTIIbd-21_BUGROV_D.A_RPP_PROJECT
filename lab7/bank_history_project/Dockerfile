 # Устанавливаем переменные окружения

 FROM python:3.11-slim
 ENV PYTHONUNBUFFERED=1 \
     PYTHONDONTWRITEBYTECODE=1

 # Создаём рабочую директорию
 WORKDIR /app

 # Устанавливаем зависимости для PostgreSQL
 RUN apt-get update -qq && apt-get install -y postgresql-client

 # Копируем и устанавливаем зависимости
 COPY requirements.txt /app/
 RUN pip install --no-cache-dir -r requirements.txt

 # Копируем код приложения
 COPY . /app

 # Запускаем Gunicorn
 CMD ["gunicorn", "bank_history.wsgi:application", "--bind", "0.0.0.0:80"]