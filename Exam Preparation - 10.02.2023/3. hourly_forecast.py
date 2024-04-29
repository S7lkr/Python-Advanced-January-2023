def forecast(*args):
    result = []
    weather_priority = ("Sunny", "Cloudy", "Rainy")

    for type_w in weather_priority:
        for city, weather in sorted(args):
            if weather == type_w:
                result.append(f"{city} - {weather}")
    return "\n".join(result)

# def forecast(*args):
#     result = []
#
#     def add_cities(type_of_city):
#         cities = []
#         for city, weather in args:
#             if weather == type_of_city:
#                 cities.append(city)
#         for town in sorted(cities):
#             result.append(f"{town} - {type_of_city}")
#     add_cities("Sunny")
#     add_cities("Cloudy")
#     add_cities("Rainy")
#
#     return "\n".join(result)


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))