from faker import Faker
import random
import pytest

fake = Faker()

genres = ['комедия', 'драма', 'ужасы', 'фантастика', 'боевик', 'мелодрама', 'детектив', 'мистика', 'триллер']
word_count = random.randint(1, 5)

@pytest.fixture
def generate_valid_movie():
    return {
        "title": fake.sentence(nb_words=word_count).strip('.'),
        "genre": random.choice(genres),
        "year": random.randint(1895, 2025)
    }

@pytest.fixture
def generate_invalid_movie():
    invalid_data = [
        {"title": "", "genre": random.choice(genres), "year": random.randint(1895, 2025)},
        {"title": fake.sentence(), "genre": random.randint(100, 999), "year": fake.word()},
        {"title": None, "genre": random.choice(genres), "year": random.randint(1895, 2025)},
        {"title": fake.sentence(), "genre": random.choice(genres), "year": ""},
        {"title": fake.sentence(), "genre": random.choice(genres), "year": -2025},
    ]
    return random.choice(invalid_data)