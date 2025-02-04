#include <stdio.h>

int main() {
    int cur[3], bot[3];
    scanf("%d:%d:%d", &cur[0], &cur[1], &cur[2]);
    scanf("%d:%d:%d", &bot[0], &bot[1], &bot[2]);
    int curS = cur[0] * 3600 + cur[1] * 60 + cur[2];
    int botS = bot[0] * 3600 + bot[1] * 60 + bot[2];
  
    int c = botS - curS;
    if (c <= 0){
        c = (c + 24 * 3600);  
    }

    int h = c / 3600;
    int m = (c % 3600) / 60;
    int s = (c % 3600) % 60;

    printf("%02d:%02d:%02d\n", h, m, s);
    return 0;
}
