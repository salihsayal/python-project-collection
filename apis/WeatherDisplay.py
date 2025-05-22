def displayWeather(response):
    print(f"Current weather in {response["address"]}")
    print(response["currentConditions"]["conditions"],response["currentConditions"]["temp"],"°C")
