#include <stdio.h>
#include <string.h>

#define MAX_LEN 10002

int main() {
    int C;
    scanf("%d", &C);
    getchar();
    int dap = 0;

    for (int i = 0; i < C; i++) {
        char code[MAX_LEN];
        fgets(code, MAX_LEN, stdin);
        int tmp = 0;
        int j = 0;
        while (j < strlen(code)) {
            if (j + 3 <= strlen(code) && strncmp(&code[j], "for", 3) == 0) {
                tmp++;
                j+=3;
            }
            else if (j + 5 <= strlen(code) && strncmp(&code[j], "while", 5) == 0) {
                tmp++;
                j+=5;
            }
            else {
                j++;
            }
        }
        dap = (dap < tmp) ? tmp : dap;
    }
    printf("%d\n", dap);
    return 0;
}