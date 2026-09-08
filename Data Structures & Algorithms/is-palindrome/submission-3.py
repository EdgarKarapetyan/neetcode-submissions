class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerS = [ch for ch in s.lower() if ch.isalnum()]
        LS = len(lowerS)
        # if LS == 1:
        #     return True
        # lowerS = list(s.lower().replace(" ", ""))
        # print(lowerS)
        for i in range(LS // 2):
            if lowerS[i] != lowerS[LS -i - 1]:
                return False
        return True
        