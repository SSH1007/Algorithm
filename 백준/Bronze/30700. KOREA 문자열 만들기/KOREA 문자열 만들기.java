import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String S = scanner.nextLine();
        String[] K = {"K", "O", "R", "E", "A"};
        int j = 0;
        StringBuilder tmp = new StringBuilder();

        for (int i = 0; i < S.length(); i++) {
            if (S.charAt(i) == K[j].charAt(0)) {
                tmp.append(S.charAt(i));
                j = (j + 1) % 5;
            }
        }
        System.out.println(tmp.length());
    }
}