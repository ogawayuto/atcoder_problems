#include <bits/stdc++.h>
using namespace std;

int main()
{
  long N, M, P, Y, lim;
  cin >> N >> M;
  vector<priority_queue<pair<long, long>, vector<pair<long, long>>, greater<pair<long, long>>>> q(N);
  vector<string> ans(M);

  for (long i = 0; i < M; i++)
  {
    cin >> P >> Y;
    q.at(P - 1).push({Y, i});
  }
  for (long i = 0; i < N; i++)
  {
    lim = q.at(i).size();
    for (long j = 0; j < lim; j++)
    {
      char buf[100];
      sprintf(buf, "%06lo%06lo", i + 1, j + 1);
      ans[q.at(i).top().second] = string(buf);
      q.at(i).pop();
    }
  }
  for (long i = 0; i < M; i++)
  {
    cout << ans.at(i) << endl;
  }
}
