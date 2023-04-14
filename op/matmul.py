import numpy as np
from typing import Type

from op.op_class import Op
from value.tensor import Tensor

class MatMul(Op):

	@staticmethod
	def apply(A: Type[Tensor], B: Type[Tensor]):
		return Tensor(np.matmul(A.data, B.data))


	@staticmethod
	def derivative(A: Type[Tensor], B: Type[Tensor]):
		MatMul._validate_shape()	

		dA = np.zeros(A.shape + (A.shape[0], B.shape[-1]))
		dB = np.zeros(B.shape + (A.shape[0], B.shape[-1]))

		for i in range(A.shape[0]):
			for j in range(B.shape[-1]):
				for j_prime in range(dA.shape[1]):
					dA[i][j_prime][i][j] = B.data[j_prime][j]

				for i_prime in range(dB.shape[0]):
					dB[i_prime][j][i][j] = A.data[i][i_prime]

		# TODO: This is just a broadcasted A^T & B^T lol. Refactor 
		# into simple op.apply calls.
		return Tensor(dA), Tensor(dB)


	@staticmethod
	def _validate_shape():
		pass