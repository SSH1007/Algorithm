import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Map<String, String> mos_dict = new HashMap<>();
        mos_dict.put(".-", "A");
        mos_dict.put("-...", "B");
        mos_dict.put("-.-.", "C");
        mos_dict.put("-..", "D");
        mos_dict.put(".", "E");
        mos_dict.put("..-.", "F");
        mos_dict.put("--.", "G");
        mos_dict.put("....", "H");
        mos_dict.put("..", "I");
        mos_dict.put(".---", "J");
        mos_dict.put("-.-", "K");
        mos_dict.put(".-..", "L");
        mos_dict.put("--", "M");
        mos_dict.put("-.", "N");
        mos_dict.put("---", "O");
        mos_dict.put(".--.", "P");
        mos_dict.put("--.-", "Q");
        mos_dict.put(".-.", "R");
        mos_dict.put("...", "S");
        mos_dict.put("-", "T");
        mos_dict.put("..-", "U");
        mos_dict.put("...-", "V");
        mos_dict.put(".--", "W");
        mos_dict.put("-..-", "X");
        mos_dict.put("-.--", "Y");
        mos_dict.put("--..", "Z");
        mos_dict.put(".----", "1");
        mos_dict.put("..---", "2");
        mos_dict.put("...--", "3");
        mos_dict.put("....-", "4");
        mos_dict.put(".....", "5");
        mos_dict.put("-....", "6");
        mos_dict.put("--...", "7");
        mos_dict.put("---..", "8");
        mos_dict.put("----.", "9");
        mos_dict.put("-----", "0");
        mos_dict.put("--..--", ",");
        mos_dict.put(".-.-.-", ".");
        mos_dict.put("..--..", "?");
        mos_dict.put("---...", ":");
        mos_dict.put("-....-", "-");
        mos_dict.put(".--.-.", "@");

        int N = Integer.parseInt(sc.nextLine());
        String[] S = sc.nextLine().split(" ");
        String dap = "";
        for (int n = 0; n < N; n++) {
            dap += mos_dict.get(S[n]);
        }
        System.out.println(dap);
    }
}