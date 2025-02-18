import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int cnt = 1;

        while (true) {
            int o = scanner.nextInt();
            int w = scanner.nextInt();
            if (o == 0 && w == 0) {
                break;
            }
            scanner.nextLine();

            int alive = 1;

            while (true) {
                if (!scanner.hasNextLine()) {
                    break;
                }

                String input = scanner.nextLine().trim();
                if (input.isEmpty()) {
                    continue;
                }

                String[] parts = input.split(" ");
                String c = parts[0];

                if (c.equals("#")) {
                    break;
                }

                int n = Integer.parseInt(parts[1]);

                if (alive == 1) {
                    if (c.equals("E")) {
                        w -= n;
                    } else if (c.equals("F")) {
                        w += n;
                    }
                }

                if (w <= 0) {
                    alive = 0;
                }
            }

            if (alive == 1) {
                if (o * 2 > w && w > o / 2) {
                    System.out.println(cnt + " :-)");
                } else {
                    System.out.println(cnt + " :-(");
                }
            } else {
                System.out.println(cnt + " RIP");
            }
            cnt++;
        }
        scanner.close();
    }
}