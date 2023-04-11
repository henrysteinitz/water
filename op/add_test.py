import numpy as np
from numpy.testing import assert_array_equal
import unittest

from op.add import Add
from value.tensor import Tensor


class TestAdd(unittest.TestCase):

	def test_add_two_tensors(self):
		A = Tensor(np.ones([2, 2]))
		B = Tensor(np.ones([2, 2]))
		result = Add(A, B)
		assert_array_equal(result.data, np.array([[2.0, 2.0], [2.0, 2.0]]))


	def test_node_generation(self):
		A = Tensor(np.ones([2, 2]), id="A")
		B = Tensor(np.zeros([2, 2]), id="B")
		C = Add(A, B)
		C.id = "C"
		D = Add(A, C)
		D.id = "D"
		result = Add(A, D, D)
		
		# Verify result has 3 operands.
		self.assertEqual(len(result.operands), 3)

		# Verify the first operand is A
		self.assertEqual(result.operands[0].value.id, "A")
		assert_array_equal(result.operands[0].value.data, np.ones([2, 2]))

		# Traverse op graph to D.
		result = result.operands[1].value
		self.assertEqual(result.id, "D")

		# Traverse op graph to C.
		result = result.operands[1].value
		self.assertEqual(result.id, "C")

		# Traverse op graph to B.
		result = result.operands[1].value
		self.assertEqual(result.id, "B")


if __name__ == '__main__':
    unittest.main()