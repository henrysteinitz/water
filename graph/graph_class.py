from typing import Type
from random import randint

class Graph:

	def __init__(self, id=None):
		self.node_map = {}
		self.id_list = []  # Topologically sorted list of node IDs 

		if id is None:
			self.id = "Graph {}".format(randint(0, 100000))
		else:
			self.id = id


	def __setitem__(self, idx: str, node: Type["Node"]):
		if idx not in self.node_map:
			self.node_map[idx] = node
			self.id_list.append(idx)

			# Save id list position for ordered graph traversal.
			node.id_list_idx = len(self.id_list) - 1
		
		node.graph = self


	def clear_all_derivatives(self):
		for id in self.node_map:
			self.node_map[id].clear_derivative()