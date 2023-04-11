import numpy as np
import itertools

from op.op_class import Op
from graph.node import Node
from value.tensor import Tensor


class Add(Op):

	def apply(*xs):
		Add._validate_input(*xs)

		result = np.zeros(xs[0].shape)
		for x in xs:
			result += x.data
		return Tensor(result)


	# TODO: Consider broadcasting.
	def derivative(*xs):
		Add._validate_input(*xs)

		result = []
		for x in xs:
			x_deriv = np.zeros([*x.shape, *x.shape])
			for idx in itertools.product(*[range(i) for i in x.shape]):
				x_deriv[idx][idx] = 1.0
			result.append(x_deriv)
		return Tensor(result)


	@staticmethod
	def _validate_input(*xs):
		if len(xs) < 1:
			raise ValueError("Add must be called with at least one Tensor argument.")

		# TODO: Allow boradcasting.
		for x in xs:
			if x.shape != xs[0].shape:
				raise ValueError("Broadcasting not yet supported. All tensor arguments to add must have the same shape.")

		return None
