from movie_collection import *

def user_commands():
    while True:
        command = input('Введите свою команду - добавление/удаление/поиск/список/завершение: ').lower()

        if command == 'добавление':
            title = input('Введите название фильма: ')
            genre = input('Введите жанр фильма: ')
            year = int(input('Введите год выпуска фильма: '))

            new_movie = Movie(title=title, genre=genre, year=year)
            collection.add_movie(new_movie)


        elif command == 'удаление':
            title = input('Введите название фильма: ')
            collection.remove_movie(title)

        elif command == 'поиск':
            criterion = input('Введите критерий поиска - название/жанр/год: ').lower()

            if criterion == 'название':
                value = input('Введите название: ').lower()
                print(collection.find_movie_title(value))

            elif criterion == 'жанр':
                value = input('Введите жанр: ').lower()
                print(collection.find_movie_genre(value))

            elif criterion == 'год':
                value = int(input('Введите год: '))
                print(collection.find_movie_year(value))

            else:
                print('Критерий поиска не распознан')

        elif command == 'список':

            print('\nСписок фильмов:')
            for i, movie in enumerate(collection, 1):
                print(f"{i}. {movie}")

        elif command == 'завершение':
            print('Всего доброго!')
            break

        else:
            print('Команда не распознана')

user_commands()