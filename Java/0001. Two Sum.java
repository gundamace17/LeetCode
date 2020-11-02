package com.company;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[j] == target - nums[i]) {
                    System.out.println(i + ", " + j);
                    return new int[] {i, j};
                }
            }
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}

public class Main {

    public static void main(String[] args) {
	    Solution mySol = new Solution();
	    int[] myNum = {2,7,11,15};
	    int myTarget = 9;
	    mySol.twoSum(myNum, myTarget);
    }
}
