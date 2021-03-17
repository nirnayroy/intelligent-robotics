import numpy as np
from
'''
f = g+h

#at each step pick cell having lowest f

g = the movement cost to move from the starting point
 to a given square on the grid, following the path 
 generated to get there. 

h = the estimated movement cost to move from that
 given square on the grid to the final destination. 

// A* Search Algorithm
1.  Initialize the open list
2.  Initialize the closed list
    put the starting node on the open 
    list (you can leave its f at zero)

3.  while the open list is not empty
    a) find the node with the least f on 
       the open list, call it "q"

    b) pop q off the open list
  
    c) generate q's 8 successors and set their 
       parents to q
   
    d) for each successor
        i) if successor is the goal, stop search
          successor.g = q.g + distance between 
                              successor and q
          successor.h = distance from goal to 
          successor (This can be done using many 
          ways, we will discuss three heuristics- 
          Manhattan, Diagonal and Euclidean 
          Heuristics)
          
          successor.f = successor.g + successor.h

        ii) if a node with the same position as 
            successor is in the OPEN list which has a 
           lower f than successor, skip this successor

        iii) if a node with the same position as 
            successor  is in the CLOSED list which has
            a lower f than successor, skip this successor
            otherwise, add  the node to the open list
     end (for loop)
  
    e) push q on the closed list
    end (while loop)

'''
sptSet = set()
graph = { "a" : {"b": np.random.randint(1, 10),"c":np.random.randint(1, 10)},
          "b" : ["a":np.random.randint(1, 10), "d":np.random.randint(1, 10)],
          "c" : ["a":np.random.randint(1, 10), "d":np.random.randint(1, 10)],
          "d" : ["e":np.random.randint(1, 10)],
          "e" : ["d":np.random.randint(1, 10)]
         }

distance_dict = {"a":0, "b":np.inf, "c":np.inf, "d":np.inf, "e":np.inf}
source_node = "a"
target_node "e"

def get_next_shortest(graph, node, f):



open_list = ["a"]
closed_list = []


f =- 1
while len(open_list)!=0:
	g = 0
	f = min([distance_dict[k] for k in open_list])

	q = list(distance_dict.keys())[list(distance_dict.values()).index(f)]
	open_list.pop(q)
	successors_dict = graph(q)
	for i in successors_dict.keys():
		distance_dict[i] = g + graph[q][i] + h
		if i == target_node:
			break
		elif distance_dict[i]>min([distance_dict[a]: for a in open_list]):
			pass
		elif distance_dict[i]>min([distance_dict[a]: for a in closed_list]):
			pass
		else:
			open_list.apppend(i)
			g += graph[q][i]
	closed_list.append(q)

openlist = ["a"]
closedlist = []
pathlist = []
while (the destination node has not been reached):
    min_f = min([distance_dict[k] for k in openlist])
	q= openlist[openlist.index(min_f)]   
	pathlist.append(q) 

    if q==target_node:

        break 
    else:
    	closed_list.append(q)
    	neighbor_dict = graph(q)
        for  key, value in neighbor.items():
            if (value<g and is in closed_list) :
                replace the neighbor with the new, lower, g value 
                current node is now the neighbor's parent            
            else if (current g value is lower and this neighbor is in the open list ) :
                replace the neighbor with the new, lower, g value 
                change the neighbor's parent to our current node

            else if this neighbor is not in both lists:
                add it to the open list and set its g


			
























class environment(object):
	def __init__(self, size, n_obstacles, heuristic='Euclidean'):
		self.cost_matrix = np.zeros((size, size))
		self.heuristic = heuristic
	def heuristic(self, source, goal):
		if self.heuristic = 'Euclidean':
			return (goal[0]-source[0])**2 + (goal[1]-source[1])**2 
		else:
			pass
	def 


                                                                                                        ZAZAZAZAZAZAZAZAZAZAZAZAZAZAZAZAZAZAZAZAZAZAZA                                                                     Z             zzzzz

