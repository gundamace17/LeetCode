#include <iostream>
#include <cmath>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> prevMap;

        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i]; // Use the diff to search the other number in the array
                                         // and it must be target - nums[i]
            if(prevMap.count(diff)){     // If diff exists, return the index of diff stored in prevMap and i
                cout << prevMap[diff] << " " << i << endl;
                return { prevMap[diff], i };
            }
            prevMap[nums[i]] = i;        // Store the index of each element in nums
        }
        return {};
    }
};

int main()
{
    Solution sol;
    vector<int> nums = {2, 3, 1, 4};
    sol.twoSum(nums, 3);
    return 0;
}
