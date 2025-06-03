def validate_title(title):
    if not isinstance(title, str):
        raise TypeError("Поле 'title' должно быть строкой")
    if len(title.strip()) == 0:
        raise ValueError("Поле 'title' не может быть пустым")


def validate_genre(genre):
    if not isinstance(genre, str):
        raise ValueError("Поле 'genre' должно быть строкой")


def validate_year(year):
    if not isinstance(year, int):
        raise ValueError("Поле 'year' должно быть целым числом")
    if year < 1895 or year > 2024:
        raise ValueError("Год должен быть между 1895 и 2024")


def validate_movie_data(title, genre, year):
    validate_title(title)
    validate_genre(genre)
    validate_year(year)