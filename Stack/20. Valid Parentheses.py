class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            elif i == ")" or i == "]" or i == "}":
                if len(stack) == 0:
                    return False
                x = stack.pop()
                if i == ")" and x != "(":
                    return False
                elif i == "]" and x != "[":
                    return False
                elif i == "}" and x != "{":
                    return False

        if len(stack) > 0:
            return False
        return True


if __name__ == "__main__":
    print(Solution().isValid("([)]"))
