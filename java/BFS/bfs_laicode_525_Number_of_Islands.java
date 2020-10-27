import java.lang.*;

public class bfs_laicode_525_Number_of_Islands {
    final static int[] dx = {0, -1, 0, 1};
    final static int[] dy = {-1, 0, 1, 0};

    public int numIslands(char[][] grid) {
        // Write your solution here
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return 0;
        }
        int count = 0;
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

    private boolean inBound (char[][] grid, int r, int c) {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length) {
            return false;
        }
        return true;
    }

    private void BFS (char[][] grid, int r, int c, boolean[][] visited) {
        int rows = grid.length;
        int cols = grid[0].length;
        Queue<Integer> queue = new ArrayDeque<>();
        int code = r * cols + c;
        queue.offer(Integer.valueOf(code));
        visited[r][c] = true;
        while (!queue.isEmpty()) {
            Integer cur = queue.poll();
            for (int i = 0; i < 4; i++) {
                int x = cur.intValue() / cols + dx[i];
                int y = cur.intValue() % cols + dy[i];
                if (inBound(grid, x, y) && !visited[x][y] && grid[x][y] == '1') {
                    queue.offer(Integer.valueOf(x * cols + y));
                    visited[x][y] = true;
                }
            }
        }
        return;
    }

}
