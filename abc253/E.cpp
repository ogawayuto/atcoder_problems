#include <bits/stdc++.h>
using namespace std;

long long calc(long long N, long long x)
{
  long long res = 0, d;
  d = floor(N / x);
  if (N >= x)
  {
    res = ((x + x * d) * d) / 2;
  }
  return res;
}

int main()
{
  long long N, M, K, ans, i, j;
  cin >> N >> M >> K;
  while (i < N - 1)
