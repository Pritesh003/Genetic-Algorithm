def fitness(x1,x2):
	f = 1/(1+(x1 + x2 - 2*pow(x1,2) - pow(x2,2) + x1*x2))
	return f
