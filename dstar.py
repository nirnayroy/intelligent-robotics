import numpy as np

def expand(position):
	isRaise = check_raise(position)
	cost = 0.0
	neighbours = get_neighbours(position)
	for i in neighbours:
		if isRaise:
			if i.nextpoint() == position:
				i.setNextPointAndUpdateCost(position)
				open_list.append(i)
			else:
				cost = i.calculateCostVia(currentPoint)
				if cost<i.getCost():
					setMinimumCostToCurrentCost(position)
					open_list.append(position)
		else:
			i.calculateCostVia(position)
			if cost<i.getCost():
				i.setNextPointAndUpdateCost(position)
				open_list.append(i)

def check_raise(position):
	cost = 0
	if position.getCurrentCost() > position.getMinimumCost():
		neighbours = get_neighbours(position)
		for i in neighbours:
			cost = position.calculateCostVia(i)
			if cost<position.getCurrentCost():
				position.setNextPointAndUpdateCost(i)
	return position.getCurrentCost()>position.getMinimumCost()

class point(object):
	def __init__(self, postup, next_tuple):
		(self.x, self.y) = postup
		self.cost = get_cost()
		self.cost_to_goal


	def get_cost(self):

		return cost 

	def get_neighhbours(self):

		return neighbours

	def next_point(next_tuple):


new = []
open_list = []
clsoed_list= []
raised_list = []
lower_list = []
















