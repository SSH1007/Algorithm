#include <iostream>
using namespace std;
int main() {
    int n; cin >> n;
    int dangling_a = 0;
    bool unneeded_un = false;
    while (n --) {
        string s; cin >> s;
        if (s == "A") {
            ++ dangling_a;
        } else if (s == "Un") {
            if (dangling_a) {
                -- dangling_a;
            } else {
                unneeded_un = true;
            }
        }
    }
    cout << (dangling_a or unneeded_un ? "NO" : "YES") << endl;
    return 0;
}