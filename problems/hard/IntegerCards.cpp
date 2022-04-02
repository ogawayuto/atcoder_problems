#include <bits/stdc++.h>
using namespace std;

int main()
{
  long N, M, a, b, c, ans = 0;
  pair<long, long> p;
  cin >> N >> M;
  priority_queue<pair<long, long>> q;
  for (long i = 0; i < N; i++)
  {
    cin >> a;
    q.push({a, 1});
  }
  for (long i = 0; i < M; i++)
  {
    cin >> b >> c;
    q.push({c, b});
  }
  long len = q.size();
  long count = 0;
  for (long i = 0; i < len; i++)
  {
    p = q.top();
    q.pop();
    count += p.second;
    ans += p.first * p.second;
    if (count >= N)
    {
      ans -= (count - N) * p.first;
      break;
    }
  }
  cout << ans << endl;
}
