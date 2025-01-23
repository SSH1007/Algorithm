import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] As = new int[N];
        for (int i = 0; i < N; i++){
            As[i] = sc.nextInt();
        }
        int s = 0;
        int dap = 0;
        for (int a : As){
            s = Math.max(0, s+a);
            if (s >= M){
                dap ++;
            }
        }
        System.out.println(dap);
    }
}