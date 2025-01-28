#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);

    char theater[10][20];
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 20; j++) {
            theater[i][j] = '.';
        }
    }

    for (int i = 0; i < N; i++) {
        char row[4];
        scanf("%s", row);

        char r = row[0];
        int c = 0;

        if (row[2] != '\0') {
            c = (row[1] - '0') * 10 + (row[2] - '0');
        } else {
            c = row[1] - '0';
        }

        int rowIdx = r - 'A';
        int colIdx = c - 1;
        theater[rowIdx][colIdx] = 'o';
    }

    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 20; j++) {
            printf("%c", theater[i][j]);
        }
        printf("\n");
    }

    return 0;
}
