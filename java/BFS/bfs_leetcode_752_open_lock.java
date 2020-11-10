import java.util.*;

class bfs_leetcode_752_open_lock {

    public int bfs_leetcode_752_open_lock(String[] deadends, String target) {
        Set<Integer> enqueued = new HashSet<>();

        for (String deadend : deadends) {
            enqueued.add(Integer.valueOf(deadend));
        }

        Integer targetInt = Integer.valueOf(target);
        if (enqueued.contains(0)) {
            return -1;
        }
        if (targetInt.equals(0)) {
            return 0;
        }

        Queue<Integer> queue = new ArrayDeque<>();
        queue.offer(0);
        enqueued.add(0);

        int depth = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                Integer node = queue.poll();
                if (targetInt.equals(node)) {
                    return depth;
                }
                for (Integer nei : getNeighbors(node)) {
                    if (enqueued.add(nei)) {
                        queue.offer(nei);
                    }
                }
            }
            depth++;
        }
        return -1;
    }

    private static final int[] PARTS = new int[] {1, 10, 100, 1000};

    private List<Integer> getNeighbors(Integer node){
        List<Integer> result = new ArrayList<>();
        for (int i : PARTS) {
            for (int d = -1; d <= 1; d += 2) {
                int digit = (node / i) % 10;

                int nei = node + d * i;
                if (digit == 0 && d == -1) {
                    nei = node + 9 * i;
                }
                if (digit == 9 && d == 1) {
                    nei = node - 9 * i;
                }
                result.add(nei);
            }
        }
        return result;
    }
}

