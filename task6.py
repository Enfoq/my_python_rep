import time, random
"""It shows difference between 2 variations of deleting elements from massive
"""
print("-----WHILE variation\n")
massive = [random.randrange(-5,10) for _ in range(1000)]
start = time.time()
while 0 in massive:
	massive.remove(0)
print("-----FINISHED with {0:.3f} seconds".format(time.time() - start))
print("#########")
print("-----COUNTS and SORTING variation\n")
start = time.time()
counter = massive.count(0)
sort = sorted(massive, key=(lambda x: x!=0))
new_massive = sort[counter-1:]
print("-----FINISHED with {0:.3f} seconds".format(time.time() - start))


