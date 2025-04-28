import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int n = sc.nextInt();
        int w = sc.nextInt();
        int cnt = 0;
        int[] lst = new int[2];
        for (int x = 1; x < n; x++) {
            if (w == a * x + b * (n - x)) {
                lst[0] = x;
                lst[1] = n - x;
                cnt++;
            }
        }
        if (cnt != 1) {
            System.out.println(-1);
        } else {
            System.out.println(lst[0] + " " + lst[1]);
        }
        sc.close();
    }
}