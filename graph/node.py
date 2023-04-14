from typing import Type

from graph.graph_class import Graph
from value.value_class import Value


class Node:

	def __init__(self, value: Type[Value], op: Type["Op"], operands: list['Node'], id=None, graph=None):
		self.value = value
		self.op = op
		self.operands = operands
		self.id = id or self.value.id
		self.derivative = None
		self.id_list_idx = None

		if graph:
			self.graph = graph
		elif self.operands:
			self.graph = self.operands[0].graph
		else:
			self.graph = Graph()
		
		if operands:
			for operand in self.operands:
				self.graph[operand.id] = operand
		
		self.graph[self.id] = self


	# TODO: Is there any reason to support chaining here?
	def clear_derivative(self):
		self.derivative = None
		return self.derivative


	def accumulate_derivative(self, derivative):
		if self.derivative is None:
			self.derivative = derivative
			return self.derivative

		self.derivative += derivative
		return self.derivative


	def initialize_derivative(self):
		print(self.value.initial_derivative)
		self.derivative = self.value.initial_derivative