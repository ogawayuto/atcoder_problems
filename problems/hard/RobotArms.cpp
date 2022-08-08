#include <bits/stdc++.h>
using namespace std;

int main()
{
  long N, x, l, ans = 0, c = 1;
  cin >> N;
  priority_queue<pair<long, long>, vector<pair<long, long>>, greater<pair<long, long>>> q;
  vector<pair<long, long>> XL;
  for (long i = 0; i < N; i++)
  {
    cin >> x >> l;
    q.push({l, x});
  }
  while (!q.empty())
  {
    auto [l, x] = q.top();
    q.pop();
    auto itr = lower_bound(XL.begin(), XL.end(), make_pair(x, l));
    if (itr == XL.begin() && itr == XL.end())
    {
      XL.push_back({x, l});
      ans++;
    }
    else if (itr == XL.begin())
    {
      auto [rx, rl] = *(itr + 1);
      if (x + l - 1 < rl - rx + 1)
      {
        XL.insert(itr, {x, l});
        ans++;
      }
    }
    else if (itr == XL.end())
    {
      auto [lx, ll] = *(itr - 1);
      if (lx + ll - 1 < x - l + 1)
      {
        XL.insert(itr, {x, l});
        ans++;
      }
    }
    else
    {
      auto [lx, ll] = *(itr - 1);
      auto [rx, rl] = *(itr + 1);
      if (lx + ll - 1 < x - l + 1 && x + l - 1 < rl - rx + 1)
      {

        XL.insert(itr, {x, l});
        ans++;
      }
    }
  }
  cout << ans << endl;
}
