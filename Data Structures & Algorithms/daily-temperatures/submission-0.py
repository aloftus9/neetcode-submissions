# monitonic stack problem

# [30,38,30,36,35,40,28]
# [0, 0, 0, 0, 0, 0, 0]
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0]*len(temperatures)

        # Will contain days that are wiaitng to be completed
        stack = []

        for i, temp in enumerate(temperatures):
            
            while stack and temp > temperatures[stack[-1]]:
                prev_i = stack.pop()
                result[prev_i] = i - prev_i

            stack.append(i)
        return result


        