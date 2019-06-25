class Solution {
  public String longestCommonPrefix(String[] strs) {
    int len = strs.length;
    if (len == 0) {
      return "";
    }
    String pre = strs[0];
    for (int i = 1; i < len; ++i) {
      while (strs[i].indexOf(pre) != 0) {
        pre = pre.substring(0, pre.length() - 1);
      }
    }
    return pre;
  }
}
