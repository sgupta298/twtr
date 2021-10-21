"""Top-level package for twtr."""

__author__ = """Sanjay Kumar Gupta"""
__email__ = 'sanjaykrgupta298@gmail.com'
__version__ = '0.1.0'

import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import nltk
nltk.download('stopwords')
import string

def remove_punctuation(text):
    '''a function for removing punctuation'''
    import string
    # replacing the punctuations with no space, 
    # which in effect deletes the punctuation marks 
    translator = str.maketrans('', '', string.punctuation)
    # return the text stripped of punctuation marks
    return text.translate(translator)

def fix_stopwords(text):
    sw = stopwords.words('english')
    '''a function for removing the stopword'''
    # removing the stop words and lowercasing the selected words
    text = [word.lower() for word in text.split() if word.lower() not in sw]
    # joining the list of words with space separator
    return " ".join(text)    

stemmer = SnowballStemmer("english")

def stemming(text):    
    '''a function which stems each word in the given text'''
    text = [stemmer.stem(word) for word in text.split()]
    return " ".join(text)     
def cleanData(csvpath):
    df=pd.read_csv(csvpath)
    df['text'] = df['text'].apply(remove_punctuation)
    df['text'] = df['text'].apply(fix_stopwords)
    df['text'] = df['text'].apply(stemming)
    df.to_csv('new_data.csv',index=False)