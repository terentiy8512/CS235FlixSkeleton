import csv

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director


class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.dataset_of_movies = []
        self.dataset_of_actors = []
        self.dataset_of_directors = []
        self.dataset_of_genres = []

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)
            for row in movie_file_reader:
                title = row['Title']
                release_year = row['Year']
                actors = row['Actors']
                director = row['Director']
                genres = row['Genre']
                self.dataset_of_movies.append(Movie(title, int(release_year)))

                a_list = actors.split(",")
                for actor in a_list:
                    if Actor(actor.strip()) not in self.dataset_of_actors:
                        self.dataset_of_actors.append(Actor(actor.strip()))

                if Director(director.strip()) not in self.dataset_of_directors:
                    self.dataset_of_directors.append(Director(director.strip()))

                a_list = genres.split(",")
                for genre in a_list:
                    if Genre(genre.strip()) not in self.dataset_of_genres:
                        self.dataset_of_genres.append(Genre(genre.strip()))
