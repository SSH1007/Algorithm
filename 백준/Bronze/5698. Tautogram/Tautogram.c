#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX_LENGTH 1002

int main() {
    char S[MAX_LENGTH];

    while (1) {
        fgets(S, MAX_LENGTH, stdin);
        S[strcspn(S, "\n")] = '\0';
        if (strcmp(S, "*") == 0) {
            break;
        }

        char *lst = strtok(S, " ");
        char a = '\0';
        int flag = 1;

        while (lst != NULL) {
            if (a == '\0') {
                a = toupper(lst[0]);
            } else if (a != toupper(lst[0])) {
                flag = 0;
                break;
            }
            lst = strtok(NULL, " ");
        }
        if (flag) {
            printf("Y\n");
        } else {
            printf("N\n");
        }
    }
    return 0;
}