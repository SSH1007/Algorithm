#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_N 1000

int main() {
    int N;
    scanf("%d", &N);
    
    char Ns[MAX_N][MAX_N], H[MAX_N][MAX_N];
    int ns_count = 0, h_count = 0;
    
    for (int i = 0; i < N; i++) {
        scanf("%s", Ns[ns_count++]);
    }

    for (int i = 0; i < N - 1; i++) {
        scanf("%s", H[h_count++]);
    }
    
    for (int i = 0; i < ns_count; i++) {
        int is_in_H = 0;
        
        for (int j = 0; j < h_count; j++) {
            // Ns[i]와 H[j]가 동일한 문자열인 경우
            if (strcmp(Ns[i], H[j]) == 0) {
                is_in_H = 1;
                break;
            }
        }
        
        if (!is_in_H) {
            printf("%s ", Ns[i]);
            return 0;
        }
    }

    return 0;
}
