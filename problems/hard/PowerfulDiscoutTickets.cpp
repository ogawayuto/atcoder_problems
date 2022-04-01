#include <bits/stdc++.h>
using namespace std;

int main()
{
  long N, M, ans = 0, t;
  priority_queue<long> q;
  cin >> N >> M;
  for (long i = 0; i < N; i++)
  {
    cin >> t;
    q.push(t);
  }

  for (long i = 0; i < M; i++)
  {
    t = q.top();
    q.pop();
    q.push(t / 2);
  }

  for (long i = 0; i < N; i++)
  {
    t = q.top();
    ans += t;
    q.pop();
  }

  cout << ans << endl;
}
