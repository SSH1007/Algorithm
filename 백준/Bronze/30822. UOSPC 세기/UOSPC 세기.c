#include <stdio.h>
#include <string.h>

int main() {
    int n;
    char S[1001];
    
    scanf("%d", &n);
    getchar();
    fgets(S, sizeof(S), stdin);
    
    int lst[26] = {0};
    for (int i = 0; i < n; i++) {
        if (S[i] >= 'a' && S[i] <= 'z') {
            lst[S[i] - 'a']++;
        }
    }
    

    int dap = 1000;
    char targetChars[] = {'u', 'o', 's', 'p', 'c'};
    for (int i = 0; i < 5; i++) {
        int tmp = lst[targetChars[i] - 'a'];
        if (dap > tmp) {
            dap = tmp;
        }
    }
    printf("%d\n", dap);
    return 0;
}
