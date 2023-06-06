[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Интернет+Магазин)](https://git.io/typing-svg)



# Установка django

### 1) Создать виртуальное окружение установить зависимости
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

### 2) Выполнить миграции, cоздать суперпользователя и запустить сервер

    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver
    
# Установка vue
    npm i
    npm run serve
    

# Docker Run: ветка 2; branch 2
    
    
    docker-compose build
    docker-compose up 
    #
    docker-compose run --rm web-app sh -c 'python manage.py makemigrations'
    docker-compose run --rm web-app sh -c 'python manage.py migrate'
    docker-compose run --rm web-app sh -c 'python manage.py createsuperuser'
    #
    cd djackets_vue
    docker-compose build
    docker-compose up
