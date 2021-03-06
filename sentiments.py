"""
This seems to be an example of how to use sentiwordnet
"""
from sentiWordInterface import SentiWordNetCorpusReader, SentiSynset
swn_filename = 'SentiWordNet_3.0.0_20120510.txt'
swn = SentiWordNetCorpusReader(swn_filename)

# Get sentiwordnet scores from wordnet string representation
##print swn.senti_synset('breakdown.n.03')

# Get sentisynsets for a string
##print swn.senti_synsets('slow')
"""[SentiSynset('decelerate.v.01'), SentiSynset('slow.v.02'), \ SentiSynset('slow.v.03'), SentiSynset('slow.a.01'), SentiSynset('slow.a.02'), \ SentiSynset('slow.a.04'), SentiSynset('slowly.r.01'), SentiSynset('behind.r.03')]"""

#Get syn scores for a particular use
"""happy = swn.senti_synsets('happy', 'a')[0]"""
"""
[Synset('happy.a.01')]
"""
##print happy.pos_score
"""
0.625
"""
##print happy.neg_score
"""
0.25
"""
##print happy.obj_score

# Works on sentences using senti_classifier
from senti_classifier import senti_classifier
s1 = ['I could only get out of the house twice today']
s2 = ['I got out of the house twice today']
##sentences = ['The movie was the best movie', 'It was the best acting by the actors']
print s1
pos_score, neg_score = senti_classifier.polarity_scores(s1)
print 'positive:'
print pos_score
print 'negative: '
print neg_score

print s2
pos_score, neg_score = senti_classifier.polarity_scores(s2)
print 'positive:'
print pos_score
print 'negative'
print neg_score

from senti_classifier.senti_classifier import synsets_scores
##print synsets_scores['peaceful.a.01']['pos']
