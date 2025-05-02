import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int[][] lst = new int[2][26];
        Scanner sc = new Scanner(System.in);
        while (true) {
            String line = sc.nextLine();
            String[] ipt = line.split(" ");
            if (ipt[0].equals("-1")) {
                break;
            }
            int m = Integer.parseInt(ipt[0]);
            String nme = ipt[1];
            String res = ipt[2];
            int idx = nme.charAt(0) - 'A';
            if (res.equals("right")) {
                lst[1][idx] = 1;
                lst[0][idx] += m;
            } else {
                lst[0][idx] += 20;
            }
        }
        int dap = 0;
        int sum = 0;
        for (int i = 0; i < 26; i++) {
            if (lst[1][i] == 1) {
                dap += lst[0][i];
                sum++;
            }
        }
        System.out.println(sum + " " + dap);
        sc.close();
    }
}