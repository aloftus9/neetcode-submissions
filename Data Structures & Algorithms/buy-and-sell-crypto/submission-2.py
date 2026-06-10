# Two pointer

# set the best profit and move the pointers in a sliding window

# move left when the right value is less than the left value

# move the right and see if there's a new best

# Ensure left is always at the lowest point
# We need to track the low and the best
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0

        lowest = float("-inf")
        best = 0

        for right in range(1, len(prices)):

            # Losing money
            if prices[right] < prices[left]:
                left = right
            
            best = max(best, prices[right] - prices[left])
        
        return best


        