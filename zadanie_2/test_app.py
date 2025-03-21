import unittest
from datetime import datetime
from app import is_email_on_the_list, square_of_number, sort_numbers, convert_date, is_palindrome

class TestIsEmailOnTheList(unittest.TestCase):
    # testy sprawdzajace czy email znajduje lub nie znajduje sie na roznych listach:
    def setUp(self):
        self.email_list = ['123@gmail.com', '456@gmail.com', '789@gmail.com']
        self.large_list = [f'{i}@gmail.com' for i in range(100000)]
        self.large_list.append('u456@gmail.com')
    # zwykla lista
    def test_email_in_list(self):
        self.assertTrue(is_email_on_the_list(self.email_list, '123@gmail.com'))

    def test_email_not_in_list(self):
        self.assertFalse(is_email_on_the_list(self.email_list, 'not_in_list@gmail.com'))
    # lista z duza iloscia elementow
    def test_email_in_large_list(self):
        self.assertTrue(is_email_on_the_list(self.large_list, 'u456@gmail.com'))

    def test_email_not_in_large_list(self):
        self.assertFalse(is_email_on_the_list(self.large_list, 'u56@gmail.com'))
    # pusta lista
    def test_email_in_empty_list(self):
        self.assertFalse(is_email_on_the_list([], '123@gmail.com'))


class TestSquareOfNumber(unittest.TestCase):
    # testy sprawdzajace czy funkcja dziala poprawnie dla roznych liczb:
    # dodatnie
    def test_square_of_positive(self):
        self.assertEqual(square_of_number(5), 25)
    # ujemne
    def test_square_of_negative(self):
        self.assertEqual(square_of_number(-3), 9)
    # zero
    def test_square_of_zero(self):
        self.assertEqual(square_of_number(0), 0)
    # floaty
    def test_square_of_float(self):
        self.assertAlmostEqual(square_of_number(2.5), 6.25)
    # ujemne floaty
    def test_square_of_negative_float(self):
        self.assertAlmostEqual(square_of_number(-2.5), 6.25)
    # sprawdza czy funkcja zwraca poprawny typ danych
    def test_square_of_number_invalid_type(self):
        with self.assertRaises(TypeError):
            square_of_number("String")


class TestSortNumbers(unittest.TestCase):
    # testy sprawdzajace czy funkcja sortujaca dziala poprawnie dla roznych list:
    # lista zwykla
    def test_sort_basic(self):
        self.assertEqual(sort_numbers([3, 1, 2]), [1, 2, 3])
    # lista z liczbami ujemnymi
    def test_sort_with_negatives(self):
        self.assertEqual(sort_numbers([10, -1, 0]), [-1, 0, 10])
    # lista pusta
    def test_sort_empty_list(self):
        self.assertEqual(sort_numbers([]), [])
    # lista z duplikatami
    def test_sort_with_duplicates(self):
        self.assertEqual(sort_numbers([4, 2, 2, 1, 4]), [1, 2, 2, 4, 4])
    # lista z jednym elementem
    def test_sort_single_element(self):
        self.assertEqual(sort_numbers([42]), [42])


class TestConvertDate(unittest.TestCase):
    # testy sprawdzajace czy funkcja konwertujaca date dziala poprawnie
    def setUp(self):
        self.date = datetime(2025, 10, 5)
    # sprawdza czy zwracana data jest poprawna
    def test_convert_valid_date(self):
        self.assertEqual(convert_date(self.date), '2025-10-05')
    # sprawdza czy zwracana data nie jest inna niz podana
    def test_convert_invalid_date(self):
        self.assertNotEqual(convert_date(self.date), '2023-10-04')
    # sprawdza czy zwracana data jest w odpowiednim formacie - wywala AttributeError gdy jako argument podamy string
    def test_convert_date_invalid_type(self):
        with self.assertRaises(AttributeError):
            convert_date('string')
    # sprawdza poprawnosc roku przestepnego. 2024 jest rokiem przestepnym wiec 29 luty istnieje
    # 2023 nie jest rokiem przestepnym wiec 29 luty nie istnieje i zwraca blad ValueError
    def test_convert_date_leap_year(self):
        self.assertEqual(convert_date(datetime(2024, 2, 29)), '2024-02-29')
        with self.assertRaises(ValueError):
            (convert_date(datetime(2023, 2, 29)), '2023-02-29')
    # sprawdza czy zwracany typ jest stringiem
    def test_convert_date_return_type(self):
        self.assertIsInstance(convert_date(self.date), str)
        
class TestIsPalindrome(unittest.TestCase):
    # testy sprawdzajace czy funkcja sprawdzajaca czy slowo jest palindromem dziala poprawnie
    def test_palindrome_valid(self):
        self.assertTrue(is_palindrome('kajak'))

    def test_palindrome_radar(self):
        self.assertTrue(is_palindrome('radar'))

    def test_palindrome_non_palindrome(self):
        self.assertFalse(is_palindrome('hello'))

    def test_palindrome_single_character(self):
        self.assertTrue(is_palindrome('a'))

    def test_palindrome_empty_string(self):
        self.assertTrue(is_palindrome(''))
