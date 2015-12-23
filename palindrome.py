# Palindrome detector: Reads forward or backward, odd or even.

sentence = input("Enter a phrase you think is a Palindrome: ")


def is_palindrome(sentence):
    low_sent = sentence.lower()  # takes the lower case of the sentence
    # print("low_sent: {}".format(low_sent))

    cluster = list(low_sent)   # splitting the words into a list
    # print("cluster: {}".format(cluster))
    # print(len(cluster))

    fr_A = "".join(cluster)  # makes a list of letters, all words, no spaces
    # print("fr_A: {}".format(fr_A))
    # print(len(fr_A))

    fr_B = []                    # empty list to take ONLY the letters (a to z)
    no_punct = 'abcdefghijklmnopqrstuvwxyz'  # comparitor letters (a to z)
    for x in fr_A:
        if x in no_punct:
            fr_B.append(x)

    # print("This is 'fr_B': {}".format(fr_B))

    even = len(fr_B)
    # print("This is length of fr_B: {}".format(even))

    half = int(len(fr_B)/2)  # leaves the middle letter alone.

    # end = len(fr_B) + 1
    # print("This is length of fr_B + 1: {}".format(end))

    if even % 2 == 0:
        for i in range(even):
            if fr_B[i] == fr_B[- (i + 1)]:   # compares each end of list.
                return ("{} is a palindrome". format(sentence))
            else:
                return ("{} is NOT a palindrome". format(sentence))
    else:
        for i in range(half):
            if fr_B[i] == fr_B[- (i + 1)]:   # compares each end of list.
                return ("{} is a palindrome". format(sentence))
            else:
                return ("{} is NOT a palindrome". format(sentence))
        # return ("{} is NOT a palindrome". format(sentence))

print(is_palindrome(sentence))

'''
#def main():
#    # TODO: put your input/output code here
#    pass

#if __name__ == '__main__':
#    main()
'''
