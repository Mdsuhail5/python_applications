travel_log = [
    {"country": "France",
     "Countries_visited": ["Paris", "Lille", "Dijon"],
     "total_visits": 12
     },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamsburg", "Stittgart"],
        "total_visis": 5,
    }
]


def add_new_country(country, no, cities):
    new_country = {}
    new_country["country"] = country
    new_country["cities_visited"] = no
    new_country["total_visits"] = cities
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersbug"])
print(travel_log)
