"""
✅ Practice: Write a Python script that:

Reads a text file

Counts how many times each word appears

Prints the most common word"""

#ans -
def wordsChecker(filename):
    words_dict = {}
    try:
        with open(filename,"r") as file1:
            for eachLine in file1:
                eachLineArray = eachLine.strip().lower().split()
                for eachWord in eachLineArray:
                    if eachWord in words_dict:
                        words_dict[eachWord]+=1
                    else:words_dict[eachWord] = 1
            print(words_dict)
            most_common_word = ""
            highest_count = 0
            for key,value in words_dict.items():
                if words_dict[key] > highest_count:
                    highest_count = words_dict[key]
                    most_common_word = key
            print(most_common_word, "- most common word")
    except FileNotFoundError:print("- FILE NOT FOUND -")
wordsChecker("sample.txt")