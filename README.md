# REST API Event App

## DESCRIPTION: 

EventApp is a Django-based RESTful API designed for managing events such as conferences, meetups, workshops, and more. The API allows users to create, view, update, and delete events, while also supporting user registration for events. It is built using Django and Django REST Framework, providing an easy-to-use interface for managing event-related data and user interactions.

This project demonstrates how to build a fully functional REST API with user authentication, event management, and registration features. It also incorporates Docker for easy deployment.

## Key Features 💡

- **Event Management:** Create, view, update, and delete events such as conferences, workshops, and meetups.
- **User Registration & Authentication** Users can register, log in, and authenticate with JWT tokens for secure access to the API.
- **Event Registration:** Users can register for events, managing their participation.
- **CRUD Operations:** Standard CRUD functionality for event management, including event title, description, date, location, and organizer.
- **API Documentation:** Comprehensive API documentation available through the built-in interface (Swagger).
- **Email Notifications:** Sends email notifications to users upon successful event registration (Bonus feature).
- **Event Filtering/Search (Bonus feature):** Allows searching and filtering events based on date, location, and other parameters.


# Installation Guide 📕:

### Prerequisites 💻

Ensure you have Docker and Docker Compose installed on your machine. You can download them from:

- Docker: [Get Docker](https://docs.docker.com/get-docker/) 🐳
- Docker Compose: [Docker Compose](https://docs.docker.com/compose/install/) 🐳

### Environment Variables
Create a `.env` file in the root of your project directory with the following content:
```
    POSTGRES_DB=EventApp
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=12345

    SECRET_KEY=mysecretkey
    DEBUG=True
```


1. **Clone the repository:** ```git clone https://github.com/excommunicades/EventApp.git``` -> ```cd EventApp```
2. **Build and run the application with Docker Compose:** ```docker-compose up --build```

# Stopping the Services 🚪


**To stop all running services, you can use:** ```docker-compose down```

### API Endpoints

1. **Detailed API documentation can be found at:** ```http://127.0.0.1:8000/docs/```
2. **Detailed event search or filtering documentation can be found at:** ```EventApp\api_v1\api_actions\views\events_filters.py```


# Conclusion

EventApp provides a fully-featured environment for managing events with Django REST Framework and Docker. With basic event CRUD operations, user registration, and event registration features, it’s easy to get started with creating and managing events. Additional advanced features like email notifications and event search provide further functionality for enhancing the application.

## Authors 😎

- **Stepanenko Daniil** - "EventApp project"