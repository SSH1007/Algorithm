#include <stdio.h>

int main() {
    int D, M;
    scanf("%d %d", &D, &M);

    char *dic[] = {"Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"};
    int mth[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    int totalDays = D - 1;
    for (int i = 1; i < M; i++) {
        totalDays += mth[i];
    }

    int dayIndex = totalDays % 7;
    printf("%s\n", dic[dayIndex]);
    return 0;
}