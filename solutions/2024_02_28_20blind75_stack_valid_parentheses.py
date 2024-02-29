# https://leetcode.com/problems/valid-parentheses/
# all tests passed
def isValid(s: str) -> bool:

    brack_stack = []

    for v in s:
        if v in "({[":
            brack_stack.append(v)
        elif v in ")}]":
            if len(brack_stack) <= 0:
                return False

            openchar = brack_stack.pop()
            if v == ")" and openchar != "(":
                return False
            if v == "}" and openchar != "{":
                return False
            if v == "]" and openchar !="[":
                return False

    return len(brack_stack) == 0