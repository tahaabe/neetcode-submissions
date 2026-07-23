class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        paires={'(':')','[':']','{':'}'}
        opend=paires.keys()
        for c in s:
            if c in opend:
                stack.append(c)
            else:
                if not stack:
                    return False
                j=stack[len(stack)-1]
                if c==paires[j]:
                    stack.pop()
                else:
                    return False
        return len(stack)==0

        