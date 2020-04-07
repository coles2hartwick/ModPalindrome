# Sam Cole
# This is the new palindrome check that will check sentences
import string


def strip(word):
    new = word.translate(str.maketrans('', '', string.punctuation))
    new = new.replace(" ", "")
    return is_palindrome(new)


def is_palindrome(word):
    thisword = word.lower()
    if len(thisword) == 1 or 0:
        return True
    else:
        if thisword[0] == thisword[-1]:
            return is_palindrome(thisword[1:-1])
        else:
            return False


answer = 1
while int(answer) != 0:
    word = str(input("Enter a word or sentence you think might be a palindrome"))
    if strip(word):
        print("This word is a Palindrome")
    else:
        print("This word isn't a Palindrome")
    answer = input("Do you want to continue? 1 for yes 0 for no")
