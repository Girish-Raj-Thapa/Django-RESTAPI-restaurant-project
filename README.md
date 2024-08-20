# Django-RESTAPI-restaurant-project

API Final Project


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

E-Commerce REST API Project

<h2>Project Overview:</h2>
Developed a comprehensive e-commerce REST API using Django and Django REST Framework (DRF) to manage a restaurant's menu, cart, orders, and user management.
Key Features:
<h5>User Authentication:</h5> Integrated user authentication with Django REST Framework and Djoser, supporting registration, login, and token-based authentication.
<h5>User Roles and Permissions:</h5> Implemented custom permissions for different user roles including Managers, Delivery Crew, and regular users, allowing role-based access control to API endpoints.
<h5>CRUD Operations:</h5>
Menu Management: CRUD operations for menu items and categories with serializers and views to manage and query products.
Cart Management: Functionality for adding, updating, and removing items from the cart. Ensured that cart operations are user-specific.
Order Management: Users can place orders, view their orders, and update or delete them. Managers and Delivery Crew have extended permissions to manage all orders.
Group Management: Endpoints to manage user groups (Managers and Delivery Crew), including adding and removing users from these groups.
API Security: Implemented rate limiting and throttling to protect against abuse, and configured permissions to ensure data security and access control.
<h5>Technologies Used:</h5>
Backend: Django 5.0.7, Django REST Framework, Djoser
Database: SQLite (for development; easily configurable for MySQL in production)
Authentication: Token-based authentication with DRF, user management with Django's built-in User model and Groups.
<h5>Development Practices:</h5>
Version Control: Used Git for version control and collaboration.
Documentation: Provided clear API documentation and endpoints for ease of use and integration.
Testing: Implemented unit tests for API endpoints and functionality to ensure robustness.
Deployment:
Configured settings for deployment and ensured the project adheres to Django’s deployment checklist for a production environment.


