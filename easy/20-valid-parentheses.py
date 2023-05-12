class Solution:
    def isValidStack(self, s: str) -> bool:
        stack = []
        for x in s:
            if x in ["(", "[", "{"]:
                stack.append(x)
            else:
                if not stack:
                    return False
                if x == ")" and stack[-1] == "(":
                    stack.pop()
                elif x == "]" and stack[-1] == "[":
                    stack.pop()
                elif x == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        return not stack

    def isValidReplace(self, s: str) -> bool:
        while any([self.toReplace(s, "()"), self.toReplace(s, "[]"), self.toReplace(s, "{}")]):
            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")
        if s == "":
            return True
        else:
            return False
    
    def toReplace(self, s: str, bracket: str) -> bool:
        return True if bracket in s else False

if __name__ == "__main__":
    s = "()[]{}"
    sol = Solution()
    a = sol.isValidReplace(s)
    b = sol.isValidStack(s)
    assert a == b
    print(a)
