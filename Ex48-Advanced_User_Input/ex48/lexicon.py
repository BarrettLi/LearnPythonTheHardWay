dir = ('north', 'south', 'east', 'west', 'sown', 'up', 'left', 'right', 'back')
verb = ('go', 'stop', 'kill', 'eat')
stop = ('the', 'in', 'of', 'from', 'at', 'it')
noun = ('door', 'bear', 'princess', 'cabinet')

def get_tuples(word):
    
    low = word.lower()
    if low in dir:
        return ('direction', word)
    elif low in verb:
        return ('verb', word)
    elif low in stop:
        return ('stop', word)
    elif low in noun:
        return ('noun', word)
    elif low.isdigit():
        return ('number', int(word))
    else:
        return ('error', word)

def scan(sentence):
    words = sentence.split()
    return [get_tuples(word) for word in words]
    
