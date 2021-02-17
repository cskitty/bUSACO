#include <bits/stdc++.h>
#include <algorithm>

using namespace std;
int myfind(vector<int> &a, int v) {
    for (int i = 0; i < a.size(); i++) {
        if (a[i] == v) {
            return i;
        }
    }
    return 100000000;
}
int main() {
    ifstream cin("gymnastics.in");
    ofstream cout("gymnastics.out");
//    freopen("gymnastics.in", "r", stdin);
  //  freopen("gymnastics.out", "w", stdout);
    int K, N;
    cin >> K;
    cin >> N;

    vector<vector<int>> cows;
    cows.resize(K, vector<int>(N));

    for (int i = 0; i < K; i++) {
        for (int j = 0; j < N; j++) {
            cin >> cows[i][j];
        }
    }

    int ans = 0;
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            if (j != i) {
                bool working = true;
                for (int s = 0; s < K; s++) {
                    if (myfind(cows[s], i) < myfind(cows[s], j)) {
                        working = false;
                    }
                }
                if (working) {
                    ans++;
                }
            }

        }
    }
    cout << ans;
    return 0;
}