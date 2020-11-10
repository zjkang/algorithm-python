
/**
 * Definition for a point.
 * class Point {
 *     int x;
 *     int y;
 *     Point() { x = 0; y = 0; }
 *     Point(int a, int b) { x = a; y = b; }
 * }
 */

public class bfs_lintcode_611_knight_shortest_path {
    /**
     * @param grid: a chessboard included 0 (false) and 1 (true)
     * @param source: a point
     * @param destination: a point
     * @return: the shortest path
     */

    final static int[] dx = {1, 1, -1, -1, 2, 2, -2, -2};
    final static int[] dy = {2, -2, 2, -2, 1, -1, 1, -1};

    public int shortestPath(boolean[][] grid, Point source, Point destination) {
        // write your code here
        if (grid == null || grid.length < 1 || grid[0].length < 1) {
            return -1;
        }

        int steps = 0;
        int rows = grid.length;
        int cols = grid[0].length;
        boolean[][] visited = new boolean[rows][cols];

        Queue<Point> queue = new ArrayDeque<>();
        queue.offer(source);
        visited[source.x][source.y] = true;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                Point cur = queue.poll();
                if (cur.x == destination.x && cur.y == destination.y) {
                    return steps;
                }

                for (int j = 0; j < 8; j++) {
                    Point next_point = new Point(cur.x + dx[j], cur.y + dy[j]);
                    if (inBound(grid, next_point, visited)) {
                        queue.offer(next_point);
                        visited[next_point.x][next_point.y] = true;
                    }
                }
            }
            steps++;

        }
        return -1;
    }

    private boolean inBound(boolean[][] grid, Point next_point, boolean[][] visited) {
        return next_point.x >= 0 && next_point.x < grid.length &&
                next_point.y >= 0 && next_point.y < grid[0].length &&
                (visited[next_point.x][next_point.y] == false) &&
                (!grid[next_point.x][next_point.y]);
    }
}