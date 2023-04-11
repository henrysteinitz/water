from typing import Type
from graph.node import Node


class Value:

	def __init__(self, id=None):
		self.node = Node(value=self, op=None, operands=None, id=None)
		self.id = id


	@property
	def op(self):
		return self.node.op


	@property
	def operands(self):
		return self.node.operands
