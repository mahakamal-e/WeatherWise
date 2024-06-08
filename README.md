# ALX Portfolio Project - WeatherWise
![Project Logo](https://github.com/mahakamal-e/WeatherWise/raw/main/app/static/images/icone2.png)
## Introduction
WeatherWise is a portfolio project developed in the ALX Software Engineering Program. The web application provides users with current weather information and forecasts based on their location input or city name. The project utilizes Flask, SQLAlchemy, and the OpenWeatherMap API.

## Landing Page

**[Visit WeatherWise](https://mahakamal-e.github.io)**

**[Final Project Blog Article](link_to_your_final_project_blog_article)**

**Author:** [Maha Kamal]([author_link_to_LinkedIn](https://www.linkedin.com/in/maha-kamal-el/))

## Usage

WeatherWise offers a user-friendly interface for accessing weather information. Users can:

- View current weather conditions
- Check weather forecasts for the upcoming days
- Search for weather data based on their location or city name

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

## Contributing

If you would like to contribute to WeatherWise, please follow these guidelines:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.

## Screenshots
### Current Weather
![Current Weather](https://github.com/mahakamal-e/WeatherWise/raw/main/app/static/images/current_weather.png)
*Description: Display current weather conditions, including temperature, humidity, and wind speed, for a selected location.*

### Forecast
![Forecast](https://github.com/mahakamal-e/WeatherWise/raw/main/app/static/images/forecast.png)
*Description: Forecast section showing the upcoming weather predictions for the next few days, helping users plan.*

### Blog Section
![Blog Section](https://github.com/mahakamal-e/WeatherWise/raw/main/app/static/images/blog_section.png)
*Description: The blog section of WeatherWise provides users with a wealth of information and resources to enhance their weather-related knowledge and travel experiences.*

## Live Demo
[![Video Title](https://img.youtube.com/vi/0RSU9IcWSHo/0.jpg)](https://youtu.be/0RSU9IcWSHo)



## Project Story

WeatherWise was born out of my passion for weather tracking and my desire to create a user-friendly application for accessing weather data. Inspired by the challenges of accurately predicting weather patterns, I developed a tool that simplifies obtaining weather information while providing valuable insights into current conditions and forecasts.

In the development process, I faced numerous technical challenges, particularly in integrating with the OpenWeatherMap API and designing an intuitive user interface. However, with perseverance and problem-solving skills, I overcame these obstacles and successfully built WeatherWise from the ground up.

Looking ahead, I plan to add more weather metrics and better data visualization to WeatherWise. By continually improving the app, I aim to make it an essential tool for users to stay informed about important weather conditions.

## Related Projects
[OpenWeatherMap](https://openweathermap.org/) - OpenWeatherMap is a service that provides weather data, including current weather, forecasts, and historical data,
to developers and businesses through an API.
It offers a wide range of weather-related information that can be integrated into applications like WeatherWise to enhance functionality.

## Licensing
MIT License

Copyright (c) [2024] [WeatherWise]
