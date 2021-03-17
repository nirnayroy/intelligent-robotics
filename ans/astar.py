import numpy as np

def give_cost_matrix(size):
	cost = np.zeros(size)
	return cost

def get_f(cost, position, goal):
	return cost[position]+get_h(position, goal)

def get_h(position, goal):
	return ((position-goal)**2).sum()

def get_next(cost, open_list, goal):
	fs = [get_f(cost, i, goal) for i in open_list]
	next_pos = open_list[fs.index(min(fs))]
	return next_pos

def get_neighbours(position, size):
	neighbours = []
	if abs(position[0])==size:
		
	elif abs(position[1])==size:

	return neighbours

def astar(start, goal, cost):
	open_list = [start]
	closed_list = []
	while len(open_list) != 0:
		q= get_next(cost, open_list, goal)
		open_list.pop(q)
		neighbours = get_neighbours(q)
		for j in neighbours:
			if j==goal:
				open_list=[]
				break
			elif get_f(cost, j, goal)>min([get_f(cost, i, goal) for i in open_list]):
				pass
			elif get_f(cost, j, goal)>min([get_f(cost, i, goal) for i in closed_list]):
				pass
			else:
				open_list.append(j)
		closed_list.append(q)
	return closed_list

def 





