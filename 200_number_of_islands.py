class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        islands = 0
        visited = set()
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    islands += 1
                    stack = [(i,j)]
                    visited.add((i,j))
                    while stack:
                        x, y = stack.pop()
                        for d in dirs:
                            nx, ny = x+d[0], y+d[1]
                            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                                continue
                            if (nx, ny) in visited or grid[nx][ny] != "1":
                                continue
                            visited.add((nx, ny))
                            stack.append((nx, ny))
        return islands