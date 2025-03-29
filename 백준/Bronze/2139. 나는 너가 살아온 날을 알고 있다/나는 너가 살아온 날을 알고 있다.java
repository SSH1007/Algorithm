import java.util.Scanner;

public class Main {
    
    public static boolean leap(int n) {
        if ((n % 4 == 0 && n % 100 != 0) || (n % 400 == 0)) {
            return true;
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] month = {0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334};
        int[] leap_month = {0, 0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335};
        
        while (true) {
            int d = sc.nextInt();
            int m = sc.nextInt();
            int y = sc.nextInt();
            if (d == 0 && m == 0 && y == 0) {
                break;
            }
            if (leap(y)) {
                System.out.println(leap_month[m] + d);
            } else {
                System.out.println(month[m] + d);
            }
        }
        sc.close();
    }
}