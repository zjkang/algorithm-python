
public class bfs_laicode_661_word_ladder_I {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        // Write your solution here
        Set<String> wordSet = new HashSet<>(wordList);
        if (!wordSet.contains(endWord) || beginWord == null) {
            return 0;
        }
        int transformations = 1;
        Deque<String> queue = new ArrayDeque<>();
        Set<String> visited = new HashSet<>();
        queue.addLast(beginWord);
        while (!queue.isEmpty()) {
            int count = queue.size();
            for (int i = 0; i < count; i++) {
                String cur = queue.pollFirst();
                if (cur.equals(endWord)) {
                    return transformations;
                }
                for (String nei : getAdjacentWords (cur, wordSet, visited)) {
                    queue.addLast(nei);
                }
            }
            transformations++;
        }
        return 0;
    }

    private Set<String> getAdjacentWords(String word, Set<String> wordSet, Set<String> visited) {
        Set<String> result = new HashSet<>();
        char[] chars = word.toCharArray();
        for (int i = 0; i < word.length(); i++) {
            for (int j = 0; j < 26; j++) {
                char orig = chars[i];
                chars[i] = (char)('a' + j);
                String newWord = new String(chars);
                if (!word.equals(newWord) && wordSet.contains(newWord)
                        && !visited.contains(newWord)) {
                    visited.add(newWord);
                    result.add(newWord);
                }
                chars[i] = orig;
            }
        }
        return result;
    }
}
