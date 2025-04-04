# Dictionaries
d = {
    "Bug": " an error in a program",
    "Function": "a code which can be called over and over again"
}

# retrieveing items form dictionary
print(d["Bug"])

d["Loop"] = "The action of doing something over and over again"
print(d)

# Create an empty dictionary
empty_dictonary = {}

# wipe an existing dictionary
programming_dict = {}
print(programming_dict)

# Edit an item in a dictionary
d["Bug"] = "an insect"

print(d["Bug"])

# Loop through the dictionary
for key in d:
    print(key)
    print(d[key])

# Nesting dictionary in a dictionary
capitals = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg"], "total_visits": 5},
}

# nesting dictionary in a list
travel_log = [
    {"country": "France",
     "Countries_visited": ["Paris", "Lille", "Dijon"]
     "total_visits": 12
     },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamsburg", "Stittgart"],
        "total_visis": 5,
    }
]
