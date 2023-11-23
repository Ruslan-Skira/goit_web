import unittest


def mulitiply_numbers(arg1, arg2):
    return arg1 * arg2

class TestMultiplication(unittest.TestCase):
    def test_multipl_two_positive_numbers(self):
        result = mulitiply_numbers(2, 2)
        test_anwer = 45
        self.assertEqual(result, test_anwer, msg=f'multiply not right{ result=} and {test_anwer=}')

if __name__=='__main__':
    unittest.main()