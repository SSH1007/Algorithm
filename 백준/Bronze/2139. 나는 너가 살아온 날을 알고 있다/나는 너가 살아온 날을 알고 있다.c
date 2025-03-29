#include <stdio.h>

int leap(int year) {
    if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
        return 1; // True
    }
    return 0; // False
}

int main() {
    int month[] = {0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334};
    int leap_month[] = {0, 0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335};
    int d, m, y;
    while (1) {
        scanf("%d %d %d", &d, &m, &y);
        if (d == 0 && m == 0 && y == 0) {
            break;
        }
        if (leap(y)) {
            printf("%d\n", leap_month[m] + d);
        } else {
            printf("%d\n", month[m] + d);
        }
    }
    return 0;
}