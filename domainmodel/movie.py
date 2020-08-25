from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director


class Movie:
    def __init__(self, title="", release_year=int()):
        if title != "" and type(title) == str:
            self.__title = title.strip()
        if release_year >= 1900:
            self.__release_year = release_year
        self.__description = ""
        self.director = Director()
        self.actors = []
        self.genres = []
        self.runtime_minutes = int()

    def __setattr__(self, key, value):
        self.__dict__[key] = value
        if 'description' in self.__dict__:
            self.__dict__['description'] = self.__dict__['description'].strip()
        if 'runtime_minutes' in self.__dict__:
            if self.__dict__['runtime_minutes'] < 0:
                raise ValueError("Constraint: the runtime is a positive number")

    def __repr__(self):
        return "<Movie {}, {}>".format(self.__title, self.__release_year)

    def __eq__(self, other):
        string1 = self.__title + str(self.__release_year)
        string2 = other.__title + str(other.__release_year)
        return string1 == string2

    def __lt__(self, other):
        string1 = self.__title + str(self.__release_year)
        string2 = other.__title + str(other.__release_year)
        return string1 < string2

    def __hash__(self):
        string = self.__title + str(self.__release_year)
        return hash(string)

    def add_actor(self, actor: Actor):
        self.actors.append(actor)

    def remove_actor(self, actor: Actor):
        if actor in self.actors:
            index = self.actors.index(actor)
            if index != -1:
                self.actors.pop(index)

    def add_genre(self, genre: Genre):
        self.genres.append(genre)

    def remove_genre(self, genre: Genre):
        if genre in self.genres:
            index = self.genres.index(genre)
            if index != -1:
                self.genres.pop(index)


