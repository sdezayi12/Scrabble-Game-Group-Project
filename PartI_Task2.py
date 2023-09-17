def onlyEnglishLetters(word):
    if word == '&&&':
        print('Thanks for using this application, better luck next time!!!')
        exit(0)
    try:
        if not isinstance(word, str):
            return False
        return word.isalpha()
    except:
        return False

#this is for testing purposes please uncomment when running the tests
#print(onlyEnglishLetters('HELLO'))
#print(onlyEnglishLetters('HE LLO'))
#print(onlyEnglishLetters('HE3LLO'))