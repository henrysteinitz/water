from typing import Type

from value.direction import Direction
from value.value import Value

# 
class Differentiable(Value):

	def update(self, direction: Type[Direction]):
		raise NotImplementedError("A differentiable must implement update(direction, distance). For points in a smooth manifold, this is the exponential map)