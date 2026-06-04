# Brute force this with o(n^2)

# O(n): sliding window

# "wwkew"
# set = p
# best = 2

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        seen = set()
        best = 0

        for char in s:
            
            while char in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(char)
            best = max(best, len(seen))
            
        
        return(best)


        