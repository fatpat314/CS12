"""dictionary_words.py"""
import sys as sys
from random import randint

if __name__ == "__main__":
    args = sys.argv
    #accapt user argument
    num_words = args[1]
    #access file
    my_file = open("/usr/share/dict/words")
    #split into lines
    lines = my_file.readlines()

    for i in range(int(num_words)):


        random_index = randint(0, len(lines)-1)


        rand_item = lines[random_index]
        print(rand_item)

my_file.close()
