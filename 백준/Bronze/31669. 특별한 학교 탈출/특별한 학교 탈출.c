#include <stdio.h>
#include <string.h>

int main() {
    int N, M;
    scanf("%d %d", &N, &M);
    
    int lst[M];
    memset(lst, 0, sizeof(lst));
    
    for (int i = 0; i < N; i++) {
        char tmp[M + 1];
        scanf("%s", tmp);
        
        for (int m = 0; m < M; m++) {
            if (tmp[m] == 'O') {
                lst[m]++;
            }
        }
    }
    
    int found = 0;
    for (int m = 0; m < M; m++) {
        if (lst[m] == 0) {
            printf("%d\n", m + 1);
            found = 1;
            break;
        }
    }
    
    if (!found) {
        printf("ESCAPE FAILED\n");
    }

    return 0;
}
