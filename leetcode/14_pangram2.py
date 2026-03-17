class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
    
solution = Solution()
repos = print(solution.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))