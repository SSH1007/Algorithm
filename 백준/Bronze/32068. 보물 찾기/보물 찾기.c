#include <stdio.h>
#include <stdlib.h>

int main() {
    int T;
    scanf("%d", &T);
    
    while (T--) {
        int L, R, S;
        scanf("%d %d %d", &L, &R, &S);
        
        int LS = abs(L - S);
        int RS = abs(R - S);
        
        if (S == R || S == L) {
            printf("0\n");
        } else if (LS > RS) {
            printf("%d\n", RS * 2);
        } else if (LS < RS) {
            printf("%d\n", LS * 2 + 1);
        } else {
            printf("%d\n", RS * 2);
        }
    }
    
    return 0;
}
