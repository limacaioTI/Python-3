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
        self.s = s
        
        for i in s:
            count = 0

            for j in s:
                if i == j:
                    count+=1
            if count == 1:
                return s.index(i)
        return -1

solution = Solution()
resp = "loveleetcode"
print(solution.firstUniqChar(resp))