import random

def readFile(filename):
    file = None
    try:
        file = open(filename,'r')
        contents = []
        for line in file:
            line = line.strip()
            contents.append(line)
        return contents
    except FileNotFoundError:
        print(f"{filename} does not exist")
        return []
    except:
        print(f"Error processing {filename}")
        return []
    finally:
        if file is not None:
            file.close()

#this is for testing purposes please uncomment when running the tests
#Tiles = print(readFile('tiles.txt'))
#Scores = print(readFile('scores.txt'))
#Dictionary = print(readFile('dictionary.txt'))


