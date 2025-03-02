#include <stdio.h>
#include <string.h>
#include <stdlib.h>


void B(int n, char* result) {
    for (int i = 5; i >= 0; i--) {
        result[5 - i] = (n & (1 << i)) ? '1' : '0';
    }
    result[6] = '\0';
}

int main() {
    int N;
    scanf("%d", &N);
    while (N--) {
        int H, M, S;
        scanf("%d:%d:%d", &H, &M, &S);

        char binH[7], binM[7], binS[7];
        B(H, binH);
        B(M, binM);
        B(S, binS);

        char R[19];
        strcpy(R, binH);
        strcat(R, binM);
        strcat(R, binS);

        char C[19];
        int index = 0;
        for (int i = 0; i < 6; i++) {
            C[index++] = binH[i];
            C[index++] = binM[i];
            C[index++] = binS[i];
        }
        C[index] = '\0';
        printf("%s %s\n", C, R);
    }
    return 0;
}