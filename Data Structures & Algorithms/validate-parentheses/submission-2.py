class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        stack = []

        for char in s:
            if char in close_to_open:
                if len(stack) > 0 and stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
        