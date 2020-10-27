import java.lang.*;

public class bfs_laicode_525_Number_of_Islands {
    final static int[] dx = {0, -1, 0, 1};
    final static int[] dy = {-1, 0, 1, 0};

    public int numIslands(char[][] grid) {
        // Write your solution here
        int count = 0;
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return count;
        }
        int rows = grid.length;
        int cols = grid[0].length;
        boolean[][] visited = new boolean[rows][cols];
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1' && !visited[r][c]) {
                    BFS(grid, r, c, visited);
                    count++;
                }
            }
        }
        return count;
    }

    private boolean inBound(char[][] grid, int r, int c) {
        return r >= 0 && r < grid.length && c >= 0 && c < grid[0].length;
    }

    private void BFS(char[][] grid, int r, int c, boolean[][] visited) {
        Queue<Integer> queue = new ArrayDeque<>();
        int cols = grid[0].length;
        int code = r * cols + c;
        queue.offer(code);
        visited[r][c] = true;
        while (!queue.isEmpty()) {
            int cur = queue.poll();
            for (int i = 0; i < 4; i++) {
                int neighbor_r = cur / cols + dx[i];
                int neighbor_c = cur % cols + dy[i];
                if (inBound(grid, neighbor_r, neighbor_c)
                        && !visited[neighbor_r][neighbor_c]
                        && grid[neighbor_r][neighbor_c] == '1') {
                    queue.offer(neighbor_r * cols + neighbor_c);
                    visited[neighbor_r][neighbor_c] = true;
                }
            }
        }
    }
}
