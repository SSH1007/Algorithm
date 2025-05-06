import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        int dap = 0;
        int dir = 1;
        int move = 1;
        int cur = x;
        while (true) {
            int next = x + dir * move;
            if ((x <= y && y <= next) || (next <= y && y <= x)) {
                dap += Math.abs(y - cur);
                break;
            } else {
                dap += Math.abs(next - cur);
                cur = next;
                move *= 2;
                dir *= -1;
            }
        }
        System.out.println(dap);
        sc.close();
    }
}