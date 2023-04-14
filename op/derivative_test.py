import numpy as np
from numpy.testing import assert_array_equal
import unittest

from op.derivative import Derivative
from value.tensor import Tensor, Identity

class TestMatMul(unittest.TestCase):

	def test_derivative_apply(self):
		A = Tensor(np.ones([3, 3]), id="A")
		B = Tensor(np.ones([3, 3]), id="B")
		C = A + B
		result = Derivative(C, A)

		assert_array_equal(result.data, Identity(half_shape=C.shape).data)


if __name__ == '__main__':
    unittest.main()