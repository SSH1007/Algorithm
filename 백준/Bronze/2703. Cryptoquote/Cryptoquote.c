#include <stdio.h>

int main(void)
{
	int t;
	char cipher[101];
	char rule[27];
	scanf("%d", &t);
	
	for (int i = 0; i < t; i++)
	{
		scanf(" %[^\n]s", cipher);
        scanf("%s", rule);
		for (int j = 0; cipher[j]; j++)
		{
			if (cipher[j] == ' ')
			{
				fputc(' ', stdout);
			} else {
    			fputc(rule[cipher[j] - 65], stdout);
            }
		}
		fputc('\n', stdout);
	}
	return 0;
}