from typing import Type

from op.op_class import Op
from value.compose import compose
from value.differentiable import Differentiable

class Derivative(Op):

	@staticmethod
	def apply(dy: Type[Differentiable], dx: Type[Differentiable]):
		graph = dy.node.graph

		# TODO: Consider only clearing affected derivatives. If we do, we'll 
		# need to store something that identifies this traversal in Node.
		graph.clear_all_derivatives()

		dx.node.initialize_derivative()
		for i in range(dx.node.id_list_idx + 1, dy.node.id_list_idx + 1):
			node = graph.node_map[graph.id_list[i]]

			if node.op is None:
				continue
			
			derivatives = node.op.derivative(*[nd.value for nd in node.operands])
			for i in range(len(node.operands)):
				operand = node.operands[i]
				if operand.derivative is not None:
					# TODO: Compose should be build from matmul and a reshape Op. Compositions should happen
					# on a separate graph, which can be accessed by Derivative.deriviative to compute nth order 
					# derivatives on the original graph.
					composed_deriviatve = compose(operand.derivative, derivatives[i], shared_shape=operand.value.shape)
					node.accumulate_derivative(composed_deriviatve)
		
		return dy.node.derivative 



	@staticmethod
	def derivative(dy: Type[Differentiable], dx: Type[Differentiable]):

		# Derivative.apply(Derivative.apply(dy, dx), dy) should = 0
		pass