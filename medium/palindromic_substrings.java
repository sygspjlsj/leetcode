class Solution {
  public int countSubstrings(String s) {
    int len = s.length();
    boolean matrix[][] = new boolean[len][len];
    int ret = 0;
    for (int i = len - 1; i >= 0; --i) {
      for (int j = i; j < len; ++j) {
        matrix[i][j] = s.charAt(i) == s.charAt(j) && ((j - i) < 3 || matrix[i + 1][j - 1]);
        if (matrix[i][j]) {
          ret++;
        }
      }
    }
    return ret;
  }
}
