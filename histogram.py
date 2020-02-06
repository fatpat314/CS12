"""histogram.py"""

# ununique_words = 0
def wordHistogram():
    word_histogram = {}
    with open('ununique-words.txt', 'r') as file:

        #loop through file
        for line in file:
            #loop through lines
            for word in line.split(): #split into single words
                # word_histogram = {}
                single_word = word
                word_histogram[single_word] = word_histogram.get(single_word, 0) + 1

    return word_histogram

    # unique Words
def ununiqueWords(histogram):
    ununique_words = 0

    #loop through word_histogram for each word with a key of 1
    for word in histogram.keys():
        #if word frequency == 1
        if histogram[word] == 1:
            #increse counter
            ununique_words += 1
    print(f"There are {ununique_words} unique words.")

    #frequency
def frequency(word, histogram):
    #return the frequency of the given "word" in the "histogram"
    return histogram[word]


#print(f"the frequency of your word is {frequency('the', wordHistogram())}")
#ununiqueWords()







# filename = "ununique-words.txt"
# filehandle = open(filename, "r")
# lines = filehandle.readlines()
#
# word_histogram = {}
#
# for word in lines:
#     single_word = word.split(";")
#     # word = word.rstrip()
#     word_histogram[word] = word_histogram.get(single_word, 0) + 1
#
# print(word_histogram)
