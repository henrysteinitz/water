from typing import Type


class Value:

	def __init__(self, id=None, graph=None):
		from graph.node import Node
		self.node = Node(value=self, op=None, operands=None, id=None, graph=graph)
		self.id = id


	@property
	def graph(self):
		return self.node.graph
	

	@property
	def op(self):
		return self.node.op


	@property
	def operands(self):
		return self.node.operands
