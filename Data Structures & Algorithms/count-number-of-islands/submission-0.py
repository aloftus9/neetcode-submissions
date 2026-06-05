# Thinking I will recursively go through the whole matrix with DFS
# If 1, count += 1
# Need to rememebr boandaries
# Need to remember what I've seen before

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # using dfs to clear out anything around the found land
        def dfs(row, col) -> int:
            # If out of bounds or 0, just stop
            if not (
                0 <= row < len(grid) and
                0 <= col < len(grid[0]) and
                grid[row][col] == "1"
            ):
                return
            
            # Found land, now set to 0
            grid[row][col] = "0"

            if grid[row][col] == "1":
                count += 1
                grid[row][col] = 0

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                # Clear out the connecting land]
                # This function will check right, left, top, bottom and clear out the land until there's no more water
                dfs(row, col)
        return islands


        