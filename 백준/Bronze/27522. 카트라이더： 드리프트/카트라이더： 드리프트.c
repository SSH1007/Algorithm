#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct {
    char rec[10];
    char team;
} Pair;

int compare(const void *a, const void *b) {
    return strcmp(((Pair*)a)->rec, ((Pair*)b)->rec);
}

int main() {
    int red = 0, blue = 0;
    Pair lst[8];
    int score[] = {10, 8, 6, 5, 4, 3, 2, 1};

    for (int i = 0; i < 8; i++) {
        scanf("%s %c", lst[i].rec, &lst[i].team);
    }

    qsort(lst, 8, sizeof(Pair), compare);
    for (int i = 0; i < 8; i++) {
        if (lst[i].team == 'B') {
            blue += score[i];
        } else {
            red += score[i];
        }
    }
    printf("%s\n", blue > red ? "Blue" : "Red");
    return 0;
}