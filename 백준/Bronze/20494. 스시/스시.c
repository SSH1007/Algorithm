#include <stdio.h>

int main()
{
	char s;
	int n, dap=0;
	scanf("%d ", &n);
	while(n--)
		while((s = getchar()) != '\n'){
            ++dap;
        }
	printf("%d", dap);
}