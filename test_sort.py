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

    def test_insertion_sort_1(self):
        """
        Prueba para lista de tamaño 1
        """
        a = [1,6,2,7,2,4,1]
        sort.insertion_sort(a)
        self.assertEqual(a, [1,1,2,2,4,6,7])


    def test_insertion_sort_2(self):
        """
        Prueba para lista de tamaño 1
        """
        a = [2, 14, 4, 8, 9]
        sort.insertion_sort(a)
        self.assertEqual(a, [2,4,8,9,14])
        
    def test_insertion_sort_3(self):
        """
        Prueba para lista de tamaño 1
        """
        a = [0,42,42,42,1,7,3,4]
        sort.insertion_sort(a)
        self.assertEqual(a, [0,1,3,4,7,42,42,42])
        
    def test_insertion_sort_4(self):
        """
        Prueba para lista de tamaño 1
        """
        a = [10, 14, 1, 11, 13]
        sort.insertion_sort(a)
        self.assertEqual(a, [1,10,11,13,14])

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
