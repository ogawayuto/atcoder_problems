#include <bits/stdc++.h>
using namespace std;

long long f(long long n, long long x)
{
  long long rep;
  if (n >= 0){
    rep = n / x + 1;
  }
  else{
    rep = 0;
  }
  return rep;
}

int main()
{
  long long a, b, x;
  cin >> a >> b >> x;
  long long ans = f(b, x) - f(a-1, x);
  cout << ans << endl;
}


