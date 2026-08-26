#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

int main() {
    int n, result = 0;
    cin >> n;

    vector<int> N(n);
    for (int i = 0; i < n; i++) {
        cin >> N[i];
    }

    for (int num = 0; num < n; num++) {
        if (N[num] == 0) {
            continue;
        }

        int count = 0;

        for (int i = 1; i <= sqrt(N[num]); i++) {
            if (N[num] % i == 0) {
                count++;
                if (i != N[num] / i) {
                    count++;
                }
            }
        }
        result += N[num] * count;
    }

    cout << result << endl;

    return 0;
}