#include <bits/stdc++.h>
using namespace std;

map<long long, int> enumpr(long long n)
{
  map<long long, int> V;
  for (long long i = 2; i * i <= n; i++)
    while (n % i == 0)
      V[i]++, n /= i;
  if (n > 1)
    V[n]++;
  return V;
}

int main()
{
  long long N, M, ans;
  cin >> N >> M;
  map<long long, int> L;
  L = enumpr(gcd(N, M));
  ans = L.size();
  cout << ans + 1 << endl;
}
