import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int D = sc.nextInt();
        int M = sc.nextInt();
        
        String[] dic = {"Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"};
        int[] mth = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        int totalDays = D - 1;
        for (int i = 1; i < M; i++) {
            totalDays += mth[i];
        }
        int dayIndex = totalDays % 7;

        System.out.println(dic[dayIndex]);
        sc.close();
    }
}