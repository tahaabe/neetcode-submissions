import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operation={"+":operator.add ,"-":operator.sub,"*":operator.mul,"/":lambda a,b : int(a/b)}
        for i in tokens:
            if i not in operation:
                stack.append(int(i))
            else:
                a=stack.pop()
                b=stack.pop()
                result= operation[i](b,a)
                stack.append(result)
        return stack[-1]
            