row = 0
col = 0
grid = [["x" for j in range(4)] for i in range(6)]
grid[0][0] = "O"
print(grid)
grid[0][0] = "x"
row = int(input("enter the row value that you want to move to")) -1
col = int(input("ente rthe column vale that you want ot move to")) -1
grid[row][col] = "O"
lastrow = row
lastcol = col
print(grid)