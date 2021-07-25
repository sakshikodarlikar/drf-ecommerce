# drf-ecommerce
E-commerce API built using Django-Rest-Framework


### How to Use and Test this Application on your computer
- run migrations ```python manage.py makemigrations```
- run migrate ```python manage.py migrate```
- run ```python manage.py createsuperuser``` to create superuser
- run the app ```python manage.py runserver```


### Product
Using ```/product/``` you can access all the products and add new products.

Using ```/product/<pk:id>/``` access CRUD operations.


### Product Category
Using ```/category/``` you can access all the categories and add new categories.

Using ```/category/<pk:id>/``` access CRUD operations.


### Buyer
Using ```/buyer/``` you can access all the buyers and add new buyers.

Using ```/buyer/<pk:id>/``` access CRUD operations.


### Seller
Using ```/seller/``` you can access all the sellers and add new sellers.

Using ```/seller/<pk:id>/``` access CRUD operations.


### Order
Using ```/order/``` you can access all the orders and add new orders.

Using ```/order/<pk:id>/``` access CRUD operations.

