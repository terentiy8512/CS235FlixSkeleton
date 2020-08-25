from domainmodel.movie import Movie
from domainmodel.user import User
from domainmodel.review import Review


class MovieWatchingSimulation:
    def __init__(self, movie: Movie):
        self.__movie = movie
        self.users = []
        self.reviews = []

    def __repr__(self):
        if len(self.reviews) == 1 and len(self.users) == 1:
            return "{} have {} review and has been watched by {} user.".format(self.__movie, len(self.reviews), len(self.users))
        elif len(self.reviews) == 1 and len(self.users) != 1:
            return "{} have {} review and has been watched by {} users.".format(self.__movie, len(self.reviews), len(self.users))
        elif len(self.reviews) != 1 and len(self.users) == 1:
            return "{} have {} reviews and has been watched by {} user.".format(self.__movie, len(self.reviews),
                                                                                len(self.users))
        else:
            return "{} have {} reviews and has been watched by {} users.".format(self.__movie, len(self.reviews),
                                                                                len(self.users))

    def how_many_users_watched(self):
        return len(self.users)

    def how_many_reviews(self):
        return len(self.reviews)

    def watch_movie(self, user: User):
        self.users.append(user)

    def add_review(self, user: User, review: Review):
        if user in self.users:
            self.reviews.append(review)

    def remove_review_from_the_movie(self, user: User, review: Review):
        if user in self.users and review in self.reviews:
            index = self.reviews.index(review)
            self.reviews.pop(index)


class TestMovieWatchSimulation:
    def test_init(self):
        movie = Movie("Moana", 2016)
        user1 = User("terentiy8512", "12345")
        user2 = User("xabib", "123")
        user3 = User("undercop", "12345678")
        review1 = Review(movie, "This movie was very enjoyable.", 8)
        review2 = Review(movie, "Not really impressed", 4)
        review3 = Review(movie, "Loved it", 10)
        simulation = MovieWatchingSimulation(movie)

        # test 1                                  # <Movie Moana, 2016> have 0 reviews and has been watched by 0 users.
        simulation.add_review(user1, review1)
        print(simulation)

        # test 2                                  # <Movie Moana, 2016> have 0 reviews and has been watched by 0 users.
        simulation.remove_review_from_the_movie(user1, review1)
        print(simulation)

        # test 3                                 # <Movie Moana, 2016> have 0 reviews and has been watched by 1 user.
        simulation.watch_movie(user1)
        print(simulation)

        # test 4                                 # <Movie Moana, 2016> have 1 review and has been watched by 1 user.
        simulation.add_review(user1, review1)
        print(simulation)

        # test 5                                # <Movie Moana, 2016> have 1 review and has been watched by 1 user.
        simulation.add_review(user2, review2)
        print(simulation)

        # test 6                                # <Movie Moana, 2016> have 1 review and has been watched by 2 users.
        simulation.watch_movie(user2)
        print(simulation)

        # test 7
        simulation.watch_movie(user3)
        simulation.add_review(user3, review2)   # <Movie Moana, 2016> have 2 reviews and has been watched by 3 users.
        print(simulation)

        # test 8
        simulation.remove_review_from_the_movie(user3, review2)
        print(simulation)                       # <Movie Moana, 2016> have 1 review and has been watched by 3 users.


test = TestMovieWatchSimulation()
test.test_init()
