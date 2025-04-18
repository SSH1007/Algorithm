import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static int[] buildLPS(String pattern) {
        int m = pattern.length();
        int[] lps = new int[m];
        int len = 0;
        int i = 1;
        while (i < m) {
            if (pattern.charAt(i) == pattern.charAt(len)) {
                len++;
                lps[i] = len;
                i++;
            } else {
                if (len != 0) {
                    len = lps[len - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }
        return lps;
    }

    public static boolean kmpSearch(String text, String pattern) {
        int n = text.length();
        int m = pattern.length();
        int[] lps = buildLPS(pattern);
        int i = 0, j = 0;
        while (i < n) {
            if (text.charAt(i) == pattern.charAt(j)) {
                i++;
                j++;
            }
            if (j == m) {
                return true;
            } else if (i < n && text.charAt(i) != pattern.charAt(j)) {
                if (j != 0) {
                    j = lps[j - 1];
                } else {
                    i++;
                }
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String N = br.readLine();
        String K = br.readLine();
        StringBuilder filtered = new StringBuilder();
        for (char c : N.toCharArray()) {
            if (!Character.isDigit(c)) {
                filtered.append(c);
            }
        }
        if (kmpSearch(filtered.toString(), K)) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
}