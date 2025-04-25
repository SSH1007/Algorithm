#include <stdio.h>
#include <string.h>

int main() {
    int sH, sM, eH, eM;
    char N[2];
    scanf("%d %d", &sH, &sM);
    scanf("%d %d", &eH, &eM);
    scanf("%s", N);
    int dap = 0;
    while (1) {
        char tmp[5];
        sprintf(tmp, "%02d%02d", sH, sM);  
        for (int i = 0; i < 4; i++) {
            if (tmp[i] == N[0]) {
                dap++;
                break;
            }
        }
        if (sH == eH && sM == eM) {
            break;
        }
        sM += 1;
        if (sM == 60) {
            sH += 1;
            sM = 0;
        }
    }
    printf("%d\n", dap);
    return 0;
}