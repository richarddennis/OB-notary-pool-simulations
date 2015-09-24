s=set(range(1,153330)) # Set the range - 150000 Non malicious notary nodes - 3330 notary malicious nodes   #Change depending on network size, 3330 always the attack number
import random

a = [] #Number of times when a malicious pool was selected - 1 gets added to the array each

b = 0 

while b < 1000000: #Number of times to run the test

	r = random.sample(s,7) #Selects 7 random nodes - (7 is size of the pool)
	x = sum( i < 3331 for i in r) #Assumes 0 - 3330 nodes are malicious, order does not matter here
	if x >3:  #If more than 3 nodes 3330 and under are found the pool is compromised
		a.append(1) #Add to the array 
	b = b + 1 #Repeat test

print sum(a) #Number of times a compromised pool is selected
