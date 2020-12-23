public class binary_search_laicode_20_unknown_size {
    public int search(Dictionary dict, int target) {
        // Write your solution here
        if (dict == null) {
            return -1;
        }
        int left = 0;
        int right = 1;
        while (dict.get(right) != null && dict.get(right) < target) {
            left = right;
            right = right * 2;
        }
        return binarySearch(dict, target, left, right);
    }

    private int binarySearch(Dictionary dict, int target, int left, int right) {
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            if (dict.get(mid) == target) {
                return mid;
            }else if (dict.get(mid) == null|| dict.get(mid) > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        if (dict.get(left) == target) {
            return left;
        }
        if (dict.get(right) == target) {
            return right;
        }
        return -1;
    }
}
