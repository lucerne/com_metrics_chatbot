from collections import Counter
from collections import defaultdict

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


def analyzeVerbs(doc): 
    LinkingVerbs = set(['be', 'become', 'seem'])
    HelpingVerbs = set(['be', 'can', 'may', 'must', 'shall', 'will'])

    # verb token
    totalVerbs = []
    # for action verbs
    action = defaultdict(int)
    # for linking verbs
    linking = defaultdict(int)
    # for helping verbs
    helping = defaultdict(int)
    helpingMain = defaultdict(int)
    # dictionary with words that didn't fit categories for some reason...
    others = defaultdict(int)
    
    
    # adds words to totalVerbs if they are verbs
    totalVerbs += [token for token in doc if (token.pos_ == "VERB")]

    for verb in totalVerbs:
        lefts = [v for v in verb.lefts] 
        if len(lefts) == 0: 
            continue 
        left = lefts[0]
        if left.lemma_ in HelpingVerbs: 
            helping[left.lemma_] += 1
            helpingMain[verb.lemma_] += 1        
        elif verb.lemma_ in LinkingVerbs: 
            linking[verb.lemma_] += 1
        else: 
            action[verb.lemma_] += 1            
    
    return Counter(action), Counter(linking), Counter(helping), Counter(helpingMain)



