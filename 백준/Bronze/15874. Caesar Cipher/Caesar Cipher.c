#include <stdio.h>
#include <ctype.h>

int main() {
    int k, s;
    scanf("%d %d", &k, &s);
    char S[100001];
    scanf(" %[^\n]", S);
    char dap[100001];
    int i;
    for (i = 0; i < s && S[i] != '\0'; i++) {
        if (isalpha(S[i])) {
            if (isupper(S[i])) {
                dap[i] = (char)(((S[i] - 'A' + k) % 26) + 'A');
            } else {
                dap[i] = (char)(((S[i] - 'a' + k) % 26) + 'a');
            }
        } else {
            dap[i] = S[i];
        }
    }
    dap[i] = '\0';  
    printf("%s\n", dap);
    return 0;
}