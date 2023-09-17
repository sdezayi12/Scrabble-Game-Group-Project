import PartI_Task1
import PartI_Task2
import PartI_Task4
import PartI_Task5

Scores = PartI_Task1.readFile('scores.txt')
Tiles = PartI_Task1.readFile('tiles.txt')
Dictionary = PartI_Task1.readFile('dictionary.txt')

def isValid(word, myTiles, Dictionary):
    task2 = PartI_Task2.onlyEnglishLetters(word)
    while task2 == False:

        print("Only use English letters…")
        word = input('Enter a word: ')
        task2 = PartI_Task2.onlyEnglishLetters(word)
    validLetters = PartI_Task5.canBeMade(word, myTiles)

    if validLetters == True:
        if word.upper() not in Dictionary:
            print("There is no such word in the dictionary")
            word = input('Enter a word: ')
            return isValid(word,myTiles,Dictionary)
        else:
            print("You got it right, this is a valid word")
            return(f'Score of this word is: {PartI_Task4.getWordScore(word)} ')
    else:
        print("the word uses invalid letters")
        word = input('Enter a word: ')
        return isValid(word, myTiles, Dictionary)

#this is for testing purposes please uncomment when running the tests
#myTiles=PartI_Task5.theChosenSeven(Tiles)
#print (myTiles)
#word=input("Please enter in a word")
#print(isValid(word,myTiles,Dictionary))