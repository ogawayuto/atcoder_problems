#include <bits/stdc++.h>
using namespace std;

int main()
{
    long N,M=0,T,others;
    cin >> N;
    vector<int> A, B(N+1);
    A.push_back(0);
    for (long i = 0; i < N; i++)
    {
    cin >> T;
    A.push_back(T);
    }

    for (long i = N; 1<=i; i--)
    {
        others = 0;
        for (long j = 2*i; j < N+1; j=j+i){ 
            others = (others + B.at(j))%2;
        }

        if (others != A.at(i)) {
            B.at(i)++;
            M++;
         } 
    }
    cout << M << endl;
    for (long i = 1; i < N+1; i++)
    {
        if(B.at(i)==1) cout << i << " " ;
    }
  
  
  
}
