import sys
import string
import sys

def main(cin):
    alphabet = string.ascii_uppercase
    letters = {i: 0 for i in alphabet}
    letters2 = {i: 0 for i in alphabet}
    word1, word2 = cin.split("|")

    if word1 == word2:
        print(cin + " = NOT AN ANAGRAM")
        return

    for char in word1:
        letters[char] += 1
    for char in word2:
        letters2[char] += 1
    
    for key, value in letters.items():
        if value != letters2[key]:
            print(cin + " = NOT AN ANAGRAM")
            return
    print(cin + " = ANAGRAM")


if __name__ == "__main__":
    cases = int(sys.stdin.readline().rstrip())
    for caseNum in range(cases):
        main(sys.stdin.readline().rstrip())     
