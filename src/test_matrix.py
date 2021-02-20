import unittest
import matrix

class TestMatrix(unittest.TestCase):
    def test_init_default_value(self):
        mat = matrix.Matrix()
        self.assertEqual(mat.data, [[0]], "empty matrix should contain a 0")
        self.assertEqual(mat.m, 1)
        self.assertEqual(mat.n, 1)
    
    def test_init_with_data(self):
        _ = matrix.Matrix([[0, 1, 2], [5, 7, -3], [-10, 8, 1]])
        _ = matrix.Matrix([[0.3, 2.1, 1.2], [7.5, 7, -3.25], [-11.54, 7, 45]])
    
    @unittest.expectedFailure
    def test_init_with_different_sized_columns(self):
        _ = matrix.Matrix([[0, 2], [1], [8, 5, 6]])
    
    def test_identity_default(self):
        mat = matrix.Matrix.identity()

        self.assertEqual(mat.data, [[1]])
        self.assertEqual(mat.m, 1)
        self.assertEqual(mat.n, 1)
    
    def test_identity(self):
        mat = matrix.Matrix.identity(2)

        self.assertEqual(mat.data, [[1, 0], [0, 1]])
        self.assertEqual(mat.m, 2)
        self.assertEqual(mat.n, 2)

    @unittest.expectedFailure
    def test_identity_with_negative_dimension(self):
        _ = matrix.Matrix.identity(-2)
    
    def test_zeros_default(self):
        pass

if __name__ == "__main__":
    unittest.main()