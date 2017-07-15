import random

tfile = open('late-fullhd-exo.txt', 'w')

for i in range(7000):
	tfile.write("%s\n"%str(random.randint(10, 30)))

tfile.close()
