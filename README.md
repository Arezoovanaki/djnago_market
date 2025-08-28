# Market Project (Django)

> ⚠️ *Note:* This project is still under development and is not complete. It is created for practice and learning purposes.

## Project Overview
This is a simple online store built with Django.  
The main goal of this project is to practice Django, HTML, CSS, and basic web development concepts.

### Existing Features
- Simple homepage displaying products
- Pages: About Us, Login, Sign Up, Logout
- Admin panel to manage products and categories
- Product details include:
  - Description
  - Star rating
  - Discounts
- Manage categories and view products in each category

### Features Not Yet Completed
- Sorting products by category on the homepage
- Consistent product image sizes
- Full CSS styling and design
- Advanced store features (shopping cart, checkout, etc.)

## Installation and Running
1. Clone the project to your local machine:
   
   ```bash
   git clone https://github.com/Arezoovanaki/djnago_market.git
   cd django_market
   ```
2.	Create and activate a virtual environment:
	
  - On Linux | macOS
    ```bash
    python -m venv env
    source env/bin/activate
      ```
  - On Windows
    ```bash
    python -m venv env
    env\Scripts\activate 
      ```
3. Install the dependencies:
   
    ```bash
    pip install -r requirements.txt
   ```
4.	Run database migrations:
	
    ```bash
    python manage.py migrate
    ```
5.	Create superuser (for Django admin):
   
    ```bash
    python manage.py createsuperuser
    ```
6.	Run the development server:
   
    ```bash
    python manage.py runserver
    ```
