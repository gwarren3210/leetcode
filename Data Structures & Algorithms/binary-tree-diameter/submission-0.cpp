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
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int m = 0;
        height(root, m);
        return m;
    }

private:
    int height(TreeNode* root, int& m){
        if (root == nullptr) return 0;
        int left = height(root->left, m);
        int right = height(root->right, m);
        m = max(left+right, m);
        return 1 + max(left, right);
    }
};
