/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    private:
    pair<int, int> dfs(TreeNode* node){
        if (node == NULL) return {0, 0};

        pair<int, int> left = dfs(node -> left);
        pair<int, int> right = dfs(node -> right);

        int child_ans = max(node->val + left.second + right.second, left.first + right.first);
        return {child_ans, left.first + right.first};
        }
        
public:
    int rob(TreeNode* root) {
        pair<int, int> res = dfs(root);
        return max(res.first, res.second);
    }
};