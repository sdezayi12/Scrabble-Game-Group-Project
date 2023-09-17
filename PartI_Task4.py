import PartI_Task1
import PartI_Task3

def getWordScore(word):
    totalScore = 0
    for char in word:
        point = PartI_Task3.getLetterScore(char, PartI_Task1.readFile("scores.txt"))
        if point == 0:
            return 0
        else:
            totalScore += point
    return(totalScore)

#this is for testing purposes please uncomment when running the tests
#print(getWordScore('hi5'))
#print(getWordScore('HI'))
#print(getWordScore('hi'))
