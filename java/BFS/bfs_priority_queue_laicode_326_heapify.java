import java.lang.IllegalArgumentException;

public class bfs_priority_queue_laicode_326_heapify {
    public int[] heapify(int[] array) {
        // Write your solution here
        if (array == null || array.length == 0) {
            throw new IllegalArgumentException("Input array can not be null or empty");
        }
        int size = array.length;
        for (int i = size / 2 - 1; i >= 0; i--) {
            percolateDown(array, i);
        }
        return array;
    }

    private void percolateDown(int[] array, int index) {
        int size = array.length;
        while (index <= size / 2 - 1) {
            int leftChildIndex = index * 2 + 1;
            int rightChildIndex = index * 2 + 2;
            int swapCandidate = leftChildIndex;
            if (rightChildIndex <= size - 1 && array[leftChildIndex] >= array[rightChildIndex]) {
                swapCandidate = rightChildIndex;
            }
            if (array[index] > array[swapCandidate]) {
                swap(array, index, swapCandidate);
            } else {
                break;
            }
            index = swapCandidate;
        }
    }

    private void swap(int[] array, int i, int j) {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}

