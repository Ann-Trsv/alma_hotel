# Alma Hotel Booking System

![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?logo=react&logoColor=61DAFB)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?logo=postgresql&logoColor=white)

Система управления бронированиями отеля с современным веб-интерфейсом и администрированием.


## Особенности

- 🗓️ Онлайн-бронирование номеров с выбором дат
- 📱 Адаптивный личный кабинет гостя
- 🖥️ Мощная панель администратора
- 🏙️ 3D-тур по отелю (интеграция с Matterport)
- 💳 Безопасные платежи через Stripe
- 📊 Аналитика занятости в реальном времени


## Технологический стек

| Компонент       | Технологии                          |
|-----------------|-------------------------------------|
| **Бэкенд**      | Python 3.10, Django 4.2, DRF       |
| **Фронтенд**    | React 18, TypeScript, Tailwind CSS  |
| **База данных** | PostgreSQL 14                       |
| **Инфраструктура** | Docker, Nginx, Redis              |


## Запуск проекта для разработки

- 'python -m venv venv' - создание виртуального окружения
- 'source venv/bin/activate' - вход в виртуальное окружение
- 'pip install -r requirements.txt' - установка зависимостей
- 'docker compose up -d' - запуск дополнительных сервисов в Docker.
  - [PostgreSQL](https://www.postgresql.org/)
- 'python manage.py migrate' - применение миграций
- 'python manage.py runserver' - запуск сервера для разработки на http://127.0.0.1:8080

## Документация

API Reference
Admin Guide
Frontend Architecture