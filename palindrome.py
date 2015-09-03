# Palindrome detector: Reads forward or backward.

sentence = input("Enter a phrase you think is a Palindrome: ")

def is_palindrome(sentence):
    low_sent = sentence.lower() # takes the lower case of the sentence
    cluster = low_sent.split()  # splitting the words into a list
    fr_A = "".join(cluster)    # creating a list of the letters, all words, without spaces
    list_sent = (fr_A)
    fr_B = []                   # empty list to take ONLY the letters (a to z)
    punct = ('abcdefghijklmnopqrstuvwxyz')  # comparitor list of letters (a to z)
    for x in list_sent:
        for i in punct:
            if punct[i] == list_sent[x]:     #TypeError: list indices must be integers, not str
                fr_B.append(list_sent[x])
    ba = fr_B[::-1]
    if ba == fr_A:
        return ("{} is a palindrome." .format(sentence))
    else:
        return ("{} is not a palindrome." .format(sentence))

print(is_palindrome(sentence))

'''
#def main():
#    # TODO: put your input/output code here
#    pass

#if __name__ == '__main__':
#    main()
'''
