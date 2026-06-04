
# intervals
# dont need to sort
# Append the left
# merge
# finally add everything


# [1,3],[4, 6]


# [1,3] [4,6] [7,9] [10,12]
#           [5,8]
# result = [[1,3], [4, 8]

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:


        result = []

        for i in range(len(intervals)):

            newIntervalStart = newInterval[0]
            newIntervalEnd = newInterval[1]

            currentStart = intervals[i][0]
            currentEnd = intervals[i][1]

            # If the full thing is less than the target, Append
            if currentEnd < newIntervalStart:
                result.append(intervals[i])

            # if the full thing is greater than the target, then everything after is and return
            elif currentStart > newIntervalEnd:
                result.append(newInterval)
                return result + intervals[i:]

            # overlapping somehow
            else:
                newInterval[0] = min(newIntervalStart, currentStart)
                newInterval[1] = max(newIntervalEnd, currentEnd)
            
        result.append(newInterval)
        return result



