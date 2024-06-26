#!/usr/bin/python3
"""
Function to calculate the perimeter of an island in a grid
"""


def island_perimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all four possible sides
                if i == 0 or grid[i-1][j] == 0:  # Check up
                    perimeter += 1
                if i == rows - 1 or grid[i+1][j] == 0:  # Check down
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:  # Check left
                    perimeter += 1
                if j == cols - 1 or grid[i][j+1] == 0:  # Check right
                    perimeter += 1

    return perimeter
