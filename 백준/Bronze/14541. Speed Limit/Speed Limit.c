#include <stdio.h>

int main() {
    while (1) {
        int n;
        scanf("%d", &n);        
        if (n == -1) {
            break;
        }

        int dap = 0, f = 0;        
        for (int i = 0; i < n; i++) {
            int s, t;
            scanf("%d %d", &s, &t);
            
            dap += s * (t - f);
            f = t;
        }        
        printf("%d miles\n", dap);
    }
    return 0;
}