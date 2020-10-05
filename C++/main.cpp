#include <iostream>
#include <unordered_map>
#include <math.h>
#include <string>

using namespace std;

class Solution {
public:
    int titleToNumber(string s) {
        string letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        unordered_map<char, int> pairs;

        for(int i = 0; i < letters.size(); i++){
            pairs[letters[i]] = i+1;
        }

        int result = 0;
        int j = s.size();
        while(j >= 1){
            result = result + pairs[s[j-1]] * pow(26, s.size() - j);
            j--;
        }
        cout << result << endl;
        return result;
    }
};

int main()
{
    Solution sol;
    sol.titleToNumber("AA");
    return 0;
}
