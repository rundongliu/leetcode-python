/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> postorderTraversal(TreeNode *root) {
        stack<TreeNode*> s;
        vector<int> res;
        if(root==NULL)
            return res;
        s.push(root);
        while(!s.empty())
        {
            TreeNode *node = s.top();
            res.push_back(node->val);
            s.pop();
            if(node->left)
            {
                s.push(node->left);
            }
            if(node->right)
            {
                s.push(node->right);
            }
        }
        reverse(res.begin(),res.end());
        return res;
    }
};