


import sys
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn import svm
import re

count_vect = CountVectorizer(lowercase=False, ngram_range=(1, 2), min_df=0.3, stop_words='english')
tfidf_transformer = TfidfTransformer(use_idf=False, smooth_idf=True)

train_data = []  # data store for training data, list of strings
test_data = []  # data store for test data, list of strings
train_y = []  # data store for target variables for training, list of A(a)pples

# reading trainig data from text files
for line in open('apple-computers.txt', encoding="utf8"):
    if len(line.strip()) > 0:  # skip empty lines
        train_data.append(line.strip().strip('. '))
        train_y.append('computer-company')
for line in open('apple-fruit.txt', encoding="utf8"):
    if len(line.strip()) > 0:  # skip empty lines
        train_data.append(line.strip('. '))
        train_y.append('fruit')

# reading test data from STDIN
for line in sys.stdin.readlines():
    line = re.sub('\d', '', line)
    if len(line.strip()) > 0:  # skip empty lines
        test_data.append(line.strip('. '))

# training set text processing
X_train_counts = count_vect.fit_transform(train_data)
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

# training set text processing
X_new_counts = count_vect.transform(test_data)
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

svm = svm.SVC(C=1.0, kernel='linear', degree=3, gamma='auto')
clf_svm = svm.fit(X_train_tfidf, train_y)
predicted_svm = clf_svm.predict(X_new_tfidf)
for results in predicted_svm: print(results)