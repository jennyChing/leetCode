'''
68. Text Justification

Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
'''
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        currLen = 0
        currLine = []
        for w in words:
            if currLen + len(currLine) + len(w) > maxWidth:
                if len(currLine) > 1:
                    spaces = (maxWidth - currLen) // (len(currLine) - 1)
                    extraSpace = (maxWidth - currLen) % (len(currLine) - 1)
                    tmp = ""
                    for i, c in enumerate(currLine):
                        if 0 < i <= extraSpace:
                            tmp += " " * (spaces + 1)
                        elif i > extraSpace:
                            tmp += " " * (spaces)
                        tmp += c
                else: # only one word on this line
                    tmp = currLine[0] + " " * (maxWidth - len(currLine[0]))
                res.append(tmp)
                currLen = len(w)
                currLine = [w]
                continue
            currLen += len(w)
            currLine.append(w)
        tmp = ""
        for i, c in enumerate(currLine):
            if i > 0:
                tmp += " "
            tmp += c
        tmp += " " * (maxWidth - len(tmp))
        res.append(tmp)
        return res

if __name__ == '__main__':
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    words = ["a","b","c","d","e"]
    res = Solution().fullJustify(words, 3)
    print(res)


