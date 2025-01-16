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
                break;
            }
            if (containFifty(Integer.toString(n))){
                c += 1;
            }
        }
        System.out.println(c);

    }

    public static boolean containFifty(String numStr){
        return numStr.indexOf("50") != -1;
    }

}