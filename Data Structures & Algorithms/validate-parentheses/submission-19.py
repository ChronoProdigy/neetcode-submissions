class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for x in s:
            if x in ('(', '{', '['):
                stack.append(x)
            elif x == ')':
                if len(stack) == 0:
                    return False
                y = stack[-1]
                if y == '(':
                    stack.pop()
                else:
                    return False
            elif x == '}':
                if len(stack) == 0:
                    return False
                y = stack[-1]
                if y == '{':
                    stack.pop()
                else:
                    return False
            elif x == ']':
                if len(stack) == 0:
                    return False
                y = stack[-1]
                if y == '[':
                    stack.pop()
                else:
                    return False

        if len(stack) != 0:
            return False
        else:
            return True