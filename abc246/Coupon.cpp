#include <bits/stdc++.h>
using namespace std;

int main()
{
  long N, K, X, t, m, ans = 0;
  bool usable = true;
  cin >> N >> K >> X;
  vector<int> a(N);

  for (int i = 0; i < N; i++)
  {
    if (!usable)
    {
      cin >> a.at(i);
      continue;
    }
    else
    {
      cin >> t;
      m = t / X;
      K -= m;
      t = t % X;
      if (K < 0)
        usable = false;
      if (!usable)
      {
        t = t - K * X;
        K = 0;
      }
      a.at(i) = t;
    }
  }
  sort(a.begin(), a.end());
  reverse(a.begin(), a.end());
  for (int i = 0; i < N; i++)
  {
    if (K > 0)
    {
      K--;
    }
    else
    {
      ans += a.at(i);
    }
  }

  cout << ans << endl;
}
