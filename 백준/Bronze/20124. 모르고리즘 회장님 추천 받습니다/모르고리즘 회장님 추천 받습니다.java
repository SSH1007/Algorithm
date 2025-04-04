import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        List<Person> lst = new ArrayList<>();
        
        for (int i = 0; i < N; i++) {
            String[] input = br.readLine().split(" ");
            String name = input[0];
            int score = Integer.parseInt(input[1]);
            lst.add(new Person(name, score));
        }

        Collections.sort(lst, (p1, p2) -> {
            if (p2.score != p1.score) {
                return Integer.compare(p2.score, p1.score);
            } else {
                return p1.name.compareTo(p2.name);
            }
        });
        System.out.println(lst.get(0).name);
    }

    static class Person {
        String name;
        int score;
        Person(String name, int score) {
            this.name = name;
            this.score = score;
        }
    }
}