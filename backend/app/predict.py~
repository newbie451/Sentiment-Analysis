import pickle
import re,csv,nltk
from nltk.corpus import stopwords
from sys import argv
from sys import argv

string = []
for line in argv[1:]:
    string.append(line)
test_string = " ".join(str(i) for i in string)

f1 = open('/home/prathamsh/ML/classifier.pickle')
classifier = pickle.load(f1)

f2 = open('/home/prathamsh/ML/featurelist.pickle')
featureList = pickle.load(f2)

def clean_tweet(tweet):
    tweet = tweet.lower()
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    tweet = re.sub('[\s]+', ' ', tweet)
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    tweet = tweet.strip('\'"')
    return tweet

def replaceTwoOrMore(s):
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)

stop_words = stopwords.words('english')


def extract_features(tweet):
    tweet_words = set(tweet)
    features = {}
    for word in featureList:
        features['contains(%s)' % word] = (word in tweet_words)
    return features


def getFeatureVector(tweet):
    featureVector = []
    words = tweet.split()
    for w in words:
        w = replaceTwoOrMore(w)
        w = w.strip('\'"?,.')
        val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
        if(w in stop_words or val is None):
            continue
        else:
            featureVector.append(w.lower())
    return featureVector

def main(test_string):
	processedTestTweet = clean_tweet(test_string) 
	value = classifier.classify(extract_features(getFeatureVector(processedTestTweet)))
	if value=='0':
    		return "Negative"
	elif value=='1':
    		return "Positive"
	f1.close()
	f2.close()


