#include <stdio.h>

int main() {
    char* names[] = {"PROBRAIN", "GROW", "ARGOS", "ADMIN", "ANT", "MOTION", "SPG", "COMON", "ALMIGHTY"};
    int N;
    scanf("%d", &N);
    
    int idx = 0, candidate = 0;
    for (int i = 0; i < 9; i++) {
        int tmp = 0;
        for (int j = 0; j < N; j++) {
            int score;
            scanf("%d", &score);
            if (score > tmp) {
                tmp = score;
            }
        }
        if (candidate < tmp) {
            candidate = tmp;
            idx = i;
        }
    }
    printf("%s\n", names[idx]);
    return 0;
}