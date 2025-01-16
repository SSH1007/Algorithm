import java.util.Scanner;


public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int n =0, c = 0;
        while (true) {
            n += 1;
            c += 1;
            if (n == N){
                System.out.println(c);
                break;
            }
            if (Integer.toString(n).contains("50")){
                c += 1;
            }
        }

    }

}