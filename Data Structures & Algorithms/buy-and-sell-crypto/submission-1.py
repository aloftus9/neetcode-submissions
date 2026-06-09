
# initialize a list for all the prices with default value 0
# define an empty stack

# loop through the prices


# Want a list of the max price you could gain in each index
# profit is max of the remaining days minus current


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        result_list = [0]*len(prices)

        stack = []

        for i, price in enumerate(prices):

            stack.append(i)
            right_i = len(stack) - 1
            while right_i >= 0:
                prev_index = stack[right_i]
                result_list[prev_index] = max(prices[i] - prices[prev_index], result_list[prev_index])
                right_i -= 1
        print(result_list)
        return max(result_list)