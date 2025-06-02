import pytest
from movie_collection import *
from test_fixtures import *

@pytest.fixture
def collection():
    return MovieCollection()


def test_add_valid_movie(collection, generate_valid_movie):
    movie_data = generate_valid_movie
    movie = Movie(**movie_data)
    result = collection.add_movie(movie)

    assert result is True
    assert movie.title in collection.movies


def test_add_invalid_movie(collection, generate_invalid_movie):
    movie_data = generate_invalid_movie
    with pytest.raises(ValueError):
        Movie(**movie_data)


def test_add_duplicate_movie(collection, generate_valid_movie):
    movie_data = generate_valid_movie
    movie1 = Movie(**movie_data)
    movie2 = Movie(**movie_data)

    collection.add_movie(movie1)
    result = collection.add_movie(movie2)

    assert result is False
    assert len(collection.movies) == 1


def test_remove_existing_movie(collection, generate_valid_movie):
    movie_data = generate_valid_movie
    movie = Movie(**movie_data)
    collection.add_movie(movie)

    removed = collection.remove_movie(movie.title)
    assert removed is True
    assert movie.title not in collection.movies


def test_find_by_title(collection, generate_valid_movie):
    movie_data = generate_valid_movie
    movie = Movie(**movie_data)
    collection.add_movie(movie)

    results = collection.find_by_title(movie.title[:3])
    assert len(results) >= 1
    assert movie in results


def test_find_by_genre(collection, generate_valid_movie):
    movie_data = generate_valid_movie
    movie = Movie(**movie_data)
    collection.add_movie(movie)

    results = collection.find_by_genre(movie.genre)
    assert all(m.genre == movie.genre for m in results)


def test_find_by_year(collection, generate_valid_movie):
    movie_data = generate_valid_movie
    movie = Movie(**movie_data)
    collection.add_movie(movie)

    results = collection.find_by_year(movie.year)
    assert all(m.year == movie.year for m in results)