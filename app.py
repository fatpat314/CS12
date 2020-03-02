from flask import Flask
# from histogram import wordHistogram
from sample import sample_by_frequency
from markov_chain import MarkovChain
# from dictionary_words import lines
app = Flask(__name__)

@app.route('/')
def generate_words():
    my_file = open("./ununique-words.txt")
    lines = my_file.readlines()
    # print(lines)

    word_list = []

    for line in lines:
        for word in line.split():
            word_list.append(word)
    # myhistogram = wordHistogram()
    # sentence = ""
    markovchain = MarkovChain(word_list)

    # word = sample_by_frequency(myhistogram)

    '''num_words = 10
    for i in range(num_words):
        word = sample_by_frequency(myhistogram)
        sentence += " " + word

    return sentence'''

    return markovchain.walk(10)


if __name__ == '__main__':
    app.run()
