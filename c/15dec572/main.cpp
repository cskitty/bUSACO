#include <bits/stdc++.h>
using namespace std;

int N, Q;
vector<int> breeds;
vector<pair<int, int>> queries;
vector<vector<int>> prefix;

int main() {
    // I/0
    ifstream fin("bcount.in");
    ofstream fout("bcount.out");

    fin >> N >> Q;
    breeds.resize(N);
    queries.resize(Q);

    for (int i = 0; i < N; i++) {
        fin >> breeds[i];
    }

    for (int i = 0; i < Q; i++) {
        fin >> queries[i].first;
        fin >> queries[i].second;
    }

    // One based array using indexes 1, 2, and 3
    prefix.resize(4, vector<int>(N));

    // Initializing the Prefix Sum
    prefix[breeds[0]][0] = 1;

    // Prefix Sum
    for (int i = 1; i < N; i++) {
        for (int j = 1; j < 4; j++) {
            prefix[j][i] = prefix[j][i - 1];
        }
        prefix[breeds[i]][i]++;
    }

    for (int q = 0; q < Q; q++) {
        for (int i = 1; i <= 3; i++) {
            if (i>1) {
                fout << " ";
            }
            if (breeds[queries[q].first - 1] == i) {
                fout << prefix[i][queries[q].second - 1] - prefix[i][queries[q].first - 1] + 1;
            }
            else {
                fout << prefix[i][queries[q].second - 1] - prefix[i][queries[q].first - 1];
            }
        }
        fout << '\n';
    }

    return 0;
}