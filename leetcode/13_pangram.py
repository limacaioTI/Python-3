class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        pangram = 'qwertyuiopasdfghjklzxcvbnm'
        pangram_list = list(pangram)

        for i in sentence:
            for k in pangram_list:
                if i == k:
                    pangram_list.remove(k)
                    break

        return len(pangram_list) == 0
    
solution = Solution()
repos = print(solution.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))