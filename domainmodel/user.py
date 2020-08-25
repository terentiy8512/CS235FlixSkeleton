from domainmodel.movie import Movie
from domainmodel.review import Review


class User:
    def __init__(self, user_name="", password=""):
        if user_name != "" and type(user_name) is str:
            self.user_name = user_name.lower().strip()
        else:
            self.user_name = None
        if password != "" and type(password) is str:
            self.password = password
        else:
            self.password = None
        self.watched_movies = []
        self.reviews = []
        self.time_spent_watching_movies_minutes = int()

    def __repr__(self):
        return "<User {}>".format(self.user_name)

    def __eq__(self, other):
        return str(self.user_name) == str(other.user_name)

    def __lt__(self, other):
        return str(self.user_name) < str(other.user_name)

    def __hash__(self):
        return hash(self.user_name)

    def watch_movie(self, movie):
        if movie not in self.watched_movies:
            self.watched_movies.append(movie)
        self.time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        if review not in self.reviews:
            self.reviews.append(review)





