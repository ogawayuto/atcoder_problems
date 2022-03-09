#include <bits/stdc++.h>
using namespace std;

int t(int x, vector<int> a)
{
  int c = 0, d = a.size() - 1;
  int m;
  while (c+1 != d)
  {
    m = (c + d) / 2;
    if (a.at(m) >= x)
    {
      c = m;
    }
    else
      d = m;

  }
  
  return c;
}

int main()
{
  int n, q;
  cin >> n>>q;
  vector<int> a(n);
  vector<int> x(q);
  int o =a.size();
  for (int i = 0; i < n; i++)
  {
    cin >> a.at(i);
  }
  for (int i = 0; i < q; i++)
  {
    cin >> x.at(i);
  }
  sort(a.begin(),a.end());
  for (int i = 0; i < q; i++)
  {
    if(a.at(a.size()-1) < x.at(i)){
      cout<<a.size()<<endl;


    }
    else if (a.at(0) >= x.at(i))
    {
     cout<<0<<endl;
    }
    else
      cout << o-(t(x.at(i), a) + 1) << endl;
  }


}


