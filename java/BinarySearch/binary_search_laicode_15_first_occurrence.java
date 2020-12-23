public class binary_search_laicode_15_first_occurrence {
    public int firstOccur(int[] array, int target) {
        // Write your solution here
        if (array == null || array.length < 1) {
            return -1;
        }
        int left = 0;
        int right = array.length - 1;
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            if (array[mid] < target) {
                left = mid;
            } else {
                right = mid;
            }
        }
        if (array[left] == target) {
            return left;
        }
        if (array[right] == target) {
            return right;
        }
        return -1;
    }
}
