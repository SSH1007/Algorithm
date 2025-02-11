import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        int M = sc.nextInt();
        sc.nextLine(); 
        
        int[] lst = new int[M];
        for (int i = 0; i < N; i++) {
            String tmp = sc.nextLine();
            for (int m = 0; m < M; m++) {
                if (tmp.charAt(m) == 'O') {
                    lst[m]++;
                }
            }
        }
        
        boolean found = false;
        for (int m = 0; m < M; m++) {
            if (lst[m] == 0) {
                System.out.println(m + 1);
                found = true;
                break;
            }
        }
        if (!found) {
            System.out.println("ESCAPE FAILED");
        }
        sc.close();
    }
}
