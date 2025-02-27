#include <stdio.h>

int main() {
    char S[257];

    while (1) {
        fgets(S, sizeof(S), stdin);

        if (S[0] == '#') {
            break;
        }

        int dap = 0;
        for (int i = 0; S[i]; i++) {
            if (S[i] > 64) {
                dap += (S[i] - 64) * (i + 1);           
            }
        }
        printf("%d\n", dap);
    }
    return 0;
}