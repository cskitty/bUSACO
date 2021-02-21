#include <iostream>
#include <bits/stdc++.h>

using namespace std;
vector<int> nums(3);

int pivotIndex(vector<int>& nums) {
    vector<int> prefixSum;
    prefixSum.resize(nums.size());
    prefixSum[0] = nums[0];
    for (int i = 1; i < nums.size(); i++) {
        prefixSum[i] = nums[i] + prefixSum[i - 1];
    }

    if (prefixSum[nums.size() - 1] - prefixSum[0] == 0) {
        return 0;
    }
    else {
        int i;
        for (i = 1; i < nums.size(); i++) {
            //        cout << prefixSum[i - 1] << ' ' << prefixSum[nums.size() - 1] << ' ' << prefixSum[i] << endl;
            if (prefixSum[i - 1] == prefixSum[nums.size() - 1] - prefixSum[i]) {
                return i;

            }
        }
        if (i == nums.size()) {
            return -1;
        }
    }
    return 0;
}
int main() {
    vector<int> nums{1, 7, 3, 6, 5, 6};
    cout << pivotIndex(nums);
}