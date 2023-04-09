from op import Op
import numpy as np
import itertools

class Add(Op):
	def apply(self, *xs):
		return np.sum(xs)


	# TODO: Consider broadcasting.
	def derivative(self, *xs):
		# TODO: Write error.
		if len(xs) < 1:
			return 

		# TODO: Allow boradcasting. Write error.
		for x in xs:
			if x.shape != xs[0].shape:
				return

		result = []
		for x in xs:
			x_deriv = np.zeros([*x.shape, *x.shape])
			for idx in itertools.product(*[range(i) for i in x.shape]):
				x_deriv[idx][idx] = 1.0
			result.append(x_deriv)
		return result


	def backwards(self, *xs):
		pass

add = Add()
print(add.derivative(np.ones([2,2]), np.ones([2,2]),))