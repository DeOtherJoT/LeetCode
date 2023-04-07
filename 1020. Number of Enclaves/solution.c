/**
 * @brief	Solution uses a Depth First Search approach to eliminate the island clusters
 * 			that touched the edge of the map. The remaining land boxes are then summed up
 * 			and returned.
*/

void    dfs_sink(int **grid, int x, int y, int max_row, int max_col){
	if (x == -1 || y == -1 || x == max_row || y == max_col || grid[x][y] == 0)
        return ;
    grid[x][y] = 0;
    dfs_sink(grid, x + 1, y, max_row, max_col);
    dfs_sink(grid, x, y + 1, max_row, max_col);
    dfs_sink(grid, x - 1, y, max_row, max_col);
    dfs_sink(grid, x, y - 1, max_row, max_col);
}

void    sink_borders(int **grid, int row, int col){
    for (int i = 0; i < col; i++){
        dfs_sink(grid, 0, i, row, col);
        dfs_sink(grid, row - 1, i, row, col);
    }
    for (int j = 0; j < row; j++){
        dfs_sink(grid, j, 0, row, col);
        dfs_sink(grid, j, col - 1, row, col);
    }
}

// Driver function
int numEnclaves(int** grid, int gridSize, int* gridColSize){
    int row_len = gridSize, col_len = gridColSize[0];
    int i = -1, j = -1, sum = 0;

    sink_borders(grid, row_len, col_len);
    while (++i < row_len){
        j = -1;
        while (++j < col_len){
            sum += grid[i][j];
        }
    }
    return (sum);
}