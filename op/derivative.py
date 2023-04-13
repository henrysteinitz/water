from typing import Type

from value.compose import compose

class Derivative(Op):

	@staticmethod
	def apply(dy: Type[Differentiable], dx: Type[Differentiable]):
		graph = dy.node.graph

		# TODO: Consider only clearing affected derivatives. If we do, we'll 
		# need to store something that identifies this traversal in Node.
		graph.clear_all_derivatives()

		self.dx.node.intialize_derivative()
		for i in range(self.dx.id_list_idx + 1, self.dy.id_list_idx + 1):
			node = graph.id_list[idx]
			derivatives = node.op.derivative([nd.value for nd in self.operands])
			for i in range(len(node.operands)):
				operand = node.operands[i]
				if operand.derivative is not None:
					# TODO: Compose should be build from matmul and a reshape Op. Compositions should happen
					# on a separate graph, which can be accessed by Derivative.deriviative to compute nth order 
					# derivatives on the original graph.
					composed_deriviatve = compose(operand.derivative, derivatives[i], shared_shape=operand.shape)
					node.accumlate_derivative(composed_deriviatve)
		return dy.node.derivative 



	@staticmethod
	def derivative(dy: Type[Differentiable], dx: Type[Differentiable]):

		# Derivative.apply(Derivative.apply(dy, dx), dy) should = 0
		pass