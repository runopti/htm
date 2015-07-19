import sys
import numpy as np
from random import randint


def initialize(n, potentialSynapses, connectedPerm, numColumns):
	# temp_list = [] # list of pair(column, permanence value)
	for input_bit in range(len(input_vector)):
		# Each input bit is represented by some random column and
		# permanence value. This permanence value is determined with
		# two criteria: 1. it is in a small range of connectedPerm,
		# 2. the p value that is connected to the center of the inputs
		# gets a higher value. <--- why?
		mu, sigma = connectedPerm, 0.1
		permValue = np.random.normal(mu,sigma)
		columnID = randint(0, numColumns-1)
		# temp_list[i] = (columnID , permValue)
		synapse = (input_bit, permValue)
		potentialSynapses[columnID].append(synapse)

def spatial_pooler(input_vector):
	""" @param input: input_vector : an array of binary inputs (from sensory data or the previous level)
		@param output: activeColumns(t) : a list of columns that win due to the input at time t
	"""
	numColumns = 500
	connectedPerm = 0.2
	potentialSynapses = [] # for each column, we have a list of potential synapses (subset of input bits)
	initialize(n, potentialSynapses, connectedPerm)

	for c in xrange(columns.size()):
		overlap(c) = 0
		for s in xrange(connectedSynapses(c)):
			overlap(c) += 


def main():
	n = input() # number of input bits
	input_space = []
	# input_space = map(int, raw_input().split()) # input; sequence of bits
	for i in range(n):
		bit = input()
		if bit != 0 or bit != 1: raise error
		input_space.append(bit)

if __name__ == "__main__":
	main()