#include <stdio.h>
#include <string.h>

int main() {
    int cnt = 1;

    while (1) {
        int o, w;
        scanf("%d %d", &o, &w);
        if (o == 0 && w == 0) {
            break;
        }
        getchar();

        int alive = 1;
        while (1) {
            char c;
            int n;
            char input[100];
            fgets(input, sizeof(input), stdin);
            input[strcspn(input, "\n")] = '\0';
            sscanf(input, "%c %d", &c, &n);
            if (c == '#') {
                break; //
            }

            if (alive == 1) {
                if (c == 'E') {
                    w -= n;
                } else if (c == 'F') {
                    w += n;
                }
            }

            if (w <= 0) {
                alive = 0;
            }
        }

        if (alive == 1) {
            if (o * 2 > w && w > o / 2) {
                printf("%d :-)\n", cnt);
            } else {
                printf("%d :-(\n", cnt);
            }
        } else {
            printf("%d RIP\n", cnt);
        }
        cnt++;
    }
    return 0;
}