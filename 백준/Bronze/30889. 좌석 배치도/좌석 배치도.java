import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        
        char[][] theater = new char[10][20];
        
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 20; j++) {
                theater[i][j] = '.';
            }
        }
        
        for (int i = 0; i < N; i++) {
            String info = br.readLine();
            char r = info.charAt(0);
            String c = info.substring(1);
            
            int row = r - 'A';
            int col = Integer.parseInt(c) - 1;
            
            theater[row][col] = 'o';
        }
        
        for (int i = 0; i < 10; i++) {
            System.out.println(new String(theater[i]));
        }
    }
}
