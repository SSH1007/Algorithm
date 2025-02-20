#include <stdio.h>
#include <string.h>

int main() {
    char S[21];
    while (1) {
        scanf("%s", S);
        if (S[0] == '#') {
            break;
        }
        
        int idx = -1;
        int flag = 1;
        int len = strlen(S);
        char vowel[] = "aeiou";
        for (int i = 0; i < len; i++) {
            if (flag){
                for (int j = 0; j < 5; j++){
                    if (S[i] == vowel[j]){
                        idx = i;
                        flag = 0;
                        break;
                    }
                }
            } else {break;}
        }
        
        if (idx != -1) {
            printf("%s%say\n", S + idx, (idx > 0) ? strndup(S, idx) : "");
        }
        else {
            printf("%say\n", S);
        }
    }
    return 0;
}