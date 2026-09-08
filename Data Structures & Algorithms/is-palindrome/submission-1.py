class Solution:
    def isPalindrome(self, s: str) -> bool:

        if len(s) == 1:
            return True
        # lowerS = list(s.lower().replace(" ", ""))
        lowerS = [ch for ch in s.lower() if ch.isalnum()]
        print(lowerS)
        for i in range(len(lowerS) // 2):
            if lowerS[i] != lowerS[len(lowerS) - i - 1]:
                return False
        return True
        