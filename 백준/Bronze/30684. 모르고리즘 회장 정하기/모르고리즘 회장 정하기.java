import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = Integer.parseInt(scanner.nextLine());
        List<String> list = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            String name = scanner.nextLine();
            if (name.length() == 3) {
                list.add(name);
            }
        }
        Collections.sort(list);
        if (!list.isEmpty()) {
            System.out.println(list.get(0));
        }
    }
}