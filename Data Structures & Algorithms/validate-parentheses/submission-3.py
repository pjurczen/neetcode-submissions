class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if last != "(" and c == ")":
                    return False
                elif last != "{" and c == "}":
                    return False
                elif last != "[" and c == "]":
                    return False
        if len(stack) > 0:
            return False
        return True