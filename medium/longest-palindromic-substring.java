public class Test {
  public String getString(String s) {
    int n = s.length();
    String ret = null;

    boolean matrix[][] = new matrix[n][n];

    for (int i = n - 1; i >= 0; --i) {
      for (int j = i; j < n; ++j) {
        matrix[i][j] = s.charAt(i) == s.charAt(j) && (j - i < 3 || matrix[i + 1][j - 1]);
        if (matrix[i][j] && (ret == null || (j - i + 1) > ret.length())) {
          ret = s.substring(i, j + 1);
        }
      }
    }
    return ret;
  }
}
