import unittest

from series_practice_2 import *

class TestBookstoreSalesAnalysis(unittest.TestCase):

    def test_total_sales(self):
        self.assertEqual(total_sales(book_sales_series), 3870)

    def test_date_with_lowest_sales(self):
        self.assertEqual(date_with_lowest_sales(book_sales_series), "2023-11-01")

    def test_median_sales(self):
        self.assertEqual(median_sales(book_sales_series), 395.0)

    def test_days_with_sales_below(self):
        self.assertEqual(days_with_sales_below(book_sales_series, 380), ["2023-11-01", "2023-11-03", "2023-11-06"])

    def test_fancy_indexing_sales(self):
        self.assertEqual(fancy_indexing_sales(book_sales_series, [1, 4, 8]), [400, 420, 430])

    def test_percentage_difference(self):
        self.assertAlmostEqual(percentage_difference(book_sales_series), 29.73, 2)

if __name__ == '__main__':
    unittest.main()
