#include <bits/stdc++.h>
using namespace std;

int main()
{
  int N;
  cin >> N;
  vector<int> A(N);
  for (int i = 0; i < N; i++)
  {
    cin >> A.at(i);
  }
  int X, Y;
  auto itr;
  for (int i = 0; i < N; i++)
  {
    X = A.at(i);
    itr = ceil(sqrt(i)) for (int j = 0; j < ceil(sqrt(i)); j++)
    {
      Y = A.at(j);
      if (X % Y == 0)
      {
        /* code */
      }
    }
  }
}
