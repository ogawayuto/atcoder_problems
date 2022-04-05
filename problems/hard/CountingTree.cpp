
#include <bits/stdc++.h>
using namespace std;

int main()
{
  long long N, t, ans = 1;
  cin >> N;
  vector<long long> C(N, 0), D(N, 0);
  for (long long i = 0; i < N; i++)
  {
    cin >> t;
    D.at(i) = t;
    C.at(t)++;
  }
  if (C.at(0) != 1 || D.at(0) != 0)
    ans = 0;
  else
  {
    for (long long i = 1; i < N; i++)
    {
      ans *= C.at(D.at(i) - 1);
      ans %= 998244353;
    }
  }

  cout << ans % 998244353 << endl;
}
