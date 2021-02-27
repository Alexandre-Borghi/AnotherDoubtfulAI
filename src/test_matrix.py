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

    def test_init_with_different_sized_columns(self):
        with self.assertRaises(matrix.MatrixError):
            _ = matrix.Matrix([[0, 2], [1], [8, 5, 6]])

    def test_identity_default(self):
        mat = matrix.Matrix.identity()

        self.assertEqual(mat.rows, [[1]])
        self.assertEqual(mat.get_rank(), (1, 1))

    def test_identity(self):
        mat = matrix.Matrix.identity(2)

        self.assertEqual(mat.rows, [[1, 0], [0, 1]])
        self.assertEqual(mat.get_rank(), (2, 2))

    def test_identity_with_negative_rank(self):
        with self.assertRaises(matrix.MatrixError):
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

    def test_add_with_different_rank_matrices(self):
        mat1 = matrix.Matrix([[1], [1]])
        mat2 = matrix.Matrix([[2, 2], [2, 2]])

        with self.assertRaises(matrix.MatrixAdditionError):
            _ = mat1 + mat2

    def test_iadd(self):
        mat1 = matrix.Matrix([[1, 1], [1, 1]])
        mat2 = matrix.Matrix([[2, 2], [2, 2]])

        mat1 += mat2

        self.assertEqual(mat1.rows, [[3, 3], [3, 3]])

        mat1 = matrix.Matrix([[1], [1]])
        mat2 = matrix.Matrix([[2], [2]])

        mat1 += mat2

        self.assertEqual(mat1.rows, [[3], [3]])

    def test_iadd_with_different_rank_matrices(self):
        mat1 = matrix.Matrix([[1], [1]])
        mat2 = matrix.Matrix([[2, 2], [2, 2]])

        with self.assertRaises(matrix.MatrixAdditionError):
            mat1 += mat2

    def test_mul(self):
        mat1 = matrix.Matrix([[2, 3], [8, 1]])
        mat2 = mat1 * 2
        res = matrix.Matrix([[4, 6], [16, 2]])

        self.assertEqual(mat2, res)

    def test_rmul(self):
        mat1 = matrix.Matrix([[2, 3], [8, 1]])
        mat2 = 2 * mat1
        res = matrix.Matrix([[4, 6], [16, 2]])

        self.assertEqual(mat2, res)

    def test_imul(self):
        mat = matrix.Matrix([[2, 3], [8, 1]])
        mat *= 2
        res = matrix.Matrix([[4, 6], [16, 2]])

        self.assertEqual(mat, res)

    def test_matmul(self):
        mat1 = matrix.Matrix([[2, 3], [8, 1]])
        mat2 = matrix.Matrix([[2], [1]])
        res = matrix.Matrix([[7], [17]])

        self.assertEqual(res, mat1 @ mat2)
        self.assertEqual(res, mat1 * mat2)

    def test_imatmul(self):
        mat1 = matrix.Matrix([[2, 3], [8, 1]])
        mat2 = matrix.Matrix([[2], [1]])
        mat1 @= mat2
        res = matrix.Matrix([[7], [17]])

        self.assertEqual(res, mat1)

        mat1 = matrix.Matrix([[2, 3], [8, 1]])
        mat1 *= mat2

        self.assertEqual(res, mat1)

    def test_get_transpose(self):
        mat = matrix.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        res = matrix.Matrix([[1, 4, 7], [2, 5, 8], [3, 6, 9]])

        self.assertEqual(res, mat.get_transpose())

        mat = matrix.Matrix([[1, 4, 3], [8, 2, 6], [7, 8, 3], [4, 9, 6], [7, 8, 1]])
        res = matrix.Matrix([[1, 8, 7, 4, 7], [4, 2, 8, 9, 8], [3, 6, 3, 6, 1]])

        self.assertEqual(res, mat.get_transpose())

    def test_transpose(self):
        mat = matrix.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        res = matrix.Matrix([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
        mat.transpose()

        self.assertEqual(res, mat)

        mat = matrix.Matrix([[1, 4, 3], [8, 2, 6], [7, 8, 3], [4, 9, 6], [7, 8, 1]])
        res = matrix.Matrix([[1, 8, 7, 4, 7], [4, 2, 8, 9, 8], [3, 6, 3, 6, 1]])
        mat.transpose()

        self.assertEqual(res, mat)

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

    def test_getitem_out_of_range(self):
        mat = matrix.Matrix.identity(3)

        with self.assertRaises(matrix.MatrixIndexOutOfRangeError):
            _ = mat[3, 1]

        with self.assertRaises(matrix.MatrixIndexOutOfRangeError):
            _ = mat[-1, 2]

    def test_setitem(self):
        mat = matrix.Matrix.identity(3)
        mat[1, 1] = 3

        self.assertEqual(mat[1, 1], 3)

    def test_copy(self):
        mat1 = matrix.Matrix([[2, 2], [2, 2]])
        mat2 = mat1.copy()

        self.assertEqual(mat1, mat2)
    
    def test_map(self):
        mat = matrix.Matrix([[1, 2], [3, 4]])

        def triple(n):
            return 3 * n
        
        mat.map(triple)

        res = matrix.Matrix([[3, 6], [9, 12]])

        self.assertEqual(mat, res)


if __name__ == "__main__":
    unittest.main()
