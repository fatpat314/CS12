from flask import Flask
from histogram import wordHistogram
from sample import sample_by_frequency
# from dictionary_words import lines
app = Flask(__name__)

@app.route('/')
def generate_words():
    # my_file = open("./ununique-words.txt")
    # lines = my_file.readlines()
    myhistogram = wordHistogram()
    sentence = ""

    # word = sample_by_frequency(myhistogram)

    num_words = 10
    for i in range(num_words):
        word = sample_by_frequency(myhistogram)
        sentence += " " + word

    return sentence


if __name__ == '__main__':
    app.run()
