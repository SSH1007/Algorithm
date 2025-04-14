import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int blocks = 0;
        int x = 0;
        int y = 1;
        int cnt = 0;
        while (true) {
            blocks += (x * x + y * y);
            if (n < blocks) {
                break;
            }
            x += 1;
            y += 1;
            cnt += 1;
        }
        System.out.println(cnt);
    }
}