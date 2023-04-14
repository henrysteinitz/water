import itertools
import numpy as np
from typing import Type

from graph.node import Node
from value.differentiable import Differentiable
from value.value_class import Value

# Examples of tensors include:
# - Error signals (i.e. tangent vectors)
class Tensor(Differentiable):

	def __init__(self, data, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.data = data


	def update(self, direction: "Tensor"):
		self.data += direction.data


	def reshape(self, shape: list):
		return Tensor(self.data.reshape(shape))


	@property
	def initial_derivative(self):
		return Identity(half_shape=self.shape)


	@property	
	def shape(self):
		return self.data.shape


	def __matmul__(self, tensor):
		return Tensor(self.data @ tensor.data)


	def __add__(self, tensor: "Tensor"):
		from op.add import Add
		return Add(self, tensor)


class Identity(Tensor):

	def __init__(self, half_shape, *args, **kwargs):
		data = np.zeros(half_shape + half_shape)
		for idx in itertools.product(*[range(i) for i in half_shape]):
			data[idx][idx] = 1.0

		super().__init__(data, *args, **kwargs)