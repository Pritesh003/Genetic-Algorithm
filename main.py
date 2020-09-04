import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')


#importing functions
from decode import decode
from fitness import fitness
from Roulette import Roulette
from crossover import crossover
from mutation import mutation


# defining all the input parameters

l1 = 5				#string length for x1
l2 = 5				#string length for x2
L = l1+l2
N = 20				#population
Pc = 0.9			#probability for crossover
Pm = 0.05			#probability for mutation
x_1 = [0.0,0.5] 	#min and max value of x1
x_2 = [0.0,0.5] 	#min and max value of x1
iterations = 100	#number of iterations
min_values = []		#to store minimum values of each iteration
tries=[]			#to store number of iterations

population = np.random.randint(2, size=(N,L)) #random population generation

for iteration in range(iterations):
	tries.append(iteration)					#stroring number of iterations
	decoded_values = decode(population, x_1, x_2, l1, l2)	#decoding values of x1 and x2
	
	fitness_values = []						#calculating fitness values
	[fitness_values.append(fitness(decoded_values[0][i],decoded_values[0][i])) for i in range(N)]
	
	P = [f/sum(fitness_values) for f in fitness_values]	#probability of selection
	cum_prob = np.cumsum(P).tolist()		#cumulative probability
	
	n = round((N/2)*2*Pc)					#number of individuals participating in crossover
	
	Parents = Roulette(population,P,N,n)	#parents selection using Roulette selection
	
	Children = crossover(Parents,n)			#Children from crossover
	
	Children_new = mutation(Children,Pm,L)	#new chidren after mutation
	
	
	f_values = []							#calculating value of original function and storing	
	[f_values.append((1.0/fitness_values[i])-1.0) for i  in range(N)]
	
	min_values.append(min(f_values))		#storing minimum value of function for iteration
	
	population = Children_new				#redefining parameters
	N = len(Children_new)

print('Minimum value of function is ',min(min_values))	#printing result, i.e., minimum value of the function

plt.plot(tries,min_values,linewidth=1)					#plotting iterations vs min value for each iteration
plt.xlabel('Iterations')
plt.ylabel('Function Value')
plt.show()
