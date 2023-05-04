# shop_django_vue

My Shop docker run django:
branch 2

    ##
    
    docker-compose build
    docker-compose up 
    open new terminal:
    
    docker-compose run --rm web-app sh -c 'python manage.py makemigrations'
    docker-compose run --rm web-app sh -c 'python manage.py migrate'
    docker-compose run --rm web-app sh -c 'python manage.py createsuperuser'
    
    ##
    vue run docker:
    cd djackets_vue
    docker-compose build
    docker-compose up
