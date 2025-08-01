/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        return convert(nums, 0, nums.length - 1);
    }
    private TreeNode convert(int[] nums, int left, int right){
        if(left > right){
            return null;
        }
        int mid = (left + right)/2;
        TreeNode midNode = new TreeNode(nums[mid]);
        midNode.left = convert(nums, left, mid -1);
        midNode.right = convert(nums, mid+1, right);

        return midNode;
    }
}