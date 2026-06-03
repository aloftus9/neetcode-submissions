class Solution:
    # Not sorted from the beginning
    # need to sort
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals=[[1,4],[2,3],[3,4],[2,4]]
        # result = [[1,3],
        intervals.sort(key=lambda x:x[0]) # O(nlogn)
        
        result_set = [] # O[n]

        for i in range(0, len(intervals)):
            current_start = intervals[i][0]
            current_end = intervals[i][1]
            
            # if first, continue
            # if i == 0:
            #     continue

            if result_set and current_start <= result_set[-1][1]:
                result_set[-1][1] = max(current_end, result_set[-1][1])
            else:
                result_set.append([current_start, current_end])
        
        return result_set
