#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> pi;
typedef pair<ll,ll> pl;

#define mp make_pair
#define f first
#define s second
#define pb push_back
#define all(x) begin(x), end(x)
#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define F0R(i,a) FOR(i,0,a)
#define ll long long
int N;
vector<ll> cows;
vector<ll> prefixS;

int main() {
    freopen("div7.in", "r", stdin);
    freopen("div7.out", "w", stdout);

    cin >> N;

    cows.resize(N + 1);
    for (int i = 1; i <= N; i++) {
        cin >> cows[i];
    }

    prefixS.resize(N + 1);

    for (int i = 1; i <= N; ++i) {
        prefixS[i] = prefixS[i - 1] + cows[i];
    }

    int ans = 0;
    map<int, int> myMap;
    for (int i = 1; i <= N; i++) {
        int d = prefixS[i] % 7;
        if (myMap.count(d) > 0) {
            ans = max(ans, i - myMap[d]);
        }
        else {
            myMap[d] = i;
        }

    }
    cout << ans;
    return 0;

}

