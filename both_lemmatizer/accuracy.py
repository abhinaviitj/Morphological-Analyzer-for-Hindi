import random
lines = open('output_database.txt').read().splitlines()
file = open("accuracy_output.txt","w+")
for i in range (0,500) :
	myline =random.choice(lines)
	file.write(myline)
	file.write("\n")


