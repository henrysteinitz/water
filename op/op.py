from graph.node import Node

class Op:

	def __new__(cls, *xs):
		y = cls.apply(*xs)
		node = Node(y, cls, [x.node for x in xs])
		y.node = node
		return y


	@staticmethod
	def apply(*xs):
		pass

	@staticmethod
	def derivative(*xs):
		pass


	# The backward method efficiently implements derivative() applied to 
	# backpropagating scalar loss gradients.
	@staticmethod
	def backward(self, *xs):
		pass

	@staticmethod
	def inverse(self, *xs):
		pass