import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int C = sc.nextInt();
        int A = N;
        int B = N;
        for (int i = 0; i < C; i++) {
            int X = sc.nextInt();
            int Y = sc.nextInt();
            if (X >= A || Y >= B) {
                continue;
            }
            int horizonCut = X * B;
            int verticalCut = Y * A;
            if (horizonCut >= verticalCut) {
                A = X;
            } else {
                B = Y;
            }
        }
        System.out.println(A * B);
    }
}