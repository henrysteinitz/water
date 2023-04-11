from typing import Type

from value.value import Value

# 
class Differentiable(Value):

	def update(self, direction: Type[np.array], distance: float):
		raise NotImplementedError("A differentiable must implement update(direction, distance). For points in a smooth manifold, this is the exponential map)