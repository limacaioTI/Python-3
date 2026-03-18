""""
A triangle is called equilateral if it has all sides of equal length.
A triangle is called isosceles if it has exactly two sides of equal length.
A triangle is called scalene if all its sides are of different lengths.
Return a string representing the type of triangle that can be formed or "none" if it cannot form a triangle.
"""
from typing import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        
        nums.sort()
          
        if nums[0]+nums[1] <= nums[2]:
            return "none"
        else:
            if nums[0] == nums[1] and nums[1] == nums[2]:
                return "equilateral"
            elif nums[0] != nums[1] and nums[1] != nums[2] and nums[0] != nums[2]:
                return "scalene"
            return "isosceles"

s = Solution()
nums = [5,3,8]
print(s.triangleType(nums))