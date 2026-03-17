from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        for word in words:
            if word == word[::-1]:
                return word
        return ""
solution = Solution()
words = ["abc", "car", "ada", "racecar", "cool"]
resp = print(solution.firstPalindrome(words))