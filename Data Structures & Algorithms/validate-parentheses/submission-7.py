class Solution:
    def isValid(self, s: str) -> bool:
        parMap = {'(' : ')', '[' : ']', '{' : '}'}
        if len(s) % 2:
            return False
        stack = []
        strList = list(s)
        for symbol in strList:
            if symbol in parMap.values():
                if not stack:
                    return False
                lastElem = stack.pop()
                if parMap[lastElem] != symbol:
                    return False
            if symbol in parMap:
                stack.append(symbol)
                continue
        return not stack