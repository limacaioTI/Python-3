from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums_squares_sorted = []
        for num in nums:
            nums_squares_sorted.append(num*num)
        return sorted(nums_squares_sorted)
        
solution = Solution()
nums = [-4,-1,0,3,10]
print(solution.sortedSquares(nums))