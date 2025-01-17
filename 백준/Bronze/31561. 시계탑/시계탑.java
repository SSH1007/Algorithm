import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int M = sc.nextInt();
        if (M <= 30){
            System.out.println(M/2.0);
        }
        else {
            System.out.println(15+(M-30)*(3/2.0));
        }
    }

}