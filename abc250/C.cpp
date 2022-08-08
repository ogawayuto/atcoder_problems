#include <bits/stdc++.h>
using namespace std;

void q(vector<long> &A, long x)
{
  if (A.at(x) == A.size() - 1)
  {
    A.at
  }

  if (itr != f)
  {
    iter_swap(itr, itr + 1);
  }
  else
  {
    iter_swap(itr, itr - 1);
  }
}

int main()
{
  long N, Q, x;
  cin >> N >> Q;
  unordered_map<int, vector<long>> m;
  vector<long> v;
  for (int i = 0; i < N; i++)
  {
    v.at(i) = {i - 1, i, i + 1};
    m[i] = v;
  }

  for (int i = 0; i < Q; i++)
  {
    cin >> x;
    x--;
    if (m[x].at(2) == N)
    {
      swap(m[x].at(2), m[m[x].at(0)].at(0));
      swap(m[x].at(0), m[x].at(2));
    }
    else
    {
      swap(m[x].at(2), m[m[x].at(0)].at(0));
      swap(m[x].at(0), m[x].at(2));
    }
  }
  for (int i = 0; i < N; i++)
  {
    cout << v.at(i + 1) << " ";
  }
  cout << endl;
}
