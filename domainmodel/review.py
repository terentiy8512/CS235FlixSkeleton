from datetime import datetime
from domainmodel.movie import Movie


class Review:
    def __init__(self, movie=Movie(), review_text="", rating=int()):
        if type(rating) == int and rating >= 1 and rating <= 10:
            self.rating = rating
        else:
            self.rating = None
        self.movie = movie
        self.review_text = review_text.strip()
        self.timestamp = datetime.today()

    def __repr__(self):
        return "{}, Review: {}, Rating: {}, Time: {}".format(str(self.movie), str(self.review_text), str(self.rating),
                                                             str(self.timestamp))

    def __eq__(self, other):
        string1 = str(self.movie) + self.review_text + str(self.rating) + str(self.timestamp)
        string2 = str(other.movie) + other.review_text + str(other.rating) + str(other.timestamp)
        return string1 == string2



