import java.util.Scanner;

public class Main {
    
    public static int hap(int n) {
        int res = 0;
        while (n > 0) {
            res += n % 10;
            n /= 10;
        }
        return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String S = sc.nextLine();
        for (int i = 0; i < S.length(); i++) {
            char s = S.charAt(i);
            String d = "";
            int hapValue = hap((int) s);
            for (int j = 0; j < hapValue; j++) {
                d += s;
            }
            System.out.println(d);
        }
        sc.close();
    }
}