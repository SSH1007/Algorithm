#include <stdio.h>
#include <string.h>

int main() {
    int Q;
    scanf("%d", &Q);
    
    while (Q--) {
        char S[1001];
        scanf("%s", S);
        
        int tmp = 0;
        int len = strlen(S);
        char target[] = "WOW";
        int t_len = strlen(target);
        
        for (int i = 0; i <= len - t_len; i++) {
            if (strncmp(&S[i], target, t_len) == 0) {
                tmp++;
            }
        }
        
        printf("%d\n", tmp);
    }
    
    return 0;
}
