""""
Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.
Input: s = "leetcode"
Output: 0
Explanation:
The character 'l' at index 0 is the first character that does not occur at any other index.
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}

        # Conta frequência
        for char in s:
            count[char] = count.get(char, 0) + 1

        # Encontra o primeiro único
        for i, char in enumerate(s):
            if count[char] == 1:
                return i

        return -1

solution = Solution()
resp = "loveleetcode"
print(solution.firstUniqChar(resp))