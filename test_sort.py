import unittest
import sort


class TestSortingAlgorithms(unittest.TestCase):

    def test_quick_sort_1(self):
        """
        Prueba caso general #1
        """
        a = [1, 4, 6, 1, 2, 0]
        sort.quick_sort(a)
        self.assertEqual(a, [0, 1, 1, 2, 4, 6])

    def test_quick_sort_2(self):
        """
        Prueba caso general #2
        """
        a = [2, 4, 9, 2, 2, 7]
        sort.quick_sort(a)
        self.assertEqual(a, [2, 2, 2, 4, 7, 9])

    def test_quick_sort_3(self):
        """
        Prueba para lista de tamaño 1
        """
        a = [1]
        sort.quick_sort(a)
        self.assertEqual(a, [1])

    def test_quick_sort_4(self):
        """
        Prueba caso general #3
        """
        a = [0, 0, 1, 1, 1, 1, 0, 0]
        sort.quick_sort(a)
        self.assertEqual(a, [0, 0, 0, 0, 1, 1, 1, 1])


    def test_merge_sort_1(self):
        """
        Prueba caso general #1
        """
        a = [1, 4, 6, 1, 2, 0]
        sort.merge_sort(a)
        self.assertEqual(a, [0, 1, 1, 2, 4, 6])

    def test_merge_sort_2(self):
        """
        Prueba caso general #2
        """
        a = [2, 4, 9, 2, 2, 7]
        sort.merge_sort(a)
        self.assertEqual(a, [2, 2, 2, 4, 7, 9])

    def test_merge_sort_3(self):
        """
        Prueba para lista de tamaño 1
        """
        a = [1]
        sort.merge_sort(a)
        self.assertEqual(a, [1])

    def test_merge_sort_4(self):
        """
        Prueba caso general #3
        """
        a = [0, 0, 1, 1, 1, 1, 0, 0]
        sort.merge_sort(a)
        self.assertEqual(a, [0, 0, 0, 0, 1, 1, 1, 1])

if __name__ == '__main__':
    unittest.main()
