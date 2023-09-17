import PartI_Task1
import PartI_Task2
import PartI_Task3
import PartI_Task4
import PartI_Task5
import PartI_Task6

Scores = PartI_Task1.readFile('scores.txt')
Tiles = PartI_Task1.readFile('tiles.txt')
Dictionary = PartI_Task1.readFile('dictionary.txt')

print("Generating Random Tiles…")
myTiles=PartI_Task5.theChosenSeven(Tiles)
print("Tiles :", end = "  ")
for letter in myTiles:
    print(letter, end="  ")

print("\nScores:", end = "  ")
for letter in myTiles:
    print(PartI_Task3.getLetterScore(letter), end="  ")

word = input("\nEnter a word:\n")
print(PartI_Task6.isValid(word,myTiles,Dictionary))