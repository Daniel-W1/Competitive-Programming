class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans;
        unordered_map<int, int> index_map;
        
        for (int idx = 0; idx < nums.size(); idx ++){
            int new_target = target - nums[idx];
            
            if (index_map.find(new_target) != index_map.end()){
                ans.push_back(index_map[new_target]);
                ans.push_back(idx);
                break;
            }
            else{
                index_map[nums[idx]] = idx;
            }
            
        }
        return ans;
    }
};