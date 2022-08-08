#include <bits/stdc++.h>
using namespace std;

int main()
{
  long double A, B, K;
  cin >> A >> B >> K;
  cout << ceil(log(B / A) / log(K)) << endl;
}
