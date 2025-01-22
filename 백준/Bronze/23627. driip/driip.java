import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String S = sc.nextLine();
        if (S.length() >= 5 && S.endsWith("driip")){
            System.out.println("cute");
        } else {
            System.out.println("not cute");
        }
    }
}