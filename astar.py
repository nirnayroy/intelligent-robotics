import numpy as np

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
	surrounding_cells = [(x, y-1), (x+1, y-1), (x+1, y),
	(x+1, y+1), (x, y+1), (x-1, y+1), (x-1, y), (x-1,y-1)]
	for (i, j) in surrounding_cells:
		if i>size or j>size:
			surrounding_cells.remove((i,j))
		elif i<0 or j <0:
			surrounding_cells.remove((i,j))
	return surrounding_cells

def astar(start, goal, cost):
	open_list = [start]
	closed_list = []
	while len(open_list) != 0:
		q= get_next(cost, open_list, goal)
		open_list.remove(q)
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

if __name__=="__main__":
	cost = give_cost_matrix(10)
	start = (1, 3)
	goal = (7, 8)
	path = astar(start, goal, cost)
	print(path)





