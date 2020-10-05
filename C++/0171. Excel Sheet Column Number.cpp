#include <iostream>
#include <unordered_map>
#include <math.h>
#include <string>

using namespace std;

class Solution {
public:
    int titleToNumber(string s) {
        string letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; // Create a A to Z string
        unordered_map<char, int> pairs;  // Empty unordered_map for storing the value corresponding to each letter

        for(int i = 0; i < letters.size(); i++){
            pairs[letters[i]] = i+1;     // Storing the value: A -> 1, B -> 2, etc
        }

        int result = 0;  // Initialize the result value
        int j = s.size();
        while(j >= 1){
            result = result + pairs[s[j-1]] * pow(26, s.size() - j);  // like a decimal system, this case is like 26 system
            j--;
        }
        cout << result << endl;
        return result;
    }
};

int main()
{
    Solution sol;
    sol.titleToNumber("AA"); // Enter any input
    return 0;
}
