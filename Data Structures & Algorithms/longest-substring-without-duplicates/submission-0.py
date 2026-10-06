class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_string=0
        charset=set()
        l=0
        for i in range(len(s)):
            while s[i] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[i])
            max_string=max(max_string,len(charset))

        return max_string





        