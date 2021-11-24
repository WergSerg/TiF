# TiFServer
Alfa-version  This is Fanfic server

# Install
1. Скопировать все из репы
1. Выполнить создание докер образа
    1.docker-compose up db  - создание образа базы данных
    1. docker-compose up backend  - создание сервера
    1. docker-compose up pgadmin  - при необходимости админка бд
1. выполнить создание супер пользователя 
    1. Получение container_id - docker ps -aqf "name=tifserver_backend_1"
    1. docker exec -it container_id python ./src/manage.py createsuperuser
    





## URL
1. admin/ -admin panel
1. api-oauth/ - authorization
1. Text/ - list of departments
1. category-tree/ - router link for employee data
1. get-category/ - get категорий для создания текста





