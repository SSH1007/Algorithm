import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] lst0 = new int[N];
        int[] lst1 = new int[N];
        
        for (int i = 0; i < N; i++) {
            lst0[i] = sc.nextInt();
        }
        for (int i = 0; i < M; i++) {
            int B = sc.nextInt();
            for (int j = 0; j < N; j++) {
                if (B >= lst0[j]) {
                    lst1[j]++;
                    break;
                }
            }
        }
        int dap = 0;
        int maxVote = 0;
        for (int i = 0; i < N; i++) {
            if (lst1[i] > maxVote) {
                maxVote = lst1[i];
                dap = i;
            }
        }
        System.out.println(dap + 1);
        sc.close();
    }
}