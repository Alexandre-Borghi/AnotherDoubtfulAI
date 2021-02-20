class Matrix:
    """This class represents a matrix of arbitrary size.
    
    Class methods:
        identity: Creates an identity matrix of given dimension.
        zeros: Creates a matrix of given size filled with zeros.
        c_add: Adds 2 matrices together and returns the result.
    
    Methods:
        add: Adds a matrix to self and returns the result. Modifies self.
    """

    def __init__(self, data=[[0]]):
        """Constructs a matrix from a 2D array of numbers.

        Arguments:
            data (2D array): Numbers to create the matrix from.
                Default value is a 1x1 matrix with a 0.
        
        Returns:
            A Matrix filled with the numbers from the data argument.
        
        Errors:
            Raises an AssertionError if columns are not all the same size.
        """

        for i in range(len(data) - 1):
            assert len(data[i]) == len(data[i+1]),\
                "all columns should have the same number of elements"

        self.data = data
        self.m = len(self.data)
        self.n = len(self.data[0])
    
    @classmethod
    def identity(cls, dim=1):
        """Returns the identity matrix of dimension dim.

        Arguments:
            dim (number): The dimension of the (square) matrix to create.
                Default value is 1.
        
        Errors:
            Raises an AssertionError if dim is 0 or less.
        """
        assert dim > 0, "matrix dimension must be at least 1"

        d = [[0 for _ in range(dim)] for _ in range(dim)]

        for i in range(dim):
            d[i][i] = 1
        
        return Matrix(d)
    
    @classmethod
    def c_add(cls, m1, m2):
        """Adds 2 matrices of same size and returns the result.
        
        Arguments:
            m1 (Matrix): First matrix of the addition.
            m2 (Matrix): Second matrix of the addition.
        
        Returns:
            A Matrix, the result of the addition.
        """
        
        pass

    def add(self, other):
        pass