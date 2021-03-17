import numpy as np
import matplotlib.pyplot as plt

class Pathfinder(object):
	def __init__(self, size, resolution, obs, goal):
		x, y = np.arange(0, size, resolution), np.arange(0, size, resolution)
		self.size = size
		self.obstacles = obs
		self.goal = goal
		self.X, self.Y = np.meshgrid(x, y)
		self.dX, self.dY = self.get_grads(self.X, self.Y)
		self.plot_potential()
		self.plot_pot_surface()
		self.positions = self.move_robot(5, 5)
		self.plot_positions(self.positions)

	def potential(self, x, y):
		#define potential function here and give matrix
		(x_g, y_g, r_g) = self.goal
		U_goal = np.sqrt((x_g-x)**2 + (y_g-y)**2)
		U_obs = 0
		for i in self.obstacles:
			(x_o, y_o, r_o, p) = i
			dist = np.sqrt((x-x_o)**2 + (y_o-y)**2)
			U_obs = ((1/dist)-(1/p))**2
			#print(x, y)
			#U_obs[r_o<dist<p] = ((1/dist)-(1/p))**2
			if isinstance(x, np.float64):
				print('run')
				if dist<r_o:
					U_obs = 50
			else:
				U_obs = np.array(U_obs)
				U_obs[dist<r_o] = 50
		potential = U_goal + U_obs
		return potential

	def get_grads(self, x, y):
		(x_g, y_g, r_g) = self.goal
		dx, dy = (x-x_g), (y-y_g)
		for i in self.obstacles:
			(x_o, y_o, r_o, p) = i
			dist = np.sqrt((x-x_o)**2 + (y_o-y)**2)	
			dx =  dx + (-(x-x_o))/(((x-x_o)**2 + (y_o-y)**2)**2)
			dy =  dy + (-(y-y_o))/(((x-x_o)**2 + (y_o-y)**2)**2)
		return -dx, -dy

	def plot_potential(self, **kwargs):
		fig, ax = plt.subplots()
		ax.set(xlabel='X', ylabel='Y', aspect=1.0)
		ax.set_xlim([0, self.size])
		ax.set_ylim([0, self.size])
		ax.quiver(self.X, self.Y, self.dX, self.dY)
		(x_g, y_g, r_g) = self.goal
		circle1 = plt.Circle((x_g, y_g), 1, color='r')
		ax.add_patch(circle1)
		for i in self.obstacles:
			(x_o, y_o, r_o, p) = i
			circle2 = plt.Circle((x_o, y_o), 1, color='b')
			ax.add_patch(circle2)
		plt.savefig('vector_field.png')
		return plt

	def plot_pot_surface(self):
		fig = plt.figure()
		ax = fig.add_subplot(111, projection='3d')
		ax.plot_surface(self.X, self.Y, self.potential(self.X, self.Y),cmap='coolwarm')
		ax.set_title('Surface plot')
		plt.savefig('pot_surface.png')

	def move_robot(self, x, y, learning_rate=0.001, steps=100000):
		positions = []
		positions.append((x, y))
		for i in range(steps):
			dx, dy = self.get_grads(x, y)
			x += 0.1*dx
			y += 0.1*dy
			positions.append((x, y))
		#print(positions)
		return positions

	def plot_positions(self, positions):
		x = []
		y = []
		z = []
		for i in positions:
			(x_, y_) = i
			x.append(x_)
			y.append(y_)
		fig = plt.figure(figsize = (10, 7))
		plt.scatter(x, y)
		ax = plt.axes()
		ax.set(xlabel='X', ylabel='Y', aspect=1.0)
		ax.set_xlim([0, self.size])
		ax.set_ylim([0, self.size])
		ax.quiver(self.X, self.Y, self.dX, self.dY)
		(x_g, y_g, r_g) = self.goal
		circle1 = plt.Circle((x_g, y_g), 1, color='r')
		ax.add_patch(circle1)
		for i in self.obstacles:
			(x_o, y_o, r_o, p) = i
			circle2 = plt.Circle((x_o, y_o), 1, color='b')
			ax.add_patch(circle2)
		# Creating plot
		
		plt.savefig('path.png')


size=100
resolution=5

goal = (80, 80, 10)
obs = [(50, 60, 20, 30)]
obj = Pathfinder(size, resolution, obs, goal)

