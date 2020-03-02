"""histogram-list.py"""

# def listogram(lines):
#     #defines an empty list as "listogram"
#     listogram = []

#accepts 2 arguments of a word and listomram
def get_index(word, listogram):
    #setting index to 0
    index = 0
    # Loop through listogram and for each inner_list
    for inner_list in listogram:
        #if inner_list index of 0 is the word return index
        if inner_list[0] == word:
            return index
        else:
            #increse index by 1
            index += 1
    return "nope didn't find it"


def listogram(lines):
    #defines an empty list as "listogram"
    listogram = []

    #for each line in the file
    for lines in file:
        lines = lines.rstrip()
        #for each word in the lines
        for word in lines.split():
            #reset get_index to result
            result = get_index(word, listogram)
            #if result is "string"
            if result == "nope didn't find it":
                #add a dict of a word and the number 1
                listogram.append([word,1])
            else:
                #increse listogram innerlist value by 1
                listogram[result][1] += 1

    return listogram
#access files
file = open("ununique-words.txt", "r").readlines()



print(listogram(file))





# word_histogram = []
#
# def wordHistogram():
#     num = 1
#     num2 = 0
#     with open('ununique-words.txt', 'r') as file:
#
#         # loop through file
#         for line in file:
#             #loop through lines
#             for word in line.split(): #split into single words
#                 word_histogram.append([(word)])
#                 print(word,num)
#                 for list in word_histogram:
#                     if list[num2] == word_histogram[num2][num2]:
#                         num +=1
#             num2 +=1










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


# wordHistogram()
