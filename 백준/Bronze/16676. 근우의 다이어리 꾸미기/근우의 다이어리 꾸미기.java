import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int std = 11;
        int dap = 1;
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine());
        while (true) {
            if (N < std) {
                System.out.println(dap);
                break;
            } else {
                std = std * 10 + 1;
                dap += 1;
            }
        }
        sc.close();
    }
}