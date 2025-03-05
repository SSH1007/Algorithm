#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);
    
    int As[N];
    for (int i = 0; i < N; i++) {
        scanf("%d", &As[i]);
    }

    int penguin = 0;
    for (int i = 0; i < N; i++) {
        if (As[i] == -1) {
            penguin = i;
            break;
        }
    }

    int _max = 1000000000;
    int minLeft = _max;
    int minRight = _max;
    for (int i = 0; i < penguin; i++) {
        if (As[i] < minLeft) {
            minLeft = As[i];
        }
    }
    for (int i = penguin + 1; i < N; i++) {
        if (As[i] < minRight) {
            minRight = As[i];
        }
    }
    printf("%d\n", minLeft + minRight);
    return 0;
}