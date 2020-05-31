# extractivetextsummarizer
A basic extractive text summarizer which uses nltk, heapq and re.

This summarizer can be used to create summaries of the given input based on the word frequencies and the sentence scores.

Each sentence is converted in to tokens, and then based on the relative frequencies of the words, each word is scored.

The sentence score is then made to be the sum total of the scores of the words present in the words.

The sentences with the highest scores are combined to make a summary of n sentences, where n is the number of sentences the summary should have.

The text, as well as the number of sentences in the summary are provided by the user.
