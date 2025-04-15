import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        char[] S = input.toCharArray();
        boolean hasA = false;
        boolean hasB = false;
        boolean hasC = false;
        for (char c : S) {
            if (c == 'A') {
                hasA = true;
                break;
            } else if (c == 'B') {
                hasB = true;
            } else if (c == 'C') {
                hasC = true;
            }
        }
        if (hasA) {
            for (int i = 0; i < S.length; i++) {
                if (S[i] == 'B' || S[i] == 'C' || S[i] == 'D' || S[i] == 'F') {
                    S[i] = 'A';
                }
            }
        } else if (hasB) {
            for (int i = 0; i < S.length; i++) {
                if (S[i] == 'C' || S[i] == 'D' || S[i] == 'F') {
                    S[i] = 'B';
                }
            }
        } else if (hasC) {
            for (int i = 0; i < S.length; i++) {
                if (S[i] == 'D' || S[i] == 'F') {
                    S[i] = 'C';
                }
            }
        } else {
            for (int i = 0; i < S.length; i++) {
                S[i] = 'A';
            }
        }
        System.out.println(new String(S));
    }
}