import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S = br.readLine();
        HashMap<Character, String> dic = new HashMap<>();
        dic.put('B', "v");
        dic.put('E', "ye");
        dic.put('H', "n");
        dic.put('P', "r");
        dic.put('C', "s");
        dic.put('Y', "u");
        dic.put('X', "h");
        StringBuilder result = new StringBuilder();
        for (char c : S.toCharArray()) {
            if (dic.containsKey(c)) {
                result.append(dic.get(c));
            } else {
                result.append(Character.toLowerCase(c));
            }
        }
        System.out.println(result.toString());
    }
}