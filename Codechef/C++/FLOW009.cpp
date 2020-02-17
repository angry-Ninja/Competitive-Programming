#include<bits/stdc++.h>
using namespace std;
#define hot ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
int main()
{ 
    hot;
    int t;
    cin>>t;
    while(t--)
    {
    	double q,p,amt=0;
    	cin>>q>>p;
    	amt=q*p*1.0;
    	if(q>1000)
    	{
    		amt=(amt*1.0)-((amt*1.0)*0.10);
		}
		printf("%.6lf",amt);
		cout<<endl;
    }
    return 0;
}
