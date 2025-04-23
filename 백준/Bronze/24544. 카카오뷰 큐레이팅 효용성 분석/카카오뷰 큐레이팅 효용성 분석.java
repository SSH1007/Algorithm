import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] As = new int[N];
        int[] Bs = new int[N];
        for (int i = 0; i < N; i++) {
            As[i] = sc.nextInt();
        }
        for (int i = 0; i < N; i++) {
            Bs[i] = sc.nextInt();
        }
        int totalSum = 0;
        for (int a : As) {
            totalSum += a;
        }
        System.out.println(totalSum);
        int tmp = 0;
        for (int i = 0; i < N; i++) {
            tmp += ((Bs[i] ^ 1) * As[i]);
        }
        System.out.println(tmp);
    }
}