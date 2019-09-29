#Most common words

#import collections module to do some operations on dictionaries
import collections 

#define the file path to read the text from a file
file=open('/home/prasanth/Desktop/Data Science/Word_count/98-0.txt', encoding="utf8")

#stopwords
stopwords = set(line.strip() for line in open('/home/prasanth/Desktop/Data Science/Word_count/stopwords'))

#Initiate a dictionary to store the keys and values
wordcount={}

#Convert all words to lower case, split the words from paragraphs or sentences and remove punctuations
#Read every word and if the word not in the dictionary wordcount, add the word to wordcount. And if it already there in the dictionary increase the wordcount by 1.
for word in file.read().lower().split():
	word = word.replace(".","")
	word = word.replace(",","")
	word = word.replace("\"","")
	word = word.replace("“","")
	if word not in stopwords:
		if word not in wordcount:
			wordcount[word] = 1
		else:
			wordcount[word] += 1

p = collections.Counter(wordcount)

#print top 10 most common word in the file
for word, count in p.most_common(10):
	print(word, ":", count)