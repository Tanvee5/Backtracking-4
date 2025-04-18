# Problem 1 : Optimal Placement of Buildings in a grid
# Time Complexity : O((nH×W​)⋅(H×W)) where n is tehe number of building, H is the height and W is the width 
# Space Complexity : O(H×W) where n is tehe number of building, H is the height and W is the width 
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach

from collections import deque
import sys

class BuildingPlacement:
    def __init__(self):
        # define globale vriables minDist which will store the minimum distance in grid
        self.minDist = sys.maxsize
        self.H = 0
        self.W = 0
        self.result = []
        
    def findMinDistance(self, h, w, n):
        # set the global variable H and W to  height, width 
        self.H = h
        self.W = w
        # define grid matrix with size(h*w) and fill with -1
        grid = [[-1 for _ in range(w)] for _ in range(h)]
        # call backtrack function with paramter grid , n ie number of the building and 0
        self.backtrack(grid, n, 0)
        # return minDist ie minimum distance
        return self.minDist
    
    # backtrack function which explore all the combination of building placement
    def backtrack(self, grid, n, idx):
        # base case where all the building are placed then call bfs fuunction for grid to calculate minimum distance and return
        if n == 0:
            self.bfs([row[:] for row in grid])
            return
        
        # logic
        # loop from idx to (h*w)
        # here imagining 2-d grid into 1-d  array
        for j in range(idx, self.H * self.W):
            # get the row and column from idx of 1-d array
            r = j // self.W
            c = j % self.W
            # set the grid value at r anc c position as 0
            grid[r][c] = 0
            
            # recurse
            # call backtrack function with paramter grid, (n-1) buildings and (j+1) postion in 1-d array
            self.backtrack(grid, n-1, j+1)
            
            # backtrack
            # after exploring the option and again set the value of grid at r and c position as -1
            grid[r][c] = -1
    
    # bfs function to traverse grid to calculate the minDist
    def bfs(self, grid):
        # define deque
        q = deque()
        # define visited matrix with size (h*w) and set to false
        visited = [[False for _ in range(self.W)] for _ in range(self.H)]
        # define directions for exploring the neighbouring of the cell
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # # loop through grid matrix
        for i in range(self.H):
            for j in range(self.W):
                # check if the value of grid at i and jth position as 0 then append (r,c) to queue
                # and mark the cell as visited in visited matrix by setting the value for the cell as True
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited[i][j] = True
        
        # define current dist as 0
        dist = 0
        # loop until queue is empty
        while q:
            # get the current length of the queue
            size = len(q)
            # run a for loop for the current size of the queue
            for _ in range(size):
                # get the top element pair of the queue
                curr = q.popleft()
                # loop through directions array
                for dr, dc in dirs:
                    # get the new row and column 
                    nr, nc = curr[0] + dr, curr[1] + dc
                    # check if the new row and column is in bounds and the cell is not visited yet
                    if 0 <= nr < self.H and 0 <= nc < self.W and not visited[nr][nc]:
                        # if the condition is true then append row and column to queue
                        # and mark the cell as visited by setting the value as True in visited matrix
                        q.append((nr, nc))
                        visited[nr][nc] = True
            # increment the dist value
            dist += 1
        
        if self.minDist > dist - 1:
            self.result = [row[:] for row in grid]
            if dist -1 == 2:
                print("Result grid: ")
                for row in self.result:
                    print(row)
        # store minimum between minDist and current dist -1 
        self.minDist = min(self.minDist, dist - 1)

if __name__ == '__main__':
    buildingPlacement = BuildingPlacement()
    print(buildingPlacement.findMinDistance(3, 3, 1))
