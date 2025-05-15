import os
import math

class Doc:
    def __init__(self, filename):
        self.wordCount = dict()
        self.loadWordCountFromFile(filename)

    def loadWordCountFromFile(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                words = line.strip().split()
                for word in words:
                    self.wordCount[word] = self.wordCount.get(word, 0) + 1

class TFIDF:
    def __init__(self, corpusPath):
        self.corpusPath = corpusPath
        self.data = dict()
        self.loadCorpus(corpusPath)

    def loadCorpus(self, corpusPath):
        for filename in os.listdir(corpusPath):
            filepath = os.path.join(corpusPath, filename)
            if os.path.isfile(filepath):
                self.data[filename] = Doc(filepath)

    def tf(self, w, d):
        tfw = d.wordCount.get(w, 0)
        tfm = max(d.wordCount.values()) if d.wordCount else 1
        return tfw / tfm

    def idf(self, w):
        N = len(self.data)
        m = sum(1 for doc in self.data.values() if w in doc.wordCount)
        return math.log(N / (1 + m))

    def tfidf(self, w, d):
        return self.tf(w, d) * self.idf(w)

    def getKTopicWordFromCopus(self, k):
        word_tfidf = {}	 	  	      	   	      	     	   	       	 	
        for filename, doc in self.data.items():
            for word in doc.wordCount:
                tfidf_score = self.tfidf(word, doc)
                word_tfidf[word] = max(word_tfidf.get(word, 0), tfidf_score)

        sorted_words = sorted(word_tfidf.items(), key=lambda item: item[1], reverse=True)
        top_k_words = sorted([word for word, score in sorted_words[:k]])
        return top_k_words
