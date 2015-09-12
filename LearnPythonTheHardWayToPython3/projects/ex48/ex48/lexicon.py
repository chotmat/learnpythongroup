def scan(sentence):
    """
    Scan through each word of a sentence and then
    turn them into lexicon tuples
    """
    words = sentence.split()
    lexicons = []

    directions = ['north', 'south', 'east','west',
                 'down', 'up', 'left', 'right', 'back']    

    verbs = ['go', 'stop', 'kill', 'eat']

    stops = ['the', 'in', 'of', 'from', 'at', 'it']

    nouns = ['door', 'bear', 'princess', 'cabinet']

    for word in words:
        lWord = word.lower()
        if lWord in directions:
            lexicons.append(('direction', word))
        elif lWord in verbs:
            lexicons.append(('verb', word))
        elif lWord in stops:
            lexicons.append(('stop', word))
        elif lWord in nouns:
            lexicons.append(('noun', word))
        elif lWord.isdigit():
            lexicons.append(('number', int(word)))
        else: lexicons.append(('error', word))

    return lexicons
    
