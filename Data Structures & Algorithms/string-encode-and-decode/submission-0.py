class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for i in strs:
            result+=str(len(i)) + "&" + i
        return result
    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="&":
                j+=1
            length=s[i:j]
            word=s[j+1:int(length)+1+j]
            result.append(word)
            i=j+int(length)+1
        return result

