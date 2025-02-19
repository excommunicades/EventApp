# REST API Event App

## DESCRIPTION: 

Event App is a Django-based RESTful API designed for managing events such as conferences, meetups, workshops, and more. The API allows users to create, view, update, and delete events, while also supporting user registration for events. It is built using Django and Django REST Framework, providing an easy-to-use interface for managing event-related data and user interactions.

This project demonstrates how to build a fully functional REST API with user authentication, event management, and registration features. It also incorporates Docker for easy deployment.

## Key Features 💡

- **Event Management:** Create, view, update, and delete events such as conferences, workshops, and meetups.
- **User Registration & Authentication** Users can register, log in, and authenticate with JWT tokens for secure access to the API.
- **Event Registration:** Users can register for events, managing their participation.
- **CRUD Operations:** Standard CRUD functionality for event management, including event title, description, date, location, and organizer.
- **API Documentation:** Comprehensive API documentation available through the built-in interface (Swagger).
- **Email Notifications (Bonus feature):** Sends email notifications to users after successful event registration or cancellation.
- **Event Filtering/Search (Bonus feature):** Allows searching and filtering events based on date, location, and other parameters.
- **API Testing (Additional feature):** Comprehensive test suite to ensure the functionality and stability of the API.
- **Django Admin Interface:** Fully integrated Django Admin panel for easy event and registration management.
- **SuperUser Creation on Container Startup:** A superuser is automatically created when the container is launched, enabling immediate access to the Django admin interface.

**SuperUser data:**
```
username='admin',
email='admin@example.com',
password='password'
```


# Installation Guide 📕:

### Prerequisites 💻

Ensure you have Docker and Docker Compose installed on your machine. You can download them from:

- Docker: [Get Docker](https://docs.docker.com/get-docker/) 🐳
- Docker Compose: [Docker Compose](https://docs.docker.com/compose/install/) 🐳

### Environment Variables
Create a `.env` file in the root of your project directory with the following content:
```
# Database Settings

POSTGRES_DB=EventApp
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password

# Django Settings

SECRET_KEY=mysecretkey
DEBUG=True
```
If you want to send real emails (for example, using Gmail), add the following lines to your .env file:

**In EventApp/settings file you need to comment 164 line and uncomment lines from 169 to 174**
```
# Email settings

BACKEND=django.core.mail.backends.smtp.EmailBackend
HOST=smtp.gmail.com
PORT=587
USE_TLS=True
HOST_USER=your-email@gmail.com
HOST_APP_PASSWORD=your-email-app-password
```

1. **Clone the repository:** ```git clone https://github.com/excommunicades/EventApp.git``` -> ```cd EventApp```
2. **Build and run the application with Docker Compose:** ```docker-compose up --build```

# Stopping the Services 🚪


**To stop all running services, you can use:** ```docker-compose down```

# API Endpoints

1. **Detailed API documentation can be found at:** ```http://0.0.0.0:8000/swagger/```
2. **Download API schema can be found at:** ```http://0.0.0.0:8000/schema/```
3. **Detailed event search or filtering documentation can be found at:** ```EventApp\api_v1\api_actions\views\events_filters.py```

# Running Tests ♻️

You can use the test service defined in the docker-compose.yml file. This service will build the image and execute the tests in an isolated environment.

**Execute the tests:** ```docker-compose run test```


# Conclusion

Event App provides a fully-featured environment for managing events with Django REST Framework and Docker. With basic event CRUD operations, user registration, and event registration features, it’s easy to get started with creating and managing events. Additional advanced features like email notifications and event search provide further functionality for enhancing the application.

## Authors 😎

- **Stepanenko Daniil** - "EventApp project"