public class binary_search_leetcode_81_rotated_array_search_2 {
    public boolean search(int[] nums, int target) {
        if (nums == null || nums.length < 1) {
            return false;
        }
        int left = 0;
        int right = nums.length -1;
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return true;
            } else if (nums[left] < nums[mid]) {
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid;
                } else {
                    left = mid;
                }
            } else if(nums[left] == nums[mid]) {
                left++;
            } else {
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid;
                } else {
                    right = mid;
                }
            }
        }
        if ((nums[left] == target) || (nums[right] == target)) {
            return true;
        }
        return false;
    }
}
