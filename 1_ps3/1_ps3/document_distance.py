# 6.0001 Fall 2019
# Problem Set 3
# Written by: sylvant, muneezap, charz, anabell, nhung, wang19k, asinelni, shahul, jcsands

# Problem Set 3
# Name: Yeabsira Moges
# Collaborators: 
# Time Spent: 3
# Late Days Used: 0

import string
import math


# - - - - - - - - - -
# Check for similarity by comparing two texts to see how similar they are to each other


### DO NOT MODIFY THIS FUNCTION
def load_file(filename):
    """
    Args:
        filename: string, name of file to read
    Returns:
        string, contains file contents
    """
    # print("Loading file %s" % filename)
    inFile = open(filename, 'r')
    line = inFile.read().strip()
    for char in string.punctuation:
        line = line.replace(char, "")
    inFile.close()
    return line.lower()


### Problem 0: Prep Data ###
def prep_data(input_text):
    """
    Args:
        input_text: string representation of text from file,
                    assume the string is made of lowercase characters
    Returns:
        list representation of input_text, where each word is a different element in the list
    """
    s = ""
    for char in input_text:
        # check if character in text is a letter and if not, set as split character
        if char.isalpha():
            s += char
        elif s[-1] != ",":
            s+=","
        else:
            pass
    data = s.split(",")
    # remove any instances of empty strings that may have remained
    for c in data:
        if c == "":
            pass
    return data

### Problem 1: Get Frequency ###
def get_frequencies(word_list):
    """
    Args:
        word_list: list of strings, all are made of lowercase characters
    Returns:
        dictionary that maps string:int where each string
        is a letter or word in l and the corresponding int
        is the frequency of the letter or word in l
    """
    d = {}
    for word in word_list:
        # if the word isn't in word list, then add it and start at one else increment by one
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    return d


### Problem 2: Letter Frequencies ###
def get_letter_frequencies(word):
    """
    Args:
        word: word as a string
    Returns:
        dictionary that maps string:int where each string
        is a letter in word and the corresponding int
        is the frequency of the letter in word
    """
    d = {}
    for w in word:
        # if the word isn't in word list, then add it and start at one else increment by one
        if w not in d:
            d[w] = 1
        else:
            d[w] += 1
    return d


