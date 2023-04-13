import numpy as np
from numpy.testing import assert_array_equal
import unittest

from graph.graph_class import Graph
from op.add import Add
from value.tensor import Tensor


class TestAdd(unittest.TestCase):

	def test_add_apply(self):
		A = Tensor(np.ones([2, 2]))
		B = Tensor(np.ones([2, 2]))
		result = Add(A, B)
		assert_array_equal(result.data, np.array([[2.0, 2.0], [2.0, 2.0]]))


	def test_add_derivative(self):
		A = Tensor(np.ones([2, 2]))
		B = Tensor(np.ones([2, 2]))
		result = Add.derivative(A, B)

		expected_result = np.zeros([2, 2, 2, 2])
		for i in range(2):
			for j in range(2):
				expected_result[i, j, i, j] = 1.0

		assert_array_equal(result[0].data, expected_result)
		assert_array_equal(result[1].data, expected_result)


	def test_node_generation(self):
		graph = Graph(id="Test Graph")
		A = Tensor(np.ones([2, 2]), id="A", graph=graph)
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
		self.assertEqual(result.graph.id, "Test Graph")

		# Traverse op graph to D.
		result = result.operands[1].value
		self.assertEqual(result.id, "D")
		self.assertEqual(result.graph.id, "Test Graph")

		# Traverse op graph to C.
		result = result.operands[1].value
		self.assertEqual(result.id, "C")
		self.assertEqual(result.graph.id, "Test Graph")

		# Traverse op graph to B.
		result = result.operands[1].value
		self.assertEqual(result.id, "B")
		self.assertEqual(result.graph.id, "Test Graph")


if __name__ == '__main__':
    unittest.main()