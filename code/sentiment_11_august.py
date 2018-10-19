import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
def word_feats(words):
    return dict([(word,True) for word in words])
positive_vocab=['awsome', 'outstanding','fantastic']
negative_vocab=['bad','terrible','hate']
neutral_vocab=['movie','is','was','actors']

positive_features=[(word_feats(pos),'pos') for pos in positive_vocab]
negative_features=[(word_feats(neg),'neg') for neg in negative_vocab]
neutral_features=[(word_feats(neu),'neu') for neu in neutral_vocab]

train_set=negative_features+positive_features+neutral_features
classifier=NaiveBayesClassifier.train(train_set)
#predict
neg=0
pos=0
#sentence="Awsome movie ,I like it"
sentence=input("enter your text:")
sentence=sentence.lower()
words=sentence.split(' ')
for word in words:
    classResult=classifier.classify(word_feats(word))
    if classResult=='neg':
        neg=neg+1
    if classResult=='pos':
        pos=pos+1
print('positive: '+str(float(pos)/len(words)))
print('negative: '+str(float(neg)/len(words)))
