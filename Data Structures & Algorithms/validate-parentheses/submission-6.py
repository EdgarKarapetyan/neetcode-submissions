class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        opening = ['(', '[', "{"]
        closing = [')', ']', "}"]
        if len(s) % 2:
            return False
        stack = []
        for symbol in s:
            if symbol in closing and not stack:
                return False
            if symbol in opening:
                stack.append(symbol)
                continue
            if symbol in closing:
                lastElem = stack.pop()
                index = opening.index(lastElem)
                if closing[index] != symbol:
                    return False
        return not stack