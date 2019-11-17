def analyzePOS(doc):  
    '''
    parameter : doc is an article by a single author
    return : counter of POS tags
    '''
    counter = Counter([token.pos_ for token in doc])
    return counter

def rankCounter(counter): 
    '''
    parameter : counter of an article by a single author
    '''
    if len(counter) == 0:
        return None, None
    else:
        c = counter.most_common(20)
        return zip(*c)

def sumCounter(counter): 
    '''
    parameter : counter
    return : sum of counter values
    '''
    return sum(counter.values())

    
def analyzeSentence(doc):
    '''
    parameter : doc is an article by a single author
    assume sentence length is measured by number of words
    return : counter of sentence lengths'''
    lengths = Counter([len(sentence) for sentence in doc.sents])
    for sentence in doc.sents: 
        print("SENTENCE : " + sentence.text)
    return lengths

def analyzeWordLength(doc): 
    '''parameter : doc is an article by a single author
    return : counter of word lengths
    '''
    counter = Counter([len(token.lemma_) for token in doc])
    return counter

def analyzePunctuation(doc): 
    '''parameter: doc is an article by a single author
    return : counter of punctuation symbols '''
    counter = Counter([token.text for token in doc if token.pos_=='PUNCT'])
    return counter

def analyzePronoun(doc): 
    '''parameter: doc is an article by a single author
    return : counter of all pronoun '''
    counter = Counter([token.text.lower() for token in doc if (token.tag_== 'PRP' or 
                       token.tag_== 'PRP$' or 
                       token.tag_== 'WP' or 
                       token.tag_== 'WP$')])
    return counter

def analyzePronounPRP(doc):
    '''parameter: doc is an article by a single author
    return : counter of PRP '''
    counter = Counter([token.text.lower() for token in doc if token.tag_== 'PRP'])
    return counter

def analyzePronounPRPD(doc):
    '''parameter: doc is an article by a single author
    return : counter of PRP '''
    counter = Counter([token.text.lower() for token in doc if token.tag_== 'PRP$'])
    return counter

def analyzePronounWP(doc):
    '''parameter: doc is an article by a single author
    return : counter of WP '''
    counter = Counter([token.text.lower() for token in doc if token.tag_== 'WP'])
    return counter

def analyzePronounWPD(doc):
    '''parameter: doc is an article by a single author
    return : counter of WP$ '''
    counter = Counter([token.text.lower() for token in doc if token.tag_== 'WP$'])
    return counter

def analyzePronounCategories(doc):
    '''parameter: doc is an article by a single author
    return : counter of all pronoun categories '''
    counter = Counter([token.tag_ for token in doc if (token.tag_== 'PRP' or 
                       token.tag_== 'PRP$' or 
                       token.tag_== 'WP' or 
                       token.tag_== 'WP$')])
    return counter

def analyzeVerb(doc): 
    '''parameter: doc is an article by a single author
    return : counter of verb words '''
    counter = Counter([token.lemma_ for token in doc if token.pos_=='VERB'])
    return counter

def analyzeVerbRoot(doc): 
    '''parameter: doc is an article by a single author
    return : counter of verb words '''
    counter = Counter([token.lemma_ for token in doc if token.pos_=='VB'])
    return counter


def loadEmotionWords(filename):
    '''Load list of emotion words'''
    with open(filename, 'r') as f:
        lines = f.read() 
    words = set(lines.strip().split())
    return words    

def analyzeEmotionWords(doc, emos): 
    counter = Counter([token.text.lower() for token in doc if token.text.lower() in emos])    
    return counter

