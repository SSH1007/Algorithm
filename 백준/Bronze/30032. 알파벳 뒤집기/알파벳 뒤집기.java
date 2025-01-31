import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        int D = sc.nextInt();
        sc.nextLine();  // consume the leftover newline character
        
        String[] maps = new String[N];
        for (int i = 0; i < N; i++) {
            maps[i] = sc.nextLine();
        }

        // 딕셔너리 정의
        Map<Character, List<Character>> dic = new HashMap<>();
        dic.put('d', Arrays.asList('q', 'b'));
        dic.put('b', Arrays.asList('p', 'd'));
        dic.put('q', Arrays.asList('d', 'p'));
        dic.put('p', Arrays.asList('b', 'q'));

        char[][] result = new char[N][N];
        
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                char currentChar = maps[r].charAt(c);
                result[r][c] = dic.get(currentChar).get((D + 1) % 2);
            }
        }

        for (int i = 0; i < N; i++) {
            System.out.println(new String(result[i]));
        }

        sc.close();
    }
}
