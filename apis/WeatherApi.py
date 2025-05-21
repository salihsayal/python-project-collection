#!/usr/bin/env python3

from dotenv import load_dotenv
import os
import sys
import requests

load_dotenv()
api_key = os.getenv("WEATHER_API_KEY")
url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{0}%20{1}?unitGroup=us&key={2}&contentType=json'

def fetchWeatherData(country, city):
    try:
        res = requests.get(url.format(country, city, api_key))
        res.raise_for_status()
        response = res.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {res}")
        sys.exit(1)

    return response
	
