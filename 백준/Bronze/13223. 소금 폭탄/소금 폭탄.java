import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] cur = sc.nextLine().split(":");
        String[] bot = sc.nextLine().split(":");
        int curS = Integer.parseInt(cur[0]) * 3600 + Integer.parseInt(cur[1]) * 60 + Integer.parseInt(cur[2]);
        int botS = Integer.parseInt(bot[0]) * 3600 + Integer.parseInt(bot[1]) * 60 + Integer.parseInt(bot[2]);

        int c = botS - curS;
        if (c <= 0) {
            c += 24*3600;
        }

        int h = (c / 3600);
        int m = (c % 3600) / 60;
        int s = (c % 3600) % 60;
        System.out.printf("%02d:%02d:%02d\n", h, m, s);
    }
}
