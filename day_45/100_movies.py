import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Get webpage content
response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

# Find all movie titles (looking for h2 tags)
all_movies = soup.find_all("h2")

# Extract and clean movie titles
movie_titles = []
for movie in all_movies:
    title = movie.getText().strip()
    if title:  # Only add non-empty titles
        movie_titles.append(title)

# Reverse list to get correct order (1 to 100)
movies_in_order = movie_titles[::-1]

# Print all movies
for movie in movies_in_order:
    print(movie)

# Optional: Save to file
with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movies_in_order:
        file.write(f"{movie}\n")
