""" sample.py """
from random import randint

#Test text
text = 'one fish two fish red fish blure fish'
#histogram
word_counts = {'one':1, 'fish':4, 'two':1, 'red':1, 'blue':1}

#function accepts a histogram as input.
def sample_by_frequency(histogram):
    #setting random_index as random int from 0 to the sum of the object value -1
    random_index = randint(0, sum(histogram.values())-1)
    #setting start as 0
    start = 0
    #loop through histograms key, value pairs and for the key of "word" and value of "count"
    for word, count in histogram.items():
        #setting end as start plus the count
        end = start + count
        #if random_index is >= start and random_index < end:
        if random_index >= start and random_index < end:
            return word
            
        start = end

print(sample_by_frequency(word_counts))
