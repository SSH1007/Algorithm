#include <stdio.h>
#include <string.h>

int main() {
    int N;
    scanf("%d", &N);
    
    char input[N + 1];
    scanf("%s", input);
    
    int counts[3] = {0};
    for (int i = 0; i < N; i++) {
        if (input[i] == 'B') {
            counts[0]++;
        } else if (input[i] == 'S') {
            counts[1]++;
        } else if (input[i] == 'A') {
            counts[2]++;
        }
    }

    if (counts[0] == counts[1] && counts[1] == counts[2]) {
        printf("SCU\n");
    } else {
        int maxCount = counts[0];
        for (int i = 1; i < 3; i++) {
            if (counts[i] > maxCount) {
                maxCount = counts[i];
            }
        }
        if (counts[0] == maxCount) {
            printf("B");
        }
        if (counts[1] == maxCount) {
            printf("S");
        }
        if (counts[2] == maxCount) {
            printf("A");
        }
    }
    return 0;
}
