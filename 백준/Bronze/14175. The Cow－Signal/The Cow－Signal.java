import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int M = sc.nextInt();
        int N = sc.nextInt();
        int K = sc.nextInt();
        sc.nextLine();
        
        for (int i = 0; i < M; i++) {
            String S = sc.nextLine();
            for (int j = 0; j < K; j++) {
                for (char c : S.toCharArray()) {
                    for (int k = 0; k < K; k++) {
                        System.out.print(c);
                    }
                }
                System.out.println();
            }
        }
        sc.close();
    }
}