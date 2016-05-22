from random import randint

def getRand(l):
	return l[randint(0, len(l) - 1)]

nouns = []
adjs = []
prefixes = ["Order", "Knights"]
with open ('nouns.txt', 'r') as nounsFile:
	with open ('adjectives.txt', 'r') as adjsFile:
		nouns = str.split(nounsFile.read())
		adjs = str.split(adjsFile.read())

with open ("orderNames.txt", "w") as namesFile:
	for i in range(1000):
		namesFile.write("The " + getRand(prefixes) + " of the " + getRand(adjs).capitalize() \
		+ " " + getRand(nouns).capitalize() + "\n")