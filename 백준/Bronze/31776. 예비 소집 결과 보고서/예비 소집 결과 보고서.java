import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int dap = 0;
        
        for (int i = 0; i < N; i++) {
            int[] Ts = new int[3];
            for (int j = 0; j < 3; j++) {
                Ts[j] = scanner.nextInt();
            }
            
            if (Ts[0] >= 0 && Ts[1] == -1 && Ts[2] == -1) dap++;
            else if (Ts[0] >= 0 && Ts[1] >= Ts[0] && Ts[2] == -1) dap++;
            else if (Ts[0] >= 0 && Ts[1] >= Ts[0] && Ts[2] >= Ts[1]) dap++;
        }
        
        System.out.println(dap);
        scanner.close();
    }
}
