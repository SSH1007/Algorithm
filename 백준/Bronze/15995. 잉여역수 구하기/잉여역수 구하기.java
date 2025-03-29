import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int m = sc.nextInt();
        int x = 1;
        while (true) {
            if ((a * x) % m == 1) {
                break;
            }
            x++;
        }
        System.out.println(x);
        sc.close();
    }
}