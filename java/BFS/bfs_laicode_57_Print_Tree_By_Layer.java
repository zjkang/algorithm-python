/**
Get the list of list of keys in a given binary tree layer by layer.
 Each layer is represented by a list of keys and the keys are traversed from left to right.

        Examples

        5

        /    \

        3        8

        /   \        \

        1     4        11
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
import java.lang.*;

public class bfs_laicode_57_Print_Tree_By_Layer {
    public List<List<Integer>> layerByLayer(TreeNode root) {
        // Write your solution here
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) {
            return result;
        }
        Queue<TreeNode> queue = new ArrayDeque<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            int size = queue.size();
            List<Integer> curLevel = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                curLevel.add(node.key);
                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
            result.add(curLevel);
        }
        return result;
    }
}
