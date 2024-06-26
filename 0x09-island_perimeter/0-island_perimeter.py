#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of int): A 2D grid representing the map
                                    where 0 is water and 1 is land.

    Returns:
        int: The perimeter of the island.
    """
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
