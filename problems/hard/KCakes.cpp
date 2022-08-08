#include <bits/stdc++.h>
using namespace std;

int main()
{
  int K, T, a;
  priority_queue<pair<int, int>> q;
  cin >> K >> T;
  for (int i = 1; i < T + 1; i++)
  {
    cin >> a;
    q.push({a, i});
  }
  int x = 1;
  pair<int, int> h = q.top(), p;
  h.first--;
  q.pop();
  while (!q.empty())
  {
    p = q.top();
    p.first--;
    x++;
    q.pop();
    if (h.first != 0)
      q.push(h);
    h = p;
  }

  cout << K - x << endl;
}
