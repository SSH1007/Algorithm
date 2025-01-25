import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int Cu = sc.nextInt();
        int Du = sc.nextInt();
        int Cd = sc.nextInt();
        int Dd = sc.nextInt();
        int Cp = sc.nextInt();
        int Dp = sc.nextInt();
        int H = sc.nextInt();

        int sec = 0;

        while (H > 0) {
            if (sec % Cu == 0) {
                H -= Du;
            }
            if (sec % Cd == 0) {
                H -= Dd;
            }
            if (sec % Cp == 0) {
                H -= Dp;
            }
            if (H <= 0) {
                break;
            }
            sec++;
        }

        System.out.println(sec);
        
        sc.close();
    }
}