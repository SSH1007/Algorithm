import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int Q = scanner.nextInt();
        int[] balloon = new int[N + 1];
        for (int q = 0; q < Q; q++) {
            int L = scanner.nextInt();
            int I = scanner.nextInt();
            for (int i = L; i <= N; i += I) {
                balloon[i] = 1;
            }
        }
        int count = 0;
        for (int i = 1; i <= N; i++) {
            if (balloon[i] == 0) {
                count++;
            }
        }
        System.out.println(count);
        scanner.close();
    }
}