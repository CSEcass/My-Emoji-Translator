print('______Beginning of Code______')

# OBJECTIVE: retrieve words & map words to emoji
#0 - User Input Stored
Inp = input()
UserInp = Inp.split
#1 - Make dictionary for words
EmojiDict = { 
    'lol' : '😂', 
    'what' : '🤨',
    'high' : '⬆️',
    'no' : '🔴',
    'yes' : '🟢'
}
print(EmojiDict['high'])
#2 - Replace words with emojis
for UserInp in EmojiDict.items():
    print()