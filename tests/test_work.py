from work import *
from unittest import main, TestCase

data = {'Смартфон': 251, 'Компьютер': 340, 'Планшет': 36, 'ТВ': 100}


class Test_table(TestCase):

    def setUp(self):  # dispensable function to testing before general test
        pass

    def tearDown(self):  # dispensable function if you want to do something after test
        pass

    def test_test_arr(self):
        self.assertEqual(type(test_arr(data)), tuple)

    def test_percent1(self):
        self.assertEqual(type(percent([13, 256, 2])), list)


if __name__ == '__main__':
    main()
