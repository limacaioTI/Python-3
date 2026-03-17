class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        self.n = n
        self.m = m

        num1 = []
        num2 = []
        for num in range(1, n+1):
            if num % m == 0:
                num2.append(num)
            else:
                num1.append(num)
        sum_num1 = sum(num1)
        sum_num2 = sum(num2)

        print(sum_num1 - sum_num2)

solution = Solution()
output = solution.differenceOfSums(5, 1)