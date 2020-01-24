'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    #base case if the word is less than 2 letters
    if len(word) <= 1:
        return 0
    #search the first 2 letters of a word for "th"
    #recursivly remove letter 1 from word and search remaining word
    elif word[0] + word[1] == "th":
        print(word[0] + word[1])
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])
