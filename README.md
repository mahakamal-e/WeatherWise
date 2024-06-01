# ALX Portfolio Project - WeatherWise
![Project Logo](https://github.com/mahakamal-e/WeatherWise/raw/main/app/static/images/icone2.png)
## Introduction
WeatherWise is a portfolio project developed as part of the ALX Software Engineering Program. It is a web application that provides users with current weather information and forecasts based on their location input or city name. The project utilizes Flask, SQLAlchemy, and the OpenWeatherMap API.

## Landing Page
[](https://mahakamal-e.github.io/)
## Technologies Used
The following technologies were used in building WeatherWise:

- **Python 3:** Programming language used for backend development.
- **Flask:** Micro web framework used for building the web application.
- **SQLAlchemy:** Python SQL toolkit and Object-Relational Mapping (ORM) library used for database management.
- **SQLite:** Lightweight relational database management system used for storing weather data.
- **OpenWeatherMap API:** External API used to retrieve weather data based on user input.
- **HTML/CSS:** Used for frontend development and styling of web pages.
- **JavaScript:** Used for dynamic interaction and AJAX requests in the frontend.

## Project Structure
The project is structured into several modules:

| Module           | Description                                                                    |
|------------------|--------------------------------------------------------------------------------|
| `app`            | Main package containing the Flask application and related configurations.      |
| `app.config`     | Configuration settings for the Flask application.                               |
| `app.database`   | Database configuration and session management setup using SQLAlchemy.           |
| `app.init_db`    | Initialization script for creating and populating the database with default data.|
| `app.models`     | Database models defined using SQLAlchemy ORM.                                   |
| `app.routes.blog`| Blueprint containing routes for blog-related functionalities.                  |
| `app.routes.main`| Blueprint containing routes for the main functionalities of the application.   |
| `app.app_setup`| Module responsible for creating and configuring the Flask application instance.   |
## Routes and Explanations
The application has the following main routes and functionalities:

### Blog Routes (`app/routes/blog.py`)
| Route             | Description                                                                        |
|-------------------|------------------------------------------------------------------------------------|
| `/blog`           | Renders the blog page and handles AJAX requests for fetching articles by category.|
| `/blog/fetch_articles`| Handles AJAX requests for fetching articles based on category ID.                 |
| `/blog/article/<int:article_id>` | Renders a specific article based on the article ID.                            |

### Main Routes (`app/routes/main.py`)
| Route             | Description                                                                        |
|-------------------|------------------------------------------------------------------------------------|
| `/`               | Main route that fetches current weather and forecast data based on user input.      |
| `/about`          | Route to render the 'About' page.                                                  |

## How to Run Locally
To run the WeatherWise application locally, follow these steps:

1. Clone the project repository from GitHub.
2. Navigate to the project directory.
3. Create a virtual environment and activate it.
4. Install the required dependencies using `pip install -r requirements.txt`.
5. Run the Flask application with `python run.py`.
6. Access the application in your web browser at `http://localhost:5000/`.

## Contributors
- [Maha Kamal](https://github.com/mahakamal-e)
