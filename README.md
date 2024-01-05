# Django-Marketplace-Sample

This is a simple online marketplace project where users can buy and sell items. The project includes features like authentication, communication between users, a dashboard for managing items, form handling, and more.

## Features

- User Authentication: Users can register, log in, and log out.
- Communication: Users can communicate with each other.
- Dashboard: Users have a dashboard to manage their items.
- Form Handling: Customized forms for adding and managing items.

## Installation

Follow these steps to clone and run the project:

1. Clone the repository:

    ```bash
    git clone https://github.com/laslande24/Django-Marketplace-Sample.git
    cd Django-Marketplace-Sample
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser for admin access:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Access the application at [http://localhost:8000/](http://localhost:8000/)

## Usage

- Log in or register as a new user.
- Explore or create items on the marketplace.
- Add your items to sell.
- Communicate with other users.
- Manage your items using the dashboard.

## License

This project is licensed free
