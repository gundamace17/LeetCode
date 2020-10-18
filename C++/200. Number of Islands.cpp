// 200. Number of Islands.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void land_track(vector<vector<char>>& grid, int row, int col, int& m, int& n)
    {
        grid[row][col] = '#';
        if (row < m - 1 && grid[row + 1][col] == '1') land_track(grid, row + 1, col, m, n);
        if (row > 0 && grid[row - 1][col] == '1') land_track(grid, row - 1, col, m, n);
        if (col < n - 1 && grid[row][col + 1] == '1') land_track(grid, row, col + 1, m, n);
        if (col > 0 && grid[row][col - 1] == '1') land_track(grid, row, col - 1, m, n);
        return;
    }

    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        if (m == 0) return 0;

        int num = 0;
        for (int row = 0; row < m; row++)
        {
            for (int col = 0; col < n; col++)
            {
                if (grid[row][col] == '1')
                {
                    num++;
                    land_track(grid, row, col, m, n);
                }
            }
        }
        cout << num << endl;
        return num;
    }
};

int main()
{
    Solution sol;
    vector<vector<char>> matrix = { {'1', '1', '1', '1', '0'},
                                    {'1', '1', '0', '1', '0'},
                                    {'1', '1', '0', '0', '0'},
                                    {'0', '0', '0', '0', '1'} };

    sol.numIslands(matrix);
}

