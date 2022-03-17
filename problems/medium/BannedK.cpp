#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long N, a, ans, sum = 0;
    cin >> N;
    vector<long long> A(N + 1, 0), P(N + 1, 0);
    queue<long long> Q;

    for (long long i = 0; i < N; i++)
    {
        cin >> a;
        A.at(a)++;
        Q.push(a);
    }

    for (long long i = 0; i < N+1; i++)
    {
        a = A.at(i);
        P.at(i) = a * (a - 1) / 2;
        sum += P.at(i);
    }

    for (long long i = 0; i < N; i++)
    {
        long long id = Q.front();
        Q.pop();
        long long e = A.at(id);
        if (e != 0)
        {
            e = (e - 1)*(e - 2) / 2;
        }
        ans = sum - P.at(id) + e;
        cout << ans << endl;
    }
}
