# Matrix Bredth Level Search
# We want to see what's happing in the surroundings level by level

# matrix to traverse we have to do nested for loops


from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


        queue = deque()

        fresh_fruit_count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row,col))
                elif grid[row][col] == 1:
                    fresh_fruit_count += 1

        total_minutes = 0
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        while queue and fresh_fruit_count > 0:
            queue_length = len(queue)
            for rotten_banana_index in range(queue_length):
                # pop one of the rotten bananas
                rotten_banana_row, rotten_banana_col  = queue.popleft()

                # Look around the rotten banana
                for dr, dc in directions:
                    new_row = dr + rotten_banana_row
                    new_col = dc + rotten_banana_col

                    # Check boundaries?? SHouldn't matter cause we only care about 1s
                    if (
                        0 <= new_row < len(grid) and
                        0 <= new_col < len(grid[0]) and
                        grid[new_row][new_col] == 1
                    ):
                        grid[new_row][new_col] = 2
                        queue.append((new_row, new_col))
                        fresh_fruit_count -= 1

            total_minutes += 1
        
        if fresh_fruit_count != 0:
            return -1
        return total_minutes
            





                


        