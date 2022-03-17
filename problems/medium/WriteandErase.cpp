#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
    int N, a, ans;
    cin >> N;
    unordered_set<int> A;
    for (int i = 0; i < N; i++)
    {
        cin >> a;
        if (A.find(a) != A.end())
        {
            A.erase(a);
        }
        else{
            A.insert(a);
        }
    }
    ans = A.size();
    cout << ans << endl;
}
