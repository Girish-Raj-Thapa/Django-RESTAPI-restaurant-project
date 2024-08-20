# Django-RESTAPI-restaurant-project
<h1>Overview</h1>

This project is a Django-based RESTful API for an e-commerce platform, providing functionalities for menu management, cart operations, and order processing. The API supports role-based access control and dynamic views for efficient data handling.

<h2>Features</h2>

Menu Management: CRUD operations for menu items and categories.
Cart Operations: Add, remove, and list items in the cart.
Order Processing: Place, update, and retrieve orders.
Role-Based Access Control: Custom permissions for Managers and Delivery Crew.
Pagination and Search: Efficient data retrieval with search and pagination.

<h2>Technologies</h2>

Django: Web framework
Django REST Framework: API framework
Djoser: Authentication and user management
SQLite: Database (default; can be configured for other databases)
Pipenv: Dependency management

<h2>Installation</h2>

<h5>Clone the repository:</h5>
git clone https://github.com/yourusername/LittleLemon.git
cd LittleLemon
<h5>Set up the environment:</h5>
pipenv install
<h5>Run the server:</h5>
pipenv run python manage.py migrate
pipenv run python manage.py runserver

<h2>Configuration</h2>

Database: The default setup uses SQLite. To use a different database, update the DATABASES setting in settings.py.
Authentication: Configure Djoser in settings.py for token-based authentication.

<h2>Usage</h2>

<h4>API Endpoints:</h4>
/api/menu-items/: List and create menu items.
/api/menu-items/<id>/: Retrieve, update, or delete a specific menu item.
/api/cart/menu-items/: Manage cart items.
/api/orders/: List and create orders.
/api/orders/<id>/: Retrieve, update, or delete a specific order.
    
<h4>Authentication:</h4>
Use Djoser endpoints for user registration and login.
Authentication tokens should be included in request headers.

<h2>Testing</h2>

<b>Run tests using the Django test framework:</b>
pipenv run python manage.py test

<h2>Contributing</h2>

Feel free to fork the repository and submit pull requests. For any issues or feature requests, open an issue in the GitHub repository.

<h2>License</h2>

This project is licensed under the MIT License. See the LICENSE file for details.


Name for Super Admin:
    username: admin 
    email: admin@littlelemon.com
    password: littleadmin@123
    
Users:
    Managers:
        1:
        username: jhondoe
        password: littlejhon@123
        email: jhondoe@littlelemon.com 

        2: 
        username: jimmydoe
        password: littlejimmy@123
        email: jimmydoe@littlelemon.com 

    Delivery Crew:
        1:
        username: tom
        password: littletom@123
        email: tom@littlelemon.com 

        2:
        username: harry
        password: littleharry@123
        email: harry@littlelemon.com

    Customers:
        1:
        username: adrian
        password: littleadrian@123
        email: adrain@littlelemon.com

        2:
        username: lily 
        password: littlelily@123
        email: lily@littlelemon.com 



