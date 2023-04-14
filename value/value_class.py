from typing import Type
import random
import string


class Value:

	def __init__(self, id=None, graph=None):
		from graph.node import Node

		if id is None:
			id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
		self.id = id
		self.node = Node(value=self, op=None, operands=None, id=id, graph=graph)


	@property
	def graph(self):
		return self.node.graph
	

	@property
	def op(self):
		return self.node.op


	@property
	def operands(self):
		return self.node.operands
