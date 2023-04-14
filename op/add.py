import numpy as np
import itertools

from op.op_class import Op
from graph.node import Node
from value.tensor import Tensor, Identity


class Add(Op):

	def apply(*xs: list[Tensor]):
		Add._validate_input(*xs)

		result = np.zeros(xs[0].shape)
		for x in xs:
			result += x.data
		return Tensor(result)


	# TODO: Consider broadcasting.
	def derivative(*xs: list[Tensor]):
		Add._validate_input(*xs)

		return [Identity(half_shape=x.shape) for x in xs]


	@staticmethod
	def _validate_input(*xs: list[Tensor]):
		if len(xs) < 1:
			raise ValueError("Add must be called with at least one Tensor argument.")

		# TODO: Allow boradcasting.
		for x in xs:
			if x.shape != xs[0].shape:
				raise ValueError("Broadcasting not yet supported. All tensor arguments to add must have the same shape.")

		return None
