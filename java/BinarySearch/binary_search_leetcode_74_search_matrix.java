public class binary_search_leetcode_74_search_matrix {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null || matrix.length < 1 || matrix[0].length < 1) {
            return false;
        }
        int rows = matrix.length;
        int cols = matrix[0].length;
        int left = 0;
        int right = rows * cols - 1;
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            if (matrix[mid / cols][mid % cols] == target) {
                return true;
            } else if (matrix[mid / cols][mid % cols] < target) {
                left = mid;
            } else {
                right = mid;
            }
        }
        if (matrix[left / cols][left % cols] == target || matrix[right / cols][right % cols] == target) {
            return true;
        }
        return false;
    }
}
