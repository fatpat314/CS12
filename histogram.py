"""histogram.py"""
word_histogram = {}
with open('ununique-words.txt', 'r') as file:
        #word_histogram = {}
    #loop through file

    for line in file:
        #loop through lines
        for word in line.split(): #split into single words
            # word_histogram = {}
            single_word = word
            word_histogram[single_word] = word_histogram.get(single_word, 0) + 1

print(word_histogram)

# unique Words

ununique_words = 0

for word in word_histogram.keys():
    if word_histogram[word] == 1:
        ununique_words += 1
print(f"There are {ununique_words} unique words: ")

#frequency
def frequency(word, histogram):

    return histogram[word]


print(frequency("the", word_histogram))








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
