#include <bits/stdc++.h>
using namespace std;

int main()
{
  long long N, ans = 0, d = 10;
  cin >> N;
  if (N % 2 == 1)
  {
    cout << 0 << endl;
  }
  else
  {
    while (N >= d)
    {
      ans += N / d;
      d = d * 5;
    }
    cout << ans << endl;
  }
}
