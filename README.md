# Movie Class with TMDB API Integration

A Python class for representing movies, with the ability to fetch movie details from the TMDB (The Movie Database) API.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [How to Use](#how-to-use)
- [Example](#example)
- [License](#license)

## Introduction

This Python class, `Movie`, is designed to represent movies with various attributes such as title, year, director, genre, rating, description, image, and trailer. It also allows you to interact with the TMDB API to fetch additional movie details including genre, rating, description, image, and trailer.

## Features

- Create and store movie details.
- Fetch additional movie details from the TMDB API.
- Retrieve the movie trailer from the TMDB API.

## Requirements

To use the `Movie` class with TMDB API integration, you need the following:

- Python 3.x
- `requests` library (you can install it using `pip`)

## How to Use

1. Import the `Movie` class into your Python script.

2. Initialize a `Movie` object with the following parameters:
   - `title`: Movie title.
   - `year`: Release year.
   - `director`: Director's name.
   - `genre`: Initial genre information (can be updated with TMDB data).
   - `rating`: Initial rating information (can be updated with TMDB data).
   - `description`: Initial movie description (can be updated with TMDB data).
   - `image`: Initial movie image URL (can be updated with TMDB data).
   - `trailer`: Initial movie trailer URL (can be updated with TMDB data).
   - `tmdb_api_key`: Your TMDB API key.

3. Use the `fetch_movie_details` method to fetch movie details from the TMDB API.

4. Use the `fetch_movie_trailer` method to fetch the movie trailer URL from the TMDB API.

5. You can also use the `jsonDump` and `jsonLoad` methods to save and load movie data as JSON files.

## Example

Here's an example of how to use the `Movie` class with TMDB API integration:

```python
from movie import Movie

# Initialize a Movie object with your TMDB API key
tmdb_api_key = "YOUR_TMDB_API_KEY"
my_movie = Movie("Inception", "2010", "Christopher Nolan", "Action, Sci-Fi", 0.0, "A dream within a dream...", "", "", tmdb_api_key)

# Fetch additional movie details from TMDB
my_movie.fetch_movie_details()
print(my_movie)

# Fetch the movie trailer
trailer_url = my_movie.fetch_movie_trailer()
print("Trailer URL:", trailer_url)


```



## LICENSE

   
You should include this content in a file named `README.md` in your project's root directory, and it will be displayed as the project's documentation on platforms like GitHub.
