import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn



def swnScore(sentence):
	
	x=sentence.split()
	print (x)
	score=[]
	total=0; #total swn score of a tweet
	for i in range(len(x)):
		if(len(list(swn.senti_synsets(x[i])))>0):
			#if word is found in sentiword corpus
			pos=(list(swn.senti_synsets(x[i]))[0]).pos_score()
			neg=(list(swn.senti_synsets(x[i]))[0]).neg_score()
			temp=1+pos-neg
			print (temp)
			total+=temp
			#if():





k=input()
print (k)
swnScore(k)