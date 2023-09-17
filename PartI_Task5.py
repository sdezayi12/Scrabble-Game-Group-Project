import random
import PartI_Task1
Tiles=PartI_Task1.readFile('tiles.txt')
#This all one task(5) for choose 7 random unique tiles with at least one vowel

def theChosenSeven(Tiles):
    secretSeven = []
    i = 0
    while i < 7:
        i += 1
        number = random.randint(0, 97)
        secretSeven.append(number)
    secretSeven = set(secretSeven)
    while len(secretSeven) < 7:
        number = random.randint(0, 97)
        secretSeven = list(secretSeven)
        secretSeven.append(number)
        secretSeven = set(secretSeven)
    secretSeven = list(secretSeven)
    myTiles = []
    for value in secretSeven:
        myTiles.append(Tiles[value])
    return myTiles

def canBeMade(word, myTiles):
    myLetters=myTiles.copy()
    validLetter = True
    for char in word.upper():
        if char not in myLetters:
            validLetter = False
            break
        else:
            myLetters.remove(char)
    if validLetter == True:
        return True
    else:
        return False

#this is for testing purposes please uncomment when running the tests
#myTiles=theChosenSeven(Tiles)
#print(myTiles)
#word=input('Please enter a word: ')
#print(canBeMade(word, myTiles))


