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

charGifts = {"Edelgard": ["Armored Bear Stuffy", "Board Game", "Carnation", "Monarch Studies Book"], "Dimitri": ["Ceremonial Sword", "Riding Boots", "Training Weight", "Whetstone"], "Claude": ["Board Game","Book of Crest Designs", "Exotic Spices", "Riding Boots"], "Hubert": ["Coffee Beans", "Board Game", "The History of Fodlan"], "Ferdinand": ["Riding Boots", "Whetstone", "Tea Leaves"], "Linhardt": ["Tasty Baked Treat", "Book of Crest Designs", "Fishing Float"], "Caspar": ["Training Weight", "Whetstone", "Hunting Dagger", "Smoked Meat"], "Bernadetta": ["Pitcher Plant", "Armored Bear Stuffy", "Book of Sheet Music", "Watering Can", "Landscape Paiting", "Dapper Handkerchief"], "Dorothea": ["Book of Sheet Music", "Gemstone Beads", "Stylish Hair Clip"], "Petra": ["Sunflower", "Hunting Dagger", "Exotic Spices", "Smoked Meat"], "Dedue": ["Exotic Spices", "Floral Adornment", "Watering Can"], "Felix": ["Smoked Meat", "Hunting Dagger", "Training Weight", "Ceremonial Sword"], "Ashe": ["Violet", "Legends of Chivalry", "Exotic Spices", "Tasty Baked Treat", "Ancient Coin"], "Sylvain": ["Landscape Paiting", "Dapper Handkerchief", "Board Game"], "Mercedes": ["Lavender", "Tasty Baked Treat", "Goddess Statuette", "Armored Bear Stuffy", "Gemstone Beads"], "Annette": ["Book of Sheet Music", "Stylish Hair Clip", "Arithmetic Textbook"], "Ingrid": ["Riding Boots", "Smoked Meat", "Legends of Chivalry"], "Lorenz": ["Rose", "Floral Adornment", "Tea Leaves", "Book of Sheet Music"], "Raphael": ["Smoked Meat", "Training Weight", "Tasty Baked Treat", "Blue Cheese"], "Ignatz": ["Forget-me-nots", "Ancient Coin", "Landscape Paiting", "Goddess Statuette", "Ceremonial Sword"], "Lysithea": ["Lily", "Armored Bear Stuffy", "Arithmetic Textbook", "Tasty Baked Treat", "Book of Crest Designs"], "Marianne": ["Lily of the Valley", "Dapper Handkerchief", "Floral Adornment", "Armored Bear Stuffy"], "Hilda": ["Anemone", "Gemstone Beads", "Dapper Handkerchief", "Book of Sheet Music", "Stylish Hair Clip", "Armored Bear Stuffy"], "Leonie": ["Hunting Dagger", "Training Weight", "Fishing Float"], "Seteth": ["The History of Fodlan", "Fishing Float", "Dapper Handkerchief"], "Flayn": ["Forget-me-nots", "Tasty Baked Treat", "Armored Bear Stuffy", "Stylish Hair Clip", "Dapper Handkerchief"], "Hanneman": ["Arithmetic Textbook", "Tea Leaves", "Book of Crest Designs", "Dapper Handkerchief"], "Manuela": ["Book of Sheet Music", "Gemstone Beads", "Blue Cheese", "Goddess Statuette"], "Gilbert": ["Goddess Statuette", "Fishing Float", "Ceremonial Sword"], "Alois": ["Sunflower", "Ancient Coin", "Fishing Float", "Floral Adornment"], "Catherine": ["Training Weight", "Whetstone", "Legends of Chivalry", "Blue Cheese"], "Shamir": ["Sunflower", "Exotic Spices", "Coffee Beans", "Hunting Dagger", "Book of Sheet Music"], "Cyril": ["Baby's Breath", "Smoked Meat", "Hunting Dagger", "Watering Can"], "Rhea": ["Landscape Paiting", "Goddess Statuette", "Ancient Coin"], "Yuri": ["Board Game", "Tasty Baked Treat", "Goddess Statuette", "Arithmetic Textbook"], "Balthus": ["Ancient Coin", "Ceremonial Sword", "Whetstone", "Blue Cheese"], "Constance": ["Lily of the Valley", "Tea Leaves", "Arithmetic Textbook", "Book of Crest Designs"], "Hapi": ["Pitcher Plant", "Tasty Baked Treat", "Smoked Meat", "Exotic Spices", "Coffee Beans", "Hunting Dagger"], "Jeritza": ["Rose", "Tasty Baked Treat", "Whetstone", "Hunting Dagger"], "Anna": ["Forget-me-nots", "Exotic Spices", "Coffee Beans", "Blue Cheese", "Landscape Paiting", "Goddess Statuette"]
}

#Functions
def giftCount (charList):
	"""Calculates the number of times a gift is needed for a given list of characters.
	Returns a list with a count per gift.
	"""
	
	giftList = [] #List of gifts needed
	
	for char in charList:
		for key, value in charGifts.items():
			if char == key:
				giftList+= value
	
	countGifts = Counter(giftList) #Count the number of times the gift appears
	countGifts = countGifts.items() #Convert to a list of (elem, cnt) pairs
	
	return countGifts

def likedGifts(gift, charList):
	"""Gives a list of people who like a certain gift from a selected group."""
	
	finalCharList = []
	
	for key,values in charGifts.items():
		for item in values:
			if item == gift and key in charList:
				finalCharList.append(key)
	
	finalCharList.sort()
	
	return finalCharList

def popularGifts(giftList, charList):
	"""Gives the needed gifts given a list of gifts ordered by popularity of a given charList.
	Prints the result.
	"""
	
	sortedGifts = sorted(giftList, key=lambda tup: tup[1], reverse=True)
	
	for gift, count in sortedGifts:
		print (gift + ": " + str(count) + " (" + ", ".join(x for x in likedGifts(gift,charList))+")")


#List of characters
charList = []

#Read input file
#with open("characters.txt") as f:
with open(os.path.join(os.path.dirname(__file__),"characters.txt"), 'r') as f:
	
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
popularGifts(giftCount(charList), charList)
input()
