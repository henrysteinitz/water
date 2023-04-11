from math import prod
import numpy as np
from typing import Type
from tensor import Tensor


# A slight generalization of matrix multiplication for higher rank tensors 
# viewed as linear maps.
def compose(tensor1: Type[Tensor], tensor2: Type[Tensor], shared_shape: list):
	shared_total_dim = prod(shared_shape)
	tensor1_initial_shape = tensor1.shape[: - len(shared_shape)]
	tensor2_final_shape = tensor2.shape[len(shared_shape):]
	result = tensor1.reshape([-1, shared_total_dim]) @ tensor2.reshape([shared_total_dim, -1])
	return result.reshape(tensor1_initial_shape + tensor2_final_shape)
