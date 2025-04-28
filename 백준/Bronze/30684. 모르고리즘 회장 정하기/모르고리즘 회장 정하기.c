#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_STRINGS 100000
#define MAX_LENGTH 6

int cmp(const void *a, const void *b) {
    return strcmp(*(char **)a, *(char **)b);
}

int main() {
    int N;
    scanf("%d", &N);
    char *list[MAX_STRINGS];
    int count = 0;
    for (int i = 0; i < N; i++) {
        char buffer[MAX_LENGTH];
        scanf("%s", buffer);

        if (strlen(buffer) == 3) {
            list[count] = malloc(strlen(buffer) + 1);
            strcpy(list[count], buffer);
            count++;
        }
    }
    qsort(list, count, sizeof(char *), cmp);
    if (count > 0) {
        printf("%s\n", list[0]);
    }
    for (int i = 0; i < count; i++) {
        free(list[i]);
    }
    return 0;
}