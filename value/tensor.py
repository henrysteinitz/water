from typing import Type

from graph.node import Node
from value.differentiable import Differentiable
from value.value_class import Value

# Examples of tensors include:
# - Error signals (i.e. tangent vectors)
class Tensor(Differentiable):

	def __init__(self, data, id=None):
		super().__init__(id)
		self.data = data


	def update(self, direction: "Tensor"):
		self.data += direction.data


	def reshape(self, shape: list):
		return Tensor(self.data.reshape(shape))


	@property	
	def shape(self):
		return self.data.shape


	def __matmul__(self, tensor):
		return Tensor(self.data @ tensor.data)


	def __add__(self, tensor: "Tensor"):
		from op.add import Add
		return Add(self, tensor)