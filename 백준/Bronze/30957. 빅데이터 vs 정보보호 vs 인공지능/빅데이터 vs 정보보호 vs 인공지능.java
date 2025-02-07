import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        scanner.nextLine();
        
        int B = 0, S = 0, A = 0;
        String input = scanner.nextLine();
        for (char c : input.toCharArray()) {
            if (c == 'B') {
                B++;
            } else if (c == 'S') {
                S++;
            } else if (c == 'A') {
                A++;
            }
        }

        if (B == S && S == A && B == A) {
            System.out.println("SCU");
        } else {
            if (B == Math.max(B, Math.max(S, A))) {
                System.out.print("B");
            }
            if (S == Math.max(B, Math.max(S, A))) {
                System.out.print("S");
            }
            if (A == Math.max(B, Math.max(S, A))) {
                System.out.print("A");
            }
        }
        scanner.close();
    }
}
