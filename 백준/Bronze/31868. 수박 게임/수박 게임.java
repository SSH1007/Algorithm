import java.util.Scanner;


public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int cnt = 1;
        while (true) {
            if (cnt == N){
                System.out.println(K);
                break;
            }
            K/=2;
            cnt+=1;
        }
    }
    

}