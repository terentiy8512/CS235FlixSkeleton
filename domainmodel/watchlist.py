from domainmodel.movie import Movie


class WatchList:
    def __init__(self):
        self.watch_list = []
        self.index = 0

    def add_movie(self, movie: Movie):
        if movie not in self.watch_list:
            self.watch_list.append(movie)

    def remove_movie(self, movie: Movie):
        if movie in self.watch_list:
            index = self.watch_list.index(movie)
            self.watch_list.pop(index)

    def select_movie_to_watch(self, index):
        try:
            return self.watch_list[index]
        except:
            return None

    def size(self):
        return len(self.watch_list)

    def first_movie_in_watchlist(self):
        if len(self.watch_list) < 1:
            return None
        else:
            return self.watch_list[0]

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if len(self.watch_list) > self.index:
            return self.watch_list[self.index]
        else:
            raise StopIteration

    def __repr__(self):
        return "<WatchList {}>".format(self.watch_list)

    def __eq__(self, other):
        return self.watch_list == other.watch_list


class TestWatchListMethods:
    def test_init(self):
        # test 1                                                # Size of watchlist: 0
        watchlist = WatchList()                                 # <Movie Moana, 2016>
        print(f"Size of watchlist: {watchlist.size()}")
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Ice Age", 2002))
        watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
        print(watchlist.first_movie_in_watchlist())
        # test 2                                                # Size of watchlist: 1
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        print(f"Size of watchlist: {watchlist.size()}")
        # test 3                                                # Size of watchlist: 1
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Moana", 2016))
        print(f"Size of watchlist: {watchlist.size()}")
        # test 4                                                # Size of watchlist: 1
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.remove_movie(Movie("Lorean", 2015))
        print(f"Size of watchlist: {watchlist.size()}")
        # test 5                                                # Size of watchlist: 0
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.remove_movie(Movie("Moana", 2016))
        print(f"Size of watchlist: {watchlist.size()}")
        # test 6                                                # <Movie Moana, 2016>
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        # test 7                                                # None
        watchlist = WatchList()
        watchlist.add_movie(Movie("Moana", 2016))
        print(watchlist.select_movie_to_watch(1))
        # test 8                                                # <Movie Moana, 2016>
        watchlist = WatchList()                                 # <Movie Moana1, 2011>
        watchlist.add_movie(Movie("Moana", 2016))
        watchlist.add_movie(Movie("Moana1", 2011))
        for item in watchlist:
            print(item)

        print(watchlist)

f = TestWatchListMethods()
f.test_init()