# Проект "Социальная сеть"

Этот проект представляет собой простую социальную сеть, где пользователи могут создавать посты с фотографиями и описаниями, оставлять комментарии к постам других пользователей, а также ставить лайки и дизлайки.

## Описание

Проект разработан с использованием Django и Django REST Framework. Он предоставляет API для создания, просмотра, редактирования и удаления постов, комментариев, а также возможность ставить лайки и дизлайки.

## Требования

- Python 3.x
- Django
- Django REST Framework

## Установка

1. Клонируйте репозиторий:

    git clone https://github.com/beka0708/backend-test.git

2. Установите зависимости:

    pip install -r requirements.txt
3. После установки проекта, выполните миграции:
    
    python manage.py migrate
4. Затем запустите сервер:

    python manage.py runserver