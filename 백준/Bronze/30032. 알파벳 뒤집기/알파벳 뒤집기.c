#include <stdio.h>
#include <string.h>

int main() {
    int N, D;
    scanf("%d %d", &N, &D);

    char maps[N][N + 1];
    
    for (int i = 0; i < N; i++) {
        scanf("%s", maps[i]);
    }
    
    char dic[256][2];
    dic['d'][0] = 'q'; dic['d'][1] = 'b';
    dic['b'][0] = 'p'; dic['b'][1] = 'd';
    dic['q'][0] = 'd'; dic['q'][1] = 'p';
    dic['p'][0] = 'b'; dic['p'][1] = 'q';
    
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < N; c++) {
            char currentChar = maps[r][c];
            maps[r][c] = dic[currentChar][(D + 1) % 2];
        }
    }
    
    for (int i = 0; i < N; i++) {
        printf("%s\n", maps[i]);
    }

    return 0;
}
