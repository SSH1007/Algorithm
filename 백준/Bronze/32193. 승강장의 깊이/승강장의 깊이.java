import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int dap = 0;
        for (int i = 1; i <= N; i += 1){
            int A = sc.nextInt();
            int B = sc.nextInt();
            dap += A;
            dap -= B;
            System.out.println(dap);
        }
        sc.close();
    }
}