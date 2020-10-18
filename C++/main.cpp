#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) {
        for(int i = 0; i < A.size(); i++)
        {
            A[i] = pow(A[i], 2);
        }
        sort(A.begin(), A.end());
        return A;
    }
};

int main()
{
    Solution sol;
    vector<int> B = {-7, -3, 2, 3, 11};
    vector<int> A = B;
    sol.sortedSquares(B);

    for(int i = 0; i < A.size(); i++)
    {
        cout << A[i] << " ";  // -7 -3 2 3 11
    }

    cout << endl;

    for(int i = 0; i < B.size(); i++)
    {
        cout << B[i] << " ";  // 4 9 9 49 121
    }
    return 0;
}
