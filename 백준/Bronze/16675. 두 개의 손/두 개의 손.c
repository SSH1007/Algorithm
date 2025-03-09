#include <stdio.h>
#include <string.h>

int main() {
    char ML[2], MR[2], TL[2], TR[2];
    scanf("%s %s %s %s", ML, MR, TL, TR);
    
    // 민성이 올 바위, 태경이 보
    if (strcmp(ML, "R") == 0 && strcmp(MR, "R") == 0 && (strcmp(TL, "P") == 0 || strcmp(TR, "P") == 0)) {
        printf("TK\n");
    }
    // 민성이 올 보, 태경이 가위
    else if (strcmp(ML, "P") == 0 && strcmp(MR, "P") == 0 && (strcmp(TL, "S") == 0 || strcmp(TR, "S") == 0)) {
        printf("TK\n");
    }
    // 민성이 올 가위, 태경이 바위
    else if (strcmp(ML, "S") == 0 && strcmp(MR, "S") == 0 && (strcmp(TL, "R") == 0 || strcmp(TR, "R") == 0)) {
        printf("TK\n");
    }
    // 민성이 바위, 태경이 올 가위
    else if ((strcmp(ML, "R") == 0 || strcmp(MR, "R") == 0) && strcmp(TL, "S") == 0 && strcmp(TR, "S") == 0) {
        printf("MS\n");
    }
    // 민성이 가위, 태경이 올 보
    else if ((strcmp(ML, "S") == 0 || strcmp(MR, "S") == 0) && strcmp(TL, "P") == 0 && strcmp(TR, "P") == 0) {
        printf("MS\n");
    }
    // 민성이 보, 태경이 올 바위
    else if ((strcmp(ML, "P") == 0 || strcmp(MR, "P") == 0) && strcmp(TL, "R") == 0 && strcmp(TR, "R") == 0) {
        printf("MS\n");
    } else {
        printf("?\n");
    }
    return 0;
}