
# IF full left then append
# if fully right then append the newInterv

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        result = []
        for i in range(len(intervals)):
            
            # Add all the left
            if newInterval[0] > intervals[i][1]:
                result.append(intervals[i])

            # Add the interval then return with all the right
            elif newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]

            # There's an overlap. Set the new newInterval values based on current index
            else:
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
        
        result.append(newInterval)
        return result