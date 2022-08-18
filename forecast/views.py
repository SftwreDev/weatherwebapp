import requests
import datetime
from django.views import View
from django.shortcuts import render, redirect


class ForecastView(View):
    template_name = 'forecast.html'
    API_KEY = "TADA2sbxjyRkN7YyI8POKwjKPWl5ZW0A"

    def get_location_key(self, city):
        """
        It takes a city name as an argument, makes a request to the AccuWeather API, and returns the
        location key for that city
        
        :param city: The city you want to get the weather for
        :return: The location key for the city that was passed in.
        """
        req = requests.get(f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey={self.API_KEY}&q={city}")
        response = req.json()

        return response[0]['Key']

    def get_forecast(self, city):
        """
        It takes a city name as an argument, gets the location key for that city, and then uses that key to
        get the 5 day forecast for that city
        
        :param city: The city you want to get the forecast for
        :return: A JSON object
        """
        city = self.get_location_key(city)
        req = requests.get(f"http://dataservice.accuweather.com/forecasts/v1/daily/5day/{city}?apikey={self.API_KEY}")
        return req.json()

    def get(self, request):        
        """
        If the user has searched for a city, then get the forecast for that city and set the search_forecast
        variable to True. Otherwise, set the forecast to None and set the search_forecast variable to False
        
        :param request: The request object is a Python object that contains all the information about the
        request that was sent to the server
        :return: The forecast is being returned.
        """
        location = request.GET.get('city')
        if location:
            forecast =  self.get_forecast(city=request.GET.get('city'))
            search_forecast = True
        else:
            forecast =  None
            search_forecast = False
        
        context = {
            "forecast" : forecast,
            "search_forecast" : search_forecast,
            "location" : location
        }
        return render(request, self.template_name, context)

