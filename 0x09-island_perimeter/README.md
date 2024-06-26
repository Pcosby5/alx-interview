# Island Perimeter

This project contains a function to calculate the perimeter of an island in a grid.

## Description

The function `island_perimeter(grid)` calculates the perimeter of an island represented by a 2D grid. The grid contains integers where `0` represents water and `1` represents land. Each cell is a square with a side length of 1, and cells are connected horizontally or vertically.

## Usage

To use the `island_perimeter` function, you need to pass a 2D list representing the grid to the function. The function will return the perimeter of the island.

Example:

```python
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))  # Output: 12
