#!/usr/bin/env python3
"""
This module contains routes for the main functionalities of the application.
"""
from flask import Blueprint, render_template, request, jsonify
from datetime import datetime, timedelta
import requests

main_bp = Blueprint('main', __name__)


api_key = 'dc6cdfbeb6fa16620f51097e7e16aeeb'
@main_bp.route('/', methods=['GET', 'POST'])
def index():
    """
    Main route that handles both GET and POST requests. Fetches current weather 
    and forecast data based on user input. If no input is provided, it defaults 
    to Cairo.
    """
    
    city_name = 'Cairo' 
    error_message = None
    current_weather = None
    forecast = None

    if request.method == 'POST':
        if 'latitude' in request.form and 'longitude' in request.form:
            latitude = request.form.get('latitude')
            longitude = request.form.get('longitude')
            current_weather_url = (
                f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}'
                f'&lon={longitude}&units=metric&appid={api_key}'
            )
            forecast_url = (
                f'http://api.openweathermap.org/data/2.5/forecast?lat={latitude}'
                f'&lon={longitude}&units=metric&appid={api_key}'
            )
        else:
            city_name = request.form.get('city', '').strip()
            if not city_name:
                error_message = "Please enter a city name."
                return render_template('index.html', error_message=error_message)
            current_weather_url = (
                f'http://api.openweathermap.org/data/2.5/weather?q={city_name}'
                f'&units=metric&appid={api_key}'
            )
            forecast_url = (
                f'http://api.openweathermap.org/data/2.5/forecast?q={city_name}'
                f'&units=metric&appid={api_key}'
            )
    else:
        current_weather_url = (
            f'http://api.openweathermap.org/data/2.5/weather?q={city_name}'
            f'&units=metric&appid={api_key}'
        )
        forecast_url = (
            f'http://api.openweathermap.org/data/2.5/forecast?q={city_name}'
            f'&units=metric&appid={api_key}'
        )

    current_weather_response = requests.get(current_weather_url).json()
    forecast_response = requests.get(forecast_url).json()

    if (current_weather_response.get('cod') != 200 or 
            forecast_response.get('cod') != '200'):
        error_message = current_weather_response.get(
            'message', 'City not found.'
        )
        return render_template('index.html', error_message=error_message)

    current_weather = {
        'city': current_weather_response['name'],
        'temp': current_weather_response['main']['temp'],
        'description': current_weather_response['weather'][0]['description'],
        'icon': current_weather_response['weather'][0]['icon'],
        'humidity': current_weather_response['main']['humidity'],
        'wind_speed': current_weather_response['wind']['speed'],
        'lat': current_weather_response['coord']['lat'],
        'lon': current_weather_response['coord']['lon'],
    }

    forecast = []
    for item in forecast_response['list']:
        date = item['dt_txt'].split(' ')[0]
        time = item['dt_txt'].split(' ')[1]
        temp = item['main']['temp']
        if time == '12:00:00':
            day_name = datetime.strptime(date, '%Y-%m-%d').strftime('%A')
            temp_low = temp
            temp_high = temp
            for hour_item in forecast_response['list']:
                hour_time = hour_item['dt_txt'].split(' ')[1]
                if (hour_time != '12:00:00' and 
                        hour_item['dt_txt'].split(' ')[0] == date):
                    hour_temp = hour_item['main']['temp']
                    if hour_temp < temp_low:
                        temp_low = hour_temp
                    elif hour_temp > temp_high:
                        temp_high = hour_temp
            forecast.append({
                'day_name': day_name,
                'temp_low': temp_low,
                'temp_high': temp_high,
                'icon': item['weather'][0]['icon']
            })

    current_date = datetime.now().strftime('%Y-%m-%d')
    tomorrow_date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')

    combined_hourly_forecast = []
    for hour in forecast_response['list']:
        hour_time = hour['dt_txt'].split(' ')[1]
        formatted_time = datetime.strptime(hour_time, '%H:%M:%S').strftime(
            '%I:%M %p'
        )
        hour['formatted_time'] = formatted_time
        combined_hourly_forecast.append(hour)

    hourly_forecast_today = [
        hour for hour in combined_hourly_forecast 
        if hour['dt_txt'].startswith(current_date)
    ]
    hourly_forecast_tomorrow = [
        hour for hour in combined_hourly_forecast 
        if hour['dt_txt'].startswith(tomorrow_date)
    ]
    hourly_forecast_new = hourly_forecast_today + hourly_forecast_tomorrow

    return render_template(
        'index.html', 
        current_weather=current_weather, 
        forecast=forecast, 
        hourly_forecast_new=hourly_forecast_new
    )

@main_bp.route('/about')
def about():
    """Route to render the 'About' page."""
    return render_template('about.html')
