#include <stdio.h>

int main() {
    int Cu, Du, Cd, Dd, Cp, Dp, H;
    int sec = 0;

    scanf("%d %d", &Cu, &Du);
    scanf("%d %d", &Cd, &Dd);
    scanf("%d %d", &Cp, &Dp);
    scanf("%d", &H);

    while (H > 0) {
        if (sec % Cu == 0) {
            H -= Du;
        }
        if (sec % Cd == 0) {
            H -= Dd;
        }
        if (sec % Cp == 0) {
            H -= Dp;
        }
        if (H <= 0) {
            break;
        }
        sec++;
    }
    printf("%d\n", sec);

    return 0;
}