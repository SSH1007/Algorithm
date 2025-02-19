#include <stdio.h>

int main() {
    int clst[3], mlst[3];  
    for (int i = 0; i < 3; i++) {
        scanf("%d %d", &clst[i], &mlst[i]);
    }
    
    for (int i = 0; i < 100; i++) {
        int j = i%3;  // 현재 순번
        int milk = mlst[j];  // 현재 양동이 안의 우유 양
        int k = (j+1)%3;  // 다음 순번
        // 양동이 넘치지 않을 정도로 옮길 우유 양 조정
        if (clst[k] < milk + mlst[k]) {
            milk = clst[k] - mlst[k];
        }
        mlst[k] += milk;
        mlst[j] -= milk;
    }
    
    for (int i = 0; i < 3; i++) {
        printf("%d\n", mlst[i]);
    }
    return 0;
}