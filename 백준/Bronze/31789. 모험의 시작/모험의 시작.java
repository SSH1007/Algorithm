import java.util.Scanner;


public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int X = sc.nextInt();
        int S = sc.nextInt();
        int dap = 0;
        for (int i = 1; i<=N; i++){
            int c = sc.nextInt();
            int p = sc.nextInt();
            if (c <= X && dap < p){
                dap = p;
            }
        }
        if (dap > S){
            System.out.println("YES");
        }
        else {
            System.out.println("NO");
        }
    }
}