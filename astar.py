import numpy as np
from matplotlib import pyplot as plt

def give_cost_matrix(size):
	cost = np.zeros((size, size))
	return cost

def get_f(cost, position, goal):
	return cost[position]+get_h(position, goal)

def get_h(position, goal):
	return ((np.array(position)-np.array(goal))**2).sum()

def get_next(cost, open_list, goal):
	fs = [get_f(cost, i, goal) for i in open_list]
	next_pos = open_list[fs.index(min(fs))]
	return next_pos

def get_neighbours(position, size):
	(x, y)  = position
	neighbours = [(x, y-1), (x+1, y-1), (x+1, y),
	(x+1, y+1), (x, y+1), (x-1, y+1), (x-1, y), (x-1,y-1)]
	for (i, j) in neighbours:
		if i>size or j>size:
			neighbours.remove((i,j))
		elif i<0 or j <0:
			neighbours.remove((i,j))
	return neighbours

def astar(start, goal, cost, size):
	open_list = [start]
	closed_list = []
	while len(open_list) != 0:
		q= get_next(cost, open_list, goal)
		#print(q)
		neighbours = get_neighbours(q, size)
		closed_list.append(q)
		for j in neighbours:
			if j==goal:
				open_list=[]
				closed_list.append(j)
				return closed_list
			elif get_f(cost, j, goal)>min([get_f(cost, i, goal) for i in open_list]):
				continue
			if get_f(cost, j, goal)>min([get_f(cost, i, goal) for i in closed_list]):
				continue
			else:
				open_list.append(j)
		#(open_list, q)
		open_list.remove(q)



	

if __name__=="__main__":
	size = 100
	cost = give_cost_matrix(size)
	start = (1, 3)
	goal = (93, 72)
	path = astar(start, goal, cost, size)
	print(path)





