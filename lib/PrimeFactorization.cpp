//素因数分解
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
