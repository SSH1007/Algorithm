import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int T = scanner.nextInt();
        
        for (int t = 0; t < T; t++) {
            int L = scanner.nextInt();
            int R = scanner.nextInt();
            int S = scanner.nextInt();
            
            int LS = Math.abs(L - S);
            int RS = Math.abs(R - S);
            
            if (S == R || S == L) {
                System.out.println(0);
                continue;
            }
            
            if (LS > RS) {
                System.out.println(RS * 2);
            } else if (LS < RS) {
                System.out.println(LS * 2 + 1);
            } else {
                System.out.println(RS * 2);
            }
        }
        scanner.close();
    }
}