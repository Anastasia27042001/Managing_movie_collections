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

    def add_movie(self, movie: Movie) -> bool:
        if movie.title in self.movies:
            print(f'Фильм {movie.title} уже существует')
            return False
        else:
            self.movies[movie.title] = movie
            print(f'Фильм {movie.title} добавлен')
            return True

    def remove_movie(self, title: str) -> bool:
        if title not in self.movies:
            print('Фильм не найден')
            return False
        else:
            del self.movies[title]
            print(f'Фильм {title} удален')
            return True

    def find_movie_title(self, title: str) -> list[Movie]:
        result = [i for i in self.movies.values() if title in i.title]
        print(result)
        return result

    def find_movie_genre(self, genre: str) -> list[Movie]:
        result = [i for i in self.movies.values() if genre in i.genre]
        print(result)
        return result

    def find_movie_year(self, year: int) -> list[Movie]:
        result = [i for i in self.movies.values() if year == i.year]
        print(result)
        return result

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