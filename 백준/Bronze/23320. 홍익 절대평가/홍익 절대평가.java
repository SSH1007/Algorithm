import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] As = new int[N];
        for (int i = 0; i < N; i++) {
            As[i] = sc.nextInt();
        }
        int X = sc.nextInt();
        int Y = sc.nextInt();
        int tmp = 0;
        for (int a : As) {
            if (a >= Y) {
                tmp++;
            }
        }
        System.out.println((N * X / 100) + " " + tmp);
    }
}