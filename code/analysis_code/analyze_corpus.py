from collections import Counter
from collections import defaultdict
import numpy as np
import re

def termFreq(infile, keys, M): 
    # see https://towardsdatascience.com/tf-idf-for-document-ranking-from-scratch-in-python-on-real-world-dataset-796d339a4089
    '''@input M number of words in one document
    tf(t,d) = count of a word in one document / number of words in one document
    @result 
    '''    
    line = infile.readline() 
    while line:
        line = re.sub('[^0-9a-zA-Z]+', '', line)
        words = line.strip().split()
        words = [w for w in words if w.isalpha()] 
        for k in keys: 
            if k in line: 
                counter[k] += 1  
        line = infile.readline()
    result = {}
    for k in counter.keys(): 
        result[k] = counter[k]*1.0/M
    return result

def docFreq(keys, directory): 
    ''' @input keys : unique words in a directory, i.e. emos
    directory : folder to the corpus
    tf(t,d) = count of a word in corpus / number of words in corpus
    df(t) = occurrence of t in documents
    @return : counter of word : doc freq
    '''
    read_files = glob.glob(directory + '*.txt')
    counter = Counter({k:0 for k in keys})
   
    for infile in read_files:
        with open(infile, 'r', errors='replace') as f:
            counter += getFreq(infile, counter)
    return counter 
     
def getFreq(infile, counter): 
    ''' @input infile : article in txt format
    @return counter : keys and their occurances 
    '''
    line = infile.readline() 
    while line:
        for k in keys: 
            if k in line: 
                counter[k] += 1  
        line = infile.readline()
    return counter  

def invDocFreq(counter, N): 
    ''' @input keys : unique words in a directory
    N : number of words in a dictory
    idf(t) = log(N/(df + 1))
    inverse document frequency 
    @return counter of words-idf 
    ''for k in counter.keys(): '  
    result = {}
    for k in counter.keys(): 
        result[k] = np.log(N*1.0 / (counter[k] + 1))  
    return result

def tfIdf(keys, N): 
    ''' @input keys : unique words in a directory
    tf-idf(t, d) = tf(t, d) * log(N/(df + 1))
    @return counter of words- tf-idf 
    ''' 
    tf = termFreq(keys, N)
    idf = invDocFreq(keys, N)
    counter = Counter() 
    for k in keys: 
        result[k] = tf[k] * idf[k] 
    return result
    
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
    return lengths

def analyzeWordLength(doc): 
    '''parameter : doc is an article by a single author
    return : counter of word lengths
    '''
    counter = Counter([len(token.lemma_) for token in doc])
    return counter

def analyzeWordSize(doc): 
    '''parameter : doc is an article by a single author
    return : counter of word lengths
    '''
    sz = 0
    for token in doc:
        if (token.text).isalpha():
            sz += 1
    return sz 

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
    '''Filter by presence in emotion words lexicon'''
    # emo tokens
    totalEmos = []
    # emo word or phrase start with not
    emoWords = defaultdict(int)
    
    # get all emotional words  
    totalEmos += [token for token in doc if token.text.lower() in emos]
    for e in totalEmos: 
        sent = e.sent.text
        i = sent.find(e.lemma_)
        if i == 0: 
            emoWords[e.lemma_] += 1  
        else: 
            if 'not' == sent[i-1]: 
                phrase = 'not ' + e.lemma_
                emoWords[phrase] += 1
            elif i-2 >= 0 and 'not' == sent[i-2]: 
                phrase = 'not ' + e.lemma_
                emoWords[phrase] += 1 
            elif 'not' in sent[:i]: 
                phrase = '! ' + e.lemma_
                emoWords[phrase] += 1
            else: 
                emoWords[e.lemma_] += 1  
    return Counter(emoWords)

def scoreEmotion(doc, emos):
    '''Article score by occurances in emotion words lexicon'''
    sz = analyzeWordSize(doc)
    counter = Counter([token.text.lower() for token in doc if token.text.lower() in emos])    
    num = sumCounter(counter)
    return float(num/sz)

def scoreEmos(line, emos): 
    '''Use string functions to find emotion words in a string'''
    words = line.strip().split()
    words = [w for w in words if w.isalpha()]
    emoWords = [w for w in words if w in emos]
    if len(words) > 0: 
        return float(len(emoWords))/ len(words)
    else: 
        return None 

def scoreArticle(infile, emos): 
    '''
    compute the emotion scores of input files
    infile : name of file containing articles 
    result : list of scores
    '''
    line = infile.readline()
    result = []
    while line:
        s = scoreEmos(line, emos)
        if s:
            result.append(s)
        line = infile.readline()
    return result

def totalWords(infile): 
    '''
    compute total number of words in the file
    '''
    line = infile.readline()
    count = 0
    while line:
        words = line.split(' ') 
        count += len(words)
        line = infile.readline()
    return count

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
 
