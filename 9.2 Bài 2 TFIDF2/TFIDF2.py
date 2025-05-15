import os
import math

class Doc:
    '''
    Lớp mô tả một đối tượng văn bản, lớp này có 1 thuộc tính là wordCount kiểu từ điển
    '''

    def __init__(self, filename):
        self.wordCount = dict()
        self.loadWordCountFromFile(filename)

    def loadWordCountFromFile(self, filename):
        '''
        Hàm thực hiện đọc vào file filename và đếm tần suất xuất hiện các từ rồi đưa vào wordCount
        '''
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                words = line.strip().split()
                for word in words:
                    if word in self.wordCount:
                        self.wordCount[word] += 1
                    else:
                        self.wordCount[word] = 1

class TFIDF:
    '''
    Lớp mô tả việc tính chỉ số TFIDF cho các từ trong văn bản dựa trên kho văn bản
    '''

    def __init__(self, corpusPath):
        self.corpusPath = corpusPath
        self.data = dict()
        self.loadCorpus(corpusPath)

    def loadCorpus(self, corpusPath):
        '''
        Hàm đọc các file văn bản trong thư mục corpusPath, xây dựng đối tượng Doc tương ứng và đưa vào data
        '''
        for filename in os.listdir(corpusPath):
            filepath = os.path.join(corpusPath, filename)
            if os.path.isfile(filepath):
                self.data[filename] = Doc(filepath)

    def tf(self, w, d):
        '''
        Tính tf(w,d) = tfw / tfm
        '''
        tfw = d.wordCount.get(w, 0)
        tfm = max(d.wordCount.values()) if d.wordCount else 1
        return tfw / tfm

    def idf(self, w):
        '''
        Tính idf(w) = log(N / (1 + m))
        '''
        N = len(self.data)
        m = sum(1 for doc in self.data.values() if w in doc.wordCount)
        return math.log(N / (1 + m)) if N > 0 else 0

    def tfidf(self, w, d):
        '''
        Tính tfidf(w,d) = tf(w,d) * idf(w)
        '''
        return self.tf(w, d) * self.idf(w)

    def getKTopicWordFromCopus(self, k):
        '''
        Trả lại danh sách k từ khác nhau có chỉ số tfidf cao nhất trong kho văn bản
        '''
        word_tfidf = {}	 	  	      	   	      	     	   	       	 	
        for filename, doc in self.data.items():
            for word in doc.wordCount:
                tfidf_score = self.tfidf(word, doc)
                word_tfidf[word] = max(word_tfidf.get(word, 0), tfidf_score)

        sorted_words = sorted(word_tfidf.items(), key=lambda item: item[1], reverse=True)
        top_k_words = sorted([word for word, score in sorted_words[:k]])
        return top_k_words
