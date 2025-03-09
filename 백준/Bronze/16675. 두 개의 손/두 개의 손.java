import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String ML = sc.next();
        String MR = sc.next();
        String TL = sc.next();
        String TR = sc.next();
        
        // 민성이 올 바위, 태경이 보
        if (ML.equals("R") && MR.equals("R") && (TL.equals("P") || TR.equals("P"))) {
            System.out.println("TK");
        }
        // 민성이 올 보, 태경이 가위
        else if (ML.equals("P") && MR.equals("P") && (TL.equals("S") || TR.equals("S"))) {
            System.out.println("TK");
        }
        // 민성이 올 가위, 태경이 바위
        else if (ML.equals("S") && MR.equals("S") && (TL.equals("R") || TR.equals("R"))) {
            System.out.println("TK");
        }
        // 민성이 바위, 태경이 올 가위
        else if ((ML.equals("R") || MR.equals("R")) && TL.equals("S") && TR.equals("S")) {
            System.out.println("MS");
        }
        // 민성이 가위, 태경이 올 보
        else if ((ML.equals("S") || MR.equals("S")) && TL.equals("P") && TR.equals("P")) {
            System.out.println("MS");
        }
        // 민성이 보, 태경이 올 바위
        else if ((ML.equals("P") || MR.equals("P")) && TL.equals("R") && TR.equals("R")) {
            System.out.println("MS");
        } else {
            System.out.println("?");
        }
        sc.close();
    }
}