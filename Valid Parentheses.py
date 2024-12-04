class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) % 2 == 1):
            return False
        else:
            stack = []
            bracketMap = {')' : '(', ']' : '[', '}' : '{'}

            for bracket in s:
                if bracket in bracketMap:
                    if stack and stack[-1] == bracketMap[bracket]:  # if they match
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(bracket)

        return True if not stack else False