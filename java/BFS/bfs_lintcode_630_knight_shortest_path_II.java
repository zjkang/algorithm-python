import java.util.*;

public class bfs_lintcode_630_knight_shortest_path_II {
    /**
     * @param grid: a chessboard included 0 and 1
     * @return: the shortest path
     */

    final static int[] dx = {1, -1, 2, -2};
    final static int[] dy = {2, 2, 1, 1};

    class Pair {
        int x;
        int y;

        public Pair (int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object o) {
            Pair pair = (Pair) o;
            return x == pair.x && y == pair.y;
        }

        @Override
        public int hashCode () {
            return Objects.hash(x, y);
        }
    }

    public int shortestPath2(boolean[][] grid) {
        // write your code here
        if (grid == null || grid.length < 1 || grid[0].length < 1) {
            return -1;
        }

        if (grid.length == 1 && grid[0].length == 1) {
            return 0;
        }

        int rows = grid.length;
        int cols = grid[0].length;
        int steps = 0;
        Set<Pair> visited = new HashSet<>();

        Queue<Pair> queue = new ArrayDeque<>();
        Pair start = new Pair(0, 0);
        Pair end = new Pair(rows - 1, cols - 1);
        queue.offer(start);
        visited.add(start);
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                Pair cur = queue.poll();
                if (cur.x == rows - 1 && cur.y == cols - 1) {
                    return steps;
                }
                for (Pair next : getNext(cur, grid, visited)) {
                    visited.add(next);
                    queue.offer(next);
                }
            }
            steps++;
        }
        return -1;
    }

    private List<Pair> getNext (Pair cur, boolean[][] grid, Set<Pair> visited) {
        List<Pair> nexts = new ArrayList<>();
        for (int i = 0; i < 4; i++) {
            int nextX = cur.x + dx[i], nextY = cur.y + dy[i];
            Pair next = new Pair(nextX, nextY);
            if (inBound(nextX, nextY, grid) && !grid[nextX][nextY] && !visited.contains(next)) {
                nexts.add(next);
            }
        }
        return nexts;
    }

    private boolean inBound(int x, int y, boolean[][] grid) {
        return (x >= 0 && x < grid.length && y >= 0 && y < grid[0].length);
    }
}