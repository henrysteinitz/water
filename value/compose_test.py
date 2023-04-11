import unittest
from compose import compose
import numpy as np
from tensor import Tensor

class TestCompose(unittest.TestCase):

	def test_compose_shape(self):
		A = Tensor(np.ones([1, 2, 3, 4, 5]))
		B = Tensor(np.ones([3, 4, 5, 6, 7]))
		result = compose(A, B, [3, 4, 5])
		self.assertEqual(result.shape, (1, 2, 6, 7))

		A = Tensor(np.ones([11, 2, 7]))
		B = Tensor(np.ones([2, 7, 3, 4, 4]))
		result = compose(A, B, [2, 7])
		self.assertEqual(result.shape, (11, 3, 4, 4))


if __name__ == '__main__':
    unittest.main()