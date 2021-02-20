class MatrixError(Exception):
    """An exception for the Matrix class"""

    pass


class MatrixAdditionError(MatrixError):
    """An exception for matrix additions."""

    def __init__(self, m1, m2):
        self.m1 = m1.m
        self.n1 = m1.n
        self.m2 = m2.m
        self.n2 = m2.n

    def __str__(self):
        return f"Can't add {self.m1}x{self.n1} matrix with {self.m2}x{self.n2} matrix."


class MatrixIndexOutOfRangeError(MatrixError):
    """An exception for index out of range matrix errors."""

    def __init__(self, mat, index):
        self.m = mat.m
        self.n = mat.n
        self.index = index

    def __str__(self):
        return f"No {self.index[0]}, {self.index[1]} entry in {self.m}x{self.n} matrix."


class Matrix:
    """This class represents a matrix of arbitrary size.

    Note that this matrix is zero-indexed. The first entry of the 'mat' matrix
    is mat[0, 0].
    
    Class methods:
        identity: Creates an identity matrix of given rank.
        zeros: Creates a matrix of given rank filled with zeros.
    
    Methods:
        get_rank: Returns the (m, n) rank tuple of the matrix.
    """

    def __init__(self, rows=[[0]]):
        """Constructs a matrix from a 2D array of numbers.

        Arguments:
            rows (2D array): Rows (arrays) to create the matrix from.
                Default value is a 1x1 matrix with a 0.
        
        Returns:
            A Matrix filled with the numbers from the rows argument.
        
        Errors:
            Raises an MatrixError if columns are not all the same size.
        """

        for i in range(len(rows) - 1):
            if len(rows[i]) != len(rows[i + 1]):
                raise MatrixError("Rows should all have the same lengths")

        self.rows = rows
        self.m = len(self.rows)
        self.n = len(self.rows[0])

    def __getitem__(self, entry):
        """Returns the entry 'entry' of the matrix. Note that i and j start at 0.

        Usage:
            e = mat[i, j]

        Arguments:
            entry (tuple): The (i, j) tuple of the entry to return.
        
        Returns:
            The entry at (i, j)

        Errors:
            Raises a MatrixIndexOutOfRangeError if trying to index outside of matrix.
        """

        if not (0 <= entry[0] < self.m) or not (0 <= entry[1] < self.n):
            raise MatrixIndexOutOfRangeError(self, entry)

        return self.rows[entry[0]][entry[1]]

    def __setitem__(self, entry, value):
        """Modifies the 'entry' value. Note that i and j start at 0.

        Usage:
            mat[i, j] = val

        Arguments:
            entry (tuple): The (i, j) tuple of the entry to modify.
            value (number): The new value for the entry.
        
        Error:
            Raises a MatrixIndexOutOfRangeError if trying to index outside of matrix.
        """

        if not (0 <= entry[0] < self.m) or not (0 <= entry[1] < self.n):
            raise MatrixIndexOutOfRangeError(self, entry)

        self.rows[entry[0]][entry[1]] = value

    def __add__(self, other):
        """Adds a matrix to this matrix without modifying the current matrix.

        Arguments:
            other (Matrix): The matrix to add self with.
        
        Returns:
            The sum of the two matrices.
        
        Errors:
            Raises a MatrixAdditionException if adding different-sized matrices.
        """

        if self.get_rank() != other.get_rank():
            raise MatrixAdditionError(self, other)

        mat = Matrix.zeros(self.get_rank())

        for i in range(self.m):
            for j in range(self.n):
                mat[i, j] = self[i, j] + other[i, j]

        return mat

    def __iadd__(self, other):
        """Adds a matrix to this matrix and modifies the current matrix.

        Arguments:
            other (Matrix): The matrix to add self with.
        
        Returns:
            self, modified.
        
        Errors:
            Raises a MatrixAdditionException if adding different-sized matrices.
        """

        if self.get_rank() != other.get_rank():
            raise MatrixAdditionError(self, other)

        for i in range(self.m):
            for j in range(self.n):
                self[i, j] += other[i, j]

        return self

    def get_rank(self):
        """Returns the matrix rank tuple (m, n)."""

        return (self.m, self.n)

    @classmethod
    def identity(cls, rank=1):
        """Returns the identity matrix of rank 'rank'.

        Arguments:
            rank (number): The rank of the (square) matrix to create.
                Default value is 1.
        
        Returns:
            Identity matrix of rank 'rank'.
        
        Errors:
            Raises an MatrixError if rank is 0 or less.
        """

        if rank < 1:
            raise MatrixError("Matrix rank must be at least 1")

        rows = [[0 for _ in range(rank)] for _ in range(rank)]

        for i in range(rank):
            rows[i][i] = 1

        return Matrix(rows)

    @classmethod
    def zeros(cls, rank=(1, 1)):
        """Returns a zero-filled matrix of given rank.

        Arguments:
            rank (tuple): The rank (m, n) of the matrix to create.

        Returns:
            A matrix of given rank filled with zeros.
        
        Errors:
            Raise a MatrixError if rank is invalid
        """

        if rank[0] < 1 or rank[1] < 1:
            raise MatrixError("Rank must be 1 or more")

        rows = [[0 for _ in range(rank[1])] for _ in range(rank[0])]

        return Matrix(rows)
