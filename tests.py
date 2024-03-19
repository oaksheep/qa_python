import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_add_existing_book(self):

        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    def test_set_book_genre_book_in_books_genre_and_genre_in_genre(self):

        collector = BooksCollector()

        collector.add_new_book('Анна Каренина')
        collector.set_book_genre('Анна Каренина', 'Ужасы')

        assert 'Анна Каренина' in collector.get_books_with_specific_genre('Ужасы')

    def test_set_book_genre_book_not_in_books_genre(self):

        collector = BooksCollector()

        collector.set_book_genre('Детство, отрочество, юность', 'Ужасы')

        assert 'Детство, отрочество, юность' not in collector.get_books_with_specific_genre('Ужасы')

    def test_get_book_genre_one_book(self):

        collector = BooksCollector()

        collector.add_new_book('После бала')
        collector.set_book_genre('После бала', 'Детективы')

        assert collector.get_book_genre('После бала') == 'Детективы'

    @pytest.mark.parametrize('new_book, book_genre', [['Анна Каренина', 'Ужасы'], ['После бала', 'Ужасы'],
                                                      ['Детство, отрочество, юность', 'Ужасы']])
    def test_get_books_with_specific_genre_three_books_for_one_genre(self, new_book, book_genre):
        collector = BooksCollector()

        collector.add_new_book(new_book)
        collector.set_book_genre(new_book, book_genre)

        assert new_book in collector.get_books_with_specific_genre(book_genre)

    def test_get_books_genre_current(self):
        collector = BooksCollector()
        collector.add_new_book('Анна Каренина')
        collector.set_book_genre('Анна Каренина', 'Ужасы')

        assert collector.get_books_genre() == {'Анна Каренина': 'Ужасы'}

    @pytest.mark.parametrize('new_book, book_genre',
                             [['Гарри Поттер', 'Фантастика'], ['Три поросенка', 'Мультфильмы'],
                              ['Один дома', 'Комедии']])
    def test_get_books_for_children_three_books_are_ok_for_children(self, new_book, book_genre):
        collector = BooksCollector()

        collector.add_new_book(new_book)
        collector.set_book_genre(new_book, book_genre)

        assert new_book in collector.get_books_for_children()


    def test_add_book_in_favorites_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Три поросенка')
        collector.add_book_in_favorites('Три поросенка')

        assert collector.get_list_of_favorites_books() == ['Три поросенка']

    def test_delete_book_from_favorites_one_book(self):
        collector = BooksCollector()

        collector.add_new_book('Три поросенка')
        collector.add_book_in_favorites('Три поросенка')
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.delete_book_from_favorites('Три поросенка')

        assert collector.get_list_of_favorites_books() == ['Гарри Поттер']

    def test_get_list_of_favorites_books_two_books_of_three_are_favorite(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Три поросенка')
        collector.add_new_book('Один дома')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Три поросенка')

        assert collector.get_list_of_favorites_books() == ['Гарри Поттер', 'Три поросенка']
