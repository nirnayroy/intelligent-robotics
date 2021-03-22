import numpy as np
from matplotlib import pyplot as plt

def give_cost_matrix(size):
	cost = np.zeros((size, size))
	obs_size = 2
	for i in range(3):
		x = np.random.randint(obs_size, size-obs_size)
		y = np.random.randint(obs_size, size-obs_size)
		cost[x:x+obs_size, y:y+obs_size]=10
	return cost

def get_f(cost, position, goal, pathcost):
	#print(position)
	return pathcost + cost[position]+get_h(position, goal)

def get_h(position, goal):
	return ((np.array(position)-np.array(goal))**2).sum()

def get_next(cost, open_list, goal, pathcost):
	fs = [get_f(cost, i, goal, pathcost) for i in open_list]
	next_pos = open_list[fs.index(min(fs))]
	return next_pos

def get_neighbours(position, size):
	(x, y)  = position
	neighbours = [(x, y-1), (x+1, y-1), (x+1, y),
	(x+1, y+1), (x, y+1), (x-1, y+1), (x-1, y), (x-1,y-1)]
	oob = []
	for (i, j) in neighbours:
		#print(i,j, size)
		if i>(size-1) or j>(size-1):
			oob.append((i,j))
			#print('x')
		elif i<0 or j <0:
			oob.append((i,j))
	for k in oob:
		neighbours.remove(k)
	#print(neighbours)
	return neighbours

def astar(start, goal, cost, size):
	open_list = [start]
	closed_list = []
	pathcost = 0
	while len(open_list) != 0:
		q= get_next(cost, open_list, goal, pathcost)
		#print(q)
		neighbours = get_neighbours(q, size)
		closed_list.append(q)
		pathcost += cost[q]
		#print(neighbours)
		for j in neighbours:
			if j==goal:
				open_list=[]
				closed_list.append(j)
				return closed_list
			elif get_f(cost, j, goal, pathcost)>min([get_f(cost, i, goal, pathcost) for i in open_list]):
				continue
			if get_f(cost, j, goal, pathcost)>min([get_f(cost, i, goal, pathcost) for i in closed_list]):
				continue
			else:
				open_list.append(j)
		#(open_list, q)
		open_list.remove(q)

if __name__=="__main__":
	size = 10
	cost = give_cost_matrix(size)
	#print(cost)
	start = (0, 0)
	goal = (9,  9)
	path = astar(start, goal, cost, size)
	plt.imshow(cost, cmap='gray')
	plt.scatter([i[0] for i in path], [i[1] for i in path])
	plt.savefig('astar.png')
	print(path)





