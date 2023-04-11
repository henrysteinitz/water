from graph.node import Node
from value.value import Value

# Examples of tensors include:
# - Error signals (i.e. tangent vectors)
class Tensor(Value):


	def reshape(self, shape: list):
		return Tensor(self.data.reshape(shape))


	@property	
	def shape(self):
		return self.data.shape


	def __matmul__(self, tensor):
		return Tensor(self.data @ tensor.data)