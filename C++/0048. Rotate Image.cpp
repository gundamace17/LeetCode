// 0048. Rotate Image.cpp : This file contains the 'main' function. Program execution begins and ends there.
/*

Expalanation of the Algorithm:
Step1 Reverse the order of elements in matrix
Step2 Swap Matrix[i][j] with Matrix[j][i]

[[1, 2, 3]    step1   [[7, 8, 9]    step2   [[7, 4, 1] 
 [4, 5, 6]   ------>   [4, 5, 6]   ------>   [8, 5, 2]  
 [7, 8, 9]]            [1, 2, 3]]            [9, 6, 3]]

*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        std::reverse(matrix.begin(), matrix.end());

        for (int i = 0; i < matrix.size(); i++)
            for (int j = i; j < matrix[0].size(); j++)
            {
                swap(matrix[i][j], matrix[j][i]);
            }
    }
};

int main()
{
    Solution sol;
    vector<vector<int>> A = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} };
    sol.rotate(A);

    for (auto i = 0; i < A.size(); ++i)
    {
        for (auto j = 0; j < A[0].size(); ++j)
        {
            cout << A[i][j];
        }
        cout << endl;
    }
}


