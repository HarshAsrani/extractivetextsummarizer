import re
import nltk
import heapq  
nltk.download('punkt') #Only to be needed the first time the program is run

text = input("Enter some text :")
p = int(input("Enter the number of sentences to summarize to :"))

formatted_article_text = re.sub('[^a-zA-Z]', ' ', text )
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

sentence_list = nltk.sent_tokenize(text)

stopwords = nltk.corpus.stopwords.words('english')

#Making a word frequency dictionary
word_frequencies = {}  
for word in nltk.word_tokenize(formatted_article_text.lower()): 
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

maximum_frequncy = max(word_frequencies.values())

#Dividing the frequencies of all the words with the maximum frequency to make convert to relative frequency
for word in word_frequencies.keys():  
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

sentence_scores = {}

#Giving scores to each sentence based on the words present in the sentence, and their scores
for sent in sentence_list:  
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]

#Compiling the p sentences with the largest scores
summary_sentences = heapq.nlargest(p, sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentences)  

print(summary)