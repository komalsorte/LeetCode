__author__ = 'Komal Atul Sorte'
"""
Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.  It is guaranteed there is at least one word that isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  Words in the paragraph are not case sensitive.  The answer is in lowercase.
"""

import string
class Solution:
    def mostCommonWord(self, paragraph, banned):
        paragraph = paragraph.lower()
        paragraph_dict = dict()
        result = ""
        for w in string.punctuation:
            paragraph = paragraph.replace(w, " ")
        # for w in paragraph:
        #     if w not in string.punctuation:
        #         result += w

        paragraph = paragraph.split(" ")

        for word in paragraph:
            if word not in banned and word != '':
                if word in paragraph_dict.keys():
                    paragraph_dict[word] += 1
                else:
                    paragraph_dict[word] = 1
        print(paragraph_dict)

        high_score = 0
        high_key = None
        for word, count in paragraph_dict.items():
            if count > high_score:
                high_score = count
                high_key = word
        return high_key



if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    paragraph = "a, a, a, a, b,b,b,c, c"
    banned = ["a"]
    print(Solution().mostCommonWord(paragraph, banned))
