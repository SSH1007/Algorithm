import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        for (int i = 1; i <= N; i++ ){
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            int[] arr = {a, b, c};
            java.util.Arrays.sort(arr);
            a = arr[0];
            b = arr[1];
            c = arr[2];
            System.out.print("Case #"+i+": ");
            if (c*c == a*a + b*b){
                System.out.println("YES");
            }
            else {
                System.out.println("NO");
            }
        }
    }
}