#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);

    for (int n = N; n > 0; n--) {
        printf("%d %s of beer on the wall, %d %s of beer.\n", n, (n == 1 ? "bottle" : "bottles"), n, (n == 1 ? "bottle" : "bottles"));
        
        if (n - 1 > 0) {
            printf("Take one down and pass it around, %d %s of beer on the wall.\n\n", n - 1, (n - 1 == 1 ? "bottle" : "bottles"));
        } else {
            printf("Take one down and pass it around, no more bottles of beer on the wall.\n\n");
        }
    }

    printf("No more bottles of beer on the wall, no more bottles of beer.\n");
    printf("Go to the store and buy some more, %d %s of beer on the wall.\n", N, (N == 1 ? "bottle" : "bottles"));
    return 0;
}