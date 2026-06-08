
# With a graph we do want this to be an adjacency dictionary
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        


        graph = {i: [] for i in range(n)}

        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)

        seen = set()
        
        def dfs(node):
            if node in seen:
                return

            seen.add(node)

            for next_node in graph[node]:
                dfs(next_node)


        count = 0

        for node in range(n):
            if node not in seen:
                count += 1
                dfs(node)

        return count


            


        

        
        
