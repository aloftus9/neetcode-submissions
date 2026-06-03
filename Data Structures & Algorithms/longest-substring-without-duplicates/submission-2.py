class Solution:
    # Sliding window
    # WE need a set() for tracking and that set will have to be set back to 0
    # char in set
    # "zxyzxyz"
    # abcabcbb
    # 

    def lengthOfLongestSubstring(self, s: str) -> int:
        numset = set()
        l,r=0,0
        maxlen = 0
        while r<len(s):
            while s[r] in numset:
                numset.remove(s[l])
                l+=1
            numset.add(s[r])
            maxlen = max(maxlen,len(numset))
            r+=1
        return maxlen