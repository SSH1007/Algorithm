import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int sH = sc.nextInt();
        int sM = sc.nextInt();
        int eH = sc.nextInt();
        int eM = sc.nextInt();
        String N = sc.next();
        int dap = 0;
        while (true) {
            String hourStr = String.format("%02d", sH);
            String mStr = String.format("%02d", sM);
            String tStr = hourStr + mStr;
            for (int i = 0; i < tStr.length(); i++) {
                if (tStr.charAt(i) == N.charAt(0)) {
                    dap++;
                    break;
                }
            }
            if (sH == eH && sM == eM) {
                break;
            }
            sM += 1;
            if (sM == 60) {
                sH += 1;
                sM = 0;
            }
        }
        System.out.println(dap);
    }
}