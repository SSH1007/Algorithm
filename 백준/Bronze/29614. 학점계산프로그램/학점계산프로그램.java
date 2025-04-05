import java.util.HashMap;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        HashMap<String, Double> dic = new HashMap<>();
        dic.put("A", 4.0);
        dic.put("B", 3.0);
        dic.put("C", 2.0);
        dic.put("D", 1.0);
        dic.put("F", 0.0);
        dic.put("+", 0.5);

        String input = sc.nextLine();
        double dap = 0;
        int cnt = 0;
        for (int i = 0; i < input.length(); i++) {
            String grade = String.valueOf(input.charAt(i));
            dap += dic.get(grade);
            if (!grade.equals("+")) {
                cnt++;
            }
        }
        System.out.println(dap / cnt);
    }
}