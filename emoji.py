print('______Beginning of Code______')

# OBJECTIVE: retrieve words & map words to emoji
#0 - User Input Stored
Inp = input('Enter string: ')
print('User Input: ' + Inp)
UIList = []
UIList = Inp.split()
#1 - Make dictionary for words
EmojiDict = { 
    'lol' : '😂',  'what' : '🤨', 'high' : '⬆️','no' : '🔴','yes' : '🟢',
    'crying' : '😭', 'kill' : '🔪', 'eat' : '🍽', 'low' : '⬇️', 'confused' : '🤨',
    'cloud' : '☁️', 'sun' : '☀️', 'incorrect' : '❌', 'right' : '✅', 'annoyed' : '😒',
    'whining' : '😫', 'sad' : '😢', 'happy' : '😀', 'smile' : '😁', 'cheese' : '🧀',
    'bus' : '🚌', 'car' : '🚗', 'police' : '🚔', 'lights' : '🚦', 'light': '🚨'
}
#2 - Check for matching words in Inp & EmojiDict.valus()
def EmojiReplace():
    print('  Old list: ' + str(UIList))
    print('  >>Comparing list items to dictionary values...')
    for x in UIList:
        if x in EmojiDict:
            print('      ' + x + ' = ' + str(EmojiDict.get(x)))
            UIList[x.index(x)] = str(EmojiDict.get(x))
            print('      Replaced Successful: ' + UIList[x.index(x)])
        else:
            print('      Sorry, ' + x + ' is not present in this dictionary.')
    print('  <<End of list items.')
    print('  New list: ' + str(UIList))
EmojiReplace()
#3 - Print out results!
print('')
EmojiInp = ''.join(UIList)
print('User Input Emojified: ' + EmojiInp)