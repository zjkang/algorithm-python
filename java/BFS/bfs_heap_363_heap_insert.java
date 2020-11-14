import java.util.*;

public class bfs_heap_363_heap_insert {
    public int[] offerHeap(int[] array, int ele) {
        // Write your solution here
        int length = array.length;
        int index = length - 1;
        array[index] = ele;
        while (index >= 0) {
            int parent = (index - 1) / 2;
            if (parent >= 0 && array[index] < array[parent]) {
                swap(array, index, parent);
                index = parent;
            } else {
                break;
            }
        }
        return array;
    }

    private int[] swap(int[] array, int left, int right) {
        int temp = array[left];
        array[left] = array[right];
        array[right] = temp;
        return array;
    }
}
