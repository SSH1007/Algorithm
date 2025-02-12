import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int dap = 0;
        
        if (A % 2 == 0) {
            dap++;
            A++;
        }
        for (int i = A; i <= B; i += 2) {
            dap++;
        }

        System.out.println(dap);
        sc.close();
    }
}
