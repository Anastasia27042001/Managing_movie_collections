class Movie:
    def __init__(self, id: int, title: str, genre: str, year: int):
        self.id = id
        self.title = title
        self.genre = genre
        self.year = year

class MovieCollection:
    def __init__(self):
        self.movies = {}

    def add_movie(self, movie: Movie) -> bool:
        if movie not in self.movies:

    def remove_movie(self, movie: Movie) -> bool:

    def find_movie(self, title: str) -> Movie:

movie_collection = MovieCollection()

class MovieIterator:
    def __init__(self, collection: movie_collection):
        self.collection = collection