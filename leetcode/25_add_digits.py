class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:  # enquanto tiver mais de 1 dígito
            digit_sum = 0
            
            while num > 0:
                digit_sum += num % 10
                num //= 10
            
            num = digit_sum  # atualiza o número
        
        return num


sol = Solution()
print(sol.addDigits(38))  # 2