# generate_scores.py compiles, trains, and executes tweet spam detection.
# Feb 11, 2020
__author__ = 'Trevor Nelson'

import gensim
import pandas as pd
from os import path
from joblib import dump, load
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.neural_network import MLPRegressor

train_size = 5000

model = None
if not path.exists("gnews.embedding") or not path.exists("gnews.embedding.vectors.npy"):
    print("Compiling vectors...")
    model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
    model.save('gnews.embedding')
else:
    print("Loading vectors...")
    model = gensim.models.KeyedVectors.load('gnews.embedding')

# nltk.download('stopwords')
# Load stopwords
stopwords = set(stopwords.words('english'))
# https://github.com/mmihaltz/word2vec-GoogleNews-vectors
pad_to_length = 32


def split_sanitize(sentence):
    sentence = str(sentence)
    tokens = word_tokenize(sentence)
    filtered_sentence = [w for w in tokens if not w.lower() in stopwords]
    filtered_sentence += [""] * (pad_to_length - len(filtered_sentence))
    return filtered_sentence[:pad_to_length]


def embed_tokens(tokens):
    embedding = []
    for token in tokens:
        if token in model:
            embedding.extend(model[token])
        elif token.lower() in model:
            embedding.extend(model[token.lower()])
    embedding.extend((pad_to_length - len(embedding) // 300) * ([0.0, ] * 300))
    return embedding


clf = None
retrain = False
if not path.exists("classifier.joblib") or retrain:

    print("Training network...")

    spam = pd.read_csv('data/spam.csv', encoding="utf-8")
    notspam = pd.read_csv('data/notspam.csv', encoding="latin")

    X = []
    y = []

    for tweet in spam.iloc[0:train_size, 7]:
        # print(str(tweet))
        embedded = embed_tokens(split_sanitize(str(tweet)))

        if len(embedded) != 9600:
            print(embedded)
            break

        X.append(embedded)
        y.append(1.0)

    print("Loaded spam")

    for tweet in notspam.iloc[0:train_size, 5]:
        # print(str(tweet))
        embedded = embed_tokens(split_sanitize(str(tweet)))

        X.append(embedded)
        y.append(0.0)

    print("Loaded notspam")

    clf = MLPRegressor(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(20, 10), random_state=1, verbose=True)

    clf.fit(X, y)

    dump(clf, "classifier.joblib")
else:
    print("Loading classifier...")
    clf = load("classifier.joblib")

if not path.exists("leaderboard.txt"):
    print("Computing scores...")
    leaderboard = []
    with open("data/words_alpha.txt", "r") as words:
        for word in words:
            score = clf.predict([embed_tokens(split_sanitize(word.strip()))])[0]
            if score < 0.5:
                continue
            for i in range(len(leaderboard)):
                s = leaderboard[i][1]
                if score > s:
                    leaderboard.insert(i, (word.strip(), score))
                    break
            if len(leaderboard) == 0:
                leaderboard.append((word.strip(), score))
            leaderboard = leaderboard[:100]

        print(leaderboard)

while True:
    tweet = input("Enter a tweet to evaluate:\n> ")
    if tweet == "exit":
        break
    print(str(clf.predict([embed_tokens(split_sanitize(tweet))])[0] * 100) + "% spaminess")
