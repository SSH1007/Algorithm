#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[12];
    int score;
} Person;

int compare(const void *a, const void *b) {
    Person *p1 = (Person *)a;
    Person *p2 = (Person *)b;
    if (p2->score != p1->score) {
        return p2->score - p1->score;
    }
    return strcmp(p1->name, p2->name);
}

int main() {
    int N;
    scanf("%d", &N);
    Person lst[N];
    for (int i = 0; i < N; i++) {
        scanf("%s %d", lst[i].name, &lst[i].score);
    }

    qsort(lst, N, sizeof(Person), compare);
    printf("%s\n", lst[0].name);
    return 0;
}