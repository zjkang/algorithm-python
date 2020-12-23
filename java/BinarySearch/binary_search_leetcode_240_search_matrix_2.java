public class binary_search_leetcode_240_search_matrix_2 {
    public boolean searchMatrix(int[][] matrix, int target) {
        int r = matrix.length - 1;
        int c = 0;
        while (r >= 0 && c < matrix[0].length) {
            if (matrix[r][c] > target) {
                r--;
            } else if(matrix[r][c] < target) {
                c++;
            } else {
                return true;
            }
        }
        return false;
    }
}
