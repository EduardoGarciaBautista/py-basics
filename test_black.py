import unittest


def plus(num_1, num_2):
    return num_1 + num_2


class BlackBoxTest(unittest.TestCase):

    def plus_two_positives(self):
        num_1 = 10
        num_2 = 5
        result = plus(num_1, num_2)

        self.assertEqual(result, 15)


if __name__ == '__main__':
    unittest.main()
