class Solution:
    def toLowerCase(self, s: str) -> str:
        self.s = s

        return s.lower()
        
solution = Solution()
resp = "Hello World"

print(solution.toLowerCase(resp))