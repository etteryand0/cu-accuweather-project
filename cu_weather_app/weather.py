def check_bad_weather(temperature, wind_speed, precipitation_probability, humidity, pressure):
    if (temperature < 0 or temperature > 35 or
        wind_speed > 50 or
        precipitation_probability > 70 or
        humidity > 90 or
        pressure < 1000):
        return "Плохие погодные условия"
    else:
        return "Хорошие погодные условия"