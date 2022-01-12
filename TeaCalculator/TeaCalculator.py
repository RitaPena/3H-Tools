#Needed packages
from collections import Counter
import os

#Databases
blackEagles = ["Edelgard", "Hubert", "Ferdinand", "Petra", "Dorothea", "Caspar", "Linhardt", "Bernadetta"]
blueLions = ["Dimitri", "Dedue", "Felix", "Ingrid", "Sylvain", "Ashe", "Annette", "Mercedes"]
goldenDeer = ["Claude", "Hilda", "Lorenz", "Raphael", "Ignatz", "Marianne", "Lysithea", "Leonie"]
ashenWolves = ["Yuri", "Balthus", "Constance", "Hapi"]
church = ["Catherine", "Shamir", "Manuela", "Hanneman", "Gilbert", "Cyril", "Seteth", "Flayn", "Alois"]
special = ["Anna", "Jeritza", "Rhea"]

charTeas = {"Edelgard": ["Bergamot"], "Dimitri": ["Chamomile"], "Claude": ["Almyran Pine Needles", "Chamomile"], "Hubert": ["Cinnamon Blend", "Dagda Fruit Blend"], "Ferdinand": ["Almyran Pine Needles", "Southern Fruit Blend", "Seiros Tea"], "Linhardt": ["Almyran Pine Needles", "Angelica Tea"], "Caspar": ["Ginger Tea"], "Bernadetta": ["Albinean Berry Blend", "Honeyed-Fruit Blend"], "Dorothea": ["Albinean Berry Blend", "Sweet-Apple Blend"], "Petra": ["Four-Spice Blend", "Ginger Tea"], "Dedue": ["Cinnamon Blend", "Four-Spice Blend", "Ginger Tea"], "Felix": ["Almyran Pine Needles", "Four-Spice Blend"], "Ashe": ["Angelica Tea", "Mint Leaves"], "Sylvain": ["Bergamot", "Seiros Tea"], "Mercedes": ["Albinean Berry Blend", "Crescent-Moon Tea", "Southern Fruit Blend"], "Annette": ["Almond Blend", "Rose Petal Blend", "Sweet-Apple Blend"], "Ingrid": ["Chamomile", "Mint Leaves"], "Lorenz": ["Bergamot", "Rose Petal Blend", "Seiros Tea"], "Raphael": ["Almond Blend", "Ginger Tea"], "Ignatz": ["Dagda Fruit Blend", "Seiros Tea", "Lavender Blend"], "Lysithea": ["Sweet-Apple Blend", "Southern Fruit Blend", "Crescent-Moon Tea", "Honeyed-Fruit Blend"], "Marianne": ["Dagda Fruit Blend", "Cinnamon Blend", "Lavender Blend"], "Hilda": ["Albinean Berry Blend", "Southern Fruit Blend", "Rose Petal Blend", "Mint Leaves"], "Leonie": ["Four-Spice Blend", "Angelica Tea"], "Seteth": ["Four-Spice Blend", "Ginger Tea", "Angelica Tea"], "Flayn": ["Sweet-Apple Blend", "Crescent-Moon Tea", "Almond Blend"], "Hanneman": ["Bergamot", "Sweet-Apple Blend", "Honeyed-Fruit Blend", "Cinnamon Blend"], "Manuela": ["Mint Leaves", "Lavender Blend"], "Gilbert": ["Almond Blend", "Lavender Blend"], "Alois": ["Crescent-Moon Tea", "Honeyed-Fruit Blend"], "Catherine": ["Rose Petal Blend"], "Shamir": ["Crescent-Moon Tea", "Chamomile"], "Cyril": ["Almyran Pine Needles"], "Rhea": ["Crescent-Moon Tea", "Angelica Tea", "Chamomile"], "Yuri": ["Albinean Berry Blend", "Honeyed-Fruit Blend", "Seiros Tea"], "Balthus": ["Almyran Pine Needles", "Ginger Tea"], "Constance": ["Bergamot", "Rose Petal Blend", "Sweet-Apple Blend", "Albinean Berry Blend"], "Hapi": ["Cinnamon Blend", "Dagda Fruit Blend", "Four-Spice Blend"], "Jeritza": ["Albinean Berry Blend", "Southern Fruit Blend", "Honeyed-Fruit Blend", "Sweet-Apple Blend"], "Anna": ["Seiros Tea", "Dagda Fruit Blend", "Bergamot"]
}

#Functions
def teaCount (charList):
	"""Calculates the number of times a tea is needed for a given list of characters.
	Returns a list with a count per tea.
	"""
	
	teaList = [] #List of teas needed
	
	for char in charList:
		for key, value in charTeas.items():
			if char == key:
				teaList+= value
	
	countTeas = Counter(teaList) #Count the number of times the tea appears
	countTeas = countTeas.items() #Convert to a list of (elem, cnt) pairs
	
	return countTeas

def likedTeas(tea, charList):
	"""Gives a list of people who like a certain tea from a selected group."""
	
	finalCharList = []
	
	for key,values in charTeas.items():
		for item in values:
			if item == tea and key in charList:
				finalCharList.append(key)
	
	finalCharList.sort()
	
	return finalCharList

def popularTeas(teaList, charList):
	"""Gives the needed teas given a list of teas ordered by popularity of a given charList.
	Prints the result.
	"""
	
	sortedTeas = sorted(teaList, key=lambda tup: tup[1], reverse=True)
	
	for tea, count in sortedTeas:
		print (tea + ": " + str(count) + " (" + ", ".join(x for x in likedTeas(tea,charList))+")")


#List of characters
charList = []

#Read input file
#with open("characters.txt") as f:
with open(os.path.join(os.path.dirname(__file__),"charactersTea.txt"), 'r') as f:
	
	for line in f:
		line = line.strip()
		if line == 'Black Eagles':
			charList += blackEagles
		
		elif line == 'Blue Lions':
			charList += blueLions
		
		elif line == 'Golden Deer':
			charList += goldenDeer
		
		elif line == 'Ashen Wolves':
			charList+= ashenWolves
		
		elif line == 'Church':
			charList+= church
		
		elif line == 'Special':
			charList+= special
		
		else:
			charList.append(line)

#Result
print()
print("Here's your shopping list Professor!")
print()
popularTeas(teaCount(charList), charList)
input()
