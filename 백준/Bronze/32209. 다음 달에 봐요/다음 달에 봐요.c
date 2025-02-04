#include <stdio.h>

int main() {
    int Q, a, b, q = 0;
    
    scanf("%d", &Q);
    
    for (int i = 0; i < Q; i++) {
        scanf("%d %d", &a, &b);
        
        if (a % 2 != 0) {
            q += b;
        } else {
            q -= b;
        }

        if (q < 0) {
            printf("Adios\n");
            return 0;
        }
    }

    printf("See you next month\n");
    return 0;
}
