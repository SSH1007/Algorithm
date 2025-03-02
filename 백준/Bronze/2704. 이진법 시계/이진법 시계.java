import java.util.Scanner;

public class Main {
    
    public static String B(int n) {
        String bin = Integer.toBinaryString(n);
        return String.format("%6s", bin).replace(' ', '0');
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        sc.nextLine();
        
        for (int i = 0; i < N; i++) {
            String time = sc.nextLine();
            String[] parts = time.split(":");
            
            String H = B(Integer.parseInt(parts[0]));
            String M = B(Integer.parseInt(parts[1]));
            String S = B(Integer.parseInt(parts[2]));
            
            String R = H + M + S;
            String C = "";
            for (int j = 0; j < 6; j++) {
                C += H.charAt(j) + "" + M.charAt(j) + "" + S.charAt(j);
            }
            System.out.println(C + " " + R);
        }
        sc.close();
    }
}