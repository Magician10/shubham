#Name - Shubham Sinha
#Student Id- 30819806
#Start Date- 12 Aug 2019
#Last Modified - 7 sep 2019
#Program contains reading a data from text file and coverting it into integer before writing it to another text file
simstart = open("town_start", 'r')
simend = open("town_end", 'w')
sim = []
for line in simstart:
    line = int(line.strip())       #strips any extra space in a line and coverts it into integer
    sim.append(line)               #append each integer value in line to a list
for items in sim:
    simend.write("%s\n" %items)
simend.close()
simstart.close()                  #closing the file will free up the space and is helpful in larger programs
