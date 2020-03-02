"""histogram.py"""

# ununique_words = 0
def wordHistogram():
    word_histogram = {}
    with open('ununique-words.txt', 'r') as file:

        #loop through file
        for line in file:
            #loop through lines
            for word in line.split(): #split into single words
                #I dont really need this could have just kept it word.
                single_word = word
                # an entery into word histogram = word_histogram .get (from the key) and + 1 the value
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
