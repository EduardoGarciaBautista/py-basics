import unittest


def is_mayor_age(age):
    if age >= 18:
        return True
    else:
        return False


class CristalTest(unittest.TestCase):

    def is_mayor_age(self):
        age = 20
        result = is_mayor_age(age)
        self.assertEqual(result, True)

    def is_younger(self):
        age = 17
        result = is_mayor_age(age)
        self.assertEqual(False, result)


if __name__ == '__main__':
    unittest.main()
