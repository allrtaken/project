import _PyPacwar
import numpy
import random
import heapq
import math 

mutateProb = 0.02

def generate():
	return random.random() >= mutateProb

def randomSpecies():
	r=[]	
	for i in range(0,50):
		r+=[random.randint(0,3)]
	return r

binary = lambda n: n>0 and [n&1]+binary(n>>1) or []   #binary representation of no. n . Result is stored in a list.

def cross(a,b):
	r=[]
	indices=[0,4,20,23,26,38,50]
	for i in range(1,63):
		bits=binary(i)
		relem=[]
		bits=bits+[0]*(6-len(bits))		
		#print bits
		for j in range(0,6):
			if bits[j]==0:
				relem=relem+a[indices[j]:indices[j+1]]
			else:	
				relem=relem+b[indices[j]:indices[j+1]]
		r=r+[relem]
	return r
def crossAndMutate(elems):
	result=[elems[0][1]]  #seeding the new generation with the best gene from previous generation
	for i in range(0,len(elems)/2):
		for j in range(0,len(elems)/2-i):
			target=random.randint(i+1,len(elems)-1)  #selects a random gene to the right of current gene from the array
			crossed=cross(elems[i][1],elems[target][1])
			for k in range(0,len(crossed)):  #mutate the newly found crossed gene
				for l in range(0,len(crossed[k])):
					if generate():
						crossed[k][l]=random.randint(0,3);
			result+=crossed
	return result			

# Example Python module in C for Pacwar
def main():

	base_threes   = [3]*50
	threes = [3]*50
	nfittest=50
	initial=[]
	initial+=[[0, 1, 1, 0, 3, 3, 1, 1, 3, 0, 2, 2, 1, 1, 3, 2, 2, 3, 3, 2, 0, 2, 2, 3, 2, 1, 3, 2, 3, 1, 3, 1, 3, 1, 1, 1, 1, 2, 3, 0, 2, 1, 0, 1, 1, 2, 3, 1, 2, 3],[3, 0, 3, 3, 3, 1, 1, 3, 0, 0, 1, 2, 3, 1, 2, 3, 3, 3, 0, 1, 2, 3, 0, 1, 1, 1, 1, 0, 0, 3, 1, 0, 3, 3, 0, 2, 2, 1, 1, 1, 0, 0, 1, 2, 3, 1, 2, 2, 1, 2],[3, 3, 2, 0, 3, 2, 1, 2, 1, 0, 0, 3, 0, 1, 1, 1, 1, 1, 3, 3, 2, 0, 0, 1, 2, 3, 3, 3, 3, 3, 2, 1, 0, 3, 3, 1, 2, 0, 2, 0, 1, 1, 2, 2, 2, 3, 0, 1, 1, 0],[3, 1, 1, 1, 3, 1, 0, 1, 2, 2, 0, 1, 3, 1, 0, 2, 2, 3, 2, 2, 1, 1, 2, 2, 2, 3, 0, 0, 0, 1, 2, 0, 2, 1, 3, 3, 0, 1, 1, 1, 0, 3, 3, 0, 1, 3, 3, 1, 0, 3],[2, 0, 0, 0, 3, 1, 1, 3, 2, 0, 2, 3, 1, 3, 1, 3, 2, 2, 2, 2, 0, 2, 0, 1, 0, 0, 1, 3, 3, 3, 2, 3, 0, 2, 1, 2, 2, 0, 2, 3, 2, 1, 1, 0, 3, 3, 0, 2, 3, 1],[2, 1, 1, 3, 3, 2, 1, 3, 0, 2, 0, 0, 1, 1, 1, 1, 1, 0, 3, 3, 0, 2, 3, 2, 0, 0, 2, 1, 0, 0, 3, 0, 2, 0, 1, 0, 0, 2, 1, 0, 2, 0, 3, 0, 3, 1, 1, 2, 2, 1],[2, 2, 3, 0, 3, 1, 0, 0, 3, 0, 3, 0, 3, 2, 1, 3, 0, 2, 0, 0, 1, 0, 0, 0, 3, 3, 1, 3, 0, 3, 3, 0, 0, 1, 2, 1, 1, 0, 2, 1, 1, 3, 0, 2, 0, 2, 1, 0, 2, 1],[0, 1, 3, 0, 3, 3, 3, 3, 1, 0, 2, 0, 0, 1, 2, 2, 3, 0, 3, 3, 1, 3, 3, 3, 2, 3, 0, 3, 1, 1, 3, 2, 3, 2, 2, 0, 2, 2, 0, 3, 0, 2, 3, 0, 1, 0, 2, 0, 1, 0],[0, 3, 1, 3, 2, 1, 3, 2, 0, 1, 0, 0, 3, 0, 2, 3, 3, 2, 0, 1, 1, 1, 1, 1, 2, 2, 1, 2, 1, 2, 2, 1, 2, 1, 0, 0, 3, 3, 0, 2, 3, 2, 3, 0, 0, 2, 3, 3, 3, 1]]
	
	for i in range(0,75):
		initial+=[randomSpecies()]
	while True:
		myHeap=[]
		
		for i in range(0,len(initial)):
			(rounds,c1,c2) = _PyPacwar.battle(initial[i], threes)
			if c2 < c1:
				print "Win against 3! "
				print initial[i]," candidate: ",c1," threes: ",c2," rounds: ",rounds
				heapq.heappush(myHeap,(-20-(c1/(c2+1.0)),initial[i]))
				continue
			else:
				score=-(pow(c1,0.5)+pow(rounds,0.3)+(14.0/math.log(c2-c1+2,2)))
			#	if i<10:
			#		print initial[i]," candidate: ",c1," threes: ",c2," rounds: ",rounds," score: ",score
				heapq.heappush(myHeap,(score,initial[i]))

		fittest=heapq.nsmallest(nfittest,myHeap)   #fittest is a list of 'nfittest' no. of tuples where each tuple is (score,gene)
		(rounds,c1,c2) = _PyPacwar.battle(fittest[0][1], threes)
		print()
		print "Fittest after tournament: ",fittest[0]," candidate: ",c1," threes: ",c2," rounds: ",rounds
		(rounds,c1,c2) = _PyPacwar.battle(fittest[1][1], threes)
		print "2nd Fittest after tournament: ",fittest[1]," candidate: ",c1," threes: ",c2," rounds: ",rounds
		initial=crossAndMutate(fittest)
		print "intial size: ",len(initial)
	
if __name__ == "__main__": main()


