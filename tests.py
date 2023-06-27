import unittest
from printing import PrintBraille
from brailleConversionLogic import grade_one_convert_word
from brailleConversionLogic import separate_multiple_words


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_print_letters(self):
        test_object = PrintBraille("test")
        test_object.print_letters()
        self.assertEqual(1, 1)
        self.assertEqual(test_object.converted_text, ['⠞', '⠑', '⠎', '⠞'])
        self.assertIsNotNone(test_object)

    def test_print_numbers(self):
        test_object = PrintBraille("123")
        test_object.print_numbers()
        self.assertEqual(test_object.converted_text, ['⠁', '⠃', '⠉'])

    def test_print_mix(self):
        test_object = PrintBraille("1ab")
        test_object.print_mix()
        self.assertEqual(test_object.converted_text, ['⠁', '⠁', '⠃'])

    def test_grade_one_conversion(self):
        a = grade_one_convert_word('a')
        b = grade_one_convert_word('1')
        self.assertEqual(a, b)
        aa = grade_one_convert_word('aa')
        bb = grade_one_convert_word('11')
        self.assertEqual(aa, bb)

    def test_separate_multiple_words(self):
        self.assertEqual(separate_multiple_words('test test test'), ['test', 'test', 'test'])


if __name__ == '__main__':
    unittest.main()
