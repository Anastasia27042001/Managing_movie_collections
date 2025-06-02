import pytest
from movie_collection import *
from command_line import *
from test_fixtures import *

def test_add_valid_movie():
    valid_movie = generate_valid_movie()
    result = collection.add_movie(Movie(**valid_movie))

    assert result is True
    assert valid_movie["title"] in collection.movies


def test_add_invalid_movie():
    collection = MovieCollection()
    invalid_movie = generate_invalid_movie()

    try:
        collection.add_movie(Movie(**invalid_movie))
    except ValueError as e:
        assert str(e) == 'Некорректные данные'
    else:
        assert False, 'Ожидалось исключение ValueError'