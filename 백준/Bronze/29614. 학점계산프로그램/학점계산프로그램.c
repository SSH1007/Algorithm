#include <stdio.h>
#include <string.h>

double get_score(char grade) {
    switch (grade) {
        case 'A': return 4.0;
        case 'B': return 3.0;
        case 'C': return 2.0;
        case 'D': return 1.0;
        case 'F': return 0.0;
        case '+': return 0.5;
        default: return 0.0;
    }
}

int main() {
    char input[1002];
    scanf("%s", input);
    double dap = 0.0;
    int cnt = 0;
    for (int i = 0; i < strlen(input); i++) {
        char grade = input[i];
        double score = get_score(grade);
        dap += score;
        if (grade != '+') {
            cnt++;
        }
    }
    printf("%.5f\n", dap / cnt);
    return 0;
}