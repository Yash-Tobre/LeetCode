class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:


        n = len(grid)
        row_count = defaultdict(int)
        
        # Count the frequency of each row
        for row in grid:
            row_tuple = tuple(row)
            row_count[row_tuple] += 1

        count = 0
        
        # Check each column against the row frequency
        for c in range(n):
            col_tuple = tuple(grid[r][c] for r in range(n))
            if col_tuple in row_count:
                count += row_count[col_tuple]
        
        return count

            
