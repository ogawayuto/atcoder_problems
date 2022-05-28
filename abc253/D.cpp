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
  long long N, A, B, C, suma, sumb, sumn, sumc;
  cin >> N >> A >> B;
  sumn = (N * (N + 1)) / 2;
  suma = calc(N, A);
  sumb = calc(N, B);
  C = lcm(A, B);
  sumc = calc(N, C);
  cout << sumn - sumb - suma + sumc << endl;
}
