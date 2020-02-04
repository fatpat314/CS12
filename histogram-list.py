"""histogram-list.py"""
word_histogram = []

def wordHistogram():
    num = 1
    num2 = 0
    with open('ununique-words.txt', 'r') as file:

        # loop through file
        for line in file:
            #loop through lines
            for word in line.split(): #split into single words
                word_histogram.append([(word)])
                print(word,num)
                for list in word_histogram:
                    if list[num2] == word_histogram[num2][num2]:
                        num +=1
            num2 +=1
                # word_histogram[1][1] = new_histogram


            # for list in word_histogram:

                # print(word_histogram)

                # if list[num2] in word_histogram[num2]:
                #     print(list[num2])
                #     if num2 < len(word_histogram)-1:
                #         num2+=1
                        # num2-1
                        # print(word_histogram[num2])
                    # if num2 == len(word_histogram):
                        # num2 = len(word_histogram) - 1

                    # num +=1
                    # print(list, num)
                # if the list is equal to another list
                # for single_word in list:
                #     for single_word in word_histogram:
                #         if single_word == word_histogram[0]:
                #             num +=1
                # print(single_word, num)


            # print(word_histogram)


wordHistogram()