### Problem 3: Similarity ###
def calculate_similarity_score(dict1, dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        dict1: frequency dictionary of letters of word1 or words of text1
        dict2: frequency dictionary of letters of word2 or words of text2
    Returns:
        float, a number between 0 and 1, inclusive
        representing how similar the words/texts are to each other

        The difference in words/text frequencies = DIFF sums words
        from these three scenarios:
        * If an element occurs in dict1 and dict2 then
          get the difference in frequencies
        * If an element occurs only in dict1 then take the
          frequency from dict1
        * If an element occurs only in dict2 then take the
          frequency from dict2
         The total frequencies = ALL is calculated by summing
         all frequencies in both dict1 and dict2.
        Return 1-(DIFF/ALL) rounded to 2 decimal places
    """
    used = []
    diff = 0
    total = 0
    for key in dict1.keys():
        total += dict1[key]
        # if the key exists in both dictionaries, take the absolute value of the difference
        if key in dict2.keys() and key not in used:
            diff += abs(dict1[key] - dict2[key])
            used.append(key)
        # else add the value from one dictionary or the other
        elif key not in dict2.keys():
            diff += dict1[key]
    for key in dict2.keys():
        total += dict2[key]
        if key not in used:
            diff += dict2[key]
    return round(1-(diff/total), 2)



### Problem 4: Most Frequent Word(s) ###
def get_most_frequent_words(dict1, dict2):
    """
    The keys of dict1 and dict2 are all lowercase,
    you will NOT need to worry about case sensitivity.

    Args:
        dict1: frequency dictionary for one text
        dict2: frequency dictionary for another text
    Returns:
        list of the most frequent word(s) in the input dictionaries

    The most frequent word:
        * is based on the combined word frequencies across both dictionaries.
          If a word occurs in both dictionaries, consider the sum the
          freqencies as the combined word frequency.
        * need not be in both dictionaries, i.e it can be exclusively in
          dict1, dict2, or shared by dict1 and dict2.
    If multiple words are tied (i.e. share the same highest frequency),
    return an alphabetically ordered list of all these words.
    """
    combined_dict = {}
    most_frequent_num = 0
    most_frequent = []
    # create a combined dictionary of both dictionaries then loop through to find the most frequent words
    for key in dict1.keys():
        if key not in combined_dict:
            combined_dict[key] = dict1[key]
        else:
            combined_dict[key] += dict1[key]
    for key in dict2.keys():
        if key not in combined_dict:
            combined_dict[key] = dict2[key]
        else:
            combined_dict[key] += dict2[key]
    for key in combined_dict.keys():
        if combined_dict[key] > most_frequent_num:
            most_frequent_num = combined_dict[key]
    for key in combined_dict.keys():
        if combined_dict[key] == most_frequent_num:
            most_frequent.append(key)
    return most_frequent


### Problem 5: Finding TF-IDF ###
def get_tf(text_file):
    """
    Args:
        text_file: name of file in the form of a string
    Returns:
        a dictionary mapping each word to its TF

    * TF is calculatd as TF(i) = (number times word *i* appears
        in the document) / (total number of words in the document)
    * Think about how we can use get_frequencies from earlier
    """
    words = get_frequencies(prep_data(load_file(text_file)))
    total = 0
    # loop through all the words in the text file and divide by the total number of words
    for word in words:
        total += words[word]
    for word in words:
        words[word] /= total
    return words

def get_idf(text_files):
    """
    Args:
        text_files: list of names of files, where each file name is a string
    Returns:
       a dictionary mapping each word to its IDF

    * IDF is calculated as IDF(i) = log_10(total number of documents / number of
    documents with word *i* in it), where log_10 is log base 10 and can be called
    with math.log10()

    """
    combined_dict = {}
    length = len(text_files)
    # create a combined dictionary of words from all the files
    for file in text_files:
        words = get_frequencies(prep_data(load_file(file)))
        for word in words:
            if word not in combined_dict:
                combined_dict[word] = 1
            else:
                combined_dict[word] += 1
    for word in combined_dict:
        # divide the length of the list of files by the number of times the word shows up
        combined_dict[word] = math.log(length / combined_dict[word], 10)
    return combined_dict


def get_tfidf(text_file, text_files):
    """
        Args:
            text_file: name of file in the form of a string (used to calculate TF)
            text_files: list of names of files, where each file name is a string
            (used to calculate IDF)
        Returns:
           a sorted list of tuples (in increasing TF-IDF score), where each tuple is
           of the form (word, TF-IDF). In case of words with the same TF-IDF, the
           words should be sorted in increasing alphabetical order.

        * TF-IDF(i) = TF(i) * IDF(i)
        """
    tf = get_tf(text_file)
    idf = get_idf(text_files)
    tf_idf = []
    for key in tf:
        # multiply the value of the keys of tf by the values of idf
        tf_idf.append((key, tf[key]*idf[key]))
    # sort the tuples by the second value of the tf-idf using a lambda function
    return sorted(tf_idf, key=lambda tfidf: tfidf[1])




if __name__ == "__main__":
    pass
    ##Uncomment the following lines to test your implementation
    ## Tests Problem 0: Prep Data
    # test_directory = "tests/student_tests/"
    # hello_world, hello_friend = load_file(test_directory + 'hello_world.txt'), load_file(test_directory + 'hello_friends.txt')
    # world, friend = prep_data(hello_world), prep_data(hello_friend)
    # print(world) ## should print ['hello', 'world', 'hello']
    # print(friend) ## should print ['hello', 'friends']

    ## Tests Problem 1: Get Frequencies
    # world_word_freq = get_frequencies(world)
    # friend_word_freq = get_frequencies(friend)
    # print(world_word_freq) ## should print {'hello': 2, 'world': 1}
    # print(friend_word_freq) ## should print {'hello': 1, 'friends': 1}

    ## Tests Problem 2: Get Letter Frequencies
    # freq1 = get_letter_frequencies('hello')
    # freq2 = get_letter_frequencies('that')
    # print(freq1) ##  should print {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    # print(freq2) ##  should print {'t': 2, 'h': 1, 'a': 1}

    ## Tests Problem 3: Similarity
    # word1_freq = get_letter_frequencies('toes')
    # word2_freq = get_letter_frequencies('that')
    # word3_freq = get_frequencies('nah')
    # word_similarity1 = calculate_similarity_score(word1_freq, word1_freq)
    # word_similarity2 = calculate_similarity_score(word1_freq, word2_freq)
    # word_similarity3 = calculate_similarity_score(word1_freq, word3_freq)
    # word_similarity4 = calculate_similarity_score(world_word_freq, friend_word_freq)
    # print(word_similarity1) ## should print 1.0
    # print(word_similarity2) ## should print 0.25
    # print(word_similarity3) ## should print 0.0
    # print(word_similarity4) ## should print 0.4

    ## Tests Problem 4: Most Frequent Word(s)
    # freq1, freq2 = {"hello":5, "world":1}, {"hello":1, "world":5}
    # most_frequent = get_most_frequent_words(freq1, freq2)
    # print(most_frequent) ## should print ["hello", "world"]

    ## Tests Problem 5: Find TF-IDF
    # text_file = 'tests/student_tests/hello_world.txt'
    # text_files = ['tests/student_tests/hello_world.txt', 'tests/student_tests/hello_friends.txt']
    # tf = get_tf(text_file)
    # idf = get_idf(text_files)
    # tf_idf = get_tfidf(text_file, text_files)
    # print(tf) ## should print {'hello': 0.6666666666666666, 'world': 0.3333333333333333}
    # print(idf) ## should print {'hello': 0.0, 'world': 0.3010299956639812, 'friends': 0.3010299956639812}
    # print(tf_idf) ## should print [('hello', 0.0), ('world', 0.10034333188799373)]



