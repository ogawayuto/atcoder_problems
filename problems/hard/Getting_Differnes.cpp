#include <bits/stdc++.h>
using namespace std;

int main()
{
  long N, K, T, G, M=0;
  cin >> N >> K;
  vector <int> A;
  for (long i = 0; i < N; i++)
  {
    cin >> T;
    A.push_back(T);
    M = max(M,T);
    if (i!=0)
    {
        G = gcd(G,T);
    }else{
        G = T;
    }
    
  }
  if (K%G == 0 && K <= M)
  {
    print("Yes");
  }else{
    print("No");
  }
  
}
