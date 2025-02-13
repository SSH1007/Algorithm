import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            int n = sc.nextInt();
            if (n == -1) {
                break;
            }
            
            int dap = 0, f = 0;
            for (int i = 0; i < n; i++) {
                int s = sc.nextInt();
                int t = sc.nextInt();
                
                dap += s * (t - f);
                f = t;
            }
            System.out.println(dap + " miles");
        }
        sc.close();
    }
}