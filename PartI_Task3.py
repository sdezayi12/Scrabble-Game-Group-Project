import PartI_Task1

def getLetterScore(letter, Scores = PartI_Task1.readFile("scores.txt")):
    valid=False
    for pair in Scores:
        value = pair.split(' ')
        if value[0] == letter.upper():
            value[1] = int(value[1])
            valid=True
            return (value[1])
    if valid==False:
        return 0

#this is for testing purposes please uncomment when running the tests
#print(getLetterScore('H'))
#print(getLetterScore('3'))
#print(getLetterScore('AB'))