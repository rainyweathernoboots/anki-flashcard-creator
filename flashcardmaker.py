import random
with open('wordlist.txt') as f:
    targetWords = f.read().split()

def sweepTarget(text):
    for word in targetWords:
        if word in text.split():
            return True
        else: 
            continue    
    return False

def clozify(text):
    sentParse = text.split() #['turns', 'the', 'sentence', 'into', 'something', 'like', 'this']
    wordsHere = [] #makes a list which will track which of our target words appears in the sentence
    for word in targetWords: 
        if word in sentParse:
            wordsHere.append(word) #puts all the words which do appear into wordsHere
    if len(wordsHere) == 0: #checks that at least one target word appears; if not, returns False
        return False
    else:
        givenWord = random.choice(wordsHere) #picks a random target word
        occurences = [index for index, word in enumerate(sentParse) if word == givenWord] #iterates over words as [(0, 'turns'), (1, 'the'), ...] 
        sentParse[random.choice(occurences)] = '{{c1::'+givenWord+'}}'
        #need to replace a random occurence from wordsHere, in a random position in sentParse, with {{c1:missing}} 
        return [' '.join(sentParse), givenWord]

def importSents(file):
    cards = file.split('\n')
    newCards = []
    for i in cards:
        notes = i.split('	')
        print(notes)
        if i != '':
            if type(clozify(notes[0])) == list:
                notes.extend(clozify(notes[0]))
                newCards.append('|'.join(notes))
    flashcards = '\n'.join(newCards)
    with open('deck.txt', 'w') as file:
        file.write(flashcards)

with open('exSents.txt') as file:
    importSents(file.read())