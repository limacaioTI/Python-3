from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:

        match_list = []

        for index, word in enumerate(words):
            if x in word:
                match_list.append(index)
        return match_list

solution = Solution()
words = ["abc","bcd","aaaa","cbc"] 
x = "b"
print(solution.findWordsContaining(words, x))  