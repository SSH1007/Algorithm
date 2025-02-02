import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        sc.nextLine();
        String S = sc.nextLine();
        
        int[] lst = new int[26];
        for (int i = 0; i < n; i++) {
            lst[S.charAt(i) - 'a']++;
        }
        
        int dap = 1000;
        char[] targetChars = {'u', 'o', 's', 'p', 'c'};
        for (char ch : targetChars) {
            int tmp = lst[ch - 'a'];
            if (dap > tmp) {
                dap = tmp;
            }
        }
      
        System.out.println(dap);
        sc.close();
    }
}
