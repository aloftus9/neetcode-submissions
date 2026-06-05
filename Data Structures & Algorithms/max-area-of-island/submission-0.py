
# We want to go traverse through the matrix looking for a 1
# IF we see a 1, then run a Recursive DFS Function to:
# check surrounding, if 1 then set to 0 and continue, if all 0s then return (stop)
# But we need to keep track of how many more 1s the DFS function finds and store a BEST variable
# Pass a counter into the dfs function

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        def dfs(row, col, island_count) -> int:
            # Check the boundaries or water
            if not (
                0 <= row < len(grid) and
                0 <= col < len(grid[0]) and
                grid[row][col] == 1
            ):
                return island_count
            
            island_count += 1
            grid[row][col] = 0

            island_count = dfs(row + 1, col, island_count)
            island_count = dfs(row - 1, col, island_count)
            island_count = dfs(row, col + 1, island_count)
            island_count = dfs(row, col - 1, island_count)
            return island_count

    
        biggest_island_count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    new_island_count =  dfs(row, col, 0)
                    if new_island_count:
                        biggest_island_count = max(biggest_island_count, new_island_count)
        
        return biggest_island_count

        