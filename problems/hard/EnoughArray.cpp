#include <bits/stdc++.h>
using namespace std;

int main()
{
  long N, K;
  cin >> N >> K;
  vector<int> a(N);
  long prev, ans = 0, sum = 0, j = -1;
  bool end = false;
  for (long i = 0; i < N; i++)
  {
    cin >> a.at(i);
  }
  for (int i = 0; i < N; i++)
  {
    while (sum < K)
    {
      j++;
      if (N - 1 < j)
      {
        end = true;
        break;
      }
      sum += a.at(j);
    }
    if (end)
      break;
    ans += N - j;
    sum -= a.at(i);
  }
  cout << ans << endl;
}
