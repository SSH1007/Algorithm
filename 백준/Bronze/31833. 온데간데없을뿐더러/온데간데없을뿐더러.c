#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int N;
    scanf("%d", &N);

    char A[100001] = {0};
    char B[100001] = {0};

    for (int i = 0; i < N; i++) {
        int num;
        scanf("%d", &num);
        char temp[12];
        sprintf(temp, "%d", num);
        strcat(A, temp);
    }

    for (int i = 0; i < N; i++) {
        int num;
        scanf("%d", &num);
        char temp[12];
        sprintf(temp, "%d", num);
        strcat(B, temp);
    }

    long long aNum = atoll(A);
    long long bNum = atoll(B);
    if (aNum >= bNum) {
        printf("%s\n", B);
    } else {
        printf("%s\n", A);
    }

    return 0;
}
