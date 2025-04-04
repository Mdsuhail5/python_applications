import requests
from bs4 import BeautifulSoup
import re

# Get date input and construct URL
date = input(
    "Which year do you want to travel to? Type the date in format YYYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{date}"

# Get webpage content
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all song titles using the correct selector
song_names = soup.select("li ul li h3.c-title")
song_artists = soup.select("li ul li span.c-label")

# Create list of songs with their artists
songs_list = []
for i in range(len(song_names)):
    title = song_names[i].getText().strip()
    artist = song_artists[i].getText().strip()
    if title and artist:  # Only add if both title and artist exist
        songs_list.append(f"{title} - {artist}")

# Print all songs
print(f"\nBillboard Hot 100 for {date}")
print("-" * 50)
for i, song in enumerate(songs_list, 1):
    print(f"{i}. {song}")
