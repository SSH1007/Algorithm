import java.util.*;

public class Main {
    
    static class Pair {
        String rec;
        String team;
        
        Pair(String rec, String team) {
            this.rec = rec;
            this.team = team;
        }
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int red = 0, blue = 0;
        List<Pair> lst = new ArrayList<>();
        for (int n = 0; n < 8; n++) {
            String rec = sc.next();
            String team = sc.next();
            lst.add(new Pair(rec, team));
        }
        
        lst.sort(Comparator.comparing(pair -> pair.rec));
        
        int[] score = {10, 8, 6, 5, 4, 3, 2, 1};
        for (int i = 0; i < 8; i++) {
            if (lst.get(i).team.equals("B")) {
                blue += score[i];
            } else {
                red += score[i];
            }
        }
        if (blue > red) {
            System.out.println("Blue");
        } else {
            System.out.println("Red");
        }
        sc.close();
    }
}