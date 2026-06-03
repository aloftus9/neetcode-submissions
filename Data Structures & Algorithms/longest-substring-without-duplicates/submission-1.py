class Solution:
    # Sliding window
    # WE need a set() for tracking and that set will have to be set back to 0
    # char in set
    # "zxyzxyz"
    # abcabcbb
    # 

    def lengthOfLongestSubstring(self, s: str) -> int:

        unique_chars = set()
        left = 0
        best = 0

        for right in range(len(s)):
        
            while s[right] in unique_chars:
                unique_chars.remove(s[left])
                left += 1

            unique_chars.add(s[right])
            best = max(len(unique_chars), best)

        return best