# shop_django_vue
My Shop
#docker run django:
  1) docker-compose build
  2) docker-compose up
  new terminal
  3) docker-compose run --rm web-app sh -c 'python manage.py makemigrations'
  4) docker-compose run --rm web-app sh -c 'python manage.py migrate'
  5) docker-compose run --rm web-app sh -c 'python manage.py createsuperuser'
#vue run docker:
  1) cd djackets_vue
  2) docker-compose build
  3) docker-compose up
