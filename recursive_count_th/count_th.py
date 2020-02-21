'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if word == "":
        return 0

    def recurse_count_th(str, idx):
        if idx == len(str) - 1:
            return 0
        if str[idx] + str[idx+1] == "th":
            return 1 + recurse_count_th(str, idx + 1)
        else:
            return 0 + recurse_count_th(str, idx + 1)

    return recurse_count_th(word, 0)