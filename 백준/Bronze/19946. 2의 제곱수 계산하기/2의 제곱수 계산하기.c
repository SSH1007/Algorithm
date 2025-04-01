#include <stdio.h>

int main() {
	unsigned long long N;
	scanf("%llu", &N);
	int cnt = 0;
	while (N > 0) {
		if ((N & 1) > 0) cnt++;
		N >>= 1;
	}
	printf("%d",cnt);
	return 0;
}