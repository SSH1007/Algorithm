import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] bulb = new int[N];

        for (int i = 0; i < N; i++) {
            bulb[i] = sc.nextInt();
        }

        for (int i = 0; i < M; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt() - 1;
            int c = sc.nextInt();

            if (a == 1) {
                bulb[b] = c;
            } else if (a == 2) {
                for (int j = b; j < c; j++) {
                    bulb[j] = (bulb[j] + 1) % 2;
                }
            } else if (a == 3) {
                for (int j = b; j < c; j++) {
                    bulb[j] = 0;
                }
            } else {
                for (int j = b; j < c; j++) {
                    bulb[j] = 1;
                }
            }
        }

        for (int i = 0; i < N; i++) {
            System.out.print(bulb[i] + " ");
        }
        System.out.println();
        sc.close();
    }
}