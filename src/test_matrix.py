import matrix
import unittest


class TestMatrix(unittest.TestCase):
    def test_init_default_value(self):
        mat = matrix.Matrix()
        self.assertEqual(mat.rows, [[0]], "empty matrix should contain a 0")
        self.assertEqual(mat.get_rank(), (1, 1))

    def test_init_with_rows(self):
        _ = matrix.Matrix([[0, 1, 2], [5, 7, -3], [-10, 8, 1]])
        _ = matrix.Matrix([[0.3, 2.1, 1.2], [7.5, 7, -3.25], [-11.54, 7, 45]])

    @unittest.expectedFailure
    def test_init_with_different_sized_columns(self):
        _ = matrix.Matrix([[0, 2], [1], [8, 5, 6]])

    def test_identity_default(self):
        mat = matrix.Matrix.identity()

        self.assertEqual(mat.rows, [[1]])
        self.assertEqual(mat.get_rank(), (1, 1))

    def test_identity(self):
        mat = matrix.Matrix.identity(2)

        self.assertEqual(mat.rows, [[1, 0], [0, 1]])
        self.assertEqual(mat.get_rank(), (2, 2))

    @unittest.expectedFailure
    def test_identity_with_negative_dimension(self):
        _ = matrix.Matrix.identity(-2)

    def test_zeros_default(self):
        mat = matrix.Matrix.zeros()

        self.assertEqual(mat.rows, [[0]])
        self.assertEqual(mat.get_rank(), (1, 1))

    def test_zeros(self):
        mat = matrix.Matrix.zeros((2, 1))

        self.assertEqual(mat.rows, [[0], [0]])
        self.assertEqual(mat.get_rank(), (2, 1))

        mat = matrix.Matrix.zeros((1, 2))

        self.assertEqual(mat.rows, [[0, 0]])
        self.assertEqual(mat.get_rank(), (1, 2))

        mat = matrix.Matrix.zeros((3, 2))

        self.assertEqual(mat.rows, [[0, 0], [0, 0], [0, 0]])
        self.assertEqual(mat.get_rank(), (3, 2))

    def test_add(self):
        mat1 = matrix.Matrix([[1, 1], [1, 1]])
        mat2 = matrix.Matrix([[2, 2], [2, 2]])

        mat = mat1 + mat2

        self.assertEqual(mat.rows, [[3, 3], [3, 3]])

        mat1 = matrix.Matrix([[1], [1]])
        mat2 = matrix.Matrix([[2], [2]])

        mat = mat1 + mat2

        self.assertEqual(mat.rows, [[3], [3]])

    @unittest.expectedFailure
    def test_add_with_different_rank_matrices(self):
        mat1 = matrix.Matrix([[1], [1]])
        mat2 = matrix.Matrix([[2, 2], [2, 2]])

        _ = mat1 + mat2

    def test_get_rank(self):
        mat = matrix.Matrix()

        self.assertEqual(mat.get_rank(), (1, 1))

        mat = matrix.Matrix([[0, 0], [0, 0]])

        self.assertEqual(mat.get_rank(), (2, 2))

        mat = matrix.Matrix([[0], [0], [0]])

        self.assertEqual(mat.get_rank(), (3, 1))

    def test_getitem(self):
        mat = matrix.Matrix.identity(3)

        self.assertEqual(mat[0, 0], 1)
        self.assertEqual(mat[1, 0], 0)
        self.assertEqual(mat[0, 1], 0)
        self.assertEqual(mat[1, 1], 1)

    @unittest.expectedFailure
    def test_getitem_out_of_range(self):
        mat = matrix.Matrix.identity(3)

        _ = mat[3, 1]
        _ = mat[-1, 2]

    def test_setitem(self):
        mat = matrix.Matrix.identity(3)
        mat[1, 1] = 3

        self.assertEqual(mat[1, 1], 3)


if __name__ == "__main__":
    unittest.main()
