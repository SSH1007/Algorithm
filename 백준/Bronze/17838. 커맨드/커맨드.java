import java.util.Scanner;

public class Main {
    public static boolean F(String S) {
        if (S.length() != 7) {
            return false;
        }
        if (S.charAt(0) == S.charAt(1) && S.charAt(1) == S.charAt(4) &&
            S.charAt(2) == S.charAt(3) && S.charAt(3) == S.charAt(5) && S.charAt(5) == S.charAt(6) &&
            S.charAt(0) != S.charAt(2)) {
            return true;
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = Integer.parseInt(sc.nextLine());
        for (int i = 0; i < T; i++) {
            String S = sc.nextLine();
            System.out.println(F(S) ? 1 : 0);
        }
        sc.close();
    }
}