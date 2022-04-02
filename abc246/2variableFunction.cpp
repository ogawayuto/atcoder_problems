#include <bits/stdc++.h>
using namespace std;
vector<long long> divisor(long long n)
{
  vector<long long> ret;
  for (long long i = 1; i * i <= n; i++)
  {
    if (n % i == 0)
    {
      ret.push_back(i);
      if (i * i != n)
        ret.push_back(n / i);
    }
  }
  sort(ret.begin(), ret.end()); // 昇順に並べる
  return ret;
}
int main()
{
  long long N, a, b;
  cin >> N;
  vector<long long> ret = divisor(N);
  a = sqrt(ret.at(0));
  b =
}
