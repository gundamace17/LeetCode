// 200. Number of Islands.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
// Explanation of the Algorithm:
// Define a land_track function for BFS and mark visited elements as #.
// Num of island +1 and look for the next island.
// Once all 1 becomes #, return num.
//
//   { {'1', '1', '1', '1', '0'},          { {'#', '#', '#', '#', '0'},           { {'#', '#', '#', '#', '0'},
//     {'1', '1', '0', '1', '0'},   ---->    {'#', '#', '0', '#', '0'},   ---->     {'#', '#', '0', '#', '0'},
//     {'1', '1', '0', '0', '0'},            {'#', '#', '0', '0', '0'},             {'#', '#', '0', '0', '0'},
//     {'0', '0', '0', '0', '1'} }           {'0', '0', '0', '0', '1'} }            {'0', '0', '0', '0', '#'} }
//                                                   num == 1                                num == 2

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void land_track(vector<vector<char>>& grid, int row, int col, int& m, int& n)
    {
        grid[row][col] = '#'; // Mark the element that has been visited as #
        // Move down
        if (row < m - 1 && grid[row + 1][col] == '1') land_track(grid, row + 1, col, m, n);
        
        // Move up
        if (row > 0 && grid[row - 1][col] == '1') land_track(grid, row - 1, col, m, n);
        
        // Move right
        if (col < n - 1 && grid[row][col + 1] == '1') land_track(grid, row, col + 1, m, n);
        
        // Move left
        if (col > 0 && grid[row][col - 1] == '1') land_track(grid, row, col - 1, m, n);
        return;
    }

    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size();     // Set the number of row is m
        int n = grid[0].size();  // Set the number of col is n

        if (m == 0) return 0;    // If no element, return 0.

        int num = 0;             // Initialize the number of islands.
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

