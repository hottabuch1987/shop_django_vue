# shop_django_vue
My Shop
docker run django:::
  1) docker-compose build
  2) docker-compose up
  3)open new terminal:::
  4) docker-compose run --rm web-app sh -c 'python manage.py makemigrations'
  5) docker-compose run --rm web-app sh -c 'python manage.py migrate'
  6) docker-compose run --rm web-app sh -c 'python manage.py createsuperuser'
  7)vue run docker:::
  8) cd djackets_vue
  9) docker-compose build
  10) docker-compose up
