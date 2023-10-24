import json
from dotenv import load_dotenv
import os
import requests

class Movie:
    def __init__(self, title, year, director, genre, rating, description, image, trailer) -> None:
        self.title = title
        self.year = year
        self.director = director
        self.genre = genre
        self.rating = rating
        self.description = description
        self.image = image
        self.trailer = trailer
        self.tmdb_api_key = os.getenv("TMDB_API_KEY")
        self.fetch_movie_details()
        self.fetch_movie_trailer()
        self.jsonDump()
        
    def __dict__(self) -> dict:
        return {
            "title": self.title,
            "year": self.year,
            "director": self.director,
            "genre": self.genre,
            "rating": self.rating,
            "description": self.description,
            "image": self.image,
            "trailer": self.trailer,
        }

    def __str__(self) -> str:
        return f"{self.title} ({self.year}) - {self.director} - {self.genre} - {self.rating} - {self.description} - {self.image} - {self.trailer}"

    def jsonDump(self):
        jsonTemp = json.dumps(self.__dict__() , indent=4)
        with open(f"{self.title}.json", "w") as f:
            f.write(jsonTemp)
        print("JSON file created successfully")

    def fetch_movie_details(self):
        # Define the base URL and endpoint for TMDB API
        base_url = "https://api.themoviedb.org/3"
        endpoint = "/search/movie"

        # Prepare the query parameters
        params = {
            "api_key": self.tmdb_api_key,
            "query": self.title,
            "year": self.year,
        }

        # Make the API request
        response = requests.get(base_url + endpoint, params=params)

        if response.status_code == 200:
            data = response.json()

            if data.get("results"):
                # Assuming the first result is the desired movie
                movie_data = data["results"][0]

                # Update movie details with data from TMDB
                self.title = movie_data.get("title", self.title)
                self.year = movie_data.get("release_date", "")[:4]
                self.genre = ", ".join([genre["name"] for genre in movie_data.get("genres", [])])
                self.rating = movie_data.get("vote_average", 0.0)
                self.description = movie_data.get("overview", "")
                self.image = f"https://image.tmdb.org/t/p/w500{movie_data.get('poster_path', '')}"
            else:
                print("Movie not found on TMDB.")
        else:
            print("Error fetching data from TMDB API.")

    def fetch_movie_trailer(self):
        # Define the endpoint for fetching movie videos from TMDB
        endpoint = f"/movie/{self.title}/videos"
        base_url = "https://api.themoviedb.org/3"

        # Make the API request
        params = {"api_key": self.tmdb_api_key}
        response = requests.get(base_url + endpoint, params=params)

        if response.status_code == 200:
            data = response.json()

            if data.get("results"):
                # Assuming the first result is the trailer
                trailer_key = data["results"][0]["key"]
                self.trailer = f"https://www.youtube.com/watch?v={trailer_key}"
            else:
                self.trailer = "Trailer not available."
        else:
            self.trailer = "Trailer not available."

if __name__ == "__main__":
    load_dotenv()  # Load environment variables from .env
    movie1 = Movie("goodfellas", "1990", "Martin Scorsese", "", "", "", "", "")

    print(movie1.__str__())
