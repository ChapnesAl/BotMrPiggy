from math_func.general_review import *
from unittest import main, TestCase





class Test_table(TestCase):

    def test_full_assets(self):
        self.assertEqual(type(full_assets(shares_key)), str)

    def test_full_assets_to_display(self):
        self.assertEqual(type(full_assets_to_display(shares, bonds, etf, currencies, futures)), str)

    # def test_full_assets_to_display(self):
    #     self.assertEqual(type(full_assets_to_display(shares, bonds, etf, currencies, futures)), str)



if __name__ == '__main__':
    main()
