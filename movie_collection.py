class Movie:
    def __init__(self, title: str, genre: str, year: int):
        self.title = title
        self.genre = genre
        self.year = year

    def __repr__(self):
        return f'Фильм {self.title}, жанр {self.genre}, {self.year} года'

class MovieCollection:
    def __init__(self):
        self.movies: dict[str, Movie] = {}

    def add_movie(self, movie: Movie) -> None:
        if movie.title in self.movies:
            print(f'Фильм {movie.title} уже существует')
            return
        else:
            self.movies[movie.title] = movie
            print(f'Фильм {movie.title} добавлен')
            return

    def remove_movie(self, title: str) -> None:
        if title not in self.movies:
            print('Фильм не найден')
            return
        else:
            del self.movies[title]
            print(f'Фильм {title} удален')
            return

    def find_movie_title(self, title: str) -> list[Movie]:
        return [i for i in self.movies.values() if title in i.title]

    def find_movie_genre(self, genre: str) -> list[Movie]:
        return [i for i in self.movies.values() if genre in i.genre]

    def find_movie_year(self, year: int) -> list[Movie]:
        return [i for i in self.movies.values() if year == i.year]

    def __iter__(self) -> 'MovieIterator':
        return MovieIterator(list(self.movies.values()))


class MovieIterator:
    def __init__(self, movies):
        self._movies = list(movies)
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._movies):
            movie = self._movies[self._index]
            self._index += 1
            return movie
        else:
            raise StopIteration

collection = MovieCollection()