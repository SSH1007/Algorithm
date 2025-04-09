import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] buckets = new int[1001];
        for (int n = 0; n < N; n++) {
            int s = scanner.nextInt();
            int t = scanner.nextInt();
            int b = scanner.nextInt();
            for (int i = s; i <= t; i++) {
                buckets[i] += b;
            }
        }
        int max = 0;
        for (int i = 0; i < 1001; i++) {
            max = Math.max(max, buckets[i]);
        }
        System.out.println(max);
        scanner.close();
    }
}