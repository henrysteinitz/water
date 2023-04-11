import numpy as np
from numpy.testing import assert_array_equal
import unittest

from value.tensor import Tensor
from value.value_class import Value

class TestTensor(unittest.TestCase):

	def test_add_tensors(self):
		result = Tensor(np.ones([3, 4]), id="A") + Tensor(np.ones([3, 4]), id="B")
		assert_array_equal(result.data, 2 * np.ones([3, 4]))


if __name__ == '__main__':
    unittest.main()