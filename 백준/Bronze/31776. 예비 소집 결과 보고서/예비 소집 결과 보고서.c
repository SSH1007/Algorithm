#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);
    int dap = 0;
    
    for (int i = 0; i < N; i++) {
        int Ts[3];
        
        for (int j = 0; j < 3; j++) {
            scanf("%d", &Ts[j]);
        }
        
        if (Ts[0] >= 0 && Ts[1] == -1 && Ts[2] == -1) dap++;
        else if (Ts[0] >= 0 && Ts[1] >= Ts[0] && Ts[2] == -1) dap++;
        else if (Ts[0] >= 0 && Ts[1] >= Ts[0] && Ts[2] >= Ts[1]) dap++;
    }
    
    printf("%d\n", dap);
    return 0;
}
