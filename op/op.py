class Op:
	def apply(self, *xs):
		pass

	def derivative(self, *xs):
		pass

	# The backward method efficiently implements derivative() applied to 
	# backpropagating scalar loss gradients.
	def backward(self, *xs):
		pass

	def inverse(self, *xs):
		pass