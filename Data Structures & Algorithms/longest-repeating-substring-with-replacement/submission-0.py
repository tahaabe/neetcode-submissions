class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency={}
        l=0
        max_frequency=0
        res=0
        for r in range(len(s)):
            frequency[s[r]] = frequency.get(s[r], 0) + 1
            max_frequency=max(max_frequency,max(frequency.values()))
            while (r-l+1)-max_frequency>k:
                frequency[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res
            
