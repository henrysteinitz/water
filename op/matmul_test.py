import numpy as np
from numpy.testing import assert_array_equal
import unittest

from graph.graph_class import Graph
from op.matmul import MatMul
from value.tensor import Tensor

class TestMatMul(unittest.TestCase):

	def test_matmul_apply(self):
		A = Tensor(np.ones([3, 4]))
		B = Tensor(np.ones([4, 3]))
		result = MatMul(A, B).data
		assert_array_equal(result, 4 * np.ones([3, 3]))

	def test_matmul_derivative(self):
		A = Tensor(np.ones([3, 4]))
		B = Tensor(np.ones([4, 3]))
		print(MatMul.derivative(A, B)[0].data)


	def test_node_generation(self):
		graph = Graph(id="Test Graph")
		A = Tensor(np.ones([3, 4]), id="A", graph=graph)
		B = Tensor(np.ones([4, 3]), id="B")
		C = MatMul(A, B)
		C.id = "C"
		D = MatMul(C, A)
		D.id = "D"
		result = MatMul(D, B)

		self.assertEqual(len(result.operands), 2)

		# Verify the first operand is D.
		result = result.operands[0].value
		self.assertEqual(result.id, "D")
		self.assertEqual(result.graph.id, "Test Graph")
		
		# Traverse the op graph to C.
		result = result.operands[0].value
		self.assertEqual(result.id, "C")
		self.assertEqual(result.graph.id, "Test Graph")

		# Traverse the op graph to A.
		result = result.operands[0].value
		self.assertEqual(result.id, "A")
		self.assertEqual(result.graph.id, "Test Graph")
		

if __name__ == '__main__':
    unittest.main()