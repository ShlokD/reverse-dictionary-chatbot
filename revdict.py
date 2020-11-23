import nltk
import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from numpy.linalg import norm
import numpy as np

nltk.download('punkt')
nltk.download('stopwords')


def find_words_by_query(query):
    f=open('wordset.json')
    data = json.load(f)

    stop_words = set(stopwords.words('english'))
    words_token = word_tokenize(query)
    tokenized_query = [w for w in words_token if not w in stop_words]
    print(tokenized_query)

    similarities = []
    answers = []
    i=0
    similarity = 0
    answer = None
    for key,value in data.items():
        vectorA = []
        vectorB = []
        features = list(set(value)|set(tokenized_query))
        for w in features:
            if w in value:
                vectorA.append(1)
            else:
                vectorA.append(0)
            if w in tokenized_query:
                vectorB.append(1)
            else:
                vectorB.append(0)
        cosine_sim = np.dot(vectorA, vectorB)/(norm(vectorA)*norm(vectorB))
        if cosine_sim > similarity:
            answer = key
            similarity = cosine_sim
            answers.append(answer)
        similarities.append(cosine_sim)
    return answers
