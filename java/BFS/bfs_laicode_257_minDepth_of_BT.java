/**
 *Given a binary tree, find its minimum depth. The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
 *
 * Example:
 *
 * Given the below binary tree
 *
 *              5
 *
 *           /       \
 *
 *         3         8
 *
 *            \
 *
 *                4
 *
 * minimum depth is 2,path is 5→8.
 *
 * Clarification:
 *   1. The root itself can be a valid path if there is only one node in the binary tree
 *   2. If root == null, return 0
 *
 */
/**
 * public class TreeNode {
 *   public int key;
 *   public TreeNode left;
 *   public TreeNode right;
 *   public TreeNode(int key) {
 *     this.key = key;
 *   }
 * }
 */
public class bfs_laicode_257_minDepth_of_BT {
    public int minDepth(TreeNode root) {
        // Write your solution here
        if (root == null) {
            return 0;
        }
        int minDep = 0;
        Queue<TreeNode> queue = new ArrayDeque<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            int size = queue.size();
            minDep++;
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                if (node.left == null && node.right == null) {
                    return minDep;
                }
                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
        }
        return minDep;
    }
}
